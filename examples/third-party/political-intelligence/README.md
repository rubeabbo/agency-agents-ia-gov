# Política, economía, tendencias y conflictos — IA-Gov

Integración revisada el **2026-10-17**. Software reutilizable sin tarifa de licencia;
cuentas, APIs, modelos, hardware y conectividad conservan sus propios costos y condiciones.
**CORE / ÚTIL / EXPERIMENTAL es una valoración IA-Gov**, no un benchmark ni certificación upstream.

## Las cuatro categorías

Estas etiquetas se registran literalmente en `divisions.json`. Los directorios usan
slugs compatibles con la aplicación y sus scripts. No se renombra ninguna división previa.

| Categoría exacta | Agente del catálogo | Clase | Ubicación |
|---|---|---|---|
| 1. Economy and Political Agents | Political Economy Analyst | CORE | [economy-political](../../../economy-political/economy-political-analyst.md) |
| 2. Research Political News and Report | Political News Analyst | CORE | [political-news](../../../political-news/political-news-analyst.md) |
| 3. Geopolitical Trenders | Geopolitical Trend Analyst | ÚTIL | [geopolitical-trends](../../../geopolitical-trends/geopolitical-trends-analyst.md) |
| 4. Conflict Analyst | Conflict Evidence Analyst | ÚTIL | [conflict-analysis](../../../conflict-analysis/conflict-analysis-analyst.md) |

Son **cuatro perfiles de instrucciones originales para Agency/Codex**, no cuatro
programas descargados de terceros. La especialidad organiza la taxonomía; el proveedor
es una capacidad asociada. No se crean agentes ficticios “operador de herramienta”.
`ia-gov/` y las áreas anteriores se preservan.

## Qué se incorporó efectivamente

| Elemento / procedencia | Tipo real y clasificación | Incorporación / límite |
|---|---|---|
| Hack23/riksdagsmonitor | Seis skills de método, clase por skill abajo | Cada entrada portable adapta el método y distribuye el original íntegro, licencia y hash. No incluye ni ejecuta su newsroom, Actions, backend o MCP sueco. |
| marc-shade/world-intel-mcp | Conector MCP + CLI, **CORE** | Preparación reproducible del código externo en SHA fijo y entorno Python aislado. No se copia su runtime al catálogo ni se afirma que sea un agente. |
| sansan0/TrendRadar | Aplicación recolectora + MCP, **ÚTIL** | Preparación externa en SHA fijo, separada de la licencia MIT del fork. La configuración local preparada desactiva IA y notificaciones; requiere recolectar datos antes de consultarlos. |
| ayushi-006/Political_Agent | Runtime multiagente CrewAI ejecutable, **EXPERIMENTAL** | Código real copiado en [runtime/political-agent](runtime/political-agent), con cuatro roles y tres archivos reparados. Necesita Ollama/Mistral y cuenta Serper; no se garantiza ejecución gratuita ilimitada. |
| lina767/digital-war-room | Aplicación multiagente OSINT, **EXPERIMENTAL** | Bootstrap externo fijado; servidor y UI se ejecutan aparte. Su síntesis completa depende de Anthropic/OpenAI: **no es la ruta integral gratuita**. Sin claves, health/docs no prueban análisis operativo. |

El [registro legible por máquinas](registry.json) contiene repositorios, SHA exacto,
licencia, archivos originales/modificados y hashes. [ATTRIBUTIONS.md](ATTRIBUTIONS.md)
define qué se copió y qué sólo se conecta. No se incluyen otros proyectos “etc.” sin verificar.

## Skills utilizables

| Skill invocable | Clase | Categoría principal | Método |
|---|---|---|---|
| `$polintel-economic-policy-analysis` | CORE | 1. Economy and Political Agents | Mecanismo fiscal/monetario, financiación y distribución |
| `$polintel-political-science-analysis` | ÚTIL | 1. Economy and Political Agents | Instituciones, coaliciones e incentivos |
| `$polintel-investigative-journalism` | CORE | 2. Research Political News and Report | Registro de afirmaciones, documentos y corroboración |
| `$polintel-comparative-politics-reporting` | ÚTIL | 2. Research Political News and Report | Comparaciones con universo y período coherentes |
| `$polintel-global-government-analysis` | ÚTIL | 3. Geopolitical Trenders | Gobernanza, contexto internacional y tendencia |
| `$polintel-intelligence-analysis-techniques` | CORE | 4. Conflict Analyst | Hipótesis competidoras, supuestos y escenarios |

