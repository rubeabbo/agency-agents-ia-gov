# Procedencia y licencias

Se revisaron árboles Git fijados, no sólo descripciones o badges. Las licencias
íntegras están en [licenses](licenses); `registry.json` registra sus hashes.
La licencia MIT general del fork **no reemplaza** las licencias de estos materiales.

| Proyecto y autores atribuidos | Commit auditado | Licencia | Material distribuido aquí |
|---|---|---|---|
| [Hack23 / riksdagsmonitor](https://github.com/Hack23/riksdagsmonitor) y sus contribuidores | `7a67743488e2628ba339eb95785a80f40285b89f` | [Apache-2.0](licenses/riksdagsmonitor.txt) | Seis SKILL.md originales íntegros bajo `agents/political-intelligence/skills/*/references/`; seis entradas portables derivadas con aviso de cambio y copia de licencia en cada carpeta. |
| [Phoenix AGI / marc-shade/world-intel-mcp](https://github.com/marc-shade/world-intel-mcp), © 2025–2026 Phoenix AGI | `eb2f4fee199cde9f5b247016a12ccd05839bea9d` | [MIT](licenses/world-intel-mcp.txt) | Licencia para atribución y metadata/receta de conexión; **no** se distribuye su código ejecutable en este commit. El helper descarga el original a un checkout ignorado. |
| [sansan0 / TrendRadar](https://github.com/sansan0/TrendRadar) y contribuidores | `657094ed6a527441b917e16d9497fc8435ed091d` | [GPL-3.0](licenses/TrendRadar.txt) | Texto de licencia y receta independiente; **no** se copia código GPL dentro de perfiles MIT. El runtime externo conserva su GPL y su código fuente. |
| [ayushi-006 / Political_Agent](https://github.com/ayushi-006/Political_Agent) y contribuidores | `58f437ff395a4fb5bfa16c2af2b286a8a85ab67d` | [Apache-2.0](licenses/Political_Agent.txt) | README, LICENSE, pyproject y archivos Python/YAML de `src/` en `runtime/political-agent/`; se excluyen reportes generados y knowledge personal. |
| [Lina Braun / lina767/digital-war-room](https://github.com/lina767/digital-war-room), © 2026 Lina Braun | `be1d4c120c323ca270fd61bf3c0d993a7cfe8a2b` | [MIT](licenses/digital-war-room.txt) | Licencia y receta de preparación externa; **no** se distribuye su plataforma completa ni se afirma su instalación en el perfil del usuario. |

Los árboles revisados no contenían un archivo `NOTICE` de distribución para los
dos proyectos Apache seleccionados. Se preservan sus avisos en las fuentes y
licencias. Las rutas y hashes de cada archivo copiado constan en `registry.json`.
Ninguno de estos proyectos respalda oficialmente esta adaptación.

## Modificaciones de IA-Gov, 2026-10-17

- **Skills:** nuevas entradas portables en español, nombres `polintel-*`, método y
  límites aplicables a IA-Gov; originales íntegros como referencia. No se declara
  que las entradas sean copias literales ni que hereden infraestructura de Hack23.
- **Political_Agent / crew.py:** elimina la asignación upstream de un placeholder
  a `SERPERDEV_API_KEY`. Usa `SERPER_API_KEY`, nombre esperado por SerperDevTool,
  conserva la variable del operador y devuelve error claro si falta.
- **Political_Agent / main.py:** import relativo de paquete, parámetro `--topic`
  y guard `__main__`. El programa ya no corre al importarlo. También se retiran `train/replay/test` sin implementación en pyproject.toml. Los demás archivos
  seleccionados conservan sus bytes originales; no se reescribe la lógica CrewAI.
- **TrendRadar:** el helper modifica sólo el checkout externo local para fijar
  filtrado por keywords, desactivar IA/traducción/notificaciones y vaciar API key/fallback.
  No se redistribuye esa copia modificada como software MIT. Si se redistribuye,
  deben preservarse GPL, fuentes y avisos correspondientes.
- **Perfiles y helper:** aportes originales del fork bajo su licencia MIT.

Las licencias de software no conceden permisos sobre datos, contenidos de noticias,
marcas, cuentas ni servicios externos. No se transfieren secretos entre proyectos.
