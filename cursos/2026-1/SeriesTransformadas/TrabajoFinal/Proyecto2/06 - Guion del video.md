---
title: "Proyecto 2 — Guion del video (≤ 5 min)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-13
---

# Proyecto 2 — Guion del video (Etapa E)

> [!warning] Requisitos (criterio 7 — 3 pts)
> Duración **máxima 5 min** · subir a **Drive/YouTube** y entregar el **enlace** · **todos los integrantes** aparecen · orden obligatorio: **Título → Objetivos → Metodología → Análisis de resultados → Conclusiones**.

## Guion por bloques

| # | Tiempo | Quién | Qué se dice (texto guía) | Qué se muestra en pantalla |
| - | ------ | ----- | ------------------------ | -------------------------- |
| **1. Título** | 0:00–0:25 | _(int. 1)_ | "Proyecto 2 del curso Series y Transformadas: determinación del **voltaje de un capacitor** $V_o(t)$ en un circuito **RLC serie** mediante la **Transformada de Laplace** y su simulación en GNU Octave. Integrantes: …" | Portada del documento (título, curso, nombres) |
| **2. Objetivos** | 0:25–0:55 | _(int. 1)_ | "Objetivo principal: hallar $V_o(t)$ **por teoría y por simulación** y compararlas mostrando el **error**. Específicos: plantear la ecuación del circuito, resolverla por Laplace, simularla en Octave y medir el error." | Bullet list de objetivos + Figura 1 (circuito) |
| **3. Metodología** | 0:55–2:10 | _(int. 2)_ | "El circuito es un RLC serie ($L=1$ H, $R=6\ \Omega$, $C=0{,}04$ F) con una fuente escalón de 100 V. Por Kirchhoff obtenemos la EDO $v_C'' + 6v_C' + 25v_C = 2500$ con condiciones iniciales nulas. Aplicamos Laplace: la EDO se vuelve algebraica, despejamos $V_o(s)$, hacemos fracciones parciales, completamos cuadrados $(s+3)^2+4^2$ y antitransformamos. En paralelo, en Octave integramos la misma EDO con `lsode`, **sin usar la fórmula**." | Ecuación de $f(t)$ y pasos de [[Proyecto2/03 - Desarrollo analitico (teoria)|Etapa B]]; vista del script `proyecto2_laplace.m` |
| **4. Análisis de resultados** | 2:10–4:05 | _(int. 2 y 3)_ | "La solución teórica es $V_o(t) = 100[1 - e^{-3t}(\cos 4t + \tfrac34\sin 4t)]$ V. El sistema es **subamortiguado**: sube, **sobrepasa** los 100 V hasta 109,5 V hacia 0,79 s y luego oscila hasta estabilizarse en 1,33 s (Figura 2). En la Figura 3 la curva simulada se **superpone exactamente** a la teórica, y en la Figura 4 el error se queda en $10^{-6}$–$10^{-5}$ V: un RMSE de solo $8{,}3\times10^{-6}$ V." | **Figura 2** (respuesta), **Figura 3** (comparación) y **Figura 4** (error) de [[Proyecto2/04 - Simulacion (Octave)|Etapa C]]; Tabla 3 |
| **5. Conclusiones** | 4:05–4:55 | _(int. 3)_ | "Teoría y simulación dan el mismo voltaje del capacitor con un error ínfimo, lo que valida ambos métodos por caminos independientes. El capacitor se carga a la fuente con un sobreimpulso del 9,5 % propio del régimen subamortiguado. Cumplido el objetivo del proyecto." | Recuadro de $V_o(t)$ + Tabla 3 comparativa |

> [!tip] Cronometraje
> Deja ~5 s de margen por bloque; ensaya una vez con cronómetro. Si sobra tiempo, ampliar el bloque 4 (es el de más peso en la rúbrica). **No superar 5:00**.

## Checklist de grabación

- [ ] Guion ensayado y cronometrado ≤ 5:00.
- [ ] Pantalla compartida con figuras de [[Proyecto2/04 - Simulacion (Octave)]] y ecuaciones de [[Proyecto2/03 - Desarrollo analitico (teoria)]].
- [ ] **Todos los integrantes** aparecen (cámara o voz identificada) explicando su parte.
- [ ] Audio claro; figuras legibles a pantalla completa.
- [ ] Exportado ≤ 5 min y subido a **Drive/YouTube** con acceso público (o "cualquiera con el enlace").
- [ ] Enlace **probado en ventana de incógnito** y pegado abajo + en el documento + en la entrega de Canvas.

## Enlace final del video

> **URL:** _(pegar aquí tras subir)_