Fuente: [skills de Riksdagsmonitor en la versión auditada](https://github.com/Hack23/riksdagsmonitor/tree/7a67743488e2628ba339eb95785a80f40285b89f/.github/skills).
Cada carpeta en [agents/political-intelligence/skills](../../../agents/political-intelligence/skills)
contiene `SKILL.md`, `LICENSE.txt` y `references/upstream-SKILL.md`.
El original conserva contexto sueco, ejemplos históricos, enlaces relativos a su
repositorio y reglas editoriales propias. **La entrada portable delimita qué aplicar**;
no se importan como obligaciones de este fork sus workflows ni publicaciones.
Las skills no instalan herramientas ni convierten un modelo en fuente de datos actual.

## Routing y fallback

1. **Arquitecto** fija pregunta, país, período, corte, producto y necesidad de herramientas.
2. **Recopilador** reutiliza evidencia existente; el agente funcional elige método y fuentes.
3. Economía → Political Economy Analyst; noticia/informe → Political News Analyst;
   cambio internacional → Geopolitical Trend Analyst; conflicto → Conflict Evidence Analyst.
4. World Intel aporta datos públicos disponibles; TrendRadar aporta recolección/RSS local.
   Descubrir las herramientas MCP presentes antes de invocarlas. No duplicar recolección.
5. Cerbero revisa afirmaciones, fuentes, fechas, alternativas y vacíos. Rube decide uso final.

**Principal:** conectores gratuitos y documentos primarios. **Alternativa:** RSS/documentos
oficiales y datos abiertos descargados. **Contingencia:** corpus aportado con fecha y
vacíos explícitos. Ante 401/403, credenciales ausentes, 429 o caída, no inventar resultados,
no inferir que no hubo eventos y no pasar automáticamente a una API de pago.
Mantener el idioma solicitado y consultar fuentes locales; la cobertura RSS no representa
por sí misma toda una región ni toda la opinión pública.

## Preparación en Windows

Requisitos: Git, Python **3.12** para una base común (World Intel ≥3.11;
TrendRadar ≥3.12; Political_Agent ≥3.10 y <3.14), venv y pip. El comando `python`
debe apuntar a un intérprete real, no al acceso directo de Microsoft Store.
Ejecutar desde la raíz del clon de este fork. No se instala nada por clonar el catálogo.

```powershell
python scripts/political_intelligence.py verify
python scripts/political_intelligence.py list
python scripts/political_intelligence.py prepare world-intel-mcp --install-deps
```

`prepare` descarga el upstream fijado bajo `.cache/political-intelligence/` y crea
un venv por proyecto. `--install-deps` instala dependencias de ese proyecto;
sin esa opción sólo prepara el código (Political_Agent ya está copiado).
Nunca inicia análisis, webhooks, colecciones periódicas ni servidores. Las dependencias
transitivas siguen las restricciones upstream: el SHA fija el código, **no un lock de PyPI**.
Rechaza otro SHA, otro origin o cambios locales en un checkout existente: preservarlos
y usar `--cache` con una carpeta nueva. TrendRadar modifica intencionalmente su config
local; por ello una segunda preparación requiere otra carpeta, no un reset destructivo.

```powershell
# Servidor MCP stdio World Intel; el proceso lo iniciará Codex al necesitarlo.
codex mcp add ia-gov-world-intel -- "$PWD/.cache/political-intelligence/world-intel-mcp-venv/Scripts/python.exe" -m world_intel_mcp.server
codex mcp list
```

Si el módulo no expone arranque `-m` en una versión futura, usar el entrypoint
`world-intel-mcp.exe` del mismo venv; el registro fija una versión concreta.
No pasar secretos como valores literales en comandos compartidos ni guardarlos en el repositorio.
La instalación MCP en el perfil del usuario es un paso manual de la guía, **no realizado por esta integración**.

### TrendRadar

```powershell
python scripts/political_intelligence.py prepare TrendRadar --install-deps
# Recolectar una vez: sigue siendo una consulta de red y puede tardar.
Push-Location .cache/political-intelligence/TrendRadar
& ../TrendRadar-venv/Scripts/python.exe -m trendradar
Pop-Location
codex mcp add ia-gov-trendradar -- "$PWD/.cache/political-intelligence/TrendRadar-venv/Scripts/python.exe" -m mcp_server.server --project-root "$PWD/.cache/political-intelligence/TrendRadar"
```

Revisar `config/config.yaml` y sus feeds/keywords según país e idioma. El helper
aplica un perfil sin IA externa ni notificaciones y conserva RSS/recolección.
El modo AI de filtrado también debe estar desactivado mediante `filter.method: keyword`;
el helper lo fija. Las llamadas MCP de envío o mutación de configuración requieren
la instrucción correspondiente del usuario; agregar un MCP no autoriza envíos.
Variables de entorno como `AI_ANALYSIS_ENABLED` y `AI_TRANSLATION_ENABLED` pueden
prevalecer sobre YAML: no reutilizar un entorno que las habilite. Revisar también
credenciales y opciones de notificación antes de recolectar; el helper no altera
el entorno global del equipo.

### Political_Agent — runtime real, experimental

```powershell
python scripts/political_intelligence.py prepare Political_Agent --install-deps
# Instalar Ollama por su canal oficial y descargar el modelo local.
ollama pull mistral
# SERPER_API_KEY debe existir en el entorno; no se provee ninguna clave.
New-Item -ItemType Directory -Force .cache/political-report | Out-Null
Push-Location .cache/political-report
& ../political-intelligence/Political_Agent-venv/Scripts/python.exe -m ai_latest_development.main --topic "política económica argentina"
Pop-Location
```

Usa el servicio Ollama en `localhost:11434`. Ejecutar en una carpeta de salida dedicada:
upstream escribe `report.md` varias veces y el FileWriterTool puede escribir archivos.
El texto final necesita verificación de citas y actualidad. Se corrigieron import de paquete,
ejecución al importar, tema fijo, nombre de variable de Serper, sobreescritura
del secreto placeholder y entrypoints inexistentes; se conservan
los cuatro roles y la lógica original. El manifiesto identifica exactamente los cambios.
La prueba sin Serper/Ollama no acredita un informe end-to-end. No se sustituye Serper
por otra búsqueda ni se declara “sin APIs” sólo porque el modelo es local.

### digital-war-room — laboratorio externo

```powershell
python scripts/political_intelligence.py prepare digital-war-room --install-deps
Push-Location .cache/political-intelligence/digital-war-room/backend
& ../../digital-war-room-venv/Scripts/python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
Pop-Location
```

UI opcional: Node 18+, `npm install` y `npm run dev` dentro del checkout externo;
no es necesaria para los cuatro perfiles. Consultar `docs/API-KEYS.md` de esa versión.
No iniciar análisis de síntesis completa sin decidir proveedor y costo; para la ruta
free-first usar Conflict Evidence Analyst + World Intel + fuentes públicas.

## Invocarlos desde Agency Agents y Codex

Seleccionar este clon en el mecanismo de catálogo propio de Agency Agents y actualizarlo.
Buscar las cuatro etiquetas o nombres de perfil. Su aparición depende de que la app
esté leyendo este clon, no el catálogo original. Agregar perfiles no instala conectores.

Git Bash, usando los conversores **existentes** del repositorio:

```bash
bash scripts/check-divisions.sh
bash scripts/convert.sh --tool codex
bash scripts/install.sh --tool codex --division economy-political,political-news,geopolitical-trends,conflict-analysis --dry-run
# Tras revisar la selección, instalar quitando --dry-run.
```

Los TOML se generan en `integrations/codex/agents/` (ignorados por Git) y se instalan
en `~/.codex/agents/`. Mantener el clon accesible: los perfiles apuntan a sus skills y guía.
Para que Codex descubra las skills como tales, instalarlas en el proyecto de trabajo:

```powershell
python scripts/political_intelligence.py install-skills --destination .agents/skills
```

El helper incluye licencia y referencia y rechaza colisiones antes de copiar.
No modifica skills globales preexistentes. Abrir una nueva sesión de Codex si el runtime
no recarga el inventario. [Skills oficiales](https://developers.openai.com/codex/skills)
y [configuración MCP oficial](https://developers.openai.com/codex/mcp) explican ambos mecanismos.

Ejemplos de pedido:

```text
Usá Political Economy Analyst. Leé el perfil y las skills del clon IA-Gov.
Analizá la medida [X], Argentina, período [Y], corte [fecha]. Separá evidencia,
mecanismo, impactos distributivos y dos escenarios. Citá fuentes y vacíos.

Usá $polintel-intelligence-analysis-techniques sobre este corpus.
Construí hipótesis competidoras, evidencia contraria y señales de cambio;
no hagas búsquedas ni declares actualidad fuera del corpus.

Usá Political News Analyst y el MCP ia-gov-trendradar si está disponible.
Prepará un informe de los últimos siete días: fecha del hecho/publicación,
fuentes independientes, duplicados, política/economía e incertidumbres.
```

## Dependencias gratuitas y límites

| Componente | Base gratuita / límites comprobados o pendientes |
|---|---|
| Skills/perfiles | Texto local; requieren un modelo/harness. Esta integración no otorga acceso gratuito a Codex ni a modelos comerciales. |
| World Intel | Código MIT; MCP, httpx, Pydantic, feedparser, Click, Jinja2 y Rich locales. APIs públicas pueden fallar o limitar. Vector/Qdrant, PDF y dashboard son extras no necesarios para stdio. |
| World Intel: FRED/EIA | El código exige `FRED_API_KEY` / `EIA_API_KEY`; sin ellas esas herramientas devuelven error. Registro y cuota del proveedor deben verificarse en su cuenta; no se prometen llamadas ilimitadas. |
| World Intel: ACLED | Exige `ACLED_EMAIL` y `ACLED_PASSWORD`, OAuth y acceso de la cuenta. MIT del conector no licencia los datos ACLED ni garantiza elegibilidad gratuita. Alternativa: UCDP/HDX y fuentes públicas con sus propios términos. |
| World Intel: throttling | Código fija Nominatim ≥1,1 s y serialización Yahoo ≥600 ms. Son controles internos, **no cuotas concedidas por proveedores**. Otras fuentes no tienen necesariamente limitación local. |
| RSS/GDELT/Yahoo/UCDP/HDX | Disponibilidad, cobertura, términos, límites y antigüedad se comprueban por consulta. No se verificó una cuota numérica universal; tratar 429/401/403 y datos stale explícitamente. |
| TrendRadar | Python, SQLite, RSS/recolección local; proveedor NewsNow/feeds puede limitar o caer. IA LiteLLM, traducción, Jina y canales externos tienen condiciones propias. El perfil preparado desactiva IA y envíos; no representa análisis ilimitado gratis. |
| Political_Agent | CrewAI y Ollama/Mistral local requieren RAM/disco/CPU. Serper exige cuenta/clave; trial o créditos, si disponibles, no equivalen a gratuidad permanente. No se verificó ni se asignó una cuota al usuario. |
| digital-war-room | FastAPI/React locales, fuentes y claves por integración. Código MIT; síntesis con Anthropic/OpenAI tiene condiciones/costo propios. No se anuncia inferencia local equivalente sin prueba. |

Se revisaron fuentes públicas y código, no las cuentas ni planes del usuario.
World Intel guarda por defecto su caché local bajo `~/.cache/world-intel-mcp/`;
su venv aislado no implica que todos sus archivos de datos vivan dentro del clon.
Ninguna automatización, notificación, despliegue o gasto queda habilitado por estos archivos.
Ver [QA.md](QA.md) para distinguir pruebas ejecutadas de validaciones pendientes.
