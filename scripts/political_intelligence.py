#!/usr/bin/env python3
"""Prepare pinned external runtimes; never launch analysis or configure user accounts."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'examples/third-party/political-intelligence'


def registry():
    return json.loads((DOC / 'registry.json').read_text(encoding='utf-8'))


def run(*args, cwd=None):
    subprocess.run([str(a) for a in args], cwd=cwd, check=True)


def output(*args, cwd=None):
    return subprocess.check_output([str(a) for a in args], cwd=cwd, text=True).strip()


def venv_python(folder):
    return folder / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')


def verify():
    data = registry()
    for project in data['projects']:
        path = DOC / project['license_path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != project['license_sha256']:
            raise ValueError(f'License modified: {path}')
    for skill in data['skills']:
        path = ROOT / skill['reference']
        if hashlib.sha256(path.read_bytes()).hexdigest() != skill['original_sha256']:
            raise ValueError(f'Upstream reference modified: {path}')
        if not (ROOT / skill['path']).is_file():
            raise ValueError(f'Missing skill: {skill["path"]}')
    for entry in data['imported_files']:
        path = ROOT / entry['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry['distributed_sha256']:
            raise ValueError(f'Runtime differs from manifest: {path}')
    print(f'PASS: {len(data["projects"])} licenses, {len(data["skills"])} original skill references, '
          f'{len(data["imported_files"])} runtime files')


def checkout(project, cache):
    """Refuse pre-existing mismatched repos instead of resetting/deleting user changes."""
    dest = cache / project['id']
    if not dest.exists():
        run('git', 'clone', '--no-checkout', '--filter=blob:none', project['url']+'.git', dest)
        run('git', '-C', dest, 'checkout', '--detach', project['commit'])
    actual = output('git', '-C', dest, 'rev-parse', 'HEAD')
    if actual != project['commit']:
        raise ValueError(f'{dest}: expected {project["commit"]}, got {actual}; use a fresh --cache')
    origin = output('git', '-C', dest, 'remote', 'get-url', 'origin')
    if origin.rstrip('/').removesuffix('.git') != project['url']:
        raise ValueError(f'{dest}: unexpected remote; use a fresh --cache')
    if output('git', '-C', dest, 'status', '--porcelain', '--untracked-files=normal'):
        raise ValueError(f'{dest}: local modifications; preserve them and use a fresh --cache')
    return dest


def free_trendradar_config(source, python):
    # Use YAML parser from TrendRadar's own environment; no third-party dependency for this CLI.
    code = """from pathlib import Path
import yaml
p = Path('config/config.yaml')
data = yaml.safe_load(p.read_text(encoding='utf-8'))
for key in ('ai_filter', 'ai_analysis', 'ai_translation', 'notification'):
    if key in data:
        data[key]['enabled'] = False
        if 'enable' in data[key]: data[key]['enable'] = False
data['ai']['api_key'] = ''
data['ai']['fallback_models'] = []
data['filter']['method'] = 'keyword'
p.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
print('TrendRadar: AI and notifications disabled in local checkout')
"""
    run(python, '-c', code, cwd=source)


def prepare(project_id, cache, install):
    data = registry()
    project = next(p for p in data['projects'] if p['id'] == project_id)
    if project_id == 'riksdagsmonitor':
        raise ValueError('Use install-skills; the full Swedish newsroom is not a dependency')
    cache = cache.resolve()
    cache.mkdir(parents=True, exist_ok=True)
    if project_id == 'Political_Agent':
        source = DOC / 'runtime/political-agent'
    else:
        source = checkout(project, cache)
    env = cache / (project_id+'-venv')
    python = venv_python(env)
    if install:
        # Reuse only a venv created for this exact source and SHA by this helper.
        marker = env / 'ia-gov-runtime.json'
        expected = {'project': project_id, 'commit': project['commit'], 'source': str(source)}
        if env.exists():
            if not marker.is_file() or json.loads(marker.read_text()) != expected:
                raise ValueError(f'{env}: unrecognized environment; use a fresh --cache')
        else:
            run(sys.executable, '-m', 'venv', env)
            marker.write_text(json.dumps(expected), encoding='utf-8')
        if project_id == 'digital-war-room':
            run(python, '-m', 'pip', 'install', '-r', source/'backend/requirements.txt')
        else:
            run(python, '-m', 'pip', 'install', '-e', source)
        if project_id == 'TrendRadar':
            free_trendradar_config(source, python)
    print(json.dumps({'project': project_id, 'source': str(source),
        'commit': project['commit'], 'python': str(python), 'dependencies_installed': install,
        'next': 'Read the guide; no server, collector, notifications or analysis was started.'}, indent=2))


def install_skills(destination):
    verify()
    sources = [ROOT / s['path'] for s in registry()['skills']]
    targets = [(p.parent, destination.resolve()/p.parent.name) for p in sources]
    # Preflight all collisions before copying anything.
    for source, target in targets:
        if target.exists():
            raise ValueError(f'{target} already exists; choose another destination (no overwrite)')
    for source, target in targets:
        shutil.copytree(source, target)
    print(f'Installed {len(targets)} skills with references and licenses into {destination.resolve()}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list')
    commands.add_parser('verify')
    prepare_parser = commands.add_parser('prepare')
    prepare_parser.add_argument('project', choices=[p['id'] for p in registry()['projects'] if p['id']!='riksdagsmonitor'])
    prepare_parser.add_argument('--cache', type=Path, default=ROOT/'.cache/political-intelligence')
    prepare_parser.add_argument('--install-deps', action='store_true')
    skills_parser = commands.add_parser('install-skills')
    skills_parser.add_argument('--destination', required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'list':
            print(json.dumps(registry(), ensure_ascii=False, indent=2))
        elif args.command == 'verify':
            verify()
        elif args.command == 'prepare':
            prepare(args.project, args.cache, args.install_deps)
        else:
            install_skills(args.destination)
    except (ValueError, OSError, subprocess.CalledProcessError, StopIteration) as exc:
        parser.exit(1, f'Preparation failed: {exc}\n')


if __name__ == '__main__':
    main()
