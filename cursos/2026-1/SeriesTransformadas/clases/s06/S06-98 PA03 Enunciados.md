---
title: "PA03 - Enunciados y desarrollo de los 5 ejercicios"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 98
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/integral-de-contorno
  - tema/funcion-logaritmica
  - tema/teorema-de-cauchy
  - tema/integral-de-riemann
  - tema/derivada
date: 2026-05-03
---

> [!info] Sobre esta evaluacion
> **Participacion en Clase 3 (PA03)** — Series y Transformadas. Trabajo individual, entrega en PDF (o imagenes si no es posible) por UTP+CLASS antes del domingo 3 de mayo 11:59 PM. Metadatos completos en [[S06-99 PA03 sem 06]]. Consigna oficial: [[PA03-Enunciados.pdf]].
>
> Mezcla 4 preguntas de **fundamentos reales** (integrales de linea reales, logaritmos reales, sumas de Riemann, derivadas) y **1 pregunta compleja** (Pregunta 3) sobre el tema central de la semana.

## Pregunta 1 — Integral de linea real sobre arco circular

### Enunciado

Evaluar la integral de linea:

$$I = \int_{C}(x^2 - y)\,dx + (2xy)\,dy$$

donde $C$ es el arco de la circunferencia $x^2 + y^2 = 9$ que va de $(3, 0)$ a $(0, 3)$ en sentido **antihorario**.

a) Determina el rango de $t$.
b) Aplica la parametrizacion $x(t)$, $y(t)$.
c) Resuelve la integral.

### Referencia teorica

Ver [[S06-1 Tema 06 - Integral de contorno en funciones complejas|integral de contorno (parametrizacion)]] — la idea es analoga al caso complejo pero en el plano $xy$ real. Una integral de linea de la forma $\int P\,dx + Q\,dy$ se evalua parametrizando la curva $C$ por $t$ y reduciendola a una integral simple en $t$.

### a) Rango de $t$

La circunferencia $x^2 + y^2 = 9$ tiene radio $r = 3$. Parametrizacion estandar antihoraria:

$$x(t) = 3\cos t, \qquad y(t) = 3\,\text{sen}\,t$$

- En $t = 0$: $(x, y) = (3, 0)$ ✓ (punto inicial)
- En $t = \pi/2$: $(x, y) = (0, 3)$ ✓ (punto final)
- $t$ creciente → sentido antihorario ✓

$$\boxed{t \in \left[0, \tfrac{\pi}{2}\right]}$$

### b) Parametrizacion

$$x(t) = 3\cos t \implies dx = -3\,\text{sen}\,t\,dt$$

$$y(t) = 3\,\text{sen}\,t \implies dy = 3\cos t\,dt$$

### c) Sustituir y resolver

Sustituimos en cada termino:

$$x^2 - y = 9\cos^2 t - 3\,\text{sen}\,t$$

$$(x^2 - y)\,dx = (9\cos^2 t - 3\,\text{sen}\,t)(-3\,\text{sen}\,t)\,dt = (-27\,\text{sen}\,t\cos^2 t + 9\,\text{sen}^2 t)\,dt$$

$$2xy = 2(3\cos t)(3\,\text{sen}\,t) = 18\,\text{sen}\,t\cos t$$

$$(2xy)\,dy = 18\,\text{sen}\,t\cos t \cdot 3\cos t\,dt = 54\,\text{sen}\,t\cos^2 t\,dt$$

Sumando:

$$I = \int_{0}^{\pi/2}\bigl[(-27 + 54)\,\text{sen}\,t\cos^2 t + 9\,\text{sen}^2 t\bigr]\,dt = \int_{0}^{\pi/2}\bigl[27\,\text{sen}\,t\cos^2 t + 9\,\text{sen}^2 t\bigr]\,dt$$

**Primera integral** (cambio $u = \cos t$, $du = -\text{sen}\,t\,dt$):

$$\int_{0}^{\pi/2} 27\,\text{sen}\,t\cos^2 t\,dt = 27\int_{1}^{0} u^2(-du) = 27\int_{0}^{1} u^2\,du = 27 \cdot \tfrac{1}{3} = 9$$

**Segunda integral** (identidad $\text{sen}^2 t = (1 - \cos 2t)/2$):

$$\int_{0}^{\pi/2} 9\,\text{sen}^2 t\,dt = 9 \cdot \tfrac{1}{2}\left[t - \tfrac{\text{sen}\,2t}{2}\right]_0^{\pi/2} = \tfrac{9}{2}\left[\tfrac{\pi}{2} - 0\right] = \tfrac{9\pi}{4}$$

