# Universidad Vault

Vault de Obsidian para apuntes universitarios. Todo el contenido está en español.

## Estructura

```
Universidad/
├── utils/                             # Scripts utilitarios para recolección de contenido
│   ├── parse_vtt.py                   # Parsea subtítulos VTT de YouTube a texto limpio
│   └── semana_actual.py               # Calcula la semana del ciclo (config en INICIOS_CICLO)
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
│           ├── Anuncios.md            # Comunicados del docente (cronologico ascendente)
│           ├── *.base                 # Vistas de base de datos
│           ├── anuncios-attachments/  # Imagenes embebidas en anuncios
│           └── clases/
│               └── sNN/              # Semana NN (e.g. s01 = semana 01)
│                   ├── SNN-0 Título.md    # Notas de clase (numeradas por tema)
│                   ├── SNN-1 Tema ...md
│                   └── attachments/       # Imagenes pegadas desde clase
```

## Cursos del ciclo activo (2026-1)

Mapeo curso del portal UTP → carpeta del vault. Los UUIDs son estables durante el ciclo. Al cambiar de ciclo, regenerar esta tabla navegando a la página de cursos del portal.

| Curso (portal)                            | Sigla | Modalidad    | Docente                       | Carpeta vault         | Course UUID                            | Section UUID                           |
| ----------------------------------------- | ----- | ------------ | ----------------------------- | --------------------- | -------------------------------------- | -------------------------------------- |
| Circuitos Electrónicos Amplificadores     | 29579 | Presencial   | jorge luis robles bokun       | `Amplificadores`      | `08eb7f8d-ab62-53df-9b46-c0ca85f1f263` | `55733e4b-ebe4-5b86-8284-d0afbacba5cd` |
| Controlador Lógico Programable Plc        | 25286 | Presencial   | jorge luis guerrero cardenas  | `PLC`                 | `2bcfdc80-6c82-53f7-b910-4b4dd5ebaba6` | `8e09f862-b5fa-5106-8fdc-c7f9b2850c99` |
| Maquinas Eléctricas Estáticas y Rotativas | 14199 | Virtual 24/7 | charlton harley pretel diaz   | `MaquinasElectricas`  | `40ee9986-a006-5cb9-a550-2e82d236051d` | `70765508-9fb9-5029-aa08-d47e3b6ff0ff` |
| Series y Transformadas                    | 14081 | Virtual 24/7 | jose fernando torres diaz     | `SeriesTransformadas` | `0b1407f5-d982-5ee2-b893-1a1e0f3f02e7` | `a9dcc407-c04b-5d30-b7c4-fb698f891128` |

URL base por curso: `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`

**Ignorar siempre** en la lista de cursos del portal: "RUTA LABORAL …", "Ruta Laboral", "English Discoveries Placement Test".

## Calendario del ciclo

- Las semanas comienzan **lunes** y terminan **domingo** (convención Perú).
- El ciclo dura **18 semanas**.
- Ciclo **2026-1** → Semana 01 = lunes **23 de marzo de 2026**.
- Para inferir la semana actual usar `python utils/semana_actual.py [YYYY-MM-DD]` (sin argumento usa hoy). Nuevos ciclos se agregan al diccionario `INICIOS_CICLO` del script.
- Cuando el usuario diga "extrae la semana actual" sin número, calcular con el script.
- En el portal, los tabs de Foros/Notas/Evaluaciones marcan "Semana NN - Semana actual" — sirve como verificación cruzada.

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

### Anuncios

```yaml
---
title: "Anuncios - Nombre del curso"
curso: "[[Curso MOC]]"
tipo: anuncios
tags:
  - curso/nombre-curso
  - tipo/anuncios
date: 2026-05-03
---
```

**Nombre de archivo:** `Anuncios.md` (uno por curso, en la raíz de la carpeta del curso).

**Estructura:** un H1 con el curso y modalidad; luego una sección `## YYYY-MM-DD HH:MM AM/PM — Título corto` por anuncio en orden cronológico **ascendente** (más antiguo arriba). Cuerpo del anuncio en blockquote. Imágenes embebidas con `![[YYYY-MM-DD_descripcion.png]]` desde `<curso>/anuncios-attachments/`.

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

**Property `curso` como wikilink:** En notas de clase, ejercicio, formulario, silabo y anuncios usar `"[[Curso MOC]]"` para que el MOC aparezca como backlink.

