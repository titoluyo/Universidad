# Entrenamiento: Mapeo del portal UTP

Notas de trabajo para construir el procedimiento de extraer info de una semana completa.
Al finalizar, integrar lo confirmado en `CLAUDE.md`.

## URL base
`https://class.utp.edu.pe/`

Al ingresar muestra la página de cursos del ciclo activo (actualmente **2026-1**, cambia cada ciclo). Filtro lateral: **"Periodo actual"** muestra agrupado por periodo. El curso 2026-1 vive bajo `2026 - Ciclo 1 Marzo PREG (001) (Actual)`.

## Mapeo cursos portal → carpeta vault (ciclo 2026-1)

| Curso (portal)                            | Sigla | Modalidad    | Docente                       | Carpeta vault         | Course UUID                            | Section UUID                           |
| ----------------------------------------- | ----- | ------------ | ----------------------------- | --------------------- | -------------------------------------- | -------------------------------------- |
| Circuitos Electrónicos Amplificadores     | 29579 | Presencial   | jorge luis robles bokun       | `Amplificadores`      | `08eb7f8d-ab62-53df-9b46-c0ca85f1f263` | `55733e4b-ebe4-5b86-8284-d0afbacba5cd` |
| Controlador Lógico Programable Plc        | 25286 | Presencial   | jorge luis guerrero cardenas (+1) | `PLC`             | `2bcfdc80-6c82-53f7-b910-4b4dd5ebaba6` | `8e09f862-b5fa-5106-8fdc-c7f9b2850c99` |
| Maquinas Eléctricas Estáticas y Rotativas | 14199 | Virtual 24/7 | charlton harley pretel diaz   | `MaquinasElectricas`  | `40ee9986-a006-5cb9-a550-2e82d236051d` | `70765508-9fb9-5029-aa08-d47e3b6ff0ff` |
| Series y Transformadas                    | 14081 | Virtual 24/7 | jose fernando torres diaz     | `SeriesTransformadas` | `0b1407f5-d982-5ee2-b893-1a1e0f3f02e7` | `a9dcc407-c04b-5d30-b7c4-fb698f891128` |

URL base por curso:
`https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`

**IGNORAR siempre:**
- `RUTA LABORAL - LIMA CENTRO 5` (40030, 2026-1)
- `Ruta Laboral` (10025, ciclo PRED-MARZO25)
- `English Discoveries Placement Test` (Período Predeterminado)

## Tabs (los 8 cursos confirmados, mismos para los 4)

Cada tab cambia solo el segmento final del path después de `<base>/section/<section_uuid>/`:

| Tab          | Path                | Contenido                                                                                |
| ------------ | ------------------- | ---------------------------------------------------------------------------------------- |
| Sílabo       | `/syllabus`         | PDF embebido en `<iframe>` desde S3 (`ms-utp-prd-silbiaback-cd.s3.amazonaws.com/pdfs/approved/complete/<ciclo>/<modalidad>/<codigo_curso>.pdf`) |
| Contenido    | `/learnv2`          | Acordeón por semana con materiales/lecciones (estructura varía por modalidad — ver abajo) |
| Evaluaciones | `/listEvaluation`   | Lista de evaluaciones por semana con fechas y estado. **Virtual 24/7** la trae poblada (15 evals típico); **Presencial** suele decir "muy pronto…" porque las evaluaciones se gestionan en clase |
| Tareas       | `/listHomework`     | Tareas por semana. Vacío en cursos actuales                                              |
| Foros        | `/listForum`        | Foros agrupados por semana + foro general "Foro De Consulta" siempre presente            |
| Notas        | `/calification`     | Calificaciones por semana                                                                |
| Anuncios     | `/announcements`    | Comunicados del docente con fecha (uno por semana típico)                                |
| Zoom         | `/zoom`             | Calendario de clases sincrónicas: título / semana / fecha / meeting ID / link            |

## Estructura del tab Contenido (varía por modalidad/curso)

### URL de cada item de contenido
`/learnv2/week/<N>/unit/<section_uuid>/theme/<theme_uuid>/content/<content_uuid>/<tipo>`

Donde `<tipo>` puede ser:
- `html` → "Contenido personalizado" — rich text con LaTeX (fórmulas como `<img alt="LaTeX: ...">`) y figuras. **Es el tipo principal para extraer en cursos Virtual 24/7.**
- `pdf` → "Material ∙ PDF" — slide/lectura descargable
- `url` → "Material ∙ URL" — link externo (ej: descargar plantilla)
- `evaluation/<id>` → "Evaluación calificada" o "Evaluación no calificada"
- `video` → (no observado aún, pero el path sugiere su existencia)