### Resultado

$$\boxed{I = 9 + \frac{9\pi}{4}}$$

---

## Pregunta 2 — Funcion logaritmica real $\log_5(2x+3)$

### Enunciado

Sea $f(x) = \log_5(2x + 3)$.

a) Explica la definicion de logaritmo y las condiciones sobre la base y el argumento.
b) Determina el dominio y rango de la funcion.
c) Evalua $f(11)$ y $f(2)$ aplicando la definicion.
d) Resuelve la ecuacion $\log_5(2x + 3) = 3$.

### Referencia teorica

Aunque la pregunta usa logaritmo real, el concepto se extiende al [[S05-1 Tema 05 - Funciones complejas elementales#2. Funcion logaritmica|logaritmo complejo]] (semana 5) que es multivaluado.

### a) Definicion de logaritmo

$$\log_b(a) = c \iff b^c = a$$

**Condiciones:**

| Condicion | Razon |
| --------- | ----- |
| $b > 0$   | Para que $b^c$ este definido sin ambiguedad para todo $c \in \mathbb{R}$ |
| $b \neq 1$ | Si $b = 1$, $b^c = 1$ siempre, no se puede invertir |
| $a > 0$   | Porque $b^c > 0$ siempre que $b > 0$, asi que el rango de $b^c$ son los reales positivos |

En esta pregunta: $b = 5$ (cumple $b > 0$ y $b \neq 1$), $a = 2x + 3$ (debe satisfacer $a > 0$).

### b) Dominio y rango

**Dominio:** se requiere $2x + 3 > 0$:

$$2x + 3 > 0 \implies x > -\tfrac{3}{2}$$

$$\boxed{\text{Dom}(f) = \left(-\tfrac{3}{2},\ +\infty\right)}$$

**Rango:** la funcion logaritmo es **biyectiva** de $(0, \infty) \to \mathbb{R}$. Como $2x + 3$ toma todos los valores de $(0, \infty)$ cuando $x \in (-3/2, \infty)$:

$$\boxed{\text{Rango}(f) = \mathbb{R} = (-\infty,\ +\infty)}$$

### c) Evaluar $f(11)$ y $f(2)$

**$f(11)$:**

$$f(11) = \log_5(2 \cdot 11 + 3) = \log_5(25) = \log_5(5^2)$$

Por la definicion ($\log_5 5^c = c$):

$$\boxed{f(11) = 2}$$

**$f(2)$:**

$$f(2) = \log_5(2 \cdot 2 + 3) = \log_5(7)$$

Como $7$ no es potencia entera de $5$, aplicamos cambio de base:

$$\log_5(7) = \frac{\ln 7}{\ln 5} = \frac{\log 7}{\log 5}$$

Numericamente:

$$\boxed{f(2) = \log_5(7) = \frac{\ln 7}{\ln 5} \approx 1{,}209}$$

### d) Resolver $\log_5(2x + 3) = 3$

Aplicar definicion (convertir a forma exponencial):

$$\log_5(2x + 3) = 3 \iff 2x + 3 = 5^3 = 125$$

Despejando:

$$2x = 122 \implies x = 61$$

**Verificacion:** $x = 61 > -3/2$ ✓ (esta en el dominio). Y $f(61) = \log_5(2 \cdot 61 + 3) = \log_5(125) = \log_5(5^3) = 3$ ✓.

$$\boxed{x = 61}$$

---

## Pregunta 3 — Integral compleja $\oint_{|z|=2} z\,dz$

### Enunciado

Sea $C$ la circunferencia orientada **antihoraria** $|z| = 2$. Calcular:

$$I = \oint_{C} z\,dz$$

a) Representa $z$ en forma exponencial.
b) Indica el rango de $t$.
c) Aplica la definicion de la integral compleja.

### Referencia teorica

Ver [[S06-1 Tema 06 - Integral de contorno en funciones complejas|integral de contorno por forma exponencial (Metodo B)]] y [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]]. Como $f(z) = z$ es **entera** (analitica en todo $\mathbb{C}$), por el Teorema de Cauchy se espera $I = 0$. Lo verificaremos por calculo directo.

### a) Forma exponencial de $z$

Sobre $|z| = 2$ con parametro $t$:

$$z(t) = 2\,e^{it}$$

### b) Rango de $t$

Vuelta completa antihoraria:

$$\boxed{t \in [0, 2\pi]}$$

### c) Aplicar definicion

Calculamos $dz$:

$$dz = 2i\,e^{it}\,dt$$

Producto $z\,dz$:

$$z\,dz = (2\,e^{it})(2i\,e^{it})\,dt = 4i\,e^{2it}\,dt$$

La integral:

$$I = \int_{0}^{2\pi} 4i\,e^{2it}\,dt$$

Resolviendo (antiderivada $\int e^{2it}\,dt = \dfrac{e^{2it}}{2i}$):

$$I = 4i \cdot \left[\frac{e^{2it}}{2i}\right]_{0}^{2\pi} = 2\,\bigl[e^{2it}\bigr]_{0}^{2\pi} = 2\,\bigl[e^{4\pi i} - e^{0}\bigr]$$

Como $e^{4\pi i} = \cos(4\pi) + i\,\text{sen}(4\pi) = 1 + 0 = 1$ y $e^0 = 1$:

$$I = 2\,[1 - 1] = 0$$

### Resultado

$$\boxed{\oint_{|z|=2} z\,dz = 0}$$

> [!success] Consistencia con el Teorema de Cauchy
> Como $f(z) = z$ es entera (sin singularidades), por [[S06-3 Tema 06 - Teorema de Cauchy|Cauchy]] se cumple $\oint_C z\,dz = 0$ para **cualquier** contorno cerrado simple — en particular para $|z| = 2$. Mismo resultado obtenido en [[S06-4 Tema 06 - Cauchy Ejercicio 1 - contorno triangular|Ej1]] (contorno triangular) y [[S06-5 Tema 06 - Cauchy Ejercicio 2 - circle via Green|Ej2]] (vía Green con $|z|=1$).

---

## Pregunta 4 — Integral de Riemann $\int_0^1 x^2\,dx = 1/3$

### Enunciado

Aplicar la **definicion general de integral (Riemann)** para demostrar que:

$$\int_{0}^{1} x^2\,dx = \frac{1}{3}$$

a) Sumas superiores e inferiores con particion regular.
b) Suma de Riemann (suma derecha).

### Referencia teorica

La definicion de integral como limite de sumas conecta con la [[S06-1 Tema 06 - Integral de contorno en funciones complejas#Conocimientos previos|definicion de integral de contorno como limite de sumatoria]] $\lim_{n\to\infty}\sum f(z_k)\Delta z_k$ — es el caso analogo real.

### Particion regular de $[0, 1]$

Dividimos $[0, 1]$ en $n$ subintervalos de igual ancho:

$$\Delta x = \frac{1 - 0}{n} = \frac{1}{n}$$

Puntos de la particion: $x_i = \dfrac{i}{n}$ para $i = 0, 1, 2, \ldots, n$.

Como $f(x) = x^2$ es **estrictamente creciente** en $[0, 1]$:

- Minimo en $[x_{i-1}, x_i]$: $f(x_{i-1}) = (i-1)^2/n^2$
- Maximo en $[x_{i-1}, x_i]$: $f(x_i) = i^2/n^2$

### a) Sumas superiores e inferiores

**Suma inferior:**

$$L_n = \sum_{i=1}^{n} f(x_{i-1})\,\Delta x = \sum_{i=1}^{n} \frac{(i-1)^2}{n^2} \cdot \frac{1}{n} = \frac{1}{n^3}\sum_{i=0}^{n-1} i^2$$

Usando la formula $\displaystyle\sum_{i=0}^{n-1} i^2 = \frac{(n-1)n(2n-1)}{6}$:

$$L_n = \frac{(n-1)n(2n-1)}{6n^3}$$

**Suma superior:**

$$U_n = \sum_{i=1}^{n} f(x_i)\,\Delta x = \sum_{i=1}^{n} \frac{i^2}{n^2} \cdot \frac{1}{n} = \frac{1}{n^3}\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6n^3}$$

**Limites cuando $n \to \infty$:**

Expandiendo $L_n$:

$$L_n = \frac{2n^3 - 3n^2 + n}{6n^3} = \frac{1}{3} - \frac{1}{2n} + \frac{1}{6n^2} \xrightarrow[n\to\infty]{} \frac{1}{3}$$

Expandiendo $U_n$:

$$U_n = \frac{2n^3 + 3n^2 + n}{6n^3} = \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2} \xrightarrow[n\to\infty]{} \frac{1}{3}$$

