---
title: "Proyecto 1 — Simulación en Octave"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/octave
  - tema/simulacion
  - tema/error-cuadratico-medio
date: 2026-07-13
---

# Proyecto 1 — Simulación en Octave (Etapa S)

> [!info] Alcance
> Reconstrucción numérica de la señal con la serie de Fourier hallada en [[Proyecto1/03 - Desarrollo analitico (teoria)|la Etapa T]], usando **GNU Octave** (ver [[S16-5 Tema 02 - Programa Octave|S16-5]]). Cubre **Dominio de simulación (3 pts)** y aporta el **error simulado** para la discusión (criterio 5). El script y las figuras son reproducibles: ejecutan la misma matemática que el desarrollo teórico.

> [!warning] Capturas oficiales pendientes
> Las figuras de abajo se generaron con el script para tener el material listo. Para la entrega, **ejecutar `proyecto1_fourier.m` en Octave** y capturar además la pantalla del editor + la consola (`printf`), como pide la [[Proyecto1/02 - Plan de trabajo#Etapa S — Simulación en Octave|tarea S4]]. Instalar Octave desde [octave.org/download](https://octave.org/download) si aún no está.

## 1. Programa (script de Octave)

Archivo: [`proyecto1_fourier.m`](proyecto1_fourier.m). Define la señal, reconstruye $S_N(t)$ con los coeficientes **teóricos**, grafica y calcula el error. Núcleo del script:

```octave
% --- Parametros ---
A  = 12*sqrt(2);   T = 1/60;   w0 = 2*pi/T;     % A=16.97 V, 60 Hz

% --- Coeficientes teoricos (media onda) ---
a_coef = @(n) (n==0).*(2*A/pi) + (n>=2 & mod(n,2)==0).*(-2*A./(pi*(n.^2-1)));
b_coef = @(n) (n==1).*(A/2);

% --- Senal original y reconstruccion S_N ---
f_orig = @(t) A*sin(w0*t) .* (sin(w0*t) >= 0);      % media onda
function y = S_N(t, N, A, w0, a_coef, b_coef)
  y = (a_coef(0)/2) * ones(size(t));                % DC = A/pi
  for n = 1:N
    y = y + a_coef(n)*cos(n*w0*t) + b_coef(n)*sin(n*w0*t);
  end
end

% --- Error cuadratico medio ---
P = A^2/4;                                          % potencia media
Ek_teorico = P - (a_coef(0)/2)^2 - 0.5*sum(...);    % Parseval reducido
Ek_simulado = trapz(tp, (fp - S_N(tp,k,...)).^2)/T; % integracion numerica
```

> [!note] Detalles de implementación
> - La media onda se genera con la máscara `.*(sin(w0*t) >= 0)`: conserva el semiciclo positivo y anula el negativo (equivale a la definición por tramos).
> - `t = linspace(0, 2*T, 8000)` → paso $\approx T/4000$, suficientemente fino para que `trapz` sea preciso (ver [[Proyecto1/02 - Plan de trabajo#8. Riesgos y mitigaciones|riesgo de paso grueso]]).
> - El error teórico usa la **fórmula de Parseval reducida**; el simulado integra $\lbrack f-S_k\rbrack^2$ con `trapz`. Que ambos coincidan valida a la vez la teoría y el código.

## 2. Resultados gráficos

### Figura 1 — Señal original

Un rectificador de media onda deja pasar solo el semiciclo positivo del seno de 60 Hz.

![[fig1_senal.png]]

### Figura 2 — Aproximación $S_N(t)$ vs. señal original

Superposición para $N = 1, 2, 4, 10$ armónicos.

![[fig2_superposicion.png]]

> [!tip] Lectura de la Figura 2
> - **$N=1$**: solo DC + fundamental → una senoide desplazada que ni siquiera se anula en el semiciclo "apagado" (baja hasta valores negativos). Aproximación pobre.
> - **$N=2$**: al entrar el 2.º armónico la curva ya "aplana" el tramo cero y sigue la joroba. Salto de calidad enorme (el error cae de 9,5 % a 0,47 %).
> - **$N=4$** y **$N=10$**: prácticamente indistinguibles de $f(t)$. Sin sobreoscilaciones de [[S12-0 Tema 01 - Analisis de las series de Fourier#3. Fenómeno de Gibbs|Gibbs]] porque la señal es continua.

### Figura 3 — Error cuadrático medio $E_k$ vs. $k$

Escala semilogarítmica; se superponen el $E_k$ **teórico** (Parseval) y el **simulado** (`trapz`).

![[fig3_error.png]]

> [!note] La "escalera"
> Las mesetas (de $k=2$ a $3$, de $4$ a $5$, …) aparecen porque los armónicos **impares** $\ge 3$ tienen coeficiente **cero**: añadirlos no reduce el error. Cada peldaño hacia abajo corresponde a un armónico **par** nuevo. Las dos curvas (teórica y simulada) se solapan por completo.

## 3. Error simulado vs. teórico

Error cuadrático medio $E_k$ por los dos caminos, con su diferencia relativa:

| $k$ | $E_k$ teórico [V²] | $E_k$ simulado [V²] | Dif. relativa |
| --- | ------------------ | ------------------- | ------------- |
| 1 | $6{,}81950$ | $6{,}81950$ | $< 0{,}001\%$ |
| 2 | $0{,}334943$ | $0{,}334944$ | $< 0{,}001\%$ |
| 4 | $0{,}0755611$ | $0{,}0755617$ | $0{,}001\%$ |
| 6 | $0{,}0279195$ | $0{,}0279199$ | $0{,}002\%$ |
| 10 | $0{,}00726069$ | $0{,}00726096$ | $0{,}004\%$ |

> [!success] Validación cruzada
> La diferencia teórico–simulado es **menor al 0,01 %** en todos los casos (cumple el DoD del [[Proyecto1/02 - Plan de trabajo#5. Entregables y definición de terminado (DoD)|plan]], < 1 %). El pequeño residuo crece con $k$ porque los armónicos altos exigen más resolución temporal a `trapz`; con el paso elegido ($T/4000$) es despreciable. Esto **confirma que la serie analítica es correcta**: dos métodos independientes (integral simbólica de Parseval y cuadratura numérica) dan el mismo error.

## 4. Empaquetado de evidencia (para la entrega)

- [x] Script `proyecto1_fourier.m` en la carpeta del proyecto.
- [x] Figuras exportadas a `attachments/` (`fig1_senal.png`, `fig2_superposicion.png`, `fig3_error.png`).
- [ ] Captura de pantalla del **editor de Octave** con el código.
- [ ] Captura de la **consola** con la tabla de `printf` (valores de $E_k$).
- [ ] Código completo al **anexo** del documento final.

## Bibliografía

- Eaton, J. W., et al. (2024). *GNU Octave: A high-level interactive language for numerical computations*. https://octave.org
- Notas del curso: [[S16-5 Tema 02 - Programa Octave|Programa Octave]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|método del error cuadrático]].
