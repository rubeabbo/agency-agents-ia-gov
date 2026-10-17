"""Offline integration tests: provenance, safe preparation, configuration and runtime repairs."""
import ast
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('polintel', Path(__file__).with_name('political_intelligence.py'))
polintel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(polintel)


class IntegrationTests(unittest.TestCase):
    def test_manifest_and_required_categories(self):
        polintel.verify()
        data = polintel.registry()
        self.assertEqual([x['label'] for x in data['categories']], [
            '1. Economy and Political Agents', '2. Research Political News and Report',
            '3. Geopolitical Trenders', '4. Conflict Analyst'])
        divisions = json.loads((polintel.ROOT/'divisions.json').read_text(encoding='utf-8'))['divisions']
        for c in data['categories']:
            self.assertEqual(divisions[c['id']]['label'], c['label'])
            self.assertTrue((polintel.ROOT/c['profile']).is_file())

    def test_install_includes_licenses_and_refuses_partial_collision(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)/'skills'
            first = polintel.registry()['skills'][0]['id']
            (dest/first).mkdir(parents=True)
            with self.assertRaises(ValueError):
                polintel.install_skills(dest)
            self.assertEqual(list(dest.iterdir()), [dest/first])
            fresh = Path(tmp)/'fresh'
            polintel.install_skills(fresh)
            for skill in polintel.registry()['skills']:
                self.assertTrue((fresh/skill['id']/'LICENSE.txt').is_file())
                self.assertTrue((fresh/skill['id']/'references/upstream-SKILL.md').is_file())

    def test_checkout_rejects_mismatched_sha_without_reset(self):
        with tempfile.TemporaryDirectory() as tmp:
            project={'id':'tool','commit':'expected','url':'https://github.com/example/tool'}
            (Path(tmp)/'tool').mkdir()
            with patch.object(polintel,'output',return_value='other'), patch.object(polintel,'run') as execute:
                with self.assertRaises(ValueError):
                    polintel.checkout(project,Path(tmp))
                execute.assert_not_called()

    def test_checkout_rejects_dirty_tree_and_wrong_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            project={'id':'tool','commit':'expected','url':'https://github.com/example/tool'}
            (Path(tmp)/'tool').mkdir()
            for results in [('expected','https://github.com/other/tool'),
                            ('expected',project['url']+'.git',' M config.yaml')]:
                with patch.object(polintel,'output',side_effect=results), patch.object(polintel,'run') as execute:
                    with self.assertRaises(ValueError):
                        polintel.checkout(project,Path(tmp))
                    execute.assert_not_called()

    def test_crew_preserves_secret_and_has_clear_missing_key_error(self):
        source = polintel.DOC/'runtime/political-agent/src/ai_latest_development/crew.py'
        tree = ast.parse(source.read_text(encoding='utf-8'))
        credential_check = next(node for node in tree.body if isinstance(node, ast.If))
        isolated = ast.Module(body=[credential_check],type_ignores=[])
        import os
        with patch.dict(os.environ, {'SERPER_API_KEY':'test-placeholder-not-a-secret'}, clear=True):
            exec(compile(isolated,str(source),'exec'),{'os':os})
            self.assertEqual(os.environ['SERPER_API_KEY'],'test-placeholder-not-a-secret')
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(RuntimeError,'SERPER_API_KEY required'):
            exec(compile(isolated,str(source),'exec'),{'os':os})

    def test_main_import_has_no_side_effect_and_cli_passes_topic(self):
        import types
        from unittest.mock import Mock
        source=polintel.DOC/'runtime/political-agent/src/ai_latest_development/main.py'
        fake=types.ModuleType('fake.crew')
        fake.AiLatestPoliticalNews=Mock()
        namespace={'__name__':'fake.main','__package__':'fake'}
        with patch.dict(sys.modules,{'fake.crew':fake}):
            exec(compile(source.read_text(),str(source),'exec'),namespace)
        fake.AiLatestPoliticalNews.assert_not_called()
        with patch.object(sys,'argv',['run_crew','--topic','budget Argentina']):
            namespace['run']()
        args=fake.AiLatestPoliticalNews.return_value.crew.return_value.kickoff.call_args.kwargs
        self.assertEqual(args['inputs']['topic'],'budget Argentina')

    def test_free_trendradar_profile_switches_off_ai_and_notifications(self):
        # Execute exactly the subprocess configuration logic with a temporary config.
        import yaml
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp)
            (folder/'config').mkdir()
            config={key:{'enabled':True} for key in ('ai_filter','ai_analysis','ai_translation','notification')}
            config.update(ai={'api_key':'placeholder','fallback_models':['paid']},filter={'method':'ai'})
            path=folder/'config/config.yaml'
            path.write_text(yaml.safe_dump(config),encoding='utf-8')
            polintel.free_trendradar_config(folder,sys.executable)
            result=yaml.safe_load(path.read_text(encoding='utf-8'))
            self.assertEqual(result['filter']['method'],'keyword')
            self.assertFalse(result['ai_analysis']['enabled'])
            self.assertFalse(result['ai_translation']['enabled'])
            self.assertFalse(result['notification']['enabled'])
            self.assertEqual(result['ai']['api_key'],'')


if __name__ == '__main__':
    unittest.main(verbosity=2)
