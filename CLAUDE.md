# Universidad Vault

Vault de Obsidian para apuntes universitarios. Todo el contenido está en español.

## Estructura

```
Universidad/
├── cursos/
│   └── [ciclo]/                   # e.g. 2026-1
│       └── [Curso]/               # e.g. Motores, PLC, Amplificadores, SeriesTransformadas
│           ├── Formulario.md      # Referencia de fórmulas del curso
│           └── clases/
│               └── sNN/           # Sesión NN
│                   ├── SNN-0 Título.md    # Notas de clase (numeradas por tema)
│                   ├── SNN-1 Tema ...md
│                   └── attachments/       # Imágenes pegadas desde clase
```

## Convenciones para notas

- **Idioma:** Español siempre (incluidos títulos, properties, tags)
- **Nombres de archivo:** `SNN-X Tema NN - Título descriptivo.md` (sin tildes en nombres de archivo)
- **Carpetas de sesión:** `sNN/` en minúsculas (sNN = semana NN, e.g. `s01` = semana 01)
- **Imágenes:** se guardan en `attachments/` dentro de cada sesión, se referencian con `![[nombre.png]]`
- **Fórmulas:** LaTeX con `$$...$$` para bloques y `$...$` inline
- **Estructura de nota:** Encabezados `##` para secciones principales, `###` para subsecciones
- **Frontmatter:** YAML con `title`, `tags`, `date` como mínimo en notas nuevas (e.g. `date: 2026-03-29`)
- **Bibliografía:** Sección `## Bibliografía` al final con formato APA cuando aplique
- **Listas "Donde:":** Después de una fórmula, listar variables con `- $símbolo$ = descripción`

## Reglas generales

### Sintaxis y formato
- Usar siempre Obsidian Flavored Markdown (wikilinks, callouts, embeds, properties)
- Preferir `[[wikilinks]]` para enlaces internos (Obsidian rastrea renombrados automáticamente) y `[texto](url)` solo para enlaces externos
- Incluir frontmatter YAML en cada nota nueva: `title`, `tags`, `date` como mínimo
- Usar tags jerárquicos cuando tenga sentido (e.g. `#curso/motores`, `#tema/electromagnetismo`)
- Usar callouts `> [!tipo]` para resaltar información importante, advertencias o ejemplos clave

### Contenido y estructura
- Mantener el mismo estilo expositivo de las notas actuales: explicativo, didáctico, con desarrollo paso a paso
- Al crear nuevas notas, seguir la numeración correlativa de la sesión (SNN-X)
- Las carpetas de attachments son por sesión, no globales

### Protección
- No modificar notas existentes a menos que el usuario lo pida explícitamente
- No borrar archivos sin pedir confirmación
- No crear archivos README, índices ni MOCs a menos que se soliciten

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
