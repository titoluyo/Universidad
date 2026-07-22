---
title: "Proyecto 2 v2 — Guion del video"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-16
---

# Proyecto 2 v2 — Guion del video (individual)

> [!warning] Requisitos del criterio "Dominio del tema (video)" (3 pts)
> Duración **máxima 5 minutos** · subir a **Drive o YouTube** y entregar el enlace (no adjuntar el archivo pesado) · debe especificar en orden: **Título → Objetivos → Metodología → Análisis de los resultados → Conclusiones** · modalidad **individual**: un solo presentador (aparecer en cámara al menos al inicio).

> [!tip] Apoyo visual
> El video se graba sobre el **deck de 11 diapositivas** definido en [[07 - Diapositivas (contenido)]]. La línea *Qué se muestra* de cada bloque referencia esas láminas como **D1…D11**; el mapa completo diapositiva ↔ bloque está en ese archivo.
> Dentro del texto hablado, las marcas **[Dn]** indican el **momento exacto de cambiar de lámina** (no se leen en voz alta).

## Guion por bloques (presentador único)

### Bloque 1 — Título (0:00–0:25)

**Qué se dice:**

> **[D1 + cámara]** "Buenas. Soy Tito Luyo Murata. Presento mi Proyecto Final del curso Series y Transformadas: *Determinación del voltaje de un capacitor en un circuito R–L–C serie mediante la Transformada de Laplace y su simulación en GNU Octave*."

**Qué se muestra:** Cámara + **D1** (portada)

### Bloque 2 — Objetivos (0:25–0:55)

**Qué se dice:**

> **[D2]** "El objetivo es hallar el voltaje del capacitor $V_o(t)$ por dos vías independientes —analítica, con la Transformada de Laplace, y numérica, simulando en Octave— y comparar ambas mostrando el error. **[→ D3]** El circuito propuesto usa valores comerciales: R de 6 ohmios, L de 1 milihenrio, C de 4 microfaradios y una fuente escalón de 300 voltios. El capacitor parte descargado —condiciones iniciales nulas— y la salida de interés es su voltaje, $V_o = q/C$."

**Qué se muestra:** **D2** (objetivos) → **D3** (circuito, Figura 1)

### Bloque 3 — Metodología (0:55–2:15)

**Qué se dice:**

> **[D4]** "Primero planteo la malla con la ley de voltajes de Kirchhoff, lo que da una ecuación diferencial de segundo orden en la carga: **[→ D5]** $q'' + 6000q' + 2{,}5\times10^8 q = 3\times10^5$, con condiciones iniciales nulas. Aplico la Transformada de Laplace —que convierte la EDO en una ecuación algebraica—, despejo $Q(s)$, descompongo en fracciones parciales, completo cuadrados y antitransformo. La carga dividida entre C da el voltaje pedido. **[→ D4, rama roja — opcional: el script en Octave]** En paralelo, simulo en Octave integrando la misma EDO con `lsode`, **sin usar la fórmula**: es una vía independiente."

**Qué se muestra:** **D4** (metodología: dos vías) → **D5** (EDO → $Q(s)$ → cuadrados); opcional: cerrar el bloque mostrando el script abierto en Octave

### Bloque 4 — Análisis de resultados (2:15–4:00)

**Qué se dice:**

> **[D6]** "La solución cerrada es $V_o(t) = 300 - e^{-3000t}(300\cos\omega_d t + 57{,}97\sin\omega_d t)$, con $\omega_d \approx 15\,524$ rad/s. **[→ D7]** La respuesta es un transitorio oscilatorio amortiguado: el capacitor sube desde cero, **sobrepasa la fuente hasta 463,5 voltios** —un 54 % más— en solo 0,2 milisegundos, oscila a unos 2,5 kilohertz y se estabiliza en 300 voltios en 1,3 milisegundos. **[→ D8]** La simulación reproduce exactamente la misma curva: **[→ D9]** el error máximo es de nueve cienmilésimas de voltio, con un RMSE de $3{,}8\times10^{-5}$ V — una coincidencia mejor que una parte en un millón."

**Qué se muestra:** **D6** (fórmula de $V_o$) → **D7** (Figura 2, pico) → **D8** (Figura 3, superposición) → **D9** (Figura 4 + tabla del error)

### Bloque 5 — Conclusiones (4:00–4:50)

**Qué se dice:**

> **[D10]** "Tres conclusiones. Teórica: Laplace entrega la solución exacta y revela el pico de 463 voltios — el dato de diseño clave: los componentes deben soportar mucho más que los 300 nominales. De simulación: un método numérico independiente llega al mismo resultado, validando el modelo. Y de la comparación: con un error relativo menor a $10^{-4}$ por ciento, teoría y simulación son equivalentes — se cumple el objetivo del proyecto." **[→ D11]** *(pasar a la lámina de cierre mientras te despides)*

**Qué se muestra:** **D10** (tres conclusiones) → **D11** (cierre con el recuadro de $V_o(t)$)

> [!tip] Cronometraje
> Deja ~10 s de margen total: cierra máximo en 4:50 para no arriesgar el límite de 5:00. Ensaya el bloque 3 (el más denso) por separado.

## Checklist de grabación

- [ ] Guion ensayado completo ≤ 4:50.
- [ ] Deck de 11 diapositivas generado desde [[07 - Diapositivas (contenido)]] y abierto en modo presentación (opcional: Octave con el script abierto para el cierre del bloque 3).
- [ ] Ensayado el paso de láminas según el mapa: D1 · D2–D3 · D4–D5 · D6–D9 · D10–D11.
- [ ] Aparecer en cámara al menos en el bloque 1 (requisito: el integrante aparece explicando).
- [ ] Audio claro, sin ruido de fondo.
- [ ] Exportar, verificar duración ≤ 5:00 y subir a Drive/YouTube.
- [ ] Enlace probado en **ventana de incógnito** (acceso: cualquiera con el enlace).
- [ ] Pegar el enlace en la portada de [[05 - Documento final]] **antes de exportar el PDF** y también en el campo de la entrega.

## Enlace final del video

_(pegar aquí tras subir)_
