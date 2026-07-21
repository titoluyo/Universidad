---
title: "Proyecto 2 v2 — Decisión y alcance"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/transformada-de-laplace
  - tema/circuito-rlc
date: 2026-07-16
---

# Proyecto 2 v2 — Decisión y alcance

> [!important] Esta carpeta contiene el ENTREGABLE del PROY
> El Proyecto Final (30 %, vence **mar 21 jul 11:59 p.m., 1 intento**) se entrega desde esta carpeta. La [[../Proyecto2/05 - Documento final|versión 1]] queda **intacta como archivo de referencia** — no se borra ni se modifica.

## Por qué existe esta v2

1. **El PROY corresponde al Proyecto 2 (Laplace).** El docente aclaró que el cruce de la consigna es intencional: quien desarrolló el Proyecto 1 (Fourier) en el [[../Proyecto1/APF - Avance Proyecto Final (contenido)|APF]] desarrolla el Proyecto 2 en el Proyecto Final — todos pasan por ambas transformadas. Ver [[../Consigna oficial - Proyecto Final (transcripcion)|consigna transcrita]].
2. **La consigna no define el circuito** — dice "un circuito específico" sin figura ni valores, y no existe ningún circuito con $V_o$ como incógnita en el material del curso (verificado: s14 resuelve carga y corriente; s15 es T. de Fourier; s17 es T. Z). Proponerlo es parte del trabajo del estudiante, igual que la señal del Proyecto 1.
3. **Decisión metodológica de esta v2:** seguir el **método exacto de clase** ([[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|S14-3]]): plantear la ecuación en la **carga** $q(t)$ por Kirchhoff, aplicar Laplace, fracciones parciales, completar cuadrados y antitransformar — y añadir como paso propio la conversión $V_o(t) = q(t)/C$, que es exactamente lo que pide la consigna. La v1 planteaba directamente en $v_C$ e incluía una tabla de parámetros de 2.º orden ($\zeta$, $M_p$, $t_s$) ajena al curso; esta v2 se mantiene en el vocabulario del curso.

## El circuito de esta versión (decisión del 16 jul 2026)

Circuito **serie en orden R–L–C** con fuente escalón, valores **comerciales realistas** (escala de electrónica de potencia):

| Parámetro | Valor | Justificación |
| --------- | ----- | ------------- |
| $R$ | $6\ \Omega$ | valor comercial estándar |
| $L$ | $1\ \text{mH}$ | inductancia típica de filtro |
| $C$ | $4\ \mu\text{F}$ | capacitor de película estándar |
| $E$ | $300$ V (escalón, cierra en $t=0$) | bus de continua típico (≈ pico de la red de 220 V RMS) |

- Dinámica en **milisegundos** (transitorio muere en ≈ 1,3 ms), oscilación a ≈ 2,47 kHz.
- Amortiguamiento **débil** → el capacitor sobrepasa la fuente hasta ≈ **463 V** (~54 % por encima de 300 V): hallazgo de ingeniería central de la discusión (tensión nominal de los componentes).

**Resultado de control** (la derivación completa está en [[03 - Desarrollo analitico (teoria)]]):

$$V_o(t) = 300 - e^{-3000t}\Bigl(300\cos\omega_d t + \tfrac{900}{\sqrt{241}}\sin\omega_d t\Bigr)\ \text{V}, \qquad \omega_d = 1000\sqrt{241} \approx 15\,524\ \text{rad/s}$$

## Diferencias vs. la v1

| Aspecto | v1 (`Proyecto2/`) | **v2 (esta carpeta)** |
| ------- | ----------------- | --------------------- |
| Circuito | $L=1$ H, $R=6\ \Omega$, $C=0{,}04$ F, $E=100$ V (valores académicos) | $R=6\ \Omega$, $L=1$ mH, $C=4\ \mu$F, $E=300$ V (valores comerciales) |
| Variable de planteo | directamente $v_C$ | **carga $q$** (método de clase S14-3) + $V_o = q/C$ |
| Análisis | tabla de 2.º orden ($\zeta, M_p, t_p, t_s$) | vocabulario del curso: polos, transitorio amortiguado, régimen permanente |
| Escala temporal | segundos | milisegundos |
| Estado | archivo de referencia | **entregable del PROY** |

## Contenido de la carpeta

- [[03 - Desarrollo analitico (teoria)]] — derivación a mano, paso a paso (Dominio teórico, 3 pts).
- [[04 - Simulacion (Octave)]] — script `proyecto2v2_laplace.m`, figuras y error (Dominio de simulación, 3 pts).
- [[05 - Documento final]] — contenido completo del entregable PDF.
- [[06 - Guion del video]] — guion individual ≤ 5 min (Dominio del tema, 3 pts).
- `Prompt Word (formato).md` — maquetación Arial 12 / 1.5 / índice con el add-in de Word.

## Enlaces

- Consigna y rúbrica: [[../Consigna oficial - Proyecto Final (transcripcion)|transcripción oficial]] · [[S18-98 PROY Indicaciones]] · [[S18-99 PROY sem 18|fechas]].
- Método de clase: [[S14-1 Tema 01 - Transformadas de Laplace|S14-1 teoría]] · [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|S14-3 Ej 2]] · [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|S14-4 Ej 3]].
- Hub: [[../Trabajo Final - SyT MOC|Trabajo Final — MOC]].
