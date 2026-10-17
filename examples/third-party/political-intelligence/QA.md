# Verificación de la integración — 2026-10-17

Baseline del fork: `da8096425684264355f4db14642d197723b19927`.
Contrato: [EXECUTION-CONTRACT.md](EXECUTION-CONTRACT.md).
Revisor independiente: agente `cerbero_review`, rol Code Reviewer; revisión real
mediante herramientas sobre el checkout compartido, sin edición de producción.
Modelo/costo individual no expuestos por el runtime: no se infieren.

## Evidencia obtenida

| Criterio | Prueba | Resultado |
|---|---|---|
| Taxonomía preservada y cuatro etiquetas exactas | `bash scripts/check-divisions.sh` | PASS: 27 divisiones coherentes entre registro, directorios, conversor, linter y CI |
| Perfiles válidos | Linter sobre los cuatro agentes nuevos | PASS: 0 errores, 0 advertencias |
| Especialidades diferenciadas | `check-agent-originality.sh` contra catálogo real | PASS: similitud máxima aproximada 4,3%, inferior a warn 20% / fail 40% |
| Procedencia | `python scripts/political_intelligence.py verify` | PASS: cinco licencias, seis referencias originales y diez archivos del runtime con hashes |
| Comportamiento del helper y reparaciones | `python scripts/test_political_intelligence.py` | PASS: siete pruebas; incluye colisiones de instalación, SHA/origin incorrectos, checkout con cambios, configuración sin IA/envíos, credencial Serper y entrypoint |
| Sintaxis Python | `compileall` de helper/tests/runtime | PASS |
| Selección con instalador existente | `install.sh --tool codex --division economy-political,political-news,geopolitical-trends,conflict-analysis --dry-run` | PASS: selecciona exactamente cuatro agentes; no escribe configuración del usuario |
| Conversión Codex acotada | Conversor/lib reales sin modificar y cuatro perfiles copiados a fixture temporal | PASS: proceso terminado, cuatro conversiones; TOML parseados y cuerpo completo idéntico al perfil correspondiente |
| Runtime World Intel | `prepare world-intel-mcp --install-deps` | PASS en Python 3.12.14 Windows; paquete 0.11.0, MCP SDK 1.30.0 |
| Protocolo MCP World Intel | Inicialización stdio y `tools/list` con cliente MCP real | PASS: 139 herramientas anunciadas |
| Consulta MCP | `intel_status` | PASS: respuesta sin error; vector store no instalado, informado explícitamente |
| Fuente pública en vivo | `intel_forex_rates` → Frankfurter, GET `/v1/latest?base=USD` | PASS HTTP 200; fecha de datos 2026-10-16, fecha de consulta 2026-10-17; no se usó cuenta o clave paga |
| Código original preservado | Hashes contra bytes extraídos del Git upstream fijado | PASS; atributos Git desactivan normalización en el material auditado |
| Cambios propios limpios | `git diff --check` excluyendo snapshots/runtime/licencias upstream | PASS; whitespace original se conserva para no falsificar copias íntegras |

Las pruebas offline usan PyYAML 6.0.3 para ejecutar la transformación real de config.
El helper principal usa biblioteca estándar y ejecuta PyYAML sólo dentro del entorno
de TrendRadar, cuya dependencia ya lo incluye. CI reproduce estas pruebas en Python 3.12.

## Hallazgos reparados

- Primeros borradores de perfiles compartían demasiado texto: reescritos con métodos,
  restricciones, ejemplos y salidas específicas; control de originalidad revalidado.
- La copia upstream de Political_Agent asignaba un placeholder a `SERPERDEV_API_KEY`.
  Revisión cruzada comprobó que SerperDevTool espera `SERPER_API_KEY`; se repararon
  guard, guía, manifiesto y prueba de preservación/fallo de credencial.
- Import de paquete y llamada incondicional `run()` reparados; tema ahora configurable.
- Retirados entrypoints train/replay/test sin funciones correspondientes en upstream.
- TrendRadar tiene IA activada en la configuración upstream: el helper desactiva IA,
  traducción, notificaciones y filtrado AI en el checkout preparado; se documentan
  variables de entorno que pueden prevalecer sobre YAML.
