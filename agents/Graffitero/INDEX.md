# Graffitero — Agent Index

**Status:** active  
**Type:** IA-Gov visual-direction agent  
**Version:** 0.2

## Entry points

- `AGENT.md` — identidad, mandato y reglas operativas del agente.
- `GRAFFITERO_MASTER_PROMPT.md` — prompt maestro de ejecución.
- `manifest.yaml` — metadata y configuración base.
- `skills/` — capacidades reutilizables con prefijo `graffitero-`.
- `runtime/` — protocolo y máquina de estados.
- `contracts/` — contratos de entrada, plan visual y QA.
- `adapters/` — registro de herramientas ejecutoras.
- `policies/` — criterios de representación y control de calidad.
- `tests/` — protocolo y casos de validación.
- `ARCHITECTURE_SOURCES.md` — fuentes arquitectónicas estudiadas.
- `upstream/` — trazabilidad técnica de proyectos externos.

## Regla mental

**Agente = quién trabaja. Skill = qué sabe hacer. Tool = con qué ejecuta. MCP/adapter = cómo se conecta al tool.**

Graffitero es el agente. Sus skills se nombran `graffitero-*`.
