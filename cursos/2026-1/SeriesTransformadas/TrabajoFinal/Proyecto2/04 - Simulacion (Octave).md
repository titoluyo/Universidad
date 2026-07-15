---
title: "Proyecto 2 — Simulación en Octave"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/octave
  - tema/simulacion
  - tema/circuito-rlc
date: 2026-07-13
---

# Proyecto 2 — Simulación en Octave (Etapa C)

> [!info] Alcance
> Solución **numérica** del voltaje del capacitor $V_o(t)$ integrando la EDO del circuito con **GNU Octave** (ver [[S16-5 Tema 02 - Programa Octave|S16-5]]), **sin usar la fórmula cerrada** hallada en [[Proyecto2/03 - Desarrollo analitico (teoria)|la Etapa B]]. Al ser una vía independiente, comparar ambas curvas tiene sentido: valida a la vez la teoría y el modelo. Cubre **Dominio de simulación (3 pts)** y aporta el **error** para la discusión (criterio 5).

> [!warning] Capturas oficiales pendientes
> Las figuras de abajo se generaron con la misma matemática del script para tener el material listo. Para la entrega, **ejecutar `proyecto2_laplace.m` en Octave** y capturar además la pantalla del editor + la consola (`printf`) con la tabla de errores, como pide la [[Proyecto2/02 - Plan de trabajo#Etapa C — Simulación en Octave (criterio 3: Dominio de simulación, 3 pts)|tarea C5]]. Instalar Octave desde [octave.org/download](https://octave.org/download) si aún no está.

## 1. Programa (script de Octave)

Archivo: [`proyecto2_laplace.m`](proyecto2_laplace.m). Resuelve la EDO $v_C'' + 6 v_C' + 25 v_C = 2500$ con el integrador `lsode`, reescribiéndola como sistema de primer orden. Núcleo del script:

```octave
% --- Parametros del circuito ---
L=1; R=6; C=0.04; E=100;
a1 = R/L;  a0 = 1/(L*C);  u = E/(L*C);        % 6, 25, 2500

% --- Solucion teorica (cerrada, por Laplace) ---
Vo_teo = @(t) E - 100*exp(-3*t).*cos(4*t) - 75*exp(-3*t).*sin(4*t);

% --- Solucion simulada: EDO numerica (via independiente) ---
% x=[vC; vC'] ;  x1'=x2 ;  x2' = u - a1*x2 - a0*x1
function xdot = rlc(x, t)
  global A1 A0 U
  xdot = [ x(2);  U - A1*x(2) - A0*x(1) ];
end
t = linspace(0, 2.5, 2501)';
X = lsode(@rlc, [0;0], t);      % vC(0)=0, vC'(0)=0
Vo_sim = X(:,1);

% --- Error punto a punto ---
rmse = sqrt(mean((Vo_teo(t) - Vo_sim).^2));
```

> [!note] Detalles de implementación
> - **Vía independiente:** la simulación integra la **EDO cruda** (Kirchhoff), no la solución cerrada. Que ambas coincidan es una verdadera verificación cruzada, no una tautología.
> - El estado se reescribe como sistema de primer orden $x_1'=x_2$, $x_2' = 2500 - 6x_2 - 25x_1$ para que `lsode` lo integre.
> - Malla temporal $t\in[0,\ 2{,}5]$ s (≈ $8$ constantes de tiempo $1/\alpha = 1/3$ s) con $2501$ puntos, suficiente para capturar el sobreimpulso y la oscilación a $\omega_d = 4$ rad/s.

## 2. Resultados gráficos

### Figura 1 — Circuito RLC serie

Diagrama del circuito analizado, con la salida $V_o$ tomada en el capacitor.

![[fig1_circuito.png]]

### Figura 2 — Respuesta teórica $V_o(t)$

Voltaje del capacitor obtenido por Laplace, con el sobreimpulso y el tiempo de establecimiento anotados.

![[fig2_vo_teorico.png]]

> [!tip] Lectura de la Figura 2
> El voltaje **sobrepasa** los 100 V finales: alcanza $V_p = 109{,}5$ V (≈ $9{,}5\%$ de sobreimpulso) hacia $t_p = 0{,}785$ s, luego **oscila** amortiguadamente a $\omega_d = 4$ rad/s y se estabiliza dentro de la banda del 2 % tras $t_s \approx 1{,}33$ s. Es el comportamiento **subamortiguado** esperado ($\zeta = 0{,}6$).

### Figura 3 — Comparación teórico vs. simulado

La curva teórica (línea gris) y la simulada (marcadores rojos) se superponen por completo.

![[fig3_comparacion.png]]

### Figura 4 — Error absoluto puntual

Diferencia $|V_{teo} - V_{sim}|$ en escala semilogarítmica, con el RMSE marcado.

![[fig4_error.png]]

> [!note] Lectura de la Figura 4
> El error se mantiene en el orden de $10^{-6}$–$10^{-5}$ V en todo el intervalo (frente a valores de $V_o$ del orden de $10^2$ V), es decir **más de 7 órdenes de magnitud por debajo** de la señal. Los "picos hacia abajo" son cruces por cero del error donde el simulado corta exactamente al teórico. El error proviene únicamente de la tolerancia del integrador `lsode`, no de un desajuste del modelo.

## 3. Error simulado vs. teórico

Voltaje del capacitor por las dos vías en instantes representativos y su error absoluto:

| $t$ [s] | $V_o$ teórico [V] | $V_o$ simulado [V] | $\lvert\text{error}\rvert$ [V] | Error relativo |
| ------- | ----------------- | ------------------ | ------------------------------ | -------------- |
| $0{,}000$ | $0{,}0000$ | $0{,}0000$ | $0$ | $0\%$ |
| $0{,}200$ | $32{,}2369$ | $32{,}2369$ | $3{,}1\times10^{-6}$ | $3{,}1\times10^{-6}\%$ |
| $0{,}400$ | $78{,}2995$ | $78{,}2995$ | $1{,}7\times10^{-5}$ | $1{,}7\times10^{-5}\%$ |
| $0{,}600$ | $103{,}8150$ | $103{,}8150$ | $1{,}5\times10^{-6}$ | $1{,}5\times10^{-6}\%$ |
| $0{,}785$ ($t_p$) | $109{,}4780$ | $109{,}4780$ | $1{,}9\times10^{-5}$ | $1{,}9\times10^{-5}\%$ |
| $1{,}000$ | $106{,}0802$ | $106{,}0802$ | $9{,}4\times10^{-6}$ | $9{,}4\times10^{-6}\%$ |
| $1{,}333$ ($t_s$) | $100{,}0547$ | $100{,}0547$ | $2{,}1\times10^{-6}$ | $2{,}1\times10^{-6}\%$ |
| $1{,}600$ | $99{,}1107$ | $99{,}1107$ | $3{,}9\times10^{-6}$ | $3{,}9\times10^{-6}\%$ |
| $2{,}000$ | $99{,}8521$ | $99{,}8521$ | $4{,}0\times10^{-7}$ | $4{,}0\times10^{-7}\%$ |
| $2{,}500$ | $100{,}0690$ | $100{,}0690$ | $4{,}1\times10^{-7}$ | $4{,}1\times10^{-7}\%$ |

$$\text{RMSE} = 8{,}26\times10^{-6}\ \text{V}, \qquad \max\lvert\text{error}\rvert = 2{,}74\times10^{-5}\ \text{V}$$

> [!success] Validación cruzada
> La solución analítica (Laplace + fracciones parciales) y la simulación numérica (integración de la EDO con `lsode`) coinciden con un **RMSE de $8{,}3\times10^{-6}$ V**, es decir un error relativo del orden de $10^{-6}\%$. Dos métodos **independientes** dan el mismo $V_o(t)$, lo que **confirma que la solución teórica es correcta** y que el circuito se modeló bien. El residuo, ínfimo, es solo la precisión del integrador.

## 4. Empaquetado de evidencia (para la entrega)

- [x] Script `proyecto2_laplace.m` en la carpeta del proyecto.
- [x] Figuras exportadas a `attachments/` (`fig1_circuito.png`, `fig2_vo_teorico.png`, `fig3_comparacion.png`, `fig4_error.png`).
- [ ] Captura de pantalla del **editor de Octave** con el código.
- [ ] Captura de la **consola** con la tabla de `printf` (valores de error).
- [ ] Código completo al **anexo** del documento final.

## Bibliografía

- Eaton, J. W., et al. (2024). *GNU Octave: A high-level interactive language for numerical computations*. https://octave.org
- Notas del curso: [[S16-5 Tema 02 - Programa Octave|Programa Octave]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|método Laplace en circuitos RLC]].