## Tags

Usar 3 jerarquías de tags:

| Jerarquía | Uso | Ejemplos |
| --------- | --- | -------- |
| `curso/` | Identificar el curso | `curso/motores`, `curso/plc`, `curso/amplificadores`, `curso/series-transformadas` |
| `tipo/` | Tipo de nota | `tipo/clase`, `tipo/ejercicio`, `tipo/formulario`, `tipo/referencia`, `tipo/moc`, `tipo/dashboard`, `tipo/anuncios` |
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
- Las carpetas de attachments son por sesión, no globales (excepto `anuncios-attachments/` que es por curso)

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

## Portal UTP: estructura

MCP Server `@playwright/mcp` configurado (scope: proyecto). Permite controlar un browser headless para `class.utp.edu.pe`.

### Autenticación

- URL inicial: `https://class.utp.edu.pe/` → redirige a SSO `sso.utp.edu.pe`.
- Credenciales en `.env`: `UTP_WEB_USER`, `UTP_WEB_PASS`.
- Llenar inputs con `browser_evaluate` (set `value` + `dispatchEvent input/change`) y click "Iniciar sesión".

### Tabs por curso

Los 4 cursos comparten los mismos 8 tabs. Cada tab cambia solo el sufijo del path tras `/section/<section_uuid>/`:

| Tab          | Path             | Contenido                                                                            |
| ------------ | ---------------- | ------------------------------------------------------------------------------------ |
| Sílabo       | `/syllabus`      | PDF embebido en `<iframe>` desde S3 (`ms-utp-prd-silbiaback-cd.s3.amazonaws.com/...`)|
| Contenido    | `/learnv2`       | Acordeón por semana con materiales/lecciones (estructura varía por modalidad — ver abajo) |
| Evaluaciones | `/listEvaluation`| Lista de evaluaciones por semana con fechas y estado. **Virtual 24/7** trae las 15 pobladas; **Presencial** suele decir "muy pronto…" porque se gestionan en clase |
| Tareas       | `/listHomework`  | Tareas por semana. Vacío en cursos actuales                                          |
| Foros        | `/listForum`     | Foros agrupados por semana + foro general "Foro De Consulta" siempre presente        |
| Notas        | `/calification`  | Calificaciones por semana                                                            |
| Anuncios     | `/announcements` | Comunicados del docente con fecha; cada uno tiene URL `/announcements/<uuid>`        |
| Zoom         | `/zoom`          | Calendario de clases sincrónicas: título / semana / fecha / meeting ID / link        |

URL del PDF del Sílabo: `https://ms-utp-prd-silbiaback-cd.s3.amazonaws.com/pdfs/approved/complete/<ciclo>/<modalidad>/<codigo>_<NombreCursoSinEspacios>.pdf` — códigos vistos: `100000I21N` (Amplificadores), `100000I39M` (PLC).

### Estructura del tab Contenido

URL de cada item: `/learnv2/week/<N>/unit/<section_uuid>/theme/<theme_uuid>/content/<content_uuid>/<tipo>` donde `<tipo>` es:

- `html` → "Contenido personalizado" — rich text con LaTeX (fórmulas como `<img alt="LaTeX: ...">`) y figuras. **Tipo principal en Virtual 24/7.** Dos sub-formatos comunes:
  - **HTML inline:** texto + fórmulas LaTeX (imágenes desde el servicio AWS `5a6yscpebg.execute-api.us-east-1.amazonaws.com/latex-to-svg/<urlencoded>?scale=1` — el `alt` arranca con `LaTeX: ...`, decodear URL y normalizar caracteres unicode mathematical italic `𝑧→z, 𝑥→x, 𝑦→y, 𝜃→\theta, 𝜋→\pi, ∮→\oint`) + figuras JPEG/PNG en S3.
  - **HTML video:** `<video><source src="...mp4">` + 3 links "Descargar .MP4 / .MP3 / .PDF". El **PDF "Guion"** es la transcripción del video con el desarrollo escrito — preferir leer el Guion antes que ver el video.
- `pdf` → "Material ∙ PDF" — la página tiene un visor PDF embebido en `<iframe>`; el URL real de S3 está en el query param `d=` del iframe src (extraer con `decodeURIComponent`).
- `url` → "Material ∙ URL" — link externo.
- `evaluation/<id>` → "Evaluación calificada" / "Evaluación no calificada". **Visitar la URL solo muestra metadatos** (intentos, fechas, tipo) — el cronómetro y el intento se inician solo al hacer click en "Realizar evaluación". Útil para capturar metadatos sin consumir el intento.
- `video` → posiblemente video standalone (no observado aún; los videos suelen venir como sub-formato del `/html`).

