---
title: "Proyecto 1 — Desarrollo analítico (teoría)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/series-de-fourier
  - tema/seno-rectificado
  - tema/error-cuadratico-medio
date: 2026-07-13
---

# Proyecto 1 — Desarrollo analítico (Etapa T)

> [!info] Alcance
> Resolución **a mano, paso a paso** de la serie de Fourier del **seno rectificado de media onda**. Cubre el criterio **Dominio teórico (3 pts)** de la [[S18-98 PROY Indicaciones|rúbrica]]. Cada propiedad usada se respalda en [[S11-2 Tema 02 - Series de Fourier|S11-2]] y [[S12-0 Tema 01 - Analisis de las series de Fourier|S12-0]]. Los valores numéricos siguen el [[Proyecto1/02 - Plan de trabajo|plan]]: $A = 12\sqrt{2}\ \text{V}$, $T = 1/60\ \text{s}$.

## 1. Definición de la señal

Señal senoidal rectificada de **media onda** (un periodo):

$$f(t) = \begin{cases} A\sin(\omega_0 t), & 0 \le t < T/2 \\[4pt] 0, & T/2 \le t < T \end{cases} \qquad \omega_0 = \frac{2\pi}{T}$$

- $A = 12\sqrt{2} \approx 16{,}9706\ \text{V}$ = amplitud pico (secundario de 12 V RMS).
- $T = 1/60\ \text{s} \approx 16{,}667\ \text{ms}$ = periodo (red peruana a 60 Hz).
- $\omega_0 = 2\pi/T = 120\pi \approx 376{,}99\ \text{rad/s}$ = frecuencia angular fundamental.

> [!note] Paridad
> A diferencia del **seno rectificado de onda completa** $A\lvert\sin\omega_0 t\rvert$ resuelto en [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]] (que es **par** y solo tiene cosenos), la media onda **no es par ni impar**: al anularse en la mitad del periodo pierde toda simetría. Por eso hay que calcular $a_0$, **todos** los $a_n$ **y** los $b_n$. No se puede descartar ninguno por paridad.

Como $f(t)=0$ en $[T/2,\,T)$, todas las integrales se reducen al tramo $[0,\,T/2]$.

## 2. Término constante $a_0$

