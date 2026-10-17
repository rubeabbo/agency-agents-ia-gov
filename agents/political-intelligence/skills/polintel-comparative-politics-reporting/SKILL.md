---
name: polintel-comparative-politics-reporting
description: Comparar instituciones y políticas entre países sin mezclar universos o períodos.
license: Apache-2.0
---

# comparative-politics-reporting — adaptación portable IA-Gov

Modificado por IA-Gov el 2026-10-17 a partir de [Hack23/riksdagsmonitor](https://github.com/Hack23/riksdagsmonitor/blob/7a67743488e2628ba339eb95785a80f40285b89f/.github/skills/comparative-politics-reporting/SKILL.md).
Licencia Apache-2.0; el [original íntegro](references/upstream-SKILL.md) y la
[licencia](LICENSE.txt) se distribuyen juntos. Esta entrada es una adaptación,
no una skill oficial de Hack23 ni el runtime de su newsroom.

## Método

Explicitar unidad de comparación, período y definición. Elegir comparadores por similitud relevante; explicar diferencias institucionales que limiten transferir una conclusión entre países.

Definir primero pregunta, país, horizonte, fecha de corte y fuentes disponibles.
Usar herramientas realmente accesibles; una skill no instala MCP, no obtiene API
keys y no ejecuta búsquedas por sí sola. Sin acceso actual, trabajar con el corpus
aportado e indicar su fecha y lo que no pudo verificarse.

Entregar conclusión, evidencias con URL/fecha, explicación alternativa, confianza
y límites. Separar HECHO VERIFICADO, CLAIM DEL FABRICANTE, BENCHMARK,
EXPERIENCIA DE USUARIOS, INTERPRETACIÓN e HIPÓTESIS cuando apliquen.

Consultar la referencia original sólo para profundizar técnicas del tema.
Sus cifras, ejemplos, reglas suecas y afirmaciones legales son contexto histórico:
verificarlos para el país y fecha del encargo. Sus enlaces relativos se resuelven
contra el árbol upstream fijado en la URL anterior, no contra este fork.
Sus instrucciones de workflows, CI, publicación y archivos de Riksdagsmonitor
no forman parte de esta adaptación ni autorizan acciones externas.