Iconos en títulos: 📚 = lección, 📝 = cuestionario / examen no calificado, 🔴 = evaluación calificada principal (PA, PC, EXFN). Prefijo `(AC-SNN)` = código de actividad calificada.

**Variantes por curso/modalidad:**

- **Virtual 24/7** (Maquinas, SyT) — 3 niveles, mapea 1:1 a `sNN/SNN-X Tema NN - Título.md`:
  ```
  Semana NN
    ├─ Introducción a la semana N (1 HTML)
    ├─ Tema 01: Nombre (varios HTML — cada concepto/ejercicio es item separado)
    ├─ Tema 02: Nombre (varios HTML)
    ├─ Material ∙ PDF (opcional, ej. indicaciones de evaluación)
    ├─ Evaluación (📝 cuestionario y/o 🔴 calificada)
    └─ Cierre / Conclusiones de la semana N (1 HTML)
  ```
- **Presencial con SNN** (Amplificadores) — solo PDF de soporte:
  ```
  Semana NN
    └─ SNN
        └─ Material ∙ PDF — SNN-Material (a veces SNN-Material2)
  ```
- **Presencial con título** (PLC) — sin SNN, con título descriptivo y materiales mixtos:
  ```
  Semana NN — Título descriptivo (e.g. "Operaciones básicas con variables digitales")
    ├─ Material ∙ URL (link externo, ej. plantillas)
    └─ Material ∙ PDF
  ```

### Helpers JavaScript útiles

```js
// Listar items de la semana N actualmente expandida
Array.from(document.querySelectorAll('a[href*="/learnv2/week/N/"]'))
  .map(a => ({ href: a.getAttribute('href'),
               type: a.href.endsWith('/html') ? 'HTML' :
                     a.href.endsWith('/pdf')  ? 'PDF'  :
                     a.href.endsWith('/url')  ? 'URL'  :
                     a.href.includes('/evaluation/') ? 'EVAL' : 'OTHER',
               text: a.innerText.trim().replace(/\s+/g, ' ') }));

// Expandir un acordeón por título exacto (idempotente — chequea si ya hay links dentro)
// Útil porque el toggle es stateful entre re-navegaciones; al re-cargar la pagina, las
// semanas pueden estar ya expandidas y un click "ingenuo" las cerraria.
const expandIf = (label) => {
  const p = Array.from(document.querySelectorAll('p'))
    .find(p => p.textContent.trim() === label);
  if (!p) return false;
  let container = p; for (let i=0;i<6;i++) container = container.parentElement || container;
  if (container.querySelector('a[href*="/learnv2/week/"]')) return true; // ya abierto
  let el = p; while (el && getComputedStyle(el).cursor !== 'pointer') el = el.parentElement;
  if (el) { el.click(); return true; }
  return false;
};

// Regex para sub-temas Virtual 24/7 de la semana N (Introducción / Tema XX / Cierre)
// Importante: usar \s+N$ (uno o MÁS espacios) — algunos títulos tienen doble espacio
// antes del número, e.g. "Tema 02: Teorema de Cauchy  6"
const subRegex = /^(Introducción a la semana N|Tema \d+:.*\s+N|Cierre de la semana N)$/;

// Extraer body de anuncio (descartando iconos UI estaticos)
const cks = Array.from(document.querySelectorAll('.ck-content'));
const main = cks.sort((a,b)=>b.innerText.length - a.innerText.length)[0];
const imgs = Array.from(main.querySelectorAll('img'))
  .filter(i => !i.src.includes('/static/media/'))
  .map(i => ({ src: i.src, alt: i.alt }));
return { text: main.innerText, imgs };

// Extraer URL real del PDF embebido en /pdf (esta dentro del iframe src query d=)
const ifr = document.querySelector('iframe[src*="/lib/ui/index.html"]');
const url = new URL(ifr.src);
const pdfUrl = decodeURIComponent(url.hash.split('d=')[1].split('&')[0]);
```

### Notas técnicas

