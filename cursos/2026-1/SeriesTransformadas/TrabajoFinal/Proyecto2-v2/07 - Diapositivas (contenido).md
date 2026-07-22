---
title: "Proyecto 2 v2 — Diapositivas del video (contenido)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-07-21
---

# Diapositivas del video — contenido por lámina

> [!info] Cómo usar este archivo
> Contenido listo para pegar en un **generador de diapositivas** (Gamma, Canva, PowerPoint + IA, etc.). Cada sección "Diapositiva N" indica: el **título de la lámina**, el **texto literal** que va en ella (viñetas cortas — la explicación completa la da la voz, ver [[06 - Guion del video]]), el **elemento visual** y el bloque del guion al que acompaña.
> Las fórmulas van en **texto Unicode plano** (no LaTeX) para que cualquier generador las acepte tal cual. Si el generador soporta ecuaciones, puede sustituirse por la versión LaTeX de [[05 - Documento final]].

## Especificaciones globales del deck

- **Formato:** 16:9, orientación horizontal.
- **Tipografía:** Arial (coherente con el documento entregable).
- **Paleta:** azul marino (#1F3864) como color principal + rojo (#C00000) para acentos/resultados — misma paleta de las figuras del proyecto.
- **Total:** 11 diapositivas para ≤ 5 minutos de video (≈ 25–30 s por lámina).
- **Imágenes:** están en `TrabajoFinal/Proyecto2-v2/attachments/` — `fig1_circuito.png`, `fig2_vo_teorico.png`, `fig3_comparacion.png`, `fig4_error.png`. Insertarlas tal cual (ya tienen títulos y ejes).
- **Números:** mantener coma decimal (convención del documento): 463,5 V · 0,202 ms · 3,79×10⁻⁵ V.

**Mapa diapositiva ↔ bloque del guion:**

| Diapositivas | Bloque del video | Tiempo |
| ------------ | ---------------- | ------ |
| 1 | 1 — Título | 0:00–0:25 |
| 2–3 | 2 — Objetivos | 0:25–0:55 |
| 4–5 | 3 — Metodología | 0:55–2:15 |
| 6–9 | 4 — Análisis de resultados | 2:15–4:00 |
| 10–11 | 5 — Conclusiones | 4:00–4:50 |

---

## Diapositiva 1 — Portada

**Bloque:** 1 (Título, 0:00–0:25)

**Título en la lámina:**
Determinación del voltaje de un capacitor en un circuito R–L–C serie mediante la Transformada de Laplace y su simulación en GNU Octave

**Contenido:**
- Proyecto Final (PROY) — Series y Transformadas
- Universidad Tecnológica del Perú · Ciclo 2026-1
- Docente: J. F. Torres
- Integrante: Tito Luyo Murata · Modalidad: individual
- Julio de 2026

**Visual:** fondo sobrio azul marino; opcionalmente `fig1_circuito.png` pequeña como motivo decorativo.

---

## Diapositiva 2 — Objetivos

**Bloque:** 2 (Objetivos, 0:25–0:55)

**Título en la lámina:** Objetivos

**Contenido:**
- **Objetivo principal:** determinar el voltaje del capacitor Vo(t) por dos vías independientes — **analítica** (Transformada de Laplace) y **por simulación** (GNU Octave) — y comparar ambas mostrando el **error**.
- Plantear la ecuación diferencial del circuito con la ley de Kirchhoff (en la carga q)
- Resolver Q(s) con Laplace y obtener Vo(t) = q(t)/C en forma cerrada
- Simular la misma ecuación en Octave por una vía independiente (lsode)
- Comparar teoría vs. simulación cuantificando el error

**Visual:** lista con iconos simples (fórmula, computadora, balanza).

---

## Diapositiva 3 — El circuito propuesto

**Bloque:** 2 (Objetivos, 0:25–0:55)

**Título en la lámina:** El circuito: R–L–C serie con fuente escalón

**Contenido:**
- R = 6 Ω · L = 1 mH · C = 4 µF · E = 300 V (escalón, interruptor cierra en t = 0)
- Valores comerciales típicos de electrónica de potencia (bus DC de 300 V)
- Condiciones iniciales: q(0) = 0, I(0) = 0 (capacitor descargado)
- Salida de interés: **Vo = q/C** (voltaje del capacitor)

**Visual:** `fig1_circuito.png` grande (ocupa media lámina o más).

---

## Diapositiva 4 — Metodología: ruta de solución

**Bloque:** 3 (Metodología, 0:55–2:15)

**Título en la lámina:** Metodología: dos vías independientes

**Contenido (diagrama de flujo, dos ramas):**

Rama 1 — Teoría (Laplace):
- Ley de voltajes de Kirchhoff → EDO de 2.º orden en la carga q
- Transformada de Laplace → ecuación algebraica → despejar Q(s)
- Fracciones parciales → completar cuadrados → antitransformar
- q(t) → **Vo(t) = q(t)/C**

Rama 2 — Simulación (Octave):
- La misma EDO se integra numéricamente con **lsode**
- **Sin usar la fórmula cerrada** → vía independiente

Cierre común: Comparación → error (RMSE)

**Visual:** diagrama de flujo con las dos ramas en paralelo que convergen en un bloque final "Comparación (error)". Rama 1 en azul, rama 2 en rojo.

---

## Diapositiva 5 — Desarrollo teórico (dominio s)

**Bloque:** 3 (Metodología, 0:55–2:15)

**Título en la lámina:** De la EDO a Q(s)

**Contenido:**
- EDO del circuito (CI nulas):  **q″ + 6000 q′ + 2,5×10⁸ q = 3×10⁵**
- Aplicando Laplace y despejando:  **Q(s) = 3×10⁵ / [ s (s² + 6000 s + 2,5×10⁸) ]**
- Fracciones parciales:  A = 1,2×10⁻³ · B = −1,2×10⁻³ · D = −7,2
- Completando cuadrados:  s² + 6000 s + 2,5×10⁸ = (s + 3000)² + ωd² , con **ωd = 1000·√241 ≈ 15 524 rad/s**

**Visual:** las 4 líneas como ecuaciones grandes y centradas, una debajo de otra (es la lámina "matemática" del video; sin figuras).

---

## Diapositiva 6 — Resultado teórico

**Bloque:** 4 (Análisis, 2:15–4:00)

**Título en la lámina:** Solución exacta por Laplace

**Contenido:**
- En recuadro destacado (rojo):  **Vo(t) = 300 − e^(−3000t) · [ 300 cos(ωd t) + 57,97 sen(ωd t) ]  V**
- Corriente:  I(t) = 19,32 · e^(−3000t) · sen(ωd t)  A
- Autocomprobación física:  Vo(0) = 0 ✓ · I(0) = 0 ✓ · Vo(∞) = 300 V = E ✓

**Visual:** la fórmula de Vo(t) como protagonista (recuadro, tamaño grande); las otras dos líneas debajo, menores.

---

## Diapositiva 7 — Respuesta teórica: el pico de 463,5 V

**Bloque:** 4 (Análisis, 2:15–4:00)

**Título en la lámina:** Transitorio oscilatorio amortiguado

**Contenido:**
- Polos complejos: s = −3000 ± j·15 524 → oscilación amortiguada
- **Pico: 463,5 V (+54,5 % sobre la fuente) en t = 0,202 ms**
- Frecuencia de oscilación: ≈ 2,47 kHz · se estabiliza en 300 V en ≈ 1,3 ms
- Dato de diseño: los componentes deben soportar mucho más que los 300 V nominales

**Visual:** `fig2_vo_teorico.png` grande (el pico ya está anotado en la figura).

---

## Diapositiva 8 — Simulación en Octave

**Bloque:** 4 (Análisis, 2:15–4:00)

**Título en la lámina:** Simulación independiente con lsode

**Contenido:**
- Estado x = [q, q′] → lsode integra la EDO original (no conoce la fórmula)
- Malla: 0 a 2 ms, 4001 puntos (Δt = 0,5 µs)
- **Las curvas teórica y simulada se superponen por completo**

**Visual:** `fig3_comparacion.png` grande. Opcional: mini-captura del núcleo del script (5 líneas de código) en una esquina.

---

## Diapositiva 9 — Comparación con el error

**Bloque:** 4 (Análisis, 2:15–4:00)

**Título en la lámina:** El error: teoría vs. simulación

**Contenido:**
- **RMSE = 3,79×10⁻⁵ V** · error máximo = 9,19×10⁻⁵ V
- Error relativo **< 10⁻⁴ %** en todo el intervalo

Tabla (versión abreviada de la Tabla 2):

| t [ms] | Vo teórico [V] | Vo simulado [V] | error [V] |
| ------ | -------------- | --------------- | ----------- |
| 0,1000 | 252,9746 | 252,9746 | 1,71×10⁻⁵ |
| 0,2025 (pico) | 463,4778 | 463,4777 | 5,86×10⁻⁵ |
| 0,5000 | 280,9761 | 280,9761 | 1,97×10⁻⁵ |
| 1,0000 | 314,1571 | 314,1570 | 5,02×10⁻⁵ |
| 2,0000 | 299,3577 | 299,3577 | 1,45×10⁻⁵ |

**Visual:** `fig4_error.png` a un lado (escala logarítmica con el RMSE marcado) + la tabla al otro.

---

## Diapositiva 10 — Conclusiones

**Bloque:** 5 (Conclusiones, 4:00–4:50)

**Título en la lámina:** Conclusiones

**Contenido (3 bloques numerados):**
1. **Teórica.** Laplace entrega la solución exacta y revela el pico de 463,5 V: los componentes deben especificarse para tensiones muy superiores a los 300 V nominales (capacitor de 500–630 V).
2. **De simulación.** Un método numérico independiente (lsode) reproduce toda la dinámica partiendo solo de la EDO: el modelo del circuito queda validado.
3. **De la comparación.** Con error relativo < 10⁻⁴ % (RMSE = 3,79×10⁻⁵ V), teoría y simulación son equivalentes: **se cumple el objetivo del proyecto**.

**Visual:** tres tarjetas o bloques horizontales, la tercera destacada en rojo.

---

## Diapositiva 11 — Cierre

**Bloque:** 5 (Conclusiones, 4:00–4:50)

**Título en la lámina:** Gracias

**Contenido:**
- Recuadro con la fórmula final:  Vo(t) = 300 − e^(−3000t) · [ 300 cos(ωd t) + 57,97 sen(ωd t) ]  V
- Tito Luyo Murata · Series y Transformadas · UTP 2026-1
- Referencias completas en el documento del proyecto (formato APA)

**Visual:** fondo igual a la portada; lámina que queda fija mientras se despide.

---

## Checklist tras generar el deck

- [ ] 11 láminas, formato 16:9, tipografía Arial.
- [ ] Las 4 figuras insertadas desde `attachments/` sin recortar (títulos y ejes visibles).
- [ ] Fórmulas legibles a tamaño de video (probar en miniatura: la de Vo(t) debe leerse).
- [ ] Coma decimal en todos los números (463,5 — no 463.5).
- [ ] Exportar también a PDF/PPT como respaldo.
- [ ] Ensayar el guion con las láminas: cada bloque del video debe caer en su diapositiva según el mapa de arriba.
