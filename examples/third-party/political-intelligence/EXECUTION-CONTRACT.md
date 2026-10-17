# Integración política IA-Gov — misión y ejecución v1

Fecha: 2026-10-17. Humano: Rube. Nivel N3 (repositorio + fuentes + instalación + validación).

## Misión y autoridad

Pedido: incorporar efectivamente agentes y habilidades gratuitos de los proyectos
indicados en `rubeabbo/agency-agents-ia-gov`, respetando la arquitectura existente,
con cuatro categorías exactas, clasificación, licencias, uso y evidencia en GitHub.
La conversación anterior sólo devuelve referencias opacas: no se presupone su contenido.
Categorías literales: `1. Economy and Political Agents`,
`2. Research Political News and Report`, `3. Geopolitical Trenders`, `4. Conflict Analyst`.
Upstream: `Hack23/riksdagsmonitor`, `marc-shade/world-intel-mcp`,
`sansan0/TrendRadar`, `ayushi-006/Political_Agent`, `lina767/digital-war-room`.
Fuentes de verdad: pedido vigente; `divisions.json`, scripts y convenciones del fork;
árboles Git y licencias de los upstream fijados en `registry.json`.
No se modifican `sources/`, agentes existentes ni licencias de terceros.

## Cobertura, actores y grafo

| Requisito | Productor / nodo | Producto | Validación |
|---|---|---|---|
| R1 Inspección previa | Orquestador / T1 | baseline da8096425684264355f4db14642d197723b19927 | lectura de registro, conversor, linter y CI |
| R2 Licencias y realidad técnica | Integrador / T2 | registro con SHA, tipo, clasificación y límites | licencias y código fuente fijados |
| R3 Cuatro categorías exactas | Integrador / T3 | cuatro divisiones visibles con slugs compatibles | check-divisions, conversión y selección |
| R4 Incorporación efectiva | Integrador / T3 | skills upstream, runtime CrewAI reparado, bootstrap de conectores | hashes, sintaxis, pruebas offline y MCP real |
| R5 Uso y routing | Integrador / T4 | guía Windows/Codex, atribuciones y fallback | revisión cruzada contra pedido |
| R6 Publicación comprobada | Orquestador / T6 | commit en main sin reescribir historia | árbol remoto y lectura de archivos por SHA |

Grafo: T1 → T2 → gate de cobertura → T3 → T4 → T5 (QA independiente) → T6.
Las lecturas independientes de fuentes pueden solaparse. Publicación espera pruebas y revisión.
El orquestador integra y publica; un revisor independiente evalúa y no modifica producción.
Contexto del revisor: este contrato, pedido y archivos cambiados; no credenciales ni corpus del proyecto.

## Decisiones, límites y fallbacks

Cerradas: mantener taxonomía por capacidad; etiquetas literalmente pedidas; no confundir
perfiles Markdown con programas, skills con MCP ni instalación con ejecución validada.
Los cuatro agentes de catálogo serán perfiles funcionales originales, con habilidades externas
atribuidas. Cada skill tendrá entrada portable adaptada y referencia upstream íntegra
sin cambios (hash comprobable); runtimes aislados por proyecto.
No se instala nada en el perfil del usuario ni se configuran secretos; eso no fue solicitado.
No se activan despliegues, notificaciones ni APIs de pago.

Principal de publicación: GitHub conectado, árbol basado en main y actualización fast-forward
con SHA esperado. Alternativa: Git con credenciales ya disponibles. Contingencia: conservar
checkout y reportar bloqueo real. Nunca forzar un push ni sobrescribir cambios concurrentes.
Principal de datos gratuito: world-intel/RSS y fuentes públicas; alternativa: documentos aportados;
contingencia: señalar vacío, nunca inventar datos. Infraestructura y hardware local tienen costo.
Dos reparaciones por defecto; ante fallo sistémico, replantear.

## Gates y salida

Gate previo: trazabilidad R1–R6 y viabilidad de licencias. Gate técnico: divisiones, linter,
conversión Codex, selección, manifiesto/hash y pruebas de rutas normales y de fallo.
Gate independiente: tipos reales, gratuidad condicionada, atribuciones y alcance.
Gate remoto: commit alcanzable desde main y archivos iguales a los verificados.
Salida: cambios publicados con enlaces; limitaciones reales de runtime declaradas en QA.
Registrar versiones, herramientas ejecutadas y resultados; no inventar mediciones de costo.
