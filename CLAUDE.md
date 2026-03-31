# Universidad Vault

Vault de Obsidian para apuntes universitarios. Todo el contenido está en español.

## Estructura

```
Universidad/
├── plantillas/                        # Templates para nuevas notas
│   ├── Plantilla - Nota de clase.md
│   ├── Plantilla - Formulario.md
│   └── Plantilla - Ejercicio.md
├── cursos/
│   └── [ciclo]/                       # e.g. 2026-1
│       ├── Dashboard [ciclo].md       # Indice del semestre
│       ├── Evaluaciones.base          # Vista de evaluaciones del ciclo
│       └── [Curso]/                   # e.g. Motores, PLC, Amplificadores, SeriesTransformadas
│           ├── [Curso] MOC.md         # Mapa de contenido del curso
│           ├── Silabo.md              # Silabo del curso
│           ├── Formulario.md          # Referencia de formulas del curso
│           ├── *.base                 # Vistas de base de datos
│           └── clases/
│               └── sNN/              # Semana NN (e.g. s01 = semana 01)
│                   ├── SNN-0 Título.md    # Notas de clase (numeradas por tema)
│                   ├── SNN-1 Tema ...md
│                   └── attachments/       # Imagenes pegadas desde clase
```

## Convenciones para notas

- **Idioma:** Español siempre (incluidos títulos, properties, tags)
- **Nombres de archivo:** `SNN-X Tema NN - Título descriptivo.md` (sin tildes en nombres de archivo)
- **Carpetas de sesión:** `sNN/` en minúsculas (sNN = semana NN, e.g. `s01` = semana 01)
- **Imágenes:** se guardan en `attachments/` dentro de cada sesión, se referencian con `![[nombre.png]]`
- **Fórmulas:** LaTeX con `$$...$$` para bloques y `$...$` inline
- **Estructura de nota:** Encabezados `##` para secciones principales, `###` para subsecciones
- **Bibliografía:** Sección `## Bibliografía` al final con formato APA cuando aplique
- **Listas "Donde:":** Después de una fórmula, listar variables con `- $símbolo$ = descripción`

## Frontmatter

Todas las notas deben tener frontmatter YAML. Los campos dependen del tipo de nota:

### Notas de clase

```yaml
---
title: "Titulo descriptivo"
curso: "[[Curso MOC]]"
unidad: 1
semana: 1
orden: 1
tipo: clase
tags:
  - curso/nombre-curso
  - tipo/clase
  - tema/nombre-del-tema
date: 2026-03-28
---
```

### Formularios

```yaml
---
title: "Formulario - Nombre del curso"
curso: "[[Curso MOC]]"
tipo: formulario
tags:
  - curso/nombre-curso
  - tipo/formulario
date: 2026-03-28
---
```

### Ejercicios

```yaml
---
title: "Titulo del ejercicio"
curso: "[[Curso MOC]]"
unidad: 1
semana: 1
tipo: ejercicio
tags:
  - curso/nombre-curso
  - tipo/ejercicio
  - tema/nombre-del-tema
date: 2026-03-28
---
```

### Silabos

```yaml
---
title: Silabo - Nombre del curso
curso: "[[Curso MOC]]"
tags:
  - curso/nombre-curso
  - silabo
date: 2026-03-29
aliases:
  - Silabo Nombre Curso
---
```

**Nombre de archivo:** `Silabo - Nombre descriptivo del curso.md`

**Estructura de secciones** (en este orden, sin numerar):

1. `## Datos generales` — tabla con Codigo, Ciclo, Carreras, Creditos, Ensenanza, Horas semanales
2. `## Fundamentacion`
3. `## Sumilla`
4. `## Logro general de aprendizaje`
5. `## Unidades y logros especificos de aprendizaje` — cada unidad como `### Unidad N: Nombre (semanas X-Y)` con callout `> [!abstract] Logro especifico` y lista de **Temario**. Separar unidades con `---`
6. `## Metodologia` — párrafo compacto
7. `## Sistema de evaluacion` — fórmula en LaTeX `$$...$$`, tabla con columnas Tipo/Descripcion/Semana/Peso/Observacion, callout `> [!warning] Indicaciones importantes`
8. `## Competencias por carrera` — tabla Carrera/Competencias especificas
9. `## Cronograma de actividades` — una tabla por unidad (`### Unidad N: Nombre`) con columnas Semana/Temas/Evaluaciones. Evaluaciones en **negrita**
10. `## Bibliografia` — subsecciones `### Base` y `### Complementaria`

### MOCs y Dashboards

