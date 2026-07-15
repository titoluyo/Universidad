---
title: "PA04 — Enunciados y desarrollo de los 5 ejercicios"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 98
tipo: evaluacion
subtipo: pa
tags:
  - curso/series-transformadas
  - tipo/evaluacion
  - subtipo/pa
  - tema/series-de-taylor
  - tema/series-de-maclaurin
  - tema/series-de-laurent
date: 2026-05-31
---

Desarrollo de la **Participación Académica 4 (PA04)**. Metadatos y consigna en [[S10-99 PA04 sem 10]]. Enunciados tomados de [[PA4-Enunciados-ESTUDIANTE.pdf|PA-4 -ESTUDIANTE.pdf]] (capturado al iniciar el intento el 31 may 2026).

> [!info] Material de apoyo
> Teoría base de la semana: [[S10-0 Tema 01 - Series de Maclaurin y Laurent|Maclaurin y Laurent]] · [[S09-0 Tema 01 - Series de Taylor en numeros complejos|Taylor]] · [[S08-0 Tema 01 - Series de potencias en complejos|Series de potencias]] · [[Formulario - Series y Transformadas|Formulario]].

---

## Pregunta 1 — Taylor de $f(x)=\dfrac{e^{x}}{1-x}$ en $x_0=0$

### a) Puntos de singularidad

$e^{x}$ es **entera** (analítica en todo el plano). La única singularidad proviene del denominador:

$$1 - x = 0 \;\Rightarrow\; x = 1 \quad(\text{polo simple})$$

### b) Serie de Taylor (Maclaurin) centrada en $0$