- Las imágenes del portal están en S3 (`utp-prd-upload-file-storage.s3.amazonaws.com/pao/content/<uuid>/<file>`), son públicas y se descargan sin auth.
- curl falla en Windows (exit code 35, SSL error) — usar siempre PowerShell `Invoke-WebRequest`.
- Los warnings de PowerShell `UnauthorizedAccess` son del profile, no del comando — ignorar si el output termina en "OK".
- Las fórmulas en el portal aparecen como `img "LaTeX: ..."` en el snapshot — convertir a `$$...$$` o `$...$`.
- Descargar en lotes paralelos (3-4 imágenes por comando PowerShell) para eficiencia.
- Esperar ~1.2-2s después de un click en acordeón antes de leer (el SPA renderiza async).

## Procedimiento: Extraer contenido HTML de un item del portal (Virtual 24/7)

Cubre la extracción de UN item `/html` (típicamente "Contenido personalizado" con texto, fórmulas LaTeX y figuras).

### Flujo

1. **Navegar** al link `/learnv2/week/N/.../content/<id>/html`. Esperar ~2s.
2. **Detectar formato** (browser_evaluate):
   - Si tiene `<video>` o link "Descargar .PDF" → es **video con Guion** (saltar al paso 3b).
   - Si solo tiene texto + LaTeX images + figuras → es **HTML inline** (paso 3a).
3a. **HTML inline:** serializar el `.ck-content` preservando orden de `<img>` con sus `alt`. Convertir `<img alt="LaTeX: <expr>">` a `$<expr>$` (inline) o `$$<expr>$$` (bloque, si la expresion contiene `\frac`, `\sum`, `\int`). Normalizar caracteres unicode mathematical italic (`𝑧→z`, etc.). Descargar figuras (img sin prefijo "LaTeX:") a `attachments/`.
3b. **Video con Guion:** descargar el PDF "Guion" (link "Descargar .PDF") a `attachments/<TXX-EjY-Guion-descripcion>.pdf` con PowerShell. Leer el PDF con `Read` para extraer enunciado, datos y desarrollo paso a paso.
4. **Crear la nota** con todo el contenido (sin resumir), fórmulas en LaTeX, imágenes embebidas con `![[nombre.png]]`, callouts `> [!summary]` / `> [!success]` / `> [!warning]` para estructurar.
5. **Actualizar el Formulario** del curso con las fórmulas nuevas, incluyendo `Fuente: [[nota]]`.

## Procedimiento: Extraer una semana completa de un curso

Cuando el usuario diga "extrae el Curso X, semana Y" (o "la semana actual"):

1. **Determinar contexto**
   - Identificar `<carpeta_vault>` y `<modalidad>` desde la tabla de "Cursos del ciclo activo".
   - Si no se especifica Y, calcular semana actual con `utils/semana_actual.py`.
   - Construir URL: `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`.

2. **Navegar y autenticar** (ver "Autenticación" arriba).

3. **Expandir Semana Y**
   - Buscar el `<p>` con texto exacto `Semana NN` (con padding cero, e.g. "Semana 06").
   - Subir al primer ancestro con `cursor: pointer` y click; esperar 1-2s.
   - **Virtual 24/7:** además expandir cada `<p>` `Introducción a la semana N`, `Tema XX: ... N`, `Cierre de la semana N`.

4. **Inventariar items**
   - Listar todos los `<a href*="/learnv2/week/N/">` y clasificar por sufijo (`/html`, `/pdf`, `/url`, `/evaluation/...`).
   - Capturar el texto visible del link (incluye prefijos 📚/📝/🔴 y nombres como "Tema 01: …").
   - Para Virtual 24/7, registrar también el `theme_uuid` del href para agrupar items por tema.

5. **Cruzar con tabs auxiliares** (lecturas rápidas, no se duplican)
   - `/listEvaluation` → confirmar fechas y tipo de evaluaciones de la semana Y.
   - `/announcements` → leer comunicado(s) de la semana (si existen) — instrucciones del docente, recordatorios, fe de erratas.
   - `/listForum`, `/listHomework` → detectar foros/tareas con fecha en la semana Y.

6. **Crear estructura local**
   - Carpeta: `cursos/<ciclo>/<carpeta_vault>/clases/sNN/` (donde `sNN` = semana en minúscula con padding, e.g. `s06`).
   - Carpeta: `cursos/<ciclo>/<carpeta_vault>/clases/sNN/attachments/` para imágenes/PDFs.