Con la fórmula de [[S11-2 Tema 02 - Series de Fourier#Término constante $a_0$|S11-2]] $a_0=\frac{2}{T}\int_0^T f(t)\,dt$:

$$a_0 = \frac{2}{T}\int_0^{T/2} A\sin(\omega_0 t)\,dt = \frac{2A}{T}\left[-\frac{\cos(\omega_0 t)}{\omega_0}\right]_0^{T/2}$$

En $t=T/2$: $\omega_0 t = \frac{2\pi}{T}\cdot\frac{T}{2}=\pi$, luego $\cos\pi=-1$ y $\cos 0=1$:

$$a_0 = \frac{2A}{T\,\omega_0}\bigl[-\cos\pi + \cos 0\bigr] = \frac{2A}{T\,\omega_0}(1+1) = \frac{4A}{T\,\omega_0}$$

Como $T\,\omega_0 = 2\pi$:

$$\boxed{\,a_0 = \frac{2A}{\pi}\,} \qquad\Rightarrow\qquad \text{DC} = \frac{a_0}{2} = \frac{A}{\pi} \approx 5{,}402\ \text{V}$$

El valor promedio $A/\pi$ es la componente continua que entregaría este rectificador a un condensador de filtro.

## 3. Coeficientes de cosenos $a_n$

$$a_n = \frac{2}{T}\int_0^{T/2} A\sin(\omega_0 t)\cos(n\omega_0 t)\,dt$$

Con la identidad producto→suma $\sin\alpha\cos\beta = \tfrac{1}{2}\bigl[\sin(\alpha+\beta)+\sin(\alpha-\beta)\bigr]$:

$$a_n = \frac{A}{T}\int_0^{T/2}\bigl[\sin\bigl((1+n)\omega_0 t\bigr) + \sin\bigl((1-n)\omega_0 t\bigr)\bigr]\,dt$$

Se usa el resultado auxiliar (para $m$ entero $\neq 0$):

$$\int_0^{T/2}\sin(m\omega_0 t)\,dt = \left[-\frac{\cos(m\omega_0 t)}{m\omega_0}\right]_0^{T/2} = \frac{1-\cos(m\pi)}{m\omega_0} = \frac{1-(-1)^m}{m\omega_0} = \begin{cases}0, & m\ \text{par} \\[3pt] \dfrac{2}{m\omega_0}, & m\ \text{impar}\end{cases}$$

> [!warning] El caso $n=1$ va aparte
> La fórmula general que se obtiene abajo divide entre $n^2-1$, que se anula en $n=1$. Hay que tratar $n=1$ con su propia integral.

**Caso $n=1$:** el segundo seno se vuelve $\sin(0)=0$, y $\sin(2\omega_0 t)$ tiene $m=2$ (par):

$$a_1 = \frac{A}{T}\int_0^{T/2}\sin(2\omega_0 t)\,dt = \frac{A}{T}\cdot 0 = 0 \qquad\Rightarrow\qquad \boxed{a_1 = 0}$$

**Caso $n\ge 2$:** los índices son $m=n+1$ y $m=1-n$.

- Si $n$ es **impar** ($n\ge 3$): $n+1$ es par y $1-n$ es par → ambas integrales valen $0$ → $a_n = 0$.
- Si $n$ es **par**: $n+1$ es impar y $1-n$ es impar → ambas sobreviven:

$$a_n = \frac{A}{T}\left[\frac{2}{(n+1)\omega_0} + \frac{2}{(1-n)\omega_0}\right] = \frac{2A}{T\omega_0}\cdot\frac{(1-n)+(n+1)}{(n+1)(1-n)} = \frac{2A}{T\omega_0}\cdot\frac{2}{1-n^2}$$

Con $T\omega_0=2\pi$:

$$\boxed{\,a_n = -\frac{2A}{\pi\,(n^2-1)}\quad (n\ \text{par}); \qquad a_n = 0\quad (n\ \text{impar})\,}$$

Valores numéricos ($A=16{,}9706$ V):

| $n$ | 2 | 4 | 6 | 8 | 10 |
| --- | - | - | - | - | -- |
| $a_n$ [V] | $-3{,}601$ | $-0{,}720$ | $-0{,}309$ | $-0{,}171$ | $-0{,}109$ |

## 4. Coeficientes de senos $b_n$

$$b_n = \frac{2}{T}\int_0^{T/2} A\sin(\omega_0 t)\sin(n\omega_0 t)\,dt$$

Con $\sin\alpha\sin\beta = \tfrac{1}{2}\bigl[\cos(\alpha-\beta)-\cos(\alpha+\beta)\bigr]$:

$$b_n = \frac{A}{T}\int_0^{T/2}\bigl[\cos\bigl((1-n)\omega_0 t\bigr) - \cos\bigl((1+n)\omega_0 t\bigr)\bigr]\,dt$$

**Caso $n=1$:** el primer coseno es $\cos 0 = 1$ y el segundo $\cos(2\omega_0 t)$:

$$b_1 = \frac{A}{T}\int_0^{T/2}\bigl[1 - \cos(2\omega_0 t)\bigr]\,dt = \frac{A}{T}\left[t - \frac{\sin(2\omega_0 t)}{2\omega_0}\right]_0^{T/2}$$

En $t=T/2$: $\sin(2\omega_0\cdot T/2)=\sin(2\pi)=0$, luego el corchete vale $T/2$:

$$b_1 = \frac{A}{T}\cdot\frac{T}{2} = \frac{A}{2} \qquad\Rightarrow\qquad \boxed{b_1 = \frac{A}{2} \approx 8{,}485\ \text{V}}$$

**Caso $n\ge 2$:** ahora $1-n\neq 0$ y $1+n\neq 0$ son enteros, y para entero $m\neq 0$:

$$\int_0^{T/2}\cos(m\omega_0 t)\,dt = \left[\frac{\sin(m\omega_0 t)}{m\omega_0}\right]_0^{T/2} = \frac{\sin(m\pi)}{m\omega_0} = 0$$

Por lo tanto ambos términos se anulan:

$$\boxed{\,b_n = 0 \quad (n\ge 2)\,}$$

Solo sobrevive la fundamental: la media onda conserva **media** senoide del seno de entrada, y ese "medio seno" aporta exactamente $A/2$ a la fundamental.

## 5. Serie de Fourier resultante

Reuniendo los términos no nulos (DC, la fundamental en seno, y los armónicos **pares** en coseno):

> [!success] Serie de Fourier — seno rectificado de media onda
> $$\boxed{\;f(t) = \frac{A}{\pi} + \frac{A}{2}\sin(\omega_0 t) - \frac{2A}{\pi}\sum_{k=1}^{\infty}\frac{\cos(2k\,\omega_0 t)}{4k^2 - 1}\;}$$
>
> Desarrollada: $\;f(t) = \dfrac{A}{\pi} + \dfrac{A}{2}\sin\omega_0 t - \dfrac{2A}{\pi}\!\left(\dfrac{\cos 2\omega_0 t}{3} + \dfrac{\cos 4\omega_0 t}{15} + \dfrac{\cos 6\omega_0 t}{35} + \cdots\right)$

donde se reindexaron los pares $n=2k$ (así $n^2-1 = 4k^2-1$ da los denominadores $3,15,35,\dots$). Esta expresión coincide con la referencia de control del [[Proyecto1/02 - Plan de trabajo#2. Definición concreta del caso|plan §2]], lo que valida el desarrollo.

> [!note] Lectura física de cada término
> - $A/\pi$ → **nivel DC** que ve la carga tras el rectificador.
> - $\tfrac{A}{2}\sin\omega_0 t$ → **rizado fundamental** a 60 Hz (el más grande y el que el filtro debe atenuar).
> - armónicos pares (120 Hz, 240 Hz, …) → rizado residual, decreciente como $1/(4k^2-1)$.

## 6. Error cuadrático medio teórico

Con la **fórmula reducida** de [[S12-0 Tema 01 - Analisis de las series de Fourier#Error y error cuadrático medio|S12-0]]:

$$E_k = \frac{1}{T}\int_0^{T}\!\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)$$

**Potencia media** (solo el primer semiperiodo aporta; $\int_0^{T/2}\sin^2\omega_0 t\,dt = T/4$):

$$\frac{1}{T}\int_0^{T} f^2\,dt = \frac{A^2}{T}\int_0^{T/2}\sin^2(\omega_0 t)\,dt = \frac{A^2}{T}\cdot\frac{T}{4} = \frac{A^2}{4} = 72{,}00\ \text{V}^2$$

**Potencia por término:** $\dfrac{a_0^2}{4} = \dfrac{A^2}{\pi^2}$; para $n=1$, $a_1^2+b_1^2 = (A/2)^2 = A^2/4$; para $n$ par, $a_n^2 = \dfrac{4A^2}{\pi^2(n^2-1)^2}$; el resto $0$.

Evaluando (con $A^2 = 288\ \text{V}^2$, $P = 72\ \text{V}^2$):

| $k$ | Términos incluidos | $E_k$ [V²] | $E_k/A^2$ | Potencia residual $E_k/P$ |
| --- | ------------------ | ---------- | --------- | ------------------------- |
| 1 | DC + fundamental | $6{,}8195$ | $2{,}37\times10^{-2}$ | $9{,}47\%$ |
| 2 | + armónico 2 | $0{,}33494$ | $1{,}16\times10^{-3}$ | $0{,}465\%$ |
| 4 | + armónico 4 | $0{,}075561$ | $2{,}62\times10^{-4}$ | $0{,}105\%$ |
| 6 | + armónico 6 | $0{,}027919$ | $9{,}69\times10^{-5}$ | $0{,}0388\%$ |
| 10 | + armónico 10 | $0{,}0072607$ | $2{,}52\times10^{-5}$ | $0{,}0101\%$ |

> [!tip] Interpretación
> - El salto grande es de $k=1$ a $k=2$: el **2.º armónico** ($a_2=-3{,}60$ V) es el término más energético después de la fundamental; omitirlo deja un 9,5 % de potencia sin representar.
> - $E_k$ **no cambia** al pasar de un armónico par al siguiente **impar** (p. ej. $k=2\to3$, $k=4\to5$), porque los impares $\ge 3$ aportan cero. Esto produce la "escalera" de la [[Proyecto1/04 - Simulacion (Octave)#Figura 3|Figura 3]].
> - Al ser una señal **continua** (sin discontinuidades), no hay [[S12-0 Tema 01 - Analisis de las series de Fourier#3. Fenómeno de Gibbs|fenómeno de Gibbs]] y el error decae rápido: con 10 armónicos ya solo queda el 0,01 % de la potencia. Es el mismo comportamiento del seno de onda completa de [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]].

Estos valores teóricos son la **referencia de control** contra la que se compara la [[Proyecto1/04 - Simulacion (Octave)|simulación en Octave]] (coincidencia < 0,01 %).

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano.
- Notas del curso: [[S11-2 Tema 02 - Series de Fourier|coeficientes de Fourier]], [[S12-0 Tema 01 - Analisis de las series de Fourier|error cuadrático medio]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|seno rectificado (onda completa)]].