En lugar de derivar el cociente, se **multiplican dos series de Maclaurin conocidas** ([[S09-0 Tema 01 - Series de Taylor en numeros complejos#Series de Maclaurin notables|series notables]]):

$$e^{x} = \sum_{k=0}^{\infty}\frac{x^{k}}{k!} = 1 + x + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \cdots$$
$$\frac{1}{1-x} = \sum_{j=0}^{\infty}x^{j} = 1 + x + x^{2} + x^{3} + \cdots \qquad (|x|<1)$$

El **producto de Cauchy** da el coeficiente de $x^{n}$ sumando todos los pares $k+j=n$. Como los coeficientes de $\frac{1}{1-x}$ valen $1$:

$$c_{n} = \sum_{k=0}^{n}\frac{1}{k!}\cdot 1 = \sum_{k=0}^{n}\frac{1}{k!}$$

Es decir, cada coeficiente es la **suma parcial de $e$**:

| $n$ | $c_n=\sum_{k=0}^n \frac{1}{k!}$ | Valor |
| --- | ------------------------------- | ----- |
| $0$ | $1$ | $1$ |
| $1$ | $1+1$ | $2$ |
| $2$ | $1+1+\tfrac12$ | $\tfrac{5}{2}$ |
| $3$ | $1+1+\tfrac12+\tfrac16$ | $\tfrac{8}{3}$ |
| $4$ | $1+1+\tfrac12+\tfrac16+\tfrac1{24}$ | $\tfrac{65}{24}$ |

$$f(x) = 1 + 2x + \frac{5}{2}x^{2} + \frac{8}{3}x^{3} + \frac{65}{24}x^{4} + \cdots$$

> [!success] Forma general
> $$\boxed{\;\dfrac{e^{x}}{1-x} = \sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}\frac{1}{k!}\right)x^{n}\;}\qquad |x|<1$$

**Radio de convergencia:** $R=1$, la distancia de $x_0=0$ al polo en $x=1$ ($e^x$ no aporta singularidades). Referencia del método (producto de series / radio por singularidad más cercana): [[S08-0 Tema 01 - Series de potencias en complejos|series de potencias]], [[S09-0 Tema 01 - Series de Taylor en numeros complejos|Taylor]].

---

## Pregunta 2 — Laurent de $f(z)=\dfrac{e^{1/z}}{z-1}$ en la corona $0<|z|<1$

### a) Puntos singulares y clasificación

- $z=0$: el factor $e^{1/z}$ tiene una **singularidad esencial** (su serie alrededor de $0$ tiene infinitos términos en potencias negativas). Por tanto $f$ tiene una **singularidad esencial en $z=0$**.
- $z=1$: el factor $\frac{1}{z-1}$ aporta un **polo simple** en $z=1$.

La "corona punteada alrededor de cero" es el anillo entre ambas singularidades: $0<|z|<1$.

### b) Expansión de Laurent en $0<|z|<1$

Se usan las dos series por separado y se multiplican (teoría de Laurent: [[S10-0 Tema 01 - Series de Maclaurin y Laurent#2. Serie de Laurent|anillo]]).

$$e^{1/z} = \sum_{m=0}^{\infty}\frac{1}{m!}\,z^{-m} = 1 + \frac{1}{z} + \frac{1}{2z^{2}} + \frac{1}{6z^{3}} + \cdots \qquad (z\neq 0)$$
$$\frac{1}{z-1} = -\frac{1}{1-z} = -\sum_{j=0}^{\infty}z^{j} = -\bigl(1 + z + z^{2} + \cdots\bigr) \qquad (|z|<1)$$

Multiplicando:

$$f(z) = -\left(\sum_{m=0}^{\infty}\frac{z^{-m}}{m!}\right)\left(\sum_{j=0}^{\infty}z^{j}\right)$$

El coeficiente $c_n$ de $z^{n}$ reúne los pares con $j-m=n$ (es decir $j=n+m$, con $m\ge 0$, $j\ge 0$):

> [!success] Forma general de los coeficientes
> $$f(z)=\sum_{n=-\infty}^{\infty}c_n\,z^{n}, \qquad
> c_{n} = \begin{cases}
> -\displaystyle\sum_{m=0}^{\infty}\dfrac{1}{m!} = -e, & n\ge 0,\\[3mm]
> -\displaystyle\sum_{m=-n}^{\infty}\dfrac{1}{m!}, & n<0.
> \end{cases}$$

Primeros términos (parte principal + analítica):

$$f(z) = \cdots -(e-2)\frac{1}{z^{2}} -(e-1)\frac{1}{z} \; - e\bigl(1 + z + z^{2} + \cdots\bigr)$$

- Coef. de $z^{0}$, $z^{1}$, …: todos $-e$ (porque $\sum_{m\ge0}\frac1{m!}=e$).
- Coef. de $z^{-1}$: $-\sum_{m\ge1}\frac1{m!} = -(e-1)$.
- Coef. de $z^{-2}$: $-\sum_{m\ge2}\frac1{m!} = -(e-2)$.

> [!note] Residuo en $z=0$
> El coeficiente $c_{-1}=-(e-1)=1-e$ es el **residuo** de $f$ en la singularidad esencial. (Aquí no se pide integral, pero conecta con [[S10-0 Tema 01 - Series de Maclaurin y Laurent#3. Conexión con integrales de contorno|el método de integración por Laurent]].)

---

## Pregunta 3 — Laurent de $f(z)=\dfrac{1}{z(z-2)}$ en $0<|z-2|<2$

### a) Puntos de singularidad

$$z=0 \quad\text{y}\quad z=2 \qquad(\text{ambos polos simples})$$

El anillo pedido $0<|z-2|<2$ rodea la singularidad $z_0=2$ y llega hasta la otra singularidad $z=0$ (que está a distancia $2$).

### b) Expansión (mismo método que [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)|Ej 2 de la semana]])

Sustitución $w=z-2$ (es decir $z=w+2$), con $0<|w|<2$:

$$f = \frac{1}{(w+2)\,w} = \frac{1}{w}\cdot\frac{1}{w+2} = \frac{1}{w}\cdot\frac{1}{2}\cdot\frac{1}{1+\frac{w}{2}}$$

Como $|w|<2 \Rightarrow \left|\frac{w}{2}\right|<1$, se expande la serie geométrica:

$$\frac{1}{1+\frac{w}{2}} = \sum_{n=0}^{\infty}(-1)^{n}\frac{w^{n}}{2^{n}}$$

$$f = \frac{1}{2w}\sum_{n=0}^{\infty}(-1)^{n}\frac{w^{n}}{2^{n}} = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2^{n+1}}\,w^{\,n-1}$$

Volviendo a $w=z-2$:

> [!success] Serie de Laurent en $0<|z-2|<2$
> $$f(z) = \frac{1}{2(z-2)} - \frac{1}{4} + \frac{1}{8}(z-2) - \frac{1}{16}(z-2)^{2} + \cdots$$
> $$\boxed{\;f(z) = \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2^{\,n+1}}\,(z-2)^{\,n-1}\;}$$

**Parte principal:** solo el término $\dfrac{1}{2(z-2)}$ (polo simple). **Residuo en $z=2$:** $c_{-1}=\tfrac12$.

**Verificación por fracciones parciales:** $\dfrac{1}{z(z-2)}=\dfrac{1}{2}\!\left(\dfrac{1}{z-2}-\dfrac{1}{z}\right)$; el término $\dfrac{1/2}{z-2}$ es la parte principal y $-\dfrac{1/2}{z}=-\dfrac14+\dfrac18 w-\cdots$ coincide con la parte analítica. ✓

---

## Pregunta 4 — Taylor de $f(x)=\dfrac{1}{(1-x)^{2}}$ en $x_0=0$

### a) Puntos singulares y clasificación

$$1-x=0 \;\Rightarrow\; x=1 \qquad(\text{polo de orden 2, por el exponente al cuadrado})$$

### b) Serie de Taylor centrada en $0$

Se deriva la serie geométrica $\dfrac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}$ (válida $|x|<1$):

$$\frac{d}{dx}\!\left(\frac{1}{1-x}\right) = \frac{1}{(1-x)^{2}}, \qquad \frac{d}{dx}\sum_{n=0}^{\infty}x^{n} = \sum_{n=1}^{\infty}n\,x^{n-1}$$

Reindexando ($m=n-1$):

$$f(x) = 1 + 2x + 3x^{2} + 4x^{3} + 5x^{4} + \cdots$$

> [!success] Forma general
> $$\boxed{\;\frac{1}{(1-x)^{2}} = \sum_{n=0}^{\infty}(n+1)\,x^{n}\;}\qquad |x|<1$$

**Radio de convergencia:** $R=1$ (distancia de $0$ al polo en $x=1$). Esta serie figura en el [[Formulario - Series y Transformadas#Serie geométrica (radio de convergencia $1$)|Formulario]] ($\sum n z^{n-1}=\frac{1}{(1-z)^2}$).

---

## Pregunta 5 — Maclaurin de $f(x)=\dfrac{\ln(1+x)}{n}$

**Asumiendo que $n$ es una constante distinta de cero** (se usa $k$ como índice de la serie para no confundirlo con $n$). Misma serie base que [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)|S09-1]].

### a) Punto singular

$$f(x)=\frac{\ln(1+x)}{n}$$

La función $\ln(1+x)$ deja de ser analítica cuando:

$$1+x=0 \;\Rightarrow\; x=-1$$

Por tanto, el punto singular es $x=-1$. Se clasifica como **singularidad logarítmica** (punto de ramificación); no es polo ni removible.

### b) Serie de Maclaurin

Sabemos que:

$$\ln(1+x)=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}\,x^{k}=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}+\cdots$$

Entonces:

$$f(x)=\frac{1}{n}\ln(1+x)=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{n\,k}\,x^{k}=\frac{x}{n}-\frac{x^{2}}{2n}+\frac{x^{3}}{3n}-\frac{x^{4}}{4n}+\cdots$$

Por tanto, los coeficientes son:

$$a_k=\frac{(-1)^{k+1}}{n\,k},\quad k\ge 1 \qquad\text{y}\qquad a_0=0$$

### c) Primeros cuatro términos y radio

Los primeros cuatro términos son:

$$f(x)=\frac{x}{n}-\frac{x^{2}}{2n}+\frac{x^{3}}{3n}-\frac{x^{4}}{4n}+\cdots$$

El radio de convergencia es:

$$R=1$$

porque la singularidad más cercana al centro $x=0$ está en $x=-1$, y la distancia es:

$$|-1-0|=1$$

(La constante $n$ se cancela en el criterio del cociente, así que no afecta el radio. Ver [[S08-0 Tema 01 - Series de potencias en complejos|criterio del cociente]].)

---

## Resumen de respuestas

| Preg. | Función | Singularidades | Serie | $R$ |
| ----- | ------- | -------------- | ----- | --- |
| 1 | $\frac{e^x}{1-x}$ | polo simple $x=1$ | $\sum_{n\ge0}\bigl(\sum_{k=0}^n \tfrac1{k!}\bigr)x^n$ | $1$ |
| 2 | $\frac{e^{1/z}}{z-1}$ | esencial $z=0$, polo $z=1$ | $c_n=-e\ (n\ge0)$, $c_{n}=-\!\sum_{m\ge -n}\tfrac1{m!}\ (n<0)$ | corona $0<\|z\|<1$ |
| 3 | $\frac{1}{z(z-2)}$ | polos $z=0,\,z=2$ | $\sum_{n\ge0}\frac{(-1)^n}{2^{n+1}}(z-2)^{n-1}$ | anillo $0<\|z-2\|<2$ |
| 4 | $\frac{1}{(1-x)^2}$ | polo doble $x=1$ | $\sum_{n\ge0}(n+1)x^n$ | $1$ |
| 5 | $\frac{\ln(1+x)}{n}$ | ramificación $x=-1$ | $\sum_{k\ge1}\frac{(-1)^{k+1}}{n\,k}x^k$ | $1$ |

> [!tip] Para subir a la plataforma
> La evaluación pide **un PDF** con el desarrollo (manuscrito o digital). Esta nota se puede exportar con `utils/md_to_docx.py` → PDF, o copiar el desarrollo al editor de la pregunta. El intento ya está iniciado; falta **Finalizar evaluación** tras adjuntar el PDF.