7. **Procesar cada item según tipo**
   - **`/html` inline (texto + LaTeX + figuras)** → extraer body con la función JS de "Helpers", convertir cada `<img alt="LaTeX: ...">` a `$...$` o `$$...$$` (decodear URL del src y normalizar caracteres unicode mathematical italic), descargar las figuras (alt sin "LaTeX: ") con PowerShell a `attachments/`. Crear `SNN-X Tema NN - Título.md`.
   - **`/html` video (con `<video>` + Descargar PDF/MP4/MP3)** → preferir descargar el **Guion PDF** (es la transcripción del video con todo el desarrollo escrito) en vez de procesar el video. El PDF se lee directo con `Read`. Crear nota basada en el Guion.
   - **`/pdf`** → extraer URL real del iframe (ver helpers JS), descargar a `attachments/<descripción>.pdf` con PowerShell. Si es manual de la semana → guardar en raíz de `sNN/` como `SemanaNN_Tema.pdf`. Si es indicaciones de evaluación → usar como fuente para la nota SNN-99 (o SNN-98).
   - **`/url`** → registrar como external link en la nota correspondiente; no descargar el destino.
   - **`/evaluation/<id>`** → navegar (solo lee metadatos, no consume intento), capturar fechas/tipo. Si los enunciados de las preguntas vienen en un PDF "Indicaciones" aparte, transcribir esos enunciados; si vienen solo al hacer click en "Realizar evaluación" (caso PA/PC), pedir al usuario que abra el examen y pegue los enunciados o suba un PDF. Crear `SNN-99 Evaluación …md` (metadatos + indicaciones) y `SNN-98 ... Enunciados.md` (enunciados + desarrollo si aplica). Aplicar reglas de "Evaluaciones".

8. **Actualizar referencias**
   - Renumerar notas existentes si se inserta algo entre medio (frontmatter `orden`, archivo, wikilinks).
   - Actualizar `Formulario - <Curso>.md` con fórmulas nuevas + `Fuente: [[nota]]`.
   - Actualizar `<Curso> MOC.md` con la lista de notas de la semana.
   - El `Dashboard <ciclo>.md` y `Evaluaciones.base` se refrescan solos.

9. **Verificación final**
   - Confirmar que cada item del portal tiene su contraparte en el vault (HTML→nota, PDF→attachment+ref, EVAL→nota -99).
   - Validar links rotos.

## Procedimiento: Actualizar Anuncios por curso

Cuándo:
- **Por defecto los lunes** (inicio de semana) — los docentes típicamente publican anuncio nuevo al iniciar la semana.
- **Bajo pedido:** cuando el usuario diga "actualiza anuncios" o equivalente.

Para cada curso del ciclo activo:

1. **Leer el último anuncio del archivo local** `cursos/<ciclo>/<curso>/Anuncios.md` y anotar la fecha de la sección final (es la más reciente capturada). Si no existe el archivo, tratarlo como "extracción inicial" (capturar todo).
2. **Navegar** a `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/announcements`.
3. **Listar anuncios del portal** (orden newest-first nativo): para cada `<a href*="/announcements/">` extraer `(uuid, dateRaw)` y parsear la fecha. La fecha está en la card como "Publicado: D mes, AAAA H:MM AM/PM".
4. **Detectar nuevos:** filtrar los que tengan fecha `>` el último capturado localmente. Comparar también por uuid si hay varios el mismo día.
5. **Para cada nuevo anuncio (en orden cronológico ascendente para preservar el orden del archivo):**
   - Navegar a `/announcements/<uuid>`, esperar ~1.2s.
   - Extraer body del `.ck-content` con la mayor longitud (texto + imágenes filtrando `/static/media/` que son íconos UI):
     ```js
     const cks = Array.from(document.querySelectorAll('.ck-content'));
     const main = cks.sort((a,b)=>b.innerText.length - a.innerText.length)[0];
     const imgs = Array.from(main.querySelectorAll('img'))
       .filter(i => !i.src.includes('/static/media/'))
       .map(i => ({ src: i.src, alt: i.alt }));
     return { text: main.innerText, imgs };
     ```
   - Si tiene imagen(es): descargar con PowerShell `Invoke-WebRequest` a `<curso>/anuncios-attachments/YYYY-MM-DD_descripcion.png` (sufijo `_a`/`_b` si hay varios el mismo día).
   - **OCR de imágenes con texto sustancial** (slide-anuncio): recortar área del cuerpo y upscalear ~1.4x con Pillow (`pip install Pillow`), luego leer con `Read`. Crops temporales en `_crops/` se borran al terminar.