Como $\lim L_n = \lim U_n = 1/3$, la funcion es **integrable Riemann** y:

$$\boxed{\int_{0}^{1} x^2\,dx = \frac{1}{3}}$$

### b) Suma de Riemann (suma derecha)

La suma derecha evalua $f$ en el extremo derecho de cada subintervalo:

$$S_n^{R} = \sum_{i=1}^{n} f(x_i)\,\Delta x = U_n$$

(coincide con la suma superior porque $f$ es creciente).

$$S_n^R = \frac{n(n+1)(2n+1)}{6n^3} = \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}$$

$$\lim_{n \to \infty} S_n^R = \frac{1}{3} + 0 + 0 = \frac{1}{3} \checkmark$$

> [!info] Tabla de convergencia
>
> | $n$ | $L_n$  | $U_n$  |
> | --- | ------ | ------ |
> | $1$ | $0$    | $1$    |
> | $5$ | $0{,}24$ | $0{,}44$ |
> | $10$ | $0{,}285$ | $0{,}385$ |
> | $100$ | $0{,}3284$ | $0{,}3384$ |
> | $1000$ | $0{,}33283$ | $0{,}33383$ |
> | $\infty$ | $1/3 \approx 0{,}3333$ | $1/3 \approx 0{,}3333$ |

---

## Pregunta 5 — Derivadas

### Enunciado

Aplicar **propiedades de las derivadas** para calcular las derivadas de:

a) $f(x) = 3x^4 - 5x^2 + 7x - 4$
b) $g(x) = (x^2 - 1)\,e^{2x}$

### Referencia teorica

Reglas usadas:

- **Regla de potencia:** $\dfrac{d}{dx}[x^n] = n x^{n-1}$
- **Linealidad:** $(af + bg)' = af' + bg'$
- **Regla del producto:** $(uv)' = u'v + uv'$
- **Regla de la cadena:** $\dfrac{d}{dx}[e^{u(x)}] = u'(x)\,e^{u(x)}$

Conexion: las mismas reglas se aplican a [[S03-1 Tema 03 - Derivada de una funcion compleja|derivadas de funciones complejas]] cuando son analiticas.

### a) $f(x) = 3x^4 - 5x^2 + 7x - 4$

Aplicando regla de potencia y linealidad termino por termino:

$$\frac{d}{dx}[3x^4] = 12x^3$$

$$\frac{d}{dx}[-5x^2] = -10x$$

$$\frac{d}{dx}[7x] = 7$$

$$\frac{d}{dx}[-4] = 0$$

Sumando:

$$\boxed{f'(x) = 12x^3 - 10x + 7}$$

### b) $g(x) = (x^2 - 1)\,e^{2x}$

Producto de dos funciones. Sean:

$$u(x) = x^2 - 1 \implies u'(x) = 2x$$

$$v(x) = e^{2x} \implies v'(x) = 2e^{2x} \quad (\text{regla de la cadena con } u(x) = 2x)$$

Aplicando regla del producto:

$$g'(x) = u'(x)\,v(x) + u(x)\,v'(x) = (2x)\,e^{2x} + (x^2 - 1)\,(2e^{2x})$$

Factorizando $2e^{2x}$:

$$g'(x) = 2e^{2x}\bigl[x + (x^2 - 1)\bigr] = 2e^{2x}(x^2 + x - 1)$$

$$\boxed{g'(x) = 2e^{2x}(x^2 + x - 1)}$$

---

## Resumen de respuestas

| #  | Resultado |
| -- | --------- |
| 1  | $I = 9 + \dfrac{9\pi}{4}$ |
| 2a | $\log_b a = c \iff b^c = a$, con $b > 0$, $b \neq 1$, $a > 0$ |
| 2b | $\text{Dom}(f) = (-3/2, +\infty)$, $\text{Rango}(f) = \mathbb{R}$ |
| 2c | $f(11) = 2$, $f(2) = \log_5 7 \approx 1{,}209$ |
| 2d | $x = 61$ |
| 3  | $\oint_{\|z\|=2} z\,dz = 0$ |
| 4  | $L_n = \dfrac{1}{3} - \dfrac{1}{2n} + \dfrac{1}{6n^2}$, $U_n = \dfrac{1}{3} + \dfrac{1}{2n} + \dfrac{1}{6n^2}$ → ambos → $1/3$ |
| 5a | $f'(x) = 12x^3 - 10x + 7$ |
| 5b | $g'(x) = 2e^{2x}(x^2 + x - 1)$ |