- Incidente local de validación: el integrador lanzó dos conversiones globales
  solapadas contra el mismo directorio generado. La limpieza de una provocó un
  error de escritura en la otra. Se detuvieron ambos procesos propios y se ejecutó
  una conversión acotada a los cuatro perfiles en fixture aislado con copia exacta
  del conversor y lib. Finalizó con cuatro conversiones correctas. No se afirma
  PASS de una conversión global ni se cambió el conversor para ocultar el incidente.

## Alcance comprobado y límites

No se probaron las 139 herramientas ni todas las APIs; un handshake y una consulta
exitosa no validan la cobertura completa. No se activaron Qdrant, dashboard, PDF,
colecciones periódicas ni análisis con proveedores comerciales.

Political_Agent: fuente real incorporada y reparaciones probadas sin red/modelo,
pero **no** se ejecutó el pipeline CrewAI completo con Ollama y Serper. Conserva
clase EXPERIMENTAL y la limitación aparece en la guía. No se afirma calidad de sus informes.

TrendRadar y digital-war-room: bootstrap y comandos contrastados contra el código
fijado; **no** se arrancaron aquí sus plataformas completas. Config TrendRadar se
probó sobre fixture temporal con la misma función del helper. Los upstream externos
se descargan al preparar; su código no se finge copiado dentro de este commit.

No se instalaron perfiles, skills ni servidores en la configuración personal de Codex.
Las skills se copiaron a una carpeta temporal de prueba, con licencias y referencias.
Los TOML generados son artefactos locales ignorados por Git según convención existente.

Gate independiente de entregable/alcance: **PASS**, sin hallazgos pendientes.
El revisor comprobó también los cuatro TOML nuevos con `tomllib`; el integrador
contrastó íntegramente sus cuerpos con los perfiles fuente tras la conversión aislada.

## Gate remoto

**VERIFIED:** [commit de incorporación b5f8559](https://github.com/rubeabbo/agency-agents-ia-gov/commit/b5f85593476d57470caa705c870393bd2450e8f5)
alcanzable desde `main`. Se descargó el commit desde GitHub y compararon byte a byte
los **51 archivos cambiados** contra el índice local verificado; también coincide
el conjunto de rutas cambiadas. Lectura adicional mediante el conector GitHub de
`divisions.json` y `examples/third-party/political-intelligence/README.md` en el SHA
publicado confirmó etiquetas y contenido.
Actualización fast-forward con SHA esperado; no se reescribió historia.

Comprobaciones GitHub Actions del commit de incorporación:

- [Integración política: PASS](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964496).
- [Divisiones: PASS](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964483).
- [Hermes config rewrite: PASS](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964567).
- [Runbooks: PASS](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964568).
- [Control general de herramientas: FAILURE](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964520).
  La validación del registro de 17 herramientas y del plugin Hermes pasó; el paso
  `test-convert-frontmatter.sh` falló con `Permission denied` al invocar directamente
  `scripts/convert.sh`. Git muestra modo `100644` para convert.sh y lint-agents.sh
  tanto en el baseline `da809642...` como en el commit incorporado. El permiso
  ausente es previo; no se afirma haber ejecutado el CI del baseline (no había runs
  disponibles para ese SHA). No se modifican tests generales ni se oculta el fallo.
- [Test Installer](https://github.com/rubeabbo/agency-agents-ia-gov/actions/runs/39073964454):
  Ubuntu finalizó con **54 passed, 11 failed, 1 xfail**; macOS seguía en ejecución
  al registrar esta evidencia. El primer fallo compara equipos contra una extracción
  de JSON que también recoge `label`, `icon`, `color`; el parser del instalador
  correctamente sólo recoge objetos de división. Ese test, el instalador y el
  formato anidado de `divisions.json` ya existían en el baseline. También hay fallos
  de instalación por investigar; no se atribuyen todos sin reproducción. La selección
  acotada de los cuatro agentes sí pasó y sus conversiones son válidas.

Estado global: **PASS WITH NON-BLOCKING ISSUES** para esta incorporación, con fallos
y estado pendiente del CI general documentados. No equivale a afirmar que
todo el CI del repositorio esté verde. La invocación documentada usa `bash` y la
selección de los cuatro agentes se verificó; el nuevo workflow político pasó en Linux.
