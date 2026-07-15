---
title: "Proyecto 1 — Guion del video (≤ 5 min)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-13
---

# Proyecto 1 — Guion del video (Etapa V)

> [!warning] Requisitos (criterio 7 — 3 pts)
> Duración **máxima 5 min** · subir a **Drive/YouTube** y entregar el **enlace** · **todos los integrantes** aparecen · orden obligatorio: **Título → Objetivos → Metodología → Análisis de resultados → Conclusiones**.

## Guion por bloques

| # | Tiempo | Quién | Qué se dice (texto guía) | Qué se muestra en pantalla |
| - | ------ | ----- | ------------------------ | -------------------------- |
| **1. Título** | 0:00–0:25 | _(int. 1)_ | "Proyecto 1 del curso Series y Transformadas: análisis de una **señal senoidal rectificada de media onda** mediante series de Fourier y su simulación en GNU Octave. Integrantes: …" | Portada del documento (título, curso, nombres) |
| **2. Objetivos** | 0:25–0:55 | _(int. 1)_ | "Objetivo principal: hallar la serie de Fourier de la señal **por teoría y por simulación** y compararlas con el **error cuadrático medio**. Específicos: definir la señal, calcular sus coeficientes, reconstruirla en Octave y medir el error." | Bullet list de objetivos |
| **3. Metodología** | 0:55–2:10 | _(int. 2)_ | "La señal es el semiciclo positivo de un seno de 60 Hz, amplitud $A=12\sqrt2$ V. Como no es par ni impar, calculamos $a_0$, $a_n$ y $b_n$ integrando solo en medio periodo. Tratamos aparte el caso $n=1$. Para simular usamos Octave: reconstruimos la señal con $N$ armónicos y medimos el error con `trapz`." | Ecuación de $f(t)$ + fórmulas de coeficientes de [[Proyecto1/03 - Desarrollo analitico (teoria)|Etapa T]]; vista del script `proyecto1_fourier.m` |
| **4. Análisis de resultados** | 2:10–4:05 | _(int. 2 y 3)_ | "La serie da un nivel DC $A/\pi$, una fundamental $A/2\,\sin\omega_0 t$ y armónicos pares. En la Figura 2 se ve que con 2 armónicos ya reproducimos bien la señal y con 10 es casi perfecta, **sin efecto Gibbs**. La Figura 3 muestra el error: teórico y simulado coinciden a menos del 0,01 %." | **Figura 2** (superposición) y **Figura 3** (error) de [[Proyecto1/04 - Simulacion (Octave)|Etapa S]]; Tabla 3 comparativa |
| **5. Conclusiones** | 4:05–4:55 | _(int. 3)_ | "Teoría y simulación dan el mismo error, lo que valida ambos métodos. La señal converge rápido por ser continua: 10 armónicos dejan solo 0,01 % de potencia residual. Cumplido el objetivo del proyecto." | Recuadro de la serie final + Tabla 3 |

> [!tip] Cronometraje
> Deja ~5 s de margen por bloque; ensaya una vez con cronómetro. Si sobra tiempo, ampliar el bloque 4 (es el de más peso en la rúbrica). **No superar 5:00**.

## Checklist de grabación

- [ ] Guion ensayado y cronometrado ≤ 5:00.
- [ ] Pantalla compartida con figuras de [[Proyecto1/04 - Simulacion (Octave)]] y ecuaciones de [[Proyecto1/03 - Desarrollo analitico (teoria)]].
- [ ] **Todos los integrantes** aparecen (cámara o voz identificada) explicando su parte.
- [ ] Audio claro; figuras legibles a pantalla completa.
- [ ] Exportado ≤ 5 min y subido a **Drive/YouTube** con acceso público (o "cualquiera con el enlace").
- [ ] Enlace **probado en ventana de incógnito** y pegado abajo + en el documento + en la entrega de Canvas.

## Enlace final del video

> **URL:** _(pegar aquí tras subir)_
