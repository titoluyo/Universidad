---
title: "Proyecto 2 v2 — Simulación en Octave"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/transformada-de-laplace
  - tema/circuito-rlc
  - tema/octave
date: 2026-07-16
---

# Proyecto 2 v2 — Simulación en Octave

> [!info] Alcance
> Solución **numérica e independiente** del circuito: el script **no usa la fórmula cerrada** de [[03 - Desarrollo analitico (teoria)|la teoría]] — reescribe la EDO como sistema de primer orden y la integra con `lsode`. Así la comparación teórico vs. simulado es una **validación cruzada legítima**. Cubre el criterio **Dominio de simulación (3 pts)** de la [[S18-98 PROY Indicaciones|rúbrica]]. Ejecutado en **GNU Octave 11.3.0** el 16 jul 2026.

## 1. Programa (script de Octave)

Script completo: [`proyecto2v2_laplace.m`](proyecto2v2_laplace.m). Resuelve la EDO del circuito $q'' + 6000\,q' + 2{,}5\times10^{8}\,q = 3\times10^{5}$ (CI nulas) y obtiene $V_o = q/C$. Núcleo:

```octave
% Parametros del circuito
R = 6; L = 1e-3; C = 4e-6; E = 300;
a1 = R/L;  a0 = 1/(L*C);  u = E/L;      % 6000, 2.5e8, 3e5
alpha = a1/2;  wd = sqrt(a0 - alpha^2); % 3000, 1000*sqrt(241)

% Solucion teorica cerrada (por Laplace) — solo como referencia de comparacion
Vo_teo = @(t) E - exp(-alpha*t).*(300*cos(wd*t) + (900/sqrt(241))*sin(wd*t));

% Simulacion: integracion numerica de la EDO (via independiente)
% Estado x = [q; q'] ;  x1' = x2 ;  x2' = u - a1*x2 - a0*x1
f_rlc = @(x, t) [ x(2); u - a1*x(2) - a0*x(1) ];
t = linspace(0, 2e-3, 4001)';           % 0 a 2 ms, paso 0.5 us
X = lsode(f_rlc, [0; 0], t);            % CI: q(0)=0, q'(0)=0
Vo_sim = X(:,1) / C;                    % voltaje del capacitor simulado
```

> [!note] Detalles de implementación
> - La EDO de 2.º orden se reescribe como **sistema de primer orden** en el estado $x = [q,\ q']^\top$, requisito de `lsode`.
> - Malla temporal $t \in [0,\ 2\ \text{ms}]$ con **4001 puntos** ($\Delta t = 0{,}5\ \mu$s): unas 6 constantes de tiempo ($1/\alpha \approx 0{,}33$ ms) y ~31 puntos por período de oscilación ($2\pi/\omega_d \approx 0{,}40$ ms), resolución sobrada para capturar el pico.
> - `Vo_teo` se evalúa **solo para comparar**: la trayectoria simulada sale íntegramente del integrador.

## 2. Resultados gráficos

### Figura 1 — Circuito R–L–C serie

![[fig1_circuito.png]]

Circuito serie en orden **R–L–C** ($R=6\ \Omega$, $L=1$ mH, $C=4\ \mu$F) con fuente escalón de $300$ V y salida $V_o$ en el capacitor.

### Figura 2 — Respuesta teórica $V_o(t)$

![[fig2_vo_teorico.png]]

> [!tip] Lectura
> El voltaje del capacitor **sobrepasa la fuente**: pico de $463{,}5$ V ($54{,}5\ \%$ por encima de los 300 V) en $t_p \approx 0{,}202$ ms, oscila a $f_d \approx 2{,}47$ kHz y se estabiliza en $E = 300$ V en ≈ 1,3 ms.

### Figura 3 — Comparación teórico vs. simulado

![[fig3_comparacion.png]]

Los marcadores del simulador se superponen exactamente sobre la curva teórica en todo el intervalo.

### Figura 4 — Error absoluto puntual

![[fig4_error.png]]

El error puntual se mantiene por debajo de $10^{-4}$ V en todo el intervalo (frente a señales de cientos de voltios).

## 3. Error simulado vs. teórico

Salida del script (integración `lsode` vs. fórmula cerrada de Laplace):

| $t$ [ms] | $V_o$ teórico [V] | $V_o$ simulado [V] | $\lvert\text{error}\rvert$ [V] | Error rel. [%] |
| -------- | ----------------- | ------------------ | ------------------------------ | -------------- |
| $0{,}1000$ | $252{,}9746$ | $252{,}9746$ | $1{,}71\times10^{-5}$ | $0{,}000006$ |
| $0{,}2025$ ($t_p$) | $463{,}4778$ | $463{,}4777$ | $5{,}86\times10^{-5}$ | $0{,}000020$ |
| $0{,}3000$ | $330{,}2563$ | $330{,}2563$ | $2{,}12\times10^{-7}$ | $0{,}000000$ |
| $0{,}5000$ | $280{,}9761$ | $280{,}9761$ | $1{,}97\times10^{-5}$ | $0{,}000007$ |
| $0{,}8000$ | $273{,}8488$ | $273{,}8488$ | $6{,}85\times10^{-5}$ | $0{,}000023$ |
| $1{,}0000$ | $314{,}1571$ | $314{,}1570$ | $5{,}02\times10^{-5}$ | $0{,}000017$ |
| $1{,}3100$ ($\approx t_s$) | $298{,}3726$ | $298{,}3726$ | $1{,}26\times10^{-5}$ | $0{,}000004$ |
| $2{,}0000$ | $299{,}3577$ | $299{,}3577$ | $1{,}45\times10^{-5}$ | $0{,}000005$ |

$$\text{RMSE} = 3{,}79\times10^{-5}\ \text{V} \qquad\qquad \max\lvert\text{error}\rvert = 9{,}19\times10^{-5}\ \text{V}$$

> [!success] Validación cruzada
> La diferencia relativa es **menor a $10^{-4}\ \%$** en todos los instantes evaluados. Dos vías independientes —la antitransformada simbólica de Laplace y la integración numérica de la EDO— producen la misma respuesta, lo que valida a la vez la solución teórica de [[03 - Desarrollo analitico (teoria)|la Etapa T]] y la implementación del simulador.

## 4. Empaquetado de evidencia (para la entrega)

- [x] Script `proyecto2v2_laplace.m` en la carpeta del proyecto.
- [x] Figuras exportadas a `attachments/` (`-r130`).
- [x] Tabla de error y RMSE (salida de consola registrada arriba).
- [ ] Capturas del editor de Octave + consola con el script corriendo (para el documento/video).
- [x] Código completo anexado al [[05 - Documento final|documento]] (Anexo A).

## Bibliografía

- Eaton, J. W., Bateman, D., Hauberg, S., & Wehbring, R. (2024). *GNU Octave: A high-level interactive language for numerical computations*. https://octave.org/doc/
- Notas del curso: [[S16-5 Tema 02 - Programa Octave|instalación y uso de Octave]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC de clase]].
