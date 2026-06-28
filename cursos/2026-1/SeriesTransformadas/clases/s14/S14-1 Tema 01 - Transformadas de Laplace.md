---
title: "Transformada de Laplace — definición, transformadas elementales, propiedades e inversa"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 14
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-de-laplace
  - tema/transformada-inversa-de-laplace
date: 2026-06-22
---

## Idea central

La **transformada de Laplace** es una herramienta matemática que convierte una función del **dominio del tiempo** $F(t)$ en una función de una **variable compleja** $f(s)$ (por el momento, $s$ real). Su gran utilidad es transformar **ecuaciones diferenciales** difíciles en **problemas algebraicos** sencillos, resolverlos en el dominio de $s$ y regresar al dominio del tiempo con la **transformada inversa**. Tiene aplicación directa en ingeniería y ciencias (electrónica, telecomunicaciones, análisis de sistemas lineales).

Fuente: [[T01-Lectura-transformadas-laplace.pdf|Lectura — Transformadas de Laplace]].

## 1. Definición

Sea $F(t)$ una función de $t$ definida para $t > 0$. La **transformada de Laplace** de $F(t)$, denotada por $\mathcal{L}\{F(t)\}$, se define como:

$$\boxed{\;\mathcal{L}\{F(t)\} = \int_0^{\infty} e^{-st}\,F(t)\,dt\;}$$

donde, por el momento, el parámetro $s$ es real.

> [!note] Condiciones suficientes de existencia
> Para garantizar la existencia de $\mathcal{L}\{F(t)\}$:
> - $F(t)$ debe ser **continua por tramos** (seccionalmente continua) para $t \geq 0$.
> - $F(t)$ debe ser de **orden exponencial** para $t > T$.
> - La integral de $F(t)$ debe **converger** para algún valor de $s$.

> [!tip] Notación
> Cuando una función de $t$ se indica con **mayúscula** ($F(t)$, $G(t)$, …), su transformada de Laplace se denota con la **minúscula** correspondiente ($f(s)$, $g(s)$, …).

## 2. Transformadas de algunas funciones elementales

**I. Exponencial** $F(t) = e^{kt}$. Aplicando la definición:

$$\mathcal{L}\{e^{kt}\} = \int_0^{\infty} e^{-st}\,e^{kt}\,dt = \frac{1}{s-k}\quad \text{para } s > k$$

Observación: cuando $k = 0$, se obtiene la transformada de la constante $1$:

$$\mathcal{L}\{1\} = \frac{1}{s}$$

**II. Potencia** $F(t) = t^n$. Integrando por partes:

$$\mathcal{L}\{t^n\} = \int_0^{\infty} e^{-st}\,t^n\,dt = \frac{n!}{s^{n+1}}\quad \text{si } s > 0$$

**III. Seno** $F(t) = \sin at$. Integrando por partes:

$$\mathcal{L}\{\sin at\} = \int_0^{\infty} e^{-st}\sin at\,dt = \frac{a}{s^2 + a^2}\quad \text{si } s > 0$$

**IV. Coseno** $F(t) = \cos at$. Integrando por partes:

$$\mathcal{L}\{\cos at\} = \int_0^{\infty} e^{-st}\cos at\,dt = \frac{s}{s^2 + a^2}\quad \text{si } s > 0$$

## 3. Tabla de transformadas elementales

| $F(t)$ | $\mathcal{L}\{F(t)\} = f(s)$ | Región |
| --- | --- | --- |
| $k$ | $\dfrac{k}{s}$ | $s > 0$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $s > 0$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ | $s > a$ |
| $\sin at$ | $\dfrac{a}{s^2+a^2}$ | $s > 0$ |
| $\cos at$ | $\dfrac{s}{s^2+a^2}$ | $s > 0$ |
| $\sinh at$ | $\dfrac{a}{s^2-a^2}$ | $s > \lvert a\rvert$ |
| $\cosh at$ | $\dfrac{s}{s^2-a^2}$ | $s > \lvert a\rvert$ |
| $e^{bt}\sin at$ | $\dfrac{a}{(s-b)^2+a^2}$ | |
| $e^{bt}\cos at$ | $\dfrac{s-b}{(s-b)^2+a^2}$ | |
| $e^{bt}\sinh at$ | $\dfrac{a}{(s-b)^2-a^2}$ | |
| $e^{bt}\cosh at$ | $\dfrac{s-b}{(s-b)^2-a^2}$ | |

