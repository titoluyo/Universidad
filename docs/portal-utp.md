# Portal UTP — referencia operativa

Documento de referencia para extraer contenido del portal `class.utp.edu.pe`. Cargar bajo demanda cuando el usuario pida operaciones del portal (ver triggers en `CLAUDE.md`).

MCP Server `@playwright/mcp` configurado (scope: proyecto). Permite controlar un browser headless.

Datos del ciclo activo (UUIDs por curso, docentes, modalidad) en [`cursos/2026-1/Cursos.md`](../cursos/2026-1/Cursos.md).

---

## Autenticación

- URL inicial: `https://class.utp.edu.pe/` → redirige a SSO `sso.utp.edu.pe`.
- Credenciales en `.env` (raíz del vault): `UTP_WEB_USER`, `UTP_WEB_PASS`.
- Llenar inputs con `browser_evaluate` (set `value` + `dispatchEvent input/change`) y click "Iniciar sesión".

---

## Tabs por curso

Los 4 cursos del ciclo comparten los mismos 8 tabs. Cada tab cambia solo el sufijo del path tras `/section/<section_uuid>/`:

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

URL del PDF del Sílabo: `https://ms-utp-prd-silbiaback-cd.s3.amazonaws.com/pdfs/approved/complete/<ciclo>/<modalidad>/<codigo>_<NombreCursoSinEspacios>.pdf` — códigos vistos en `Cursos.md`.

---

## Estructura del tab Contenido

URL de cada item: `/learnv2/week/<N>/unit/<section_uuid>/theme/<theme_uuid>/content/<content_uuid>/<tipo>` donde `<tipo>` es:

- `html` → "Contenido personalizado" — rich text con LaTeX (fórmulas como `<img alt="LaTeX: ...">`) y figuras. **Tipo principal en Virtual 24/7.** Dos sub-formatos comunes:
  - **HTML inline:** texto + fórmulas LaTeX (imágenes desde el servicio AWS `5a6yscpebg.execute-api.us-east-1.amazonaws.com/latex-to-svg/<urlencoded>?scale=1` — el `alt` arranca con `LaTeX: ...`, decodear URL y normalizar caracteres unicode mathematical italic `𝑧→z, 𝑥→x, 𝑦→y, 𝜃→\theta, 𝜋→\pi, ∮→\oint`) + figuras JPEG/PNG en S3.
  - **HTML video:** `<video><source src="...mp4">` + 3 links "Descargar .MP4 / .MP3 / .PDF". El **PDF "Guion"** es la transcripción del video con el desarrollo escrito — preferir leer el Guion antes que ver el video.
- `pdf` → "Material ∙ PDF" — la página tiene un visor PDF embebido en `<iframe>`; el URL real de S3 está en el query param `d=` del iframe src (extraer con `decodeURIComponent`).
- `url` → "Material ∙ URL" — link externo.
- `evaluation/<id>` → "Evaluación calificada" / "Evaluación no calificada". **Visitar la URL solo muestra metadatos** (intentos, fechas, tipo) — el cronómetro y el intento se inician solo al hacer click en "Realizar evaluación". Útil para capturar metadatos sin consumir el intento.
- `video` → posiblemente video standalone (no observado aún; los videos suelen venir como sub-formato del `/html`).

Iconos en títulos: 📚 = lección, 📝 = cuestionario / examen no calificado, 🔴 = evaluación calificada principal (PA, PC, EXFN). Prefijo `(AC-SNN)` = código de actividad calificada.

### Variantes por curso/modalidad

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

---

## Helpers JavaScript

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

// Extraer body de anuncio o item de contenido (descartando iconos UI estaticos)
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

---

## Notas técnicas

- Las imágenes del portal están en S3 (`utp-prd-upload-file-storage.s3.amazonaws.com/pao/content/<uuid>/<file>`), son públicas y se descargan sin auth.
- **curl falla en Windows** (exit code 35, SSL error) — usar siempre PowerShell `Invoke-WebRequest`.
- Los warnings de PowerShell `UnauthorizedAccess` son del profile, no del comando — ignorar si el output termina en "OK".
- Las fórmulas en el portal aparecen como `img "LaTeX: ..."` en el snapshot — convertir a `$$...$$` o `$...$`.
- Descargar en lotes paralelos (3-4 imágenes por comando PowerShell) para eficiencia.
- Esperar ~1.2-2s después de un click en acordeón antes de leer (el SPA renderiza async).

---

## Procedimiento: Extraer contenido HTML de un item

Cubre la extracción de UN item `/html` (típicamente "Contenido personalizado").

1. **Navegar** al link `/learnv2/week/N/.../content/<id>/html`. Esperar ~2s.
2. **Detectar formato** (browser_evaluate):
   - Si tiene `<video>` o link "Descargar .PDF" → es **video con Guion** (paso 3b).
   - Si solo tiene texto + LaTeX images + figuras → es **HTML inline** (paso 3a).
3a. **HTML inline:** serializar el `.ck-content` preservando orden de `<img>` con sus `alt`. Convertir `<img alt="LaTeX: <expr>">` a `$<expr>$` (inline) o `$$<expr>$$` (bloque, si la expresion contiene `\frac`, `\sum`, `\int`). Normalizar caracteres unicode mathematical italic (`𝑧→z`, etc.). Descargar figuras (img sin prefijo "LaTeX:") a `attachments/`.
3b. **Video con Guion:** descargar el PDF "Guion" (link "Descargar .PDF") a `attachments/<TXX-EjY-Guion-descripcion>.pdf` con PowerShell. Leer el PDF con `Read` para extraer enunciado, datos y desarrollo paso a paso.
4. **Crear la nota** con todo el contenido (sin resumir), fórmulas en LaTeX, imágenes embebidas con `![[nombre.png]]`, callouts `> [!summary]` / `> [!success]` / `> [!warning]` para estructurar.
5. **Actualizar el Formulario** del curso con las fórmulas nuevas, incluyendo `Fuente: [[nota]]`.

