---
title: "Proyecto 2 v2 — Prompt para Word (formato)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-16
---

# Prompt para dar formato Word al PROY (Proyecto 2 v2)

> [!tip] Vía principal: `md_to_docx.py` primero
> El script [[../../../../utils/md_to_docx.py|utils/md_to_docx.py]] (Pandoc + `reference-apa7.docx`) ya aplica **Arial 12 + interlineado 1.5** y convierte las fórmulas `$...$` a **ecuaciones nativas de Word (OMML)**. Generar primero el `.docx` con el script y usar el prompt de abajo (add-in de Claude para Word) solo para lo que el script no hace: portada, índice con páginas, numeración, rótulos de figuras/tablas y listas automáticas.

> [!info] Cómo usar
> 1. Exportar: `python utils/md_to_docx.py "cursos/2026-1/SeriesTransformadas/TrabajoFinal/Proyecto2-v2/05 - Documento final.md" -o "TitoLuyoMurata-Proyecto2-PROY.docx"` (vía `uv run` si hace falta).
> 2. Abrir el `.docx` en Word y verificar que las 4 imágenes de `attachments/` quedaron incrustadas.
> 3. Abrir el panel del **add-in de Claude para Word** y pegar el bloque completo de abajo.
> 4. Revisar contra el checklist final antes de exportar a PDF.

```text
====================================================================
Dale formato de entrega académica a este documento (Proyecto Final
de "Series y Transformadas", UTP). Aplica exactamente lo siguiente:

1. TIPOGRAFÍA GLOBAL: Arial 12 pt, interlineado 1.5, cuerpo
   justificado, márgenes 2,54 cm, espaciado 6 pt después de párrafo.

2. PORTADA (página 1, centrada, sin número de página): título
   completo del proyecto; "Proyecto Final (PROY) — Series y
   Transformadas"; "Universidad Tecnológica del Perú · Ciclo 2026-1";
   "Docente: J. F. Torres"; "Modalidad: individual";
   "Integrante: Tito Luyo Murata"; "Enlace del video: <el enlace>";
   "Julio de 2026".

3. NUMERACIÓN: páginas numeradas en el pie (arábiga desde la
   Introducción; portada e índice sin numeración arábiga visible).

4. ESTILOS: "Título 1" para las secciones 1–6 y el Anexo A;
   "Título 2" para los subapartados (2.1, 3.1, …), todo en Arial.

5. ÍNDICE: tabla de contenido automática (TOC) tras la portada,
   con números de página; debajo, LISTA DE FIGURAS y LISTA DE
   TABLAS automáticas (con números de página).

6. FIGURAS (4): centradas; usar rótulo automático de Word
   "Figura N." con su leyenda descriptiva y la cita
   "Elaboración propia" / "Elaboración propia en GNU Octave".
   - Figura 1: circuito R–L–C serie con salida en el capacitor.
   - Figura 2: respuesta teórica V_o(t) con el pico de 463,5 V.
   - Figura 3: comparación teórico vs. simulado.
   - Figura 4: error absoluto puntual con el RMSE.

7. TABLAS (2): estilo limpio (líneas horizontales), rótulo
   automático "Tabla N." encima.
   - Tabla 1: parámetros del circuito.
   - Tabla 2: V_o en instantes representativos con el error.

8. FÓRMULAS: verificar que quedaron como ecuaciones nativas OMML
   (no imágenes ni texto plano), en particular:
   - la integral de definición de la Transformada de Laplace;
   - la transformada de las derivadas;
   - la EDO  q'' + 6000 q' + 2,5×10⁸ q = 3×10⁵ ;
   - Q(s) = 3×10⁵ / [s(s² + 6000s + 2,5×10⁸)] ;
   - la completación (s+3000)² + ωd² con ωd = 1000√241 ;
   - el resultado final V_o(t) = 300 − e^(−3000t)(300 cos ωd t
     + 57,97 sin ωd t) ;
   - I(t) = 19,32 e^(−3000t) sin ωd t.

9. REFERENCIAS: formato APA 7 con sangría francesa, orden
   alfabético (Alexander & Sadiku 2013; Eaton et al. 2024;
   Hsu & Ward 1991; Zill 2018). Verificar las citas en el texto.

10. EXTENSIÓN: confirmar que el total queda entre 10 y 20 páginas;
    si falta, no rellenar — avisar; si sobra, mover parte del
    Anexo A a letra 10 pt.

11. LIMPIEZA: eliminar cualquier resto de sintaxis Obsidian
    (callouts "> [!...]", wikilinks [[...]], comentarios <!-- -->).

Al terminar: resume los cambios aplicados y dame los pasos para
exportar a PDF.
====================================================================
```

## Checklist final antes de exportar a PDF

- [ ] Portada con **enlace del video** ya pegado.
- [ ] Arial 12 / interlineado 1.5 / justificado en todo el cuerpo.
- [ ] TOC + lista de figuras + lista de tablas con números de página.
- [ ] 4 figuras y 2 tablas con rótulos numerados y "Elaboración propia".
- [ ] Fórmulas como ecuaciones OMML (editables en Word).
- [ ] Páginas numeradas; total entre **10 y 20**.
- [ ] Referencias APA 7 con sangría francesa; citas presentes en texto e imágenes.
- [ ] Sin restos de sintaxis Obsidian.
- [ ] Exportar como `TitoLuyoMurata-Proyecto2-PROY.pdf`.