> [!cite] Fuente de la tabla
> Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.

## 4. Propiedades de la transformada de Laplace

**I. Linealidad.** Si $c_1, c_2$ son constantes y $F_1, F_2$ tienen transformada $f_1(s)$, $f_2(s)$:

$$\mathcal{L}\{c_1 F_1(t) + c_2 F_2(t)\} = c_1 f_1(s) + c_2 f_2(s)$$

**II. Primera propiedad de traslación** (en $s$). Si $\mathcal{L}\{F(t)\} = f(s)$:

$$\mathcal{L}\{e^{at}F(t)\} = f(s-a)$$

**III. Segunda propiedad de traslación** (en $t$). Si $\mathcal{L}\{F(t)\} = f(s)$ y

$$G(t) = \begin{cases} F(t-a), & t > a \\ 0, & t < a \end{cases} \qquad\Longrightarrow\qquad \mathcal{L}\{G(t)\} = e^{-as}f(s)$$

**IV. Cambio de escala.** Si $\mathcal{L}\{F(t)\} = f(s)$:

$$\mathcal{L}\{F(at)\} = \frac{1}{a}\,f\!\left(\frac{s}{a}\right)$$

## 5. Transformada de Laplace de las derivadas

> [!summary] Teorema (derivadas)
> Si $\mathcal{L}\{F(t)\} = f(s)$, entonces:
> $$\mathcal{L}\{F'(t)\} = s\,f(s) - F(0)$$
> $$\mathcal{L}\{F''(t)\} = s^2 f(s) - s\,F(0) - F'(0)$$
> Y en general, para la $n$-ésima derivada:
> $$\mathcal{L}\{F^{(n)}(t)\} = s^n f(s) - s^{n-1}F(0) - s^{n-2}F'(0) - \cdots - s\,F^{(n-2)}(0) - F^{(n-1)}(0)$$

donde $F^{(n)}(t)$ es continua por tramos y de orden exponencial. **Esta es la propiedad clave** para resolver ecuaciones diferenciales con valores iniciales: las condiciones $F(0)$, $F'(0)$, … se incorporan automáticamente.

## 6. Transformada de Laplace de las integrales

$$\mathcal{L}\left\{\int_0^t F(u)\,du\right\} = \frac{f(s)}{s}$$

Generalizando para $n$ integrales sucesivas:

$$\mathcal{L}\left\{\underbrace{\int_0^t \int_0^t \cdots \int_0^t}_{n} F(u)\,du\right\} = \frac{1}{s^n}\,\mathcal{L}\{F(t)\}$$

## 7. Transformada inversa de Laplace

Si $\mathcal{L}\{F(t)\} = f(s)$, entonces $F(t)$ se denomina **transformada inversa de Laplace** de $f(s)$ y se denota:

$$F(t) = \mathcal{L}^{-1}\{f(s)\}$$

**Propiedades de la transformada inversa:**

**I. Linealidad.**

$$\mathcal{L}^{-1}\{c_1 f_1(s) + c_2 f_2(s)\} = c_1 F_1(t) + c_2 F_2(t)$$

**II. Primera propiedad de traslación.** Si $\mathcal{L}^{-1}\{f(s)\} = F(t)$:

$$\mathcal{L}^{-1}\{f(s-a)\} = e^{at}F(t)$$

**III. Segunda propiedad de traslación.** Si $\mathcal{L}^{-1}\{f(s)\} = F(t)$:

$$\mathcal{L}^{-1}\{e^{as}f(s)\} = \begin{cases} F(t-a), & t > a \\ 0, & t < a \end{cases}$$

**IV. Cambio de escala.** Si $\mathcal{L}^{-1}\{f(s)\} = F(t)$:

$$\mathcal{L}^{-1}\{f(ks)\} = \frac{1}{k}\,F\!\left(\frac{t}{k}\right)$$

> [!tip] Técnicas de la inversa
> En la práctica, para invertir $f(s)$ se usan **fracciones parciales** y **completación de cuadrados** para reescribir $f(s)$ como combinación de las formas de la tabla (especialmente $\frac{s-b}{(s-b)^2+a^2}$ y $\frac{a}{(s-b)^2+a^2}$, que devuelven $e^{bt}\cos at$ y $e^{bt}\sin at$). Ver los [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|ejercicios de circuitos RLC]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
- Material del curso: [[T01-Lectura-transformadas-laplace.pdf|Lectura — Transformadas de Laplace]].
