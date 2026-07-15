# Universidad Vault

Vault de Obsidian para apuntes universitarios. Todo el contenido está en español.

## Estructura

```
Universidad/
├── utils/                             # Scripts utilitarios
│   ├── parse_vtt.py                   # Parsea subtítulos VTT de YouTube a texto limpio
│   ├── semana_actual.py               # Calcula la semana del ciclo
│   ├── md_to_docx.py                  # Exporta nota Markdown a Word (APA v7 + LaTeX)
│   └── pngs_a_pdf.py                  # Junta imágenes (PNG/JPG) en un solo PDF, una por página
├── plantillas/                        # Templates para nuevas notas
│   ├── Plantilla - Nota de clase.md
│   ├── Plantilla - Formulario.md
│   ├── Plantilla - Ejercicio.md
│   ├── Plantilla - Evaluacion.md
│   ├── Plantilla - Anuncios.md
│   ├── Plantilla - Silabo.md
│   ├── reference-apa7.docx            # Estilos para export a Word (editable en Word)
│   └── apa-7th.csl                    # Estilo de citas APA 7ma edición
├── docs/                              # Documentación operativa cargable on-demand
│   ├── portal-utp.md                  # Estructura del portal + procedimientos de extracción
│   ├── extraccion-youtube.md          # Procedimiento para transcribir videos
│   └── exportar-docx.md               # Procedimiento para convertir notas a Word
├── cursos/
│   └── [ciclo]/                       # e.g. 2026-1
│       ├── Cursos.md                  # Hub del ciclo: UUIDs, docentes, calendario, patrones
│       ├── Dashboard [ciclo].md
│       ├── Evaluaciones.base
│       └── [Curso]/
│           ├── [Curso] MOC.md
│           ├── Silabo - [Curso].md
│           ├── Formulario - [Curso].md
│           ├── Anuncios.md
│           ├── *.base
│           ├── anuncios-attachments/
│           └── clases/
│               └── sNN/
│                   ├── SNN-X Tema NN - Título.md
│                   └── attachments/
```

## Ciclo activo

Datos del ciclo (UUIDs por curso, docentes, modalidad, fechas, patrones de anuncios) en [`cursos/2026-1/Cursos.md`](cursos/2026-1/Cursos.md).

Cursos del ciclo 2026-1: `Amplificadores`, `PLC`, `MaquinasElectricas`, `SeriesTransformadas`. Ignorar siempre del portal: `RUTA LABORAL ...`, `Ruta Laboral`, `English Discoveries Placement Test`.

## Calendario del ciclo

- Semanas comienzan **lunes** y terminan **domingo** (convención Perú).
- Ciclo dura **18 semanas**. Ciclo 2026-1 → Semana 01 = lunes **23 de marzo de 2026**.
- Para inferir la semana actual: `python utils/semana_actual.py [YYYY-MM-DD]`. Nuevos ciclos se agregan al diccionario `INICIOS_CICLO` del script.
- Cuando el usuario diga "extrae la semana actual" sin número, calcular con el script.
- En el portal, los tabs Foros/Notas/Evaluaciones marcan "Semana NN - Semana actual" — sirve como verificación cruzada.

## Convenciones para notas

- **Idioma:** Español siempre (incluidos títulos, properties, tags).
- **Nombres de archivo:** `SNN-X Tema NN - Título descriptivo.md` (sin tildes).
- **Carpetas de sesión:** `sNN/` en minúsculas (e.g. `s01` = semana 01).
- **Imágenes:** se guardan en `attachments/` dentro de cada sesión, se referencian con `![[nombre.png]]`. Excepción: `anuncios-attachments/` está en la raíz del curso (no por sesión).
- **Fórmulas:** LaTeX con `$$...$$` para bloques y `$...$` inline.
- **Estructura de nota:** Encabezados `##` para secciones principales, `###` para subsecciones.
- **Bibliografía:** Sección `## Bibliografía` al final con formato APA cuando aplique.
- **Listas "Donde:":** Después de una fórmula, listar variables con `- $símbolo$ = descripción`.

## Frontmatter

Toda nota debe tener frontmatter YAML. Tipos disponibles:

| `tipo:`       | `subtipo:` válidos                                  | Plantilla                          | Cuándo usar                                  |
| ------------- | --------------------------------------------------- | ---------------------------------- | -------------------------------------------- |
| `clase`       | —                                                   | `Plantilla - Nota de clase.md`     | Notas teóricas semanales                     |
| `ejercicio`   | —                                                   | `Plantilla - Ejercicio.md`         | Ejercicios resueltos paso a paso             |
| `formulario`  | —                                                   | `Plantilla - Formulario.md`        | Compendio de fórmulas por curso              |
| `evaluacion`  | `pa`, `pc`, `exfn`, `laboratorio`, `cuestionario`   | `Plantilla - Evaluacion.md`        | PA, PC, examen final, laboratorio, autoeval. |
| `anuncios`    | —                                                   | `Plantilla - Anuncios.md`          | Comunicados del docente                      |
| `silabo`      | —                                                   | `Plantilla - Silabo.md`            | Sílabo del curso                             |
| `moc`         | —                                                   | (sin plantilla — ver MOCs vivos)   | Mapa de contenido del curso                  |
| `dashboard`   | —                                                   | (sin plantilla — `Dashboard [ciclo].md`) | Índice del semestre                    |