---

## Procedimiento: Extraer una semana completa

**Trigger:** "extrae el Curso X, semana Y" o "extrae la semana actual".

1. **Determinar contexto**
   - Identificar `<carpeta_vault>` y `<modalidad>` desde [`cursos/<ciclo>/Cursos.md`](../cursos/2026-1/Cursos.md).
   - Si no se especifica Y, calcular semana actual con `python utils/semana_actual.py`.
   - Construir URL: `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`.

2. **Navegar y autenticar** (ver "Autenticación" arriba).

3. **Expandir Semana Y**
   - Buscar el `<p>` con texto exacto `Semana NN` (con padding cero, e.g. "Semana 06").
   - Subir al primer ancestro con `cursor: pointer` y click; esperar 1-2s.
   - **Virtual 24/7:** además expandir cada `<p>` `Introducción a la semana N`, `Tema XX: ... N`, `Cierre de la semana N` (usar el `subRegex` de Helpers).

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
   - **`/html` inline (texto + LaTeX + figuras)** → seguir "Procedimiento: Extraer contenido HTML" (paso 3a). Crear `SNN-X Tema NN - Título.md`.
   - **`/html` video** → seguir "Procedimiento: Extraer contenido HTML" (paso 3b). Crear nota basada en el Guion PDF.
   - **`/pdf`** → extraer URL real del iframe (ver helper JS), descargar a `attachments/<descripción>.pdf` con PowerShell. Si es manual de la semana → guardar en raíz de `sNN/` como `SemanaNN_Tema.pdf`. Si es indicaciones de evaluación → usar como fuente para la nota SNN-99 (o SNN-98).
   - **`/url`** → registrar como external link en la nota correspondiente; no descargar el destino.
   - **`/evaluation/<id>`** → navegar (solo lee metadatos, no consume intento), capturar fechas/tipo. Si los enunciados de las preguntas vienen en un PDF "Indicaciones" aparte, transcribir esos enunciados; si vienen solo al hacer click en "Realizar evaluación" (caso PA/PC), pedir al usuario que abra el examen y pegue los enunciados o suba un PDF. Crear `SNN-99 Evaluación …md` (metadatos + indicaciones) y opcionalmente `SNN-98 ... Enunciados.md` (enunciados + desarrollo si aplica). Aplicar reglas de "Evaluaciones" en `CLAUDE.md` y plantilla `plantillas/Plantilla - Evaluacion.md`.

8. **Actualizar referencias**
   - Renumerar notas existentes si se inserta algo entre medio (frontmatter `orden`, archivo, wikilinks).
   - Actualizar `Formulario - <Curso>.md` con fórmulas nuevas + `Fuente: [[nota]]`.
   - Actualizar `<Curso> MOC.md` con la lista de notas de la semana.
   - El `Dashboard <ciclo>.md` y `Evaluaciones.base` se refrescan solos.

9. **Verificación final**
   - Confirmar que cada item del portal tiene su contraparte en el vault (HTML→nota, PDF→attachment+ref, EVAL→nota -99).
   - Validar links rotos.

---

## Procedimiento: Actualizar Anuncios por curso

**Trigger:** "actualiza anuncios" o por defecto los lunes (inicio de semana — los docentes típicamente publican anuncio nuevo).

Para cada curso del ciclo activo (ver [`Cursos.md`](../cursos/2026-1/Cursos.md) para frecuencia esperada por docente):

1. **Leer el último anuncio del archivo local** `cursos/<ciclo>/<curso>/Anuncios.md` y anotar la fecha de la sección final (es la más reciente capturada). Si no existe el archivo, tratarlo como "extracción inicial" (capturar todo).
2. **Navegar** a `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/announcements`.
3. **Listar anuncios del portal** (orden newest-first nativo): para cada `<a href*="/announcements/">` extraer `(uuid, dateRaw)` y parsear la fecha. La fecha está en la card como "Publicado: D mes, AAAA H:MM AM/PM".
4. **Detectar nuevos:** filtrar los que tengan fecha `>` el último capturado localmente. Comparar también por uuid si hay varios el mismo día.
5. **Para cada nuevo anuncio (en orden cronológico ascendente para preservar el orden del archivo):**
   - Navegar a `/announcements/<uuid>`, esperar ~1.2s.
   - Extraer body del `.ck-content` con la mayor longitud — usar el helper "Extraer body" de Helpers JavaScript (texto + imágenes filtrando `/static/media/` que son íconos UI).
   - Si tiene imagen(es): descargar con PowerShell `Invoke-WebRequest` a `<curso>/anuncios-attachments/YYYY-MM-DD_descripcion.png` (sufijo `_a`/`_b` si hay varios el mismo día).
   - **OCR de imágenes con texto sustancial** (slide-anuncio): recortar área del cuerpo y upscalear ~1.4x con Pillow (`pip install Pillow`), luego leer con `Read`. Crops temporales en `_crops/` se borran al terminar.
6. **Append al `Anuncios.md`** del curso, una `## YYYY-MM-DD HH:MM AM/PM — Título corto` por anuncio, con el cuerpo en blockquote y embed `![[nombre]]` si aplica. Ver `plantillas/Plantilla - Anuncios.md`.
7. **No tocar anuncios anteriores** ya capturados.
8. Si no hay nuevos: reportar "sin nuevos anuncios desde <fecha>" — no modificar el archivo.