```yaml
---
title: "MOC - Nombre del curso"
curso: nombre-curso
ciclo: 2026-1
tipo: moc
tags:
  - curso/nombre-curso
  - tipo/moc
date: 2026-03-29
aliases:
  - Curso MOC
---
```

**Property `curso` como wikilink:** En notas de clase, ejercicio, formulario y silabo usar `"[[Curso MOC]]"` para que el MOC aparezca como backlink.

## Tags

Usar 3 jerarquías de tags:

| Jerarquía | Uso | Ejemplos |
| --------- | --- | -------- |
| `curso/` | Identificar el curso | `curso/motores`, `curso/plc`, `curso/amplificadores`, `curso/series-transformadas` |
| `tipo/` | Tipo de nota | `tipo/clase`, `tipo/ejercicio`, `tipo/formulario`, `tipo/referencia`, `tipo/moc`, `tipo/dashboard` |
| `tema/` | Tema específico | `tema/ley-de-ampere`, `tema/histeresis`, `tema/circuito-magnetico` |

Los tags de `tema/` se agregan orgánicamente conforme aparecen nuevos conceptos. No predefinir una taxonomía completa.

## Wikilinks

- Preferir `[[wikilinks]]` para enlaces internos (Obsidian rastrea renombrados automáticamente)
- `[texto](url)` solo para enlaces externos
- **Enlazar solo la primera mención** de un concepto que tenga su propia nota, no cada aparición
- En Formulario.md, agregar línea `Fuente: [[nota origen]]` debajo de cada sección principal

## MOCs y navegación

- Cada curso tiene un **MOC** como punto de entrada (e.g. `Motores MOC.md`)
- El semestre tiene un **Dashboard** que enlaza todos los MOCs (e.g. `Dashboard 2026-1.md`)
- Los MOCs listan todas las notas por semana y contienen el calendario de evaluaciones
- Crear MOCs y Dashboards por defecto al iniciar un nuevo curso o semestre

## Plantillas

Carpeta de plantillas: `plantillas/`

| Plantilla | Uso |
| --------- | --- |
| `Plantilla - Nota de clase.md` | Notas de clase semanales |
| `Plantilla - Formulario.md` | Formulario de fórmulas por curso |
| `Plantilla - Ejercicio.md` | Ejercicios resueltos paso a paso |

Usar la plantilla correspondiente al crear notas nuevas (Ctrl+T en Obsidian).

## Bases

Los archivos `.base` proveen vistas de datos dinámicas (plugin core Bases habilitado):
- `Notas por semana.base` en cada curso: vista tabla agrupada por semana
- `Evaluaciones.base` a nivel de ciclo: vista de silabos y evaluaciones

## Reglas generales

### Sintaxis y formato
- Usar siempre Obsidian Flavored Markdown (wikilinks, callouts, embeds, properties)
- Usar callouts `> [!tipo]` para resaltar información importante, advertencias o ejemplos clave

### Contenido y estructura
- Mantener el mismo estilo expositivo de las notas actuales: explicativo, didáctico, con desarrollo paso a paso
- Al crear nuevas notas, seguir la numeración correlativa de la sesión (SNN-X)
- Las carpetas de attachments son por sesión, no globales

### Evaluaciones
Al resolver evaluaciones, seguir estas reglas:

1. **Analizar detenidamente las imágenes** siempre que estén presentes o se incluyan en la pregunta
2. **Escribir las respuestas en el archivo** de evaluación
3. **Calcular para todas las opciones** — no solo la correcta, sino verificar qué implica cada alternativa
4. **Siempre incluir cálculos, proceso y razonamiento** en el documento para sustentar la respuesta y validar posibles errores
5. **Crear wikilinks hacia los documentos de teoría** que sustentan cada respuesta

### Protección
- No modificar notas existentes a menos que el usuario lo pida explícitamente
- No borrar archivos sin pedir confirmación

## Skills de Obsidian disponibles

Plugin `obsidian-skills` (kepano) instalado. Skills invocables:

| Skill                        | Uso                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| `obsidian:obsidian-markdown` | Crear/editar notas con sintaxis Obsidian (wikilinks, embeds, callouts, properties) |
| `obsidian:obsidian-bases`    | Crear archivos `.base` (tablas/vistas tipo base de datos)                          |
| `obsidian:json-canvas`       | Crear/editar archivos `.canvas` (diagramas con nodos y conexiones)                 |
| `obsidian:obsidian-cli`      | Interactuar con el vault vía CLI                                                   |
| `obsidian:defuddle`          | Extraer markdown limpio de páginas web                                             |

Invocar con `/skill obsidian:<nombre>` cuando sea necesario para respetar la sintaxis específica de Obsidian.
