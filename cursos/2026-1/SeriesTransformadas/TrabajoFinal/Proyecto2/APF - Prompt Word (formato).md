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

# APF — Prompt para maquetar en Word con el add-in de Claude

> [!info] Cómo usar este prompt
> 1. Abre **Microsoft Word** y pega dentro el contenido de [[APF - Documento (Laplace)|APF - Documento (Laplace).md]] (o convierte ese .md a .docx con `md_to_docx.py` y ábrelo). Las 4 imágenes están en `attachments/` (`fig1_circuito.png`, `fig2_vo_teorico.png`, `fig3_comparacion.png`) — insértalas si no se incrustaron.
> 2. Abre el panel del **add-in / extensión de Claude para Word**.
> 3. Copia y pega **todo el bloque de abajo** (entre las líneas `====`) como instrucción.
> 4. Revisa el resultado contra el checklist final antes de exportar a PDF.

> [!tip] Atajo alternativo
> El script [[exportar-docx|utils/md_to_docx.py]] ya aplica automáticamente **Arial 12 + interlineado 1.5** (plantilla `reference-apa7.docx`) y convierte las fórmulas `$...$` a ecuaciones nativas de Word. Si partes de ese .docx, este prompt se concentra en lo que falta: **índice con páginas, numeración de páginas, títulos/pies de figuras y tablas, y lista de figuras/tablas**.

---

====================  PROMPT PARA EL ADD-IN DE CLAUDE EN WORD  ====================

Actúa como maquetador experto de documentos académicos en Microsoft Word. Este documento es el **Avance de Proyecto Final (APF)** de un curso de ingeniería (UTP, Perú) sobre la Transformada de Laplace. Aplícale el siguiente formato **sin cambiar el contenido técnico ni las fórmulas**, solo su presentación. Trabaja sobre el documento actual.

**1. Tipografía e interlineado (todo el documento).**
- Fuente **Arial, tamaño 12** en todo el cuerpo del texto.
- **Interlineado 1.5** en todo el documento.
- Alineación del cuerpo **justificada**; márgenes normales (2,54 cm).
- Espaciado entre párrafos: 6 pt después; sin sangría de primera línea (o sangría uniforme, pero consistente).

**2. Portada (primera página).**
- Coloca en la primera página, centrado: el **título** del trabajo, el curso ("Series y Transformadas"), el docente ("J. F. Torres"), la modalidad, el/los integrante(s) con su código, y la fecha ("julio de 2026").
- La portada **no lleva número de página** visible.

**3. Numeración de páginas.**
- Inserta **número de página** en el pie (centrado o esquina inferior derecha), fuente Arial.
- La portada y la página del índice **no** se numeran (o usan numeración romana); el cuerpo (desde la Introducción) inicia en **página 1** con numeración arábiga.

**4. Estilos de título (imprescindible para el índice automático).**
- Aplica el estilo **Título 1** a los encabezados de sección: "1. Introducción", "2. Marco teórico", "3. Dominio teórico de la Transformada de Laplace", "4. Dominio de simulación de la Transformada de Laplace", "5. Referencias bibliográficas".
- Aplica **Título 2** a los subapartados (2.1, 2.2, 3.1, 3.2, …).
- Modifica los estilos de Título para que también usen **Arial** (color negro o azul oscuro sobrio), de modo que combinen con el cuerpo.

**5. Índice con números de página.**
- En la sección "Índice", inserta una **Tabla de contenido automática** de Word (basada en los estilos Título 1 y Título 2), que muestre **cada sección con su número de página**.
- Debajo, genera una **Lista de figuras** y una **Lista de tablas** automáticas (Referencias → Insertar tabla de ilustraciones, una para el rótulo "Figura" y otra para "Tabla"), cada entrada con su número de página.
- Reemplaza la nota provisional sobre paginación por estas tablas reales.

**6. Figuras (hay 3: Figura 1, 2 y 3).**
- Cada figura debe ir **centrada**.
- Convierte el texto de pie en un **título/subtítulo de Word** (Referencias → Insertar título, rótulo "Figura"), para que la numeración sea automática y aparezca en la Lista de figuras. El texto del pie ya está redactado (p. ej. "Figura 1. Circuito RLC serie con salida en el capacitor. Elaboración propia."). Mantén la **cita de la imagen** ("Elaboración propia" o "Elaboración propia en GNU Octave") como parte del pie —es la cita APA de la figura—.
- Pie en Arial, tamaño 10–11, centrado bajo la figura.