6. **Append al `Anuncios.md`** del curso, una `## YYYY-MM-DD HH:MM AM/PM — Título corto` por anuncio, con el cuerpo en blockquote y embed `![[nombre]]` si aplica.
7. **No tocar anuncios anteriores** ya capturados.
8. Si no hay nuevos: reportar "sin nuevos anuncios desde <fecha>" — no modificar el archivo.

### Patrones por docente conocidos

- **Amplificadores (J. Robles Bokun):** un saludo template los lunes 6:00 AM. Texto corto, sin imágenes. Esperar 1 nuevo por semana.
- **PLC (J. Guerrero Cárdenas):** un anuncio los lunes 6:00 AM con el temario de la semana. Texto, sin imágenes. Esperar 1 por semana.
- **Maquinas (Ch. Pretel Diaz):** 2 diapositivas-anuncio por semana — lunes y jueves 12:00 AM (Bienvenida parte 1 + parte 2). Imágenes PNG con título "BIENVENIDO(A) A LA SEMANA N – Marzo 26". A veces comunicados puntuales (recordatorios de evaluaciones, claves de simuladores). Esperar 2-3 por semana.
- **SyT (J. F. Torres Diaz):** 2 anuncios-tarjeta por semana — lunes "BIENVENIDO(A) A LA SEMANA N" y viernes "CIERRE SEMANA N". Imágenes PNG. Suele agregar 1-2 anuncios extra (felicitaciones por evaluaciones, invitaciones, instrucciones de PA). Esperar 3-5 por semana.

Si el patrón de un docente cambia significativamente (e.g. nuevo curso, nuevo formato), actualizar esta sección.

## Procedimiento: Extraer ejercicios de videos de YouTube

### Flujo

1. **Extraer transcripción** con `yt-dlp` (instalado): `yt-dlp --write-auto-sub --sub-lang es --skip-download --sub-format vtt -o "ruta/output" "URL"`
2. **Parsear la transcripción** VTT a texto limpio con timestamps usando el script `utils/parse_vtt.py`
3. **Analizar la transcripción** para identificar momentos clave: enunciado, datos, fórmulas, cálculos, resultado
4. **Navegar al video** con Playwright (`browser_navigate`)
5. **Cerrar diálogos** si aparecen (YouTube Premium "No thanks", cookies consent)
6. **Pausar el video** y verificar duración real (si la propaganda desplazó los tiempos, el video puede mostrar duración incorrecta hasta que se recargue)
7. **Tomar screenshots** en timestamps clave usando `browser_run_code`:
   - Pausar: `document.querySelector('video').pause()`
   - Seek: `document.querySelector('video').currentTime = seconds`
   - Esperar: `page.waitForTimeout(2000)` (dar tiempo al frame de renderizar)
   - Capturar área del video: `page.screenshot({ clip: { x: 0, y: 60, width: 914, height: 514 } })`
   - **Importante**: las coordenadas del video son fijas (`y: 60` por la barra de YouTube); verificar con `boundingBox()` si hay problemas
8. **Verificar capturas** leyéndolas — si solo muestran la barra de YouTube, el video no estaba visible (pudo haber terminado y colapsado); re-seek a `currentTime = 0` y reintentar
9. **Crear la nota** combinando transcripción + capturas, con resolución paso a paso en LaTeX

### Notas importantes

- `yt-dlp` está instalado globalmente via pip
- El script `utils/parse_vtt.py` limpia el formato VTT (elimina tags `<c>`, deduplica líneas repetidas, extrae timestamps `m:ss`)
- Los subtítulos auto-generados tienen errores de transcripción en términos técnicos (e.g. "weever" = Weber, "ampi" = Ampere) — interpretar con contexto
- Si el video tiene propaganda al inicio, la duración reportada por `document.querySelector('video').duration` puede ser solo la del ad; esperar a que termine o saltar
- Guardar las capturas del video en `attachments/` con prefijo descriptivo (e.g. `video-ej-enunciado.png`, `video2-tabla.png`)
- Al insertar un ejercicio de video entre notas existentes: renumerar las notas posteriores (archivos + frontmatter `orden` + wikilinks en Formulario y otras notas)

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
