---
title: "APF — Prompt para formatear en Microsoft Word (Claude add-in)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-13
---

# APF — Prompt para Microsoft Word (Claude Extension / Add-in)

> [!info] Cómo usarlo
> 1. Exportar primero el contenido a `.docx` con Pandoc (ya trae **ecuaciones nativas**, **figuras incrustadas** y una base de **Arial 12 / interlineado 1.5**):
>    ```powershell
>    uv run python utils/md_to_docx.py "cursos/2026-1/SeriesTransformadas/TrabajoFinal/Proyecto1/APF - Avance Proyecto Final (contenido).md"
>    ```
> 2. Abrir el `.docx` resultante en **Microsoft Word**.
> 3. Abrir el panel del **add-in de Claude** y pegar el prompt de abajo (bloque `text`).
> 4. Revisar los cambios, ajustar la portada con los datos reales y **exportar a PDF** (Archivo → Guardar como → PDF).

---

```text
Eres mi asistente de formato en Microsoft Word. El documento abierto es el "Avance de Proyecto Final" (APF) del curso Series y Transformadas (UTP). El CONTENIDO (introducción, marco teórico, dominio de simulación, dominio teórico, referencias, fórmulas y figuras) ya está escrito y NO debes cambiarlo. Tu tarea es aplicar TODO el formato exigido por la consigna. Aplica exactamente lo siguiente:

1. FUENTE E INTERLINEADO (todo el documento)
   - Fuente Arial, tamaño 12 en todo el cuerpo del texto.
   - Interlineado 1.5 en todo el documento.
   - Alineación justificada en los párrafos de prosa.
   - Títulos de sección (Introducción, Marco teórico, etc.) en Arial, negrita; mantener la jerarquía de niveles (Título 1 para secciones, Título 2 para subsecciones) para que el índice se genere bien.

2. PORTADA (primera página, sin numerar)
   - Crear una portada con: título del proyecto, "Avance de Proyecto Final (APF)", curso "Series y Transformadas", universidad UTP, ciclo 2026-1, docente, modalidad, nombre(s) e integrante(s) con su código, y la fecha (julio 2026).
   - Centrada verticalmente y horizontalmente. Si hay campos entre paréntesis "(completar)", déjalos como marcadores visibles para que yo los rellene.

3. ÍNDICE CON PÁGINAS (segunda página)
   - Insertar una Tabla de Contenido automática de Word (que muestre el número de página de cada sección y subsección). Título "Índice".
   - Debajo, insertar una "Lista de figuras" y una "Lista de tablas" (pueden ser tablas de ilustraciones automáticas de Word, con su número de página), o listarlas manualmente con su número, título breve y página.
   - El índice y las listas deben actualizarse (Actualizar campos) para reflejar la paginación real.

4. FIGURAS Y TABLAS (numeración + definición + índice)
   - Cada figura debe tener un rótulo tipo "Figura N." con una breve definición (leyenda) debajo de la imagen, usando la función Insertar título (Referencias → Insertar título), para que aparezca en la Lista de figuras.
   - Cada tabla debe tener un rótulo "Tabla N." con breve definición encima de la tabla, también con Insertar título, para que aparezca en la Lista de tablas.
   - Respetar la numeración ya presente (Figura 1, 2, 3; Tabla 1, 2, 3, 4). Centrar las figuras.
   - Verificar que cada figura conserve su cita de fuente ("Elaboración propia en GNU Octave").

5. PAGINADO
   - Numerar todas las páginas (pie de página, centrado o a la derecha).
   - La portada NO lleva número; la numeración visible puede empezar en la Introducción (o mostrar el índice como página i en números romanos si es sencillo; si no, numeración arábiga corrida a partir de la portada está bien, pero la portada sin número).

6. FÓRMULAS MATEMÁTICAS
   - Verificar que TODAS las fórmulas estén como ecuaciones nativas de Word (objeto Ecuación), correctamente digitadas y legibles, no como texto plano ni como imágenes. Las ecuaciones en bloque van centradas en su propia línea.
   - Revisar símbolos clave: A, ω₀ (omega sub cero), π, sumatorias Σ, subíndices (a₀, aₙ, bₙ, Eₖ), fracciones y el recuadro de la serie de Fourier final.

7. REFERENCIAS (APA 7)
   - La sección "Referencias bibliográficas" debe ir con sangría francesa, orden alfabético y formato APA 7 (ya está redactada; solo ajustar sangría y estilo).
   - Verificar que cada afirmación del marco teórico conserve su cita en texto (Autor, año) y que cada figura tenga su cita de fuente.

8. CONTROL DE EXTENSIÓN
   - El documento debe tener entre 10 y 20 páginas (sin contar portada e índice si es posible). Si queda por debajo de 10, sugiéreme dónde ampliar (más análisis de resultados) sin inventar contenido; si supera 20, sugiéreme qué comprimir. NO recortes contenido técnico por tu cuenta: solo avísame.

9. AL TERMINAR
   - Actualiza todos los campos (índice, listas, numeración).
   - Dame un checklist de verificación final: fuente Arial 12, interlineado 1.5, portada, índice con páginas, listas de figuras y tablas, figuras/tablas rotuladas, páginas numeradas, ecuaciones nativas, referencias APA, y el conteo de páginas actual.

Restricciones: no cambies el texto ni los datos numéricos del contenido, no elimines figuras ni tablas, no inventes referencias. Solo formato y estructura. El objetivo final es exportar a PDF listo para entregar en Canvas.
```

---

> [!tip] Notas para el PROY (siguiente entrega)
> Este prompt cubre el **APF** (solo Series de Fourier). Para el **Proyecto Final (PROY)** habrá que ampliar el mismo documento agregando: la sección de **Transformada de Laplace**, la **discusión y conclusiones con el error**, y el **video** (≤ 5 min). Se reutilizará este mismo prompt de formato añadiendo esas secciones.
