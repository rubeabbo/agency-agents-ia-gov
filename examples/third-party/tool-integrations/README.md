# Capacidades externas para agentes reales — guía Windows / Codex

PyModel, Superdesign, Onlook, Streamlit, Superset y Metabase son **herramientas, skills, MCP o aplicaciones externas**. Se utilizan desde los especialistas competentes; **no** son nuevos agentes de Agency Agents ni agentes propios de IA-Gov. En esta reorganización desaparecieron los seis perfiles llamados `Community ... Tool Operator` del catálogo, pero se conservaron los requisitos operativos, decisiones de uso, licencias y fallbacks en [registry.json](registry.json) y esta guía.

## Arquitectura por especialidad

| Área de capacidad | Responsable real | Herramientas opcionales |
| --- | --- | --- |
| Diseño y Experiencia Digital | [UI Designer](../../../design/design-ui-designer.md), [VoltAgent UI Designer](../../../digital-experience/digital-experience-voltagent-ui-designer.md) | PyModel (MCP/skill), Superdesign (skill/CLI) |
| Ingeniería de Aplicaciones | [Frontend Developer](../../../engineering/engineering-frontend-developer.md), [VoltAgent Fullstack Developer](../../../application-development/application-development-voltagent-fullstack-developer.md) | Onlook como editor visual, cuando exista una instancia compatible |
| Inteligencia de Datos y BI | [Dashboard Engineer](../../../data-intelligence/data-intelligence-dashboard-engineer.md) + [VoltAgent Data Analyst](../../../data-intelligence/data-intelligence-voltagent-data-analyst.md) | Streamlit, Metabase y Superset, según infraestructura y datos |
| Calidad y Validación Digital | [Accessibility Auditor](../../../testing/testing-accessibility-auditor.md), [VoltAgent Accessibility Tester](../../../digital-quality/digital-quality-voltagent-accessibility-tester.md) | PyModel únicamente para comprobaciones estáticas complementarias |

**Regla de activación:** comprobar en el host que la herramienta está instalada, conectada, autorizada y disponible antes de invocarla. Si no existe, continuar con trabajo local o indicar `NOT_CONNECTED`; no crear un agente intermediario para fingir integración.

## Uso en Agency Agents

Los agentes se encuentran en las cuatro divisiones funcionales nuevas y en las divisiones generales ya existentes; los programas externos **no aparecen por separado como agentes**. Elegir un especialista en Agency Agents/Codex no instala el programa que pueda utilizar.

```bash
# Desde la carpeta local del fork actualizado y en Git Bash
bash scripts/convert.sh --tool codex
bash scripts/install.sh --tool codex --list agents
bash scripts/install.sh --tool codex --agent dashboard-engineer,voltagent-fullstack-developer,voltagent-ui-designer --dry-run
```

En Agency Agents seleccioná la carpeta local de tu fork en **Configuración → Catálogo → Usa tu propio clon → Elija carpeta…**. Si habías instalado los operadores ficticios anteriormente, quitá esas instalaciones obsoletas: que desaparezcan del repositorio **no asegura** que el cliente haya limpiado sus archivos locales.

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

**No automatizamos su instalación ni lo tratamos como una integración MCP de Codex comprobada.** Frontend Developer sirve para planificar y auditar el intercambio de código con el editor cuando exista una instancia accesible y autorización explícita. No crear cuentas, gastar tokens ni usar datos sensibles por defecto.

### 4. Streamlit (ruta FREE-FIRST para dashboards Python)

En **PowerShell** y dentro de una carpeta de proyecto independiente (no dentro del código de Agency Agents):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install streamlit
.\.venv\Scripts\python.exe -m streamlit hello
```

No se activa ningún `.ps1`: el intérprete se ejecuta directamente, lo que evita problemas frecuentes de `ExecutionPolicy`. Dashboard Engineer puede producir un `app.py` y un `requirements.txt` auditables. **Community Cloud es opcional** y no debe utilizarse para datos internos/sensibles sin aprobación. Fuente: [Streamlit](https://github.com/streamlit/streamlit).

### 5. Apache Superset (BI más pesado)

Superset ofrece plataforma SQL, API y dashboards; se instala sobre una infraestructura autorizada. [La guía oficial de Docker Compose](https://superset.apache.org/docs/installation/docker-compose/) indica que el método rápido es para desarrollo, **no producción**; tampoco existe soporte oficial de instalación nativa Windows. Para pruebas desde Windows, evaluar WSL2/Linux y Docker, recursos y configuración antes de proceder. No exponer contraseñas de ejemplo, bases sensibles o puertos públicos.

Cuando haya una instancia corriendo, Dashboard Engineer podrá preparar contratos de datasets, gráficos y filtros; sólo **ejecutar** cambios si hay un método de acceso auténticamente conectado.

### 6. Metabase (BI sencillo autohospedado)

La edición abierta es **AGPL**, gratuita para autohospedar; las ediciones comerciales tienen otras condiciones. Podés evaluar el [inicio oficial para Metabase OSS](https://www.metabase.com/start/oss) en Docker o Java. Un laboratorio local en Docker no es por sí solo una instalación productiva; necesita datos persistentes, permisos, copias de seguridad y actualización.

Antes de automatizar operaciones por [la API de Metabase](https://www.metabase.com/docs/latest/api), verificar versión, endpoint y credenciales autorizadas. Para aplicaciones cerradas con dashboards incrustados, revisar las obligaciones AGPL/licencia de embedding antes de prometer integración sin costo.


## Política de selección y validación

- **Auditoría/diseño UI:** UI Designer → PyModel cuando existe su MCP local → verificación visual real y accesibilidad por un especialista distinto.
- **Bocetos e iteraciones estéticas:** UI Designer → Superdesign sólo con credenciales/créditos permitidos → Frontend Developer implementa sobre el código editable.
- **Edición visual de código:** Frontend Developer / Fullstack Developer → Onlook sólo con una instancia accesible y compatibilidad de proyecto, manteniendo un diff controlado.
- **Dashboard Python pequeño:** Data Analyst (métricas y fuentes) → Dashboard Engineer (Streamlit) → Data Visualization Engineer / QA.
- **BI autoservicio ya autohospedado:** Dashboard Engineer (Metabase OSS), verificando obligaciones AGPL y permisos.
- **BI complejo ya operado en infraestructura Linux/containers:** Dashboard Engineer (Superset), con pruebas de seguridad, acceso y rendimiento.

No equiparar GitHub con un programa instalado ni con un servidor MCP disponible. El registro es documentación de capacidades, no una conexión automática. La elección final depende del encargo y del consentimiento del responsable humano. Todas las herramientas externas conservan su licencia y sus condiciones independientes.
