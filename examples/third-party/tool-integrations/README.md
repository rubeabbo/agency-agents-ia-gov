# Integraciones externas para los agentes de Agency Agents

Esta carpeta complementa el catálogo de especialistas de `rubeabbo/agency-agents-ia-gov` con **seis capacidades externas**: PyModel, Superdesign, Onlook, Streamlit, Apache Superset y Metabase. Se documentan en [registry.json](registry.json) y disponen de *community tool operators* instalables como perfiles de agente.

> **Separación de identidades:** los operadores son adaptadores comunitarios del fork, **no agentes oficiales de las marcas y no agentes originales de IA-Gov**. Los proveedores mantienen sus respectivas autorías, licencias y condiciones de sus productos.
>
> **Qué se ha hecho en GitHub:** añadir perfiles Markdown y un registro de enrutamiento. **Qué NO se ha hecho:** instalar software en Windows/Codex, iniciar sesión, activar MCP, conectar una base de datos ni verificar funcionamiento local. Agency Agents **no ejecuta** el software del proveedor por el mero hecho de ver su adaptador en el catálogo.

## Matriz de capacidades y compatibilidad

| Herramienta (origen) | Qué se integra | Agente operador en Agency Agents | Requisito / licencia |
| --- | --- | --- | --- |
| [PyModel designer-skill](https://github.com/PyModel/designer-skill) | Skill de diseño + MCP local; preflight, referencias y controles estáticos | [Community PyModel Tool Operator](../../../design/design-community-pymodel-tool-operator.md) | Node.js 22+; núcleo sin API key; MIT |
| [Superdesign skill](https://github.com/superdesigndev/superdesign-skill) | Skill + CLI y servicio de diseño con drafts | [Community Superdesign Tool Operator](../../../design/design-community-superdesign-tool-operator.md) | Node/npm, cuenta y login; cuotas del servicio por verificar; skill MIT |
| [Onlook](https://github.com/onlook-dev/onlook) | Editor visual de código; colaboración opcional por interfaz manual | [Community Onlook Tool Operator](../../../design/design-community-onlook-tool-operator.md) | Editor OSS Apache-2.0; producto alojado nuevo en acceso anticipado; autohospedaje puede requerir claves/servicios |
| [Streamlit](https://github.com/streamlit/streamlit) | Framework Python para apps y dashboards | [Community Streamlit Tool Operator](../../../engineering/engineering-community-streamlit-tool-operator.md) | Python, venv; Apache-2.0; software local gratuito |
| [Apache Superset](https://github.com/apache/superset) | BI SQL y dashboards en instancia autorizada | [Community Apache Superset Tool Operator](../../../engineering/engineering-community-superset-tool-operator.md) | Apache-2.0; Docker/Linux para laboratorio; sin soporte oficial nativo Windows |
| [Metabase](https://github.com/metabase/metabase) | BI y dashboards sobre bases conectadas | [Community Metabase Tool Operator](../../../engineering/engineering-community-metabase-tool-operator.md) | OSS AGPL autohospedado; componentes comerciales bajo licencia separada |

La **versión distribuida del programa, la skill y el MCP original permanecen en sus repositorios de origen**. Estos adaptadores no copian código fuente ni hacen pasar servicios externos por agentes propios.

## Cómo aparecen en Agency Agents

La aplicación nativa selecciona un catálogo local. Primero, desde un clon local del fork actualizado, `git pull`; después, en Agency Agents abrí **Configuración → Catálogo → Usa tu propio clon → Elija carpeta…** y elegí esa carpeta. Refrescá el catálogo y buscá `Community`. Instalá los operadores que necesites en Codex desde la interfaz.

Alternativamente, desde **Git Bash** dentro de tu fork:

```bash
bash scripts/convert.sh --tool codex
bash scripts/install.sh --tool codex --list agents
bash scripts/install.sh --tool codex --agent community-pymodel-tool-operator,community-superdesign-tool-operator,community-onlook-tool-operator,community-streamlit-tool-operator,community-apache-superset-tool-operator,community-metabase-tool-operator --dry-run
```

Si el listado y la previsualización son correctos, **y el usuario autoriza instalar los perfiles**, quitar `--dry-run`. Eso instala **instrucciones de agentes**, no los programas externos.

## Cómo activar realmente las herramientas (Windows + Codex)

### 1. PyModel (primera opción para revisar UI)

El repositorio documenta un núcleo sin API key y un servidor MCP local. **Primero verificá Node 22+** y que tu versión de Codex tenga la configuración MCP correspondiente. Para instalar **la skill**, la instrucción upstream es:

```powershell
node --version
npx skills add PyModel/designer-skill --skill designer-skill -g -y
```

Para registrar **el MCP local**, en Codex CLI:

```powershell
codex mcp add designer-skill -- npx -y @pymodel/designer-skill-mcp
```

Verificá que estén expuestos los tres instrumentos mínimos `get_preflight_brief`, `dispatch_intent` y `review_and_gate`. Según el repositorio hay herramientas adicionales accesibles al instalar el servidor; **no se copian como agentes por separado**. Algunas referencias Niblet son opcionales y externas. **Nunca** declarar una interfaz validada sólo por aprobar comprobaciones estáticas.

Fuente: [setup y contrato de herramientas de PyModel](https://github.com/PyModel/designer-skill#setup).

### 2. Superdesign (borradores visuales de alta calidad)

Instalación de la skill en el cliente que vayas a utilizar:

```powershell
npx skills add superdesigndev/superdesign-skill
npm install -g @superdesign/cli@latest
superdesign login
```

La última línea abre un proceso de autenticación. **No se ejecuta por cuenta del usuario ni se presupone saldo de créditos**. El repositorio de skill es MIT, pero las cuotas y condiciones del servicio de generación son independientes. Usar cuando su ventaja visual justifique login, créditos y transferencia de contexto; en otros casos continuar con UI Designer y PyModel.

Fuente: [instalación de Superdesign](https://github.com/superdesigndev/superdesign-skill#install).

### 3. Onlook (edición visual de aplicaciones)

La plataforma **nueva** alojada figura como acceso anticipado con lista de espera. El repositorio GitHub corresponde al editor visual OSS, especialmente enfocado en **Next.js y Tailwind**. Para correrlo localmente, [la guía oficial](https://docs.onlook.com/self-hosting/docker-compose) exige un entorno significativo (Docker, Bun, Node, dependencias de base y variables de entorno). Algunas capacidades de IA requieren credenciales de OpenRouter, CodeSandbox u otros servicios.

**No automatizamos su instalación ni lo tratamos como una integración MCP de Codex comprobada.** El operador sirve para planificar y auditar el intercambio de código con el editor cuando exista una instancia accesible y autorización explícita. No crear cuentas, gastar tokens ni usar datos sensibles por defecto.

### 4. Streamlit (ruta FREE-FIRST para dashboards Python)

En **PowerShell** y dentro de una carpeta de proyecto independiente (no dentro del código de Agency Agents):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install streamlit
.\.venv\Scripts\python.exe -m streamlit hello
```

No se activa ningún `.ps1`: el intérprete se ejecuta directamente, lo que evita problemas frecuentes de `ExecutionPolicy`. El operador puede producir un `app.py` y un `requirements.txt` auditables. **Community Cloud es opcional** y no debe utilizarse para datos internos/sensibles sin aprobación. Fuente: [Streamlit](https://github.com/streamlit/streamlit).

### 5. Apache Superset (BI más pesado)

Superset ofrece plataforma SQL, API y dashboards; se instala sobre una infraestructura autorizada. [La guía oficial de Docker Compose](https://superset.apache.org/docs/installation/docker-compose/) indica que el método rápido es para desarrollo, **no producción**; tampoco existe soporte oficial de instalación nativa Windows. Para pruebas desde Windows, evaluar WSL2/Linux y Docker, recursos y configuración antes de proceder. No exponer contraseñas de ejemplo, bases sensibles o puertos públicos.

Cuando haya una instancia corriendo, el operador podrá preparar contratos de datasets, gráficos y filtros; sólo **ejecutar** cambios si hay un método de acceso auténticamente conectado.

### 6. Metabase (BI sencillo autohospedado)

La edición abierta es **AGPL**, gratuita para autohospedar; las ediciones comerciales tienen otras condiciones. Podés evaluar el [inicio oficial para Metabase OSS](https://www.metabase.com/start/oss) en Docker o Java. Un laboratorio local en Docker no es por sí solo una instalación productiva; necesita datos persistentes, permisos, copias de seguridad y actualización.

Antes de automatizar operaciones por [la API de Metabase](https://www.metabase.com/docs/latest/api), verificar versión, endpoint y credenciales autorizadas. Para aplicaciones cerradas con dashboards incrustados, revisar las obligaciones AGPL/licencia de embedding antes de prometer integración sin costo.

## Criterio de selección automático, con validación humana

- **Diseñar/revisar interfaz:** UI Designer → PyModel (MCP real si conectado) → revisión renderizada independiente.
- **Crear propuestas visuales o variaciones:** UI Designer → Superdesign (si hay login, créditos y permiso) → Frontend Developer.
- **Editar visualmente código web existente:** Onlook sólo si hay editor operativo y acceso autorizado; fallback Frontend Developer.
- **Dashboard ligero y Python:** Data Analyst → Community Dashboard Engineer → Streamlit → revisión funcional y visual.
- **Dashboard para usuarios de bases SQL con baja fricción de consulta:** Metabase OSS cuando ya existe infraestructura adecuada.
- **BI de mayor escala y opciones complejas de modelado/visualización:** Apache Superset si la infraestructura, permisos y operación lo justifican.

No confundir el [registro de herramientas de desarrollo soportadas por la aplicación](../../../tools.json) con este `registry.json`: el primero enumera **hosts de agentes** como Codex; el segundo enumera **herramientas externas que esos agentes podrían usar**. Modificar `tools.json` para añadir Streamlit o Onlook como si fueran otro Codex sería técnicamente incorrecto.

## Política de control y pruebas

Un adaptador siempre declara uno de estos estados: `READY` cuando la conexión y la autorización están observadas; `NOT_CONNECTED` cuando falta configuración o ejecución; `BLOCKED` por acceso, costo, credenciales o privacidad. Solo se afirma instalación tras verificar la máquina cliente. No se hacen compras, despliegues, migraciones de datos, suscripciones ni credenciales en GitHub.

La salida de una tarea debe preservar editable el resultado, describir el papel de cada agente/herramienta y dejar registro de métricas y pruebas realmente ejecutadas, sin convertir un análisis o mockup en un producto que se afirme desplegado.
