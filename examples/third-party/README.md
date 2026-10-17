# Agentes comunitarios externos — catálogo Agency Agents

Estos perfiles se incorporan al **fork de Agency Agents** para ampliar su catálogo. **No se atribuyen a la autoría original de IA-Gov** ni reemplazan a los agentes propios (Arquitecto, Cerbero, Graffitero y otros). El proveedor original y la licencia se documentan en cada perfil.

## Agentes incorporados

| Especialista (nombre en Agency Agents) | Ruta en el fork | Procedencia | Distinción |
| --- | --- | --- | --- |
| VoltAgent UI Designer | [design/design-voltagent-ui-designer.md](../../design/design-voltagent-ui-designer.md) | [UI Designer de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/ui-designer.md) | Versión externa, útil como alternativa o segunda revisión de diseño |
| VoltAgent UX Researcher | [design/design-voltagent-ux-researcher.md](../../design/design-voltagent-ux-researcher.md) | [UX Researcher de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/08-business-product/ux-researcher.md) | Alternativa para validación de UX, entrevistas y evidencia |
| VoltAgent Design Bridge | [design/design-voltagent-design-bridge.md](../../design/design-voltagent-design-bridge.md) | [Design Bridge de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/design-bridge.md) | Traduce un diseño o DESIGN.md verificable a instrucciones de implementación |
| VoltAgent Data Analyst | [engineering/engineering-voltagent-data-analyst.md](../../engineering/engineering-voltagent-data-analyst.md) | [Data Analyst de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/data-analyst.md) | Calidad de datos, contratos de indicadores, análisis y reportes |
| VoltAgent Fullstack Developer | [engineering/engineering-voltagent-fullstack-developer.md](../../engineering/engineering-voltagent-fullstack-developer.md) | [Fullstack Developer de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/fullstack-developer.md) | Aplicaciones de punta a punta: DB, API, frontend, autenticación y tests |
| VoltAgent Accessibility Tester | [testing/testing-voltagent-accessibility-tester.md](../../testing/testing-voltagent-accessibility-tester.md) | [Accessibility Tester de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/accessibility-tester.md) | Pruebas y evidencia de accesibilidad complementarias al auditor existente |
| Community Dashboard Engineer | [engineering/engineering-community-dashboard-engineer.md](../../engineering/engineering-community-dashboard-engineer.md) | Adaptación comunitaria inspirada en [Data Analyst de VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/data-analyst.md) | Implementación especializada de dashboards; **no** es un agente oficial de VoltAgent |

**Licencia de la fuente externa:** MIT, copyright (c) 2025 VoltAgent. Se conserva el texto completo de la [licencia original](LICENSE-VoltAgent.md), junto con los vínculos y créditos de cada archivo. Los perfiles importados llevan modificaciones de compatibilidad con Agency Agents, pero conservan el playbook de origen.

## Cómo se conectan sin redundancias

La biblioteca Agency Agents ya incluye `UI Designer`, `UX Researcher`, `Data Visualization Engineer`, `Accessibility Auditor` y `Frontend Developer`. Los perfiles nuevos identificados con VoltAgent se preservan por su procedencia y pueden utilizarse como **segundo criterio independiente**, no para que dos agentes editen el mismo documento en paralelo.

Un flujo adecuado para un dashboard es:

**Data Analyst (métricas y fuentes) → Community Dashboard Engineer (aplicación) → Data Visualization Engineer / UI Designer (revisión visual) → Accessibility Tester (prueba independiente) → QA/orquestador (entrega).**

Las aplicaciones, MCP y skills no deben confundirse con perfiles de agente:

- [PyModel designer-skill](https://github.com/PyModel/designer-skill) es una skill + MCP independiente. Su núcleo indica uso sin API key, pero exige instalación separada y herramientas verificadas.
- [Superdesign skill](https://github.com/superdesigndev/superdesign-skill) utiliza skill + CLI/servicio; verificar cuentas y límites gratuitos antes de adoptarlo.
- [Onlook](https://github.com/onlook-dev/onlook) es un entorno visual de desarrollo web.
- [Streamlit](https://github.com/streamlit/streamlit), [Apache Superset](https://github.com/apache/superset) y [Metabase](https://github.com/metabase/metabase) son herramientas de aplicaciones/BI. La disponibilidad de código abierto no garantiza alojamiento gratuito.

## Uso en Codex y Agency Agents

Estos archivos se registraron en las divisiones existentes (`design/`, `engineering/`, `testing/`) que el instalador reconoce por `divisions.json`. **No hace falta agregar una división IA-Gov ni cambiar las personalidades originales.**

Para Codex desde una copia local actualizada de este fork, en **Git Bash para Windows**:

```bash
git pull
bash scripts/convert.sh --tool codex
bash scripts/install.sh --tool codex --list agents
bash scripts/install.sh --tool codex --agent voltagent-data-analyst,voltagent-fullstack-developer,voltagent-ui-designer,voltagent-ux-researcher,voltagent-design-bridge,voltagent-accessibility-tester,community-dashboard-engineer --dry-run
# Quitar --dry-run para instalar, una vez verificada la selección.
```

La aplicación nativa Agency Agents admite un catálogo de **clon local seleccionado por el usuario** además de su biblioteca integrada. Se debe seleccionar la copia local de `rubeabbo/agency-agents-ia-gov` como origen y actualizarla. **Los nuevos archivos en GitHub no modifican automáticamente una instalación local, la biblioteca integrada de la aplicación ni el entorno Codex.**

La disponibilidad para ser invocados depende de la configuración real del cliente Codex; instalar no garantiza delegación autónoma. Mantener un enrutador/instrucción de uso y una validación independiente es parte de IA-Gov.

## Regla de procedencia y privacidad

El directorio `ia-gov/` permanece reservado para los agentes propios. No alterar nombres/autores originales ni afirmar que un perfil externo fue diseñado originalmente por IA-Gov. Cada agente puede acceder solo a la información mínima necesaria; no trasladar datos confidenciales a servicios externos sin autorización.