**Shape mínimo común** (todos los tipos):

```yaml
---
title: "..."
curso: "[[Curso MOC]]"   # Wikilink al MOC del curso (para que aparezca como backlink)
tipo: <tipo>
tags:
  - curso/<slug>         # e.g. curso/series-transformadas
  - tipo/<tipo>          # e.g. tipo/evaluacion
date: 2026-MM-DD
---
```

**Campos adicionales por tipo:**

- `clase` / `ejercicio` / `evaluacion`: `unidad: N`, `semana: N`, `orden: N` (orden numérico dentro de la sesión).
- `evaluacion`: agregar `subtipo: pa | pc | exfn | laboratorio | cuestionario` y tag `subtipo/<subtipo>`.
- `silabo` / `moc`: `aliases: [...]` para referencias cortas.
- `tema/...` tags se agregan orgánicamente conforme aparecen conceptos.

Para el detalle del shape de Sílabo, Evaluación y Anuncios (secciones internas, estructura de tablas, etc.), ver las plantillas correspondientes en `plantillas/`.

## Tags

Usar 4 jerarquías:

| Jerarquía  | Uso                          | Ejemplos                                         |
| ---------- | ---------------------------- | ------------------------------------------------ |
| `curso/`   | Identificar el curso         | `curso/motores`, `curso/plc`, `curso/series-transformadas` |
| `tipo/`    | Tipo de nota                 | `tipo/clase`, `tipo/evaluacion`, `tipo/anuncios` |
| `subtipo/` | Subtipo (solo evaluaciones)  | `subtipo/pa`, `subtipo/pc`, `subtipo/laboratorio`, `subtipo/cuestionario` |
| `tema/`    | Tema específico              | `tema/ley-de-ampere`, `tema/teorema-de-cauchy`   |

Los tags de `tema/` se agregan orgánicamente. No predefinir taxonomía completa.

## Wikilinks

- Preferir `[[wikilinks]]` para enlaces internos (Obsidian rastrea renombrados automáticamente).
- `[texto](url)` solo para enlaces externos.
- **Enlazar solo la primera mención** de un concepto que tenga su propia nota.
- En `Formulario.md`, agregar `Fuente: [[nota origen]]` debajo de cada sección principal.

## MOCs y navegación

- Cada curso tiene un **MOC** como punto de entrada (e.g. `Motores MOC.md`).
- El semestre tiene un **Dashboard** que enlaza todos los MOCs (e.g. `Dashboard 2026-1.md`).
- Los MOCs listan todas las notas por semana y contienen el calendario de evaluaciones.
- Crear MOCs y Dashboards por defecto al iniciar un nuevo curso o semestre.

## Plantillas

Carpeta `plantillas/`. Usar la correspondiente al crear notas nuevas (Ctrl+T en Obsidian).

| Plantilla                       | Tipo        |
| ------------------------------- | ----------- |
| `Plantilla - Nota de clase.md`  | clase       |
| `Plantilla - Ejercicio.md`      | ejercicio   |
| `Plantilla - Formulario.md`     | formulario  |
| `Plantilla - Evaluacion.md`     | evaluacion  |
| `Plantilla - Anuncios.md`       | anuncios    |
| `Plantilla - Silabo.md`         | silabo      |

## Bases

Los archivos `.base` proveen vistas de datos dinámicas (plugin core Bases habilitado):

- `Notas por semana.base` en cada curso: vista tabla agrupada por semana.
- `Evaluaciones.base` a nivel de ciclo: vista de sílabos del ciclo.

## Reglas generales

### Sintaxis y formato

- Usar siempre Obsidian Flavored Markdown (wikilinks, callouts, embeds, properties).
- Usar callouts `> [!tipo]` para resaltar información importante, advertencias o ejemplos clave.

### Contenido y estructura

- Mantener el mismo estilo expositivo de las notas actuales: explicativo, didáctico, con desarrollo paso a paso.
- Al crear nuevas notas, seguir la numeración correlativa de la sesión (`SNN-X`).
- Las carpetas de attachments son por sesión, **excepto `anuncios-attachments/`** que es por curso.

### Protección

- **No modificar notas existentes** a menos que el usuario lo pida explícitamente.
- **No borrar archivos** sin pedir confirmación.

## Reglas para evaluaciones

> [!danger] NUNCA iniciar una evaluación online sin pedido explícito
> **NUNCA pulsar el botón "Realizar evaluación" / "Iniciar evaluación"** en el portal (consume el intento y arranca el cronómetro) a menos que el usuario lo pida **explícitamente**.
> Cuando el usuario dice "comienza", "empieza" o "resuelve la prueba", se refiere a **resolverla OFFLINE** (capturar enunciados sin gastar intento y desarrollarla en el vault), **NO** a iniciarla online. Ante la duda, preguntar antes de hacer clic.

Al resolver evaluaciones, seguir estas reglas:

1. **Analizar detenidamente las imágenes** siempre que estén presentes o se incluyan en la pregunta.
2. **Escribir las respuestas en el archivo** de evaluación.
3. **Calcular para todas las opciones** — no solo la correcta, sino verificar qué implica cada alternativa (cuando es opción múltiple).
4. **Siempre incluir cálculos, proceso y razonamiento** en el documento para sustentar la respuesta y validar posibles errores.
5. **Crear wikilinks hacia los documentos de teoría** que sustentan cada respuesta.

Para el shape completo de la nota de evaluación (datos, indicaciones, enunciados, desarrollo, resumen), seguir `plantillas/Plantilla - Evaluacion.md`.

## Operaciones del portal UTP

MCP Server `@playwright/mcp` configurado (scope: proyecto) — controla un browser headless para `class.utp.edu.pe`. Credenciales en `.env`: `UTP_WEB_USER`, `UTP_WEB_PASS`.

**Triggers:** cuando el usuario diga…

- **"extrae el Curso X, semana Y"** o **"extrae la semana actual"** → seguir "Procedimiento: Extraer una semana completa" en [`docs/portal-utp.md`](docs/portal-utp.md).
- **"actualiza anuncios"** o lunes (inicio de semana) por defecto → seguir "Procedimiento: Actualizar Anuncios" en `docs/portal-utp.md`.
- **"extrae [link de item del portal]"** → seguir "Procedimiento: Extraer contenido HTML de un item" en `docs/portal-utp.md`.

`docs/portal-utp.md` contiene: autenticación, mapa de los 8 tabs, estructura del tab Contenido (HTML inline/video, PDF, URL, EVAL), helpers JavaScript, notas técnicas (S3, PowerShell), y los 3 procedimientos completos.

## Extracción de YouTube

**Trigger:** cuando el usuario pida transcribir un video de YouTube o agregar un ejercicio a partir de un link de YouTube → seguir el procedimiento en [`docs/extraccion-youtube.md`](docs/extraccion-youtube.md). Usa `yt-dlp`, [`utils/parse_vtt.py`](utils/parse_vtt.py) y screenshots vía Playwright.

## Exportación a Word (.docx)

**Triggers:** cuando el usuario diga…

- **"exporta a docx"**, **"convierte a Word"**, **"genera el Word"** → usar [`utils/md_to_docx.py`](utils/md_to_docx.py) (Pandoc + APA v7 + LaTeX nativo). Detalles en [`docs/exportar-docx.md`](docs/exportar-docx.md).
- **"edita el docx"**, **"agrega track changes/comentarios"** o tareas que requieran manipulación XML interna del `.docx` → usar el skill `docx` de Anthropic (instalación documentada en `docs/exportar-docx.md`).

## Juntar imágenes en un PDF (.png/.jpg → .pdf)

**Trigger:** cuando el usuario diga **"junta/convierte/compila estas imágenes en un PDF"** (típico: fotos/escaneos de una resolución manuscrita de PA/PC para subir al portal) → usar [`utils/pngs_a_pdf.py`](utils/pngs_a_pdf.py).

```powershell
# Carpeta completa (orden alfabético — nombrar las imágenes ...-P01, ...-P02, ...)
uv run --with img2pdf python utils/pngs_a_pdf.py "<carpeta>"
# Lista explícita + nombre de salida
uv run --with img2pdf python utils/pngs_a_pdf.py p1.png p2.png -o entrega.pdf
```

`img2pdf` es **sin pérdida** (incrusta el PNG/JPG tal cual). Por defecto ajusta cada imagen a una página A4 vertical (`--nativo` para tamaño nativo, `--tamano CARTA` para oficio carta).

## Entorno Python — qué hacer si falta algo

El intérprete `python` del PATH suele ser el **stub de Microsoft Store** (no sirve). El entorno Python se gestiona con **`uv`** (Astral); está instalado en `~/.local/bin/uv.exe`. Ejecutar scripts con dependencias efímeras vía `uv run --with <paquete> python <script>` (no requiere instalar nada global ni activar venvs).

**Si falta algo, instalar bajo demanda (preferir `uv`):**

- **Falta `uv`:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`. Tras instalar, usar `~/.local/bin/uv.exe` (puede no estar aún en el PATH de la sesión).
- **Falta una versión de Python:** `uv python install 3.12` (luego `uv run --python 3.12 ...`).
- **Falta un paquete (img2pdf, pillow, pikepdf, etc.):** no hace falta `pip install` global — pasarlo con `uv run --with <paquete> ...` y uv lo resuelve en un entorno temporal.
- **Otras herramientas del sistema (pandoc, etc.):** verificar con `Get-Command <cmd>`; instalar con `winget install <id>` si el usuario lo autoriza.

Confirmado disponible en esta máquina: `pandoc`, Microsoft **Edge** (útil como `msedge --headless --print-to-pdf` si se necesita render HTML→PDF). **No** hay (al 2026-05): Python real en PATH, ImageMagick, motor LaTeX, wkhtmltopdf — instalar vía `uv`/`winget` cuando se requieran.

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
