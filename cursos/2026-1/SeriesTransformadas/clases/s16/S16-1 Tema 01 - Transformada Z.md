---
title: "Transformada Z — definición, propiedades y región de convergencia"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-z
  - tema/region-de-convergencia
  - tema/serie-geometrica
date: 2026-07-06
---

## Idea central

La **transformada Z** es una **generalización de la transformada de Fourier** para secuencias discretas $x(n)$. Se introduce porque la transformada de Fourier **no converge para todas las secuencias**; la Z cubre una gama más amplia de señales al incorporar un factor de amortiguamiento $r^{-n}$. Es la herramienta fundamental para el análisis de sistemas y filtros digitales.

Fuente: [[T01-Lectura-transformada-z-p1.pdf|Lectura — Transformada Z (Parte 1)]].

## 1. Definición

La **transformada de Fourier** de una secuencia $x(n)$ es:

$$X(\Omega) = X(e^{i\omega}) = \sum_{n=-\infty}^{+\infty} x(n)\,e^{-i\omega n}\tag{1}$$

La **transformada Z** de la misma secuencia se define como:

$$\boxed{\;\mathcal{Z}\{x(n)\} = X(z) = \sum_{n=-\infty}^{+\infty} x(n)\,z^{-n}\;}\tag{2}$$

donde $z$ es una variable compleja continua.

> [!important] Relación Fourier ↔ Z
> Existe una relación muy cercana entre ambas: sustituyendo $z = e^{i\omega}$, la transformada Z **se convierte** en la transformada de Fourier. Es decir, la TF es la transformada Z evaluada sobre el **círculo unitario** $|z| = 1$.

Tomando $z = r e^{i\omega}$:

$$X(re^{i\omega}) = \sum_{n=-\infty}^{+\infty} x(n)\,(r^{-n})\,e^{-i\omega n}\tag{5}$$

que se interpreta como la transformada de Fourier del **producto** de $x(n)$ con la secuencia $r^{-n}$. El factor $r^{-n}$ es el que hace converger la Z aun cuando la TF de $x(n)$ no converge.

## 2. Herramienta básica: serie geométrica

$$\sum_{n=N_1}^{N_2} r^n = \frac{r^{N_1} - r^{N_2+1}}{1 - r},\qquad |r| < 1$$

$$\sum_{n=0}^{N-1} r^n = \frac{1 - r^N}{1 - r};\qquad \sum_{n=0}^{\infty} r^n = \frac{1}{1 - r},\quad |r| < 1$$

> [!tip] Estrategia general
> Para calcular una transformada Z, se parte de la **sumatoria** de la definición y se lleva a una **serie geométrica** conocida, obteniendo una expresión cerrada. Ver los ejercicios resueltos.

## 3. Propiedades de la transformada Z

| Propiedad | Fórmula |
| --------- | ------- |
| Linealidad | $\mathcal{Z}\{a\,x_1(n) + b\,x_2(n)\} = a\,X_1(z) + b\,X_2(z)$ |
| Desplazamiento en el tiempo | $\mathcal{Z}\{x(n-n_0)\,u(n-n_0)\} = z^{-n_0}\,X(z)$ |
| Corrimiento en fase | $\mathcal{Z}\{e^{i\omega n}x(n)\} = X(e^{-i\omega}z)$ |
| Operación escalar en $z$ | $\mathcal{Z}\{z_0^{\,n}x(n)\} = X\!\left(\dfrac{z}{z_0}\right)$ |
| Inversión de tiempo | $\mathcal{Z}\{x(-n)\} = X\!\left(\dfrac{1}{z}\right)$ |
| Diferenciación en frecuencia | $\mathcal{Z}\{n\,x(n)\} = -z\,\dfrac{dX(z)}{dz}$ |
| Conjugación | $\mathcal{Z}\{x^*(n)\} = X^*(z^*)$ |
| Convolución | $\mathcal{Z}\{x_1(n) * x_2(n)\} = X_1(z)\,X_2(z)$ |

> [!note] Por qué importan
> Estas propiedades convierten la solución de **ecuaciones en diferencias lineales** en simple manipulación algebraica (igual que Laplace hace con las ecuaciones diferenciales).

## 4. Región de convergencia (ROC)

La transformada Z no converge para toda secuencia ni todo $z$. El conjunto de valores de $z$ para los que converge se llama **región de convergencia (ROC)**. La condición es la sumabilidad absoluta:

$$\sum_{n=-\infty}^{+\infty} |x(n)\,r^{-n}| < \infty\tag{6}$$

El factor $r^{-n}$ hace que la Z converja aun cuando la TF de $x(n)$ no lo haga.

> [!summary] Forma de la ROC
> La ROC de $X(z)$ es una **región anular** (anillo) centrada en el origen del plano complejo: $R^- < |z| < R^+$, con posibilidad de $R^- = 0$ y/o $R^+ = \infty$.

Si $X(z)$ es una **función racional** $\dfrac{N(z)}{D(z)}$:
- las raíces de $N(z)$ son los **ceros** de $X(z)$,
- las raíces de $D(z)$ son los **polos** de $X(z)$,
- hay que considerar además los valores particulares $z=0$ y $z=\infty$.

> [!info] Figura
> La ROC se ilustra como un anillo centrado en el origen (ver Figura 1 de la [[T01-Lectura-transformada-z-p1.pdf|lectura]]).

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
- Material del curso: [[T01-Lectura-transformada-z-p1.pdf|Lectura — Transformada Z (Parte 1)]].