Iconos en los títulos:
- 📚 = lección teórica/práctica
- 📝 = cuestionario / examen no calificado
- 🔴 = evaluación calificada principal (PA, PC, EXFN)
- (AC-SNN) en el título = código de la actividad calificada

### Variantes observadas por curso

**Virtual 24/7 (Maquinas, SyT)** — estructura rica de 3 niveles:
```
Semana NN
  ├─ Introducción a la semana N (1 HTML)
  ├─ Tema 01: Nombre del tema (varios HTML — cada concepto/ejercicio es un item separado)
  ├─ Tema 02: Nombre del tema (varios HTML)
  ├─ Tema NN: ...
  ├─ Material ∙ PDF (opcional, ej. indicaciones de evaluación)
  ├─ Evaluación (📝 cuestionario y/o 🔴 calificada)
  └─ Cierre / Conclusiones de la semana N (1 HTML)
```
Cada **Tema** es un acordeón de segundo nivel que agrupa varios items. **Esto mapea 1:1 a la estructura `sNN/SNN-X Tema NN - Título.md` del vault.**

**Presencial con SNN (Amplificadores)** — solo PDF:
```
Semana NN
  └─ SNN
      └─ Material ∙ PDF — SNN-Material (1 PDF, a veces SNN-Material2)
```
El contenido del curso lo dicta el docente en clase; el PDF es solo soporte.

**Presencial con título (PLC)** — sin SNN:
```
Semana NN — Título descriptivo del tema (e.g. "Operaciones básicas con variables digitales")
  ├─ Material ∙ URL (link externo, ej. plantillas)
  └─ Material ∙ PDF (ej. SNN.s1-Material)
```

### Detalles operativos del acordeón
- Los acordeones son `cursor: pointer`. Para expandir: subir desde el `<p>` del título hasta el primer ancestro con `getComputedStyle(el).cursor === 'pointer'` y hacer `.click()`.
- Click toggles. Para ser idempotente: chequear si dentro del contenedor ya hay `<a href*="/learnv2/week/N/">` antes de clickear.
- En cursos Virtual 24/7 los temas de segundo nivel también son acordeones que hay que expandir (mismo patrón).
- Esperar ~1s tras click para que renderice antes de leer.

## Tabs auxiliares: qué tomar de cada uno al extraer una semana

- **Sílabo**: ya extraído de una vez al iniciar el curso (PDF → genera `Silabo - <Curso>.md`). No se toca por semana.
- **Evaluaciones (Virtual 24/7)**: usar como **fuente autoritativa** del calendario de evals de la semana — confirma fechas, tipo (calificada/no calificada), peso. En Presencial el calendario está en el sílabo.
- **Tareas**: revisar si la semana tiene una tarea (rara vez).
- **Foros**: revisar si la semana tiene un foro calificado.
- **Anuncios**: leer el anuncio de la semana correspondiente — suele tener instrucciones del docente, recordatorios de evals, fe de erratas.
- **Notas**: solo lectura para verificar entregas.
- **Zoom**: ignorar al extraer contenido (es para sesiones en vivo).

## Flujo "Extraer Curso X, Semana Y completa"

### 1. Determinar contexto
- Identificar `<carpeta_vault>` y `<modalidad>` desde el mapeo del curso.
- Construir URL: `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/learnv2`.

### 2. Navegar y autenticar
- `browser_navigate` a la URL del curso.
- Si redirige a SSO, autenticar con `UTP_WEB_USER` / `UTP_WEB_PASS` del `.env`.

### 3. Expandir Semana Y
- Buscar el `<p>` con texto exacto `Semana NN` (con padding cero, e.g. "Semana 06").
- Subir al primer ancestro con `cursor: pointer` y click.
- Esperar 1-2s.
- **Virtual 24/7**: además expandir cada `<p>` del tipo `Introducción a la semana N`, `Tema XX: ... N`, `Cierre de la semana N` dentro de la semana.

### 4. Inventariar items
- Buscar todos los `<a href*="/learnv2/week/N/">` y clasificar por sufijo (`/html`, `/pdf`, `/url`, `/evaluation/...`).
- Capturar el texto visible de cada link (incluye prefijos 📚/📝/🔴 y nombres como "Tema 01: ...").
- Para Virtual 24/7, registrar también el `theme_uuid` del href para agrupar items por tema (Tema 01 vs Tema 02 vs Cierre).