**7. Tablas (hay 3: Tabla 1, 2 y 3).**
- Aplica un **estilo de tabla** limpio y legible (bordes finos, fila de encabezado sombreada).
- Antes de cada tabla, coloca su **título** con rótulo de Word "Tabla" (Referencias → Insertar título, rótulo "Tabla"), para que numere automáticamente y aparezca en la Lista de tablas. Los títulos ya están redactados (p. ej. "Tabla 1. Parámetros del circuito RLC serie.").
- Texto de la tabla en Arial 11, interlineado sencillo dentro de las celdas.

**8. Fórmulas matemáticas (correctamente digitadas).**
- **Todas** las expresiones matemáticas deben quedar como **ecuaciones nativas de Word** (editor de ecuaciones / OMML), **no como texto plano ni imágenes**. Verifica especialmente:
  - La definición de la integral de Laplace.
  - La transformada de las derivadas.
  - La ecuación diferencial del circuito: v_C'' + 6 v_C' + 25 v_C = 2500.
  - V_o(s) = 2500 / [ s (s² + 6s + 25) ].
  - La completación de cuadrados (s+3)² + 4².
  - El resultado final: V_o(t) = 100 − 100 e^(−3t) cos 4t − 75 e^(−3t) sin 4t.
- Las ecuaciones "destacadas" (las que estaban en recuadro) deben ir **centradas** en su propia línea. Usa subíndices/superíndices reales (v_C, e^{−3t}, s²), no caracteres sueltos.
- Revisa que los símbolos griegos (ω, ζ, α, π) y el signo de grados/ohmios (Ω) se rendericen bien en Arial.

**9. Referencias (APA 7).**
- La lista de la sección 5 debe llevar **sangría francesa** (primera línea al margen, resto sangrado 1,27 cm), **orden alfabético** por apellido y **interlineado 1.5**.
- Verifica que cada obra citada en el texto (Alexander & Sadiku, 2013; Eaton et al., 2024; Hsu & Ward, 1991; Nilsson & Riedel, 2015; Zill, 2018) aparezca en la lista y viceversa.
- Deja las **citas en el texto** en formato autor-fecha tal como están.

**10. Control de extensión.**
- El documento final debe tener **entre 10 y 20 páginas**. Si al maquetar queda por debajo de 10, avísame para ampliar el análisis; si supera 20, sugiere qué comprimir. **No** recortes contenido técnico por tu cuenta.

**11. Limpieza.**
- Elimina cualquier marca de comentario, bloque de "nota" tipo Obsidian (`> [!info]`, `> [!note]`, `> [!warning]`) y notas al maquetador que hayan quedado del original; su contenido útil intégralo como texto normal solo si aporta al informe (p. ej. la nota de alcance del avance puede quedar como un breve párrafo al final de la sección 4).

Cuando termines, dame un **resumen** de: número de páginas resultante, si el índice y las listas de figuras/tablas se generaron correctamente, y cualquier fórmula o imagen que no se haya podido convertir. Finalmente, indícame los pasos para **exportar a PDF** (Archivo → Guardar como / Exportar → PDF) conservando la numeración y el índice.

==================================================================================

---

## Checklist de verificación (tras aplicar el prompt)

- [ ] Todo el texto en **Arial 12**, interlineado **1.5**.
- [ ] **Portada** completa (título, curso, docente, integrantes, fecha).
- [ ] **Páginas numeradas** (portada e índice sin número arábigo).
- [ ] **Índice automático** con secciones y **números de página**.
- [ ] **Lista de figuras** y **Lista de tablas** con sus páginas.
- [ ] Figuras 1–3 centradas, con **título** de Word y **cita** ("Elaboración propia") en el pie.
- [ ] Tablas 1–3 con **título** de Word numerado y estilo legible.
- [ ] **Fórmulas** como ecuaciones nativas de Word, con subíndices/superíndices correctos.
- [ ] **Referencias** en APA 7 con sangría francesa; citas en texto verificadas.
- [ ] Extensión **entre 10 y 20 páginas**.
- [ ] Exportado a **PDF** para subir a Canvas.

> [!danger] Recordatorio de alcance
> Este es el **APF** (avance): solo Transformada de Laplace, **sin** cuantificación del error, conclusiones ni video. Esos elementos —y, según tu plan, la parte adicional de **Series de Fourier**— se integran en el **Proyecto Final** completo, que se maquetará después con un prompt equivalente ampliado.