### 5. Cruzar con tabs auxiliares
- Abrir `/listEvaluation` y filtrar evaluaciones de la Semana Y → confirmar fechas y tipo.
- Abrir `/announcements` y leer el comunicado de la semana (si existe) — copiar instrucciones relevantes.
- Abrir `/listForum` y `/listHomework` para detectar foros/tareas con fecha en la Semana Y.

### 6. Crear estructura local
- Carpeta: `cursos/<ciclo>/<carpeta_vault>/clases/sNN/` (donde `sNN` es la semana en minúscula con padding, e.g. `s06`).
- Carpeta: `cursos/<ciclo>/<carpeta_vault>/clases/sNN/attachments/` para imágenes/PDFs.

### 7. Procesar cada item según tipo

**Item `/html` (Virtual 24/7)** — ya cubierto por el "Procedimiento: Extraer contenido del portal UTP" en CLAUDE.md:
- Navegar al link, expandir `<details>`, snapshot accessibility tree, extraer LaTeX (`img "LaTeX: ..."` → `$$...$$` o `$...$`), bajar imágenes con PowerShell, crear nota `SNN-X Tema NN - Título.md`.

**Item `/pdf`** — descargar:
- Tomar `<a href>` del PDF (ya viene firmado; se descarga directo).
- Guardar en `attachments/` con nombre descriptivo (e.g. `SNN-material.pdf`).
- Si el PDF es indicaciones de evaluación → ese contenido alimenta la nota `SNN-99 Evaluación ...md`.
- Si el PDF es soporte de clase Presencial → puede ser la fuente principal para crear notas SNN-X temáticas (extraer texto del PDF y reorganizarlo según convención del vault).

**Item `/url`** — registrar como external link:
- No descargar; copiar la URL real (resolver el redirect si es necesario) y referenciarla en la nota correspondiente.

**Item `/evaluation/<id>`** — abrir y extraer:
- Navegar al link, capturar enunciado y preguntas.
- Crear `SNN-99 Evaluación ... .md` o `SNN-98 Indicaciones ... .md` según convención (ya existen ejemplos en el vault).
- Aplicar las reglas de "Evaluaciones" del CLAUDE.md (analizar imágenes, calcular todas las opciones, wikilinks a teoría).

### 8. Actualizar referencias
- Renumerar notas existentes si se inserta algo entre medio (frontmatter `orden`, archivo, wikilinks).
- Actualizar `Formulario - <Curso>.md` con fórmulas nuevas + `Fuente: [[nota]]`.
- Actualizar `<Curso> MOC.md` con la lista de notas de la semana.
- Si se cierra la semana en evals: actualizar `Dashboard <ciclo>.md` y `Evaluaciones.base` se refresca solo.

### 9. Verificación final
- Confirmar que cada item del portal tiene su contraparte en el vault (HTML→nota, PDF→attachment+ref, EVAL→nota -99, anuncio→referencia en nota cabecera).
- Validar links rotos (`obsidian:obsidian-cli`).

## Apéndices

### Selectores y patrones útiles

```js
// Listar items de la semana N actualmente cargada
Array.from(document.querySelectorAll('a[href*="/learnv2/week/N/"]'))
  .map(a => ({ href: a.getAttribute('href'),
               type: a.href.endsWith('/html') ? 'HTML' :
                     a.href.endsWith('/pdf')  ? 'PDF'  :
                     a.href.endsWith('/url')  ? 'URL'  :
                     a.href.includes('/evaluation/') ? 'EVAL' : 'OTHER',
               text: a.innerText.trim().replace(/\s+/g, ' ') }));

// Expandir un acordeón por título exacto (idempotente)
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
```

### "Semana actual" en el portal
El portal marca "Semana NN - Semana actual" en los tabs Foros, Notas y Evaluaciones. Útil para inferir Y cuando el usuario dice "extrae la semana actual".

### URL del PDF de Sílabo
Patrón: `https://ms-utp-prd-silbiaback-cd.s3.amazonaws.com/pdfs/approved/complete/<ciclo>/<modalidad>/<codigo>_<NombreCursoSinEspacios>.pdf`
- ciclo URL-encoded: `2026%20-%20Ciclo%201%20Marzo`
- modalidad: `presencial` o `virtual` (presumido para 24/7)
- codigo: `100000I21N` (Amplificadores), `100000I39M` (PLC) — **sirven como código del sílabo, no del curso**

---

## Procedimiento: Actualizar Anuncios por curso

### Cuándo correrlo
- **Por defecto:** lunes (inicio de semana) — el docente típicamente publica anuncio nuevo al iniciar la semana.
- **Bajo pedido:** cuando el usuario diga "actualiza anuncios" o equivalente.

### Formato del archivo (ya establecido en sem. 1-6)
- Un solo `Anuncios.md` por curso en `cursos/<ciclo>/<carpeta_vault>/`.
- Orden **cronológico ascendente** (más antiguo arriba, más reciente abajo).
- Una sección `## YYYY-MM-DD HH:MM AM/PM — Título corto` por anuncio.
- Imágenes en `<carpeta_vault>/anuncios-attachments/` con prefijo `YYYY-MM-DD_descripcion.png`. Embed con `![[nombre]]`.
- Frontmatter `tipo: anuncios`, `tags: curso/<slug> + tipo/anuncios`, `curso: "[[<MOC del curso>]]"`.

### Flujo de actualización (por curso)

1. **Leer el último anuncio del archivo local:** `Anuncios.md` del curso, anotar la fecha de la sección final (es la más reciente capturada).
2. **Navegar** a `https://class.utp.edu.pe/student/courses/<course_uuid>/section/<section_uuid>/announcements`.
3. **Listar anuncios del portal** (orden newest-first nativo): extraer `(uuid, dateRaw)` de cada `<a href*="/announcements/">`.
4. **Detectar nuevos:** filtrar los que tengan fecha `>` el último capturado localmente. Comparar también por uuid si las fechas chocan (puede haber varios el mismo día).
5. **Para cada nuevo anuncio (en orden cronológico ascendente para preservar el orden del archivo):**
   - Navegar a `/announcements/<uuid>`, esperar ~1.2s.
   - Extraer body de `.ck-content` (texto + imágenes filtrando `/static/media/` que son íconos UI).
   - Si tiene imagen(es): descargar con PowerShell `Invoke-WebRequest` a `anuncios-attachments/YYYY-MM-DD_descripcion.png` (sufijo `_a`/`_b` si hay varios el mismo día).
   - Si la imagen tiene texto sustancial (slide-anuncio): recortar el área de cuerpo y upscalear ~1.4x con Pillow, luego leer con `Read` para OCR (ver script en `_crops/` durante semanas 1-6 para referencia).
6. **Append al `Anuncios.md`** del curso, una sección por anuncio, con cita en blockquote del cuerpo y embed de la imagen si aplica.
7. **No tocar anuncios anteriores** ya capturados.
8. Si no hay nuevos: reportar "sin nuevos anuncios desde <fecha>" — no modificar el archivo.

### Patrones por docente conocidos

- **Amplificadores (J. Robles Bokun):** un saludo template los lunes 6:00 AM. Texto corto, sin imágenes. Esperar 1 nuevo por semana.
- **PLC (J. Guerrero Cárdenas):** un anuncio los lunes 6:00 AM con el temario de la semana. Texto, sin imágenes. Esperar 1 por semana.
- **Maquinas (Ch. Pretel Diaz):** 2 diapositivas-anuncio por semana — lunes y jueves 12:00 AM (Bienvenida parte 1 + parte 2). Imágenes PNG con título "BIENVENIDO(A) A LA SEMANA N – Marzo 26" + cuerpo en HTML. A veces comunicados puntuales (recordatorios de evaluaciones, claves de simuladores). Esperar 2-3 por semana.
- **SyT (J. F. Torres Diaz):** 2 anuncios-tarjeta por semana — lunes "BIENVENIDO(A) A LA SEMANA N" y viernes "CIERRE SEMANA N". Imágenes PNG. Suele agregar 1-2 anuncios extra (felicitaciones por evaluaciones, invitaciones, instrucciones de PA). Esperar 3-5 por semana.

Si el patrón de un docente cambia significativamente (e.g. nuevo curso, nuevo formato), actualizar esta sección.

## Estado del entrenamiento

- [x] Curso → carpeta vault mapeado (4 cursos)
- [x] Tabs identificados y documentados (8 tabs, mismos para todos)
- [x] Estructura del Contenido por modalidad documentada
- [x] Diferencia entre Virtual 24/7 y las dos variantes Presencial registrada
- [x] Flujo "extraer semana" esbozado
- [ ] **Confirmación del usuario antes de mover a CLAUDE.md**
