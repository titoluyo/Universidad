---
title: "Transformada Z (Parte 2) — funciones especiales, inversa y transformada unilateral"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-z
  - tema/transformada-z-inversa
  - tema/residuos
date: 2026-07-13
---

## Idea central

Esta segunda parte completa la transformada Z con: las **transformadas de funciones especiales** (impulso, escalón, exponencial), los cuatro **métodos para invertir** la transformada Z, y la **transformada Z unilateral** (para sistemas causales). La inversión permite regresar del dominio $z$ al dominio del tiempo discreto $x(n)$.

Fuente: [[T01-Lectura-transformada-z-p2.pdf|Lectura — Transformada Z (Parte 2)]].

## 1. Transformada Z de funciones especiales

| Secuencia | Transformada Z | ROC |
| --------- | -------------- | --- |
| Impulso unitario $\delta(n)$ | $1$ | todo $z$ |
| Impulso retrasado $\delta(n-m)$ | $z^{-m}$ | $z\neq 0$ |
| Escalón unitario $u(n)$ | $\dfrac{1}{1-z^{-1}} = \dfrac{z}{z-1}$ | $|z|>1$ |
| Geométrica $a^n$ | $\dfrac{z}{z-a}$ | $|z|>a$ |
| Exponencial $e^{-at}$ (con $t=nT$) | $\dfrac{z}{z-e^{-aT}}$ | $|z|>e^{-aT}$ |

- El **impulso** se obtiene directo de la definición ($\mathcal{Z}\{\delta(n)\}=\delta(0)=1$).
- La **geométrica** sale de la propiedad de multiplicación $\mathcal{Z}\{a^n f(n)\} = X(a^{-1}z)$ aplicada al escalón.
- La **exponencial** sigue el patrón de la serie geométrica con razón $r = e^{-aT}z^{-1}$.

## 2. Transformada Z inversa

> [!summary] Definición formal (integral de contorno)
> $$x(n) = \frac{1}{2\pi i}\oint_C X(z)\,z^{n-1}\,dz$$
> donde $C$ es un contorno cerrado (p. ej. el círculo unitario) dentro de la ROC que encierra el origen.

Existen **cuatro métodos** para invertir la transformada Z:

1. **División larga** — divide $N(z)$ entre $D(z)$ para obtener la serie de potencias $x(0)+x(1)z^{-1}+\cdots$; los coeficientes son $x(n)$. Ver [[S17-2 Tema 01 - Inversa por division larga|Ej 1]].
2. **Expansión en fracciones parciales** + tabla — se divide $F(z)$ entre $z$, se expande $\frac{F(z)}{z}$ en fracciones parciales, se multiplica por $z$ cada término y se invierte con la tabla. Ver [[S17-5 Tema 01 - Ecuacion en diferencias con entrada|Ej 4]].
3. **Integral de inversión (residuos)** — ver §3.
4. **Inspección** — reconocer formas conocidas directamente.

### Método de fracciones parciales (resumen)

Si $F(z) = \dfrac{P(z)}{Q(z)} = \dfrac{z\,P_1(z)}{Q(z)}$, se divide entre $z$ y se factoriza $Q(z) = (z-\alpha_1)(z-\alpha_2)\cdots(z-\alpha_n)$:

$$\frac{F(z)}{z} = \frac{n_1}{z-\alpha_1} + \frac{n_2}{z-\alpha_2} + \cdots + \frac{n_n}{z-\alpha_n}$$

(con término especial para raíces repetidas). Luego se multiplica cada fracción por $z$ y se invierte con la tabla.

## 3. Método de la integral de inversión (residuos)

Por el **teorema de la integral de Cauchy**, la inversa se calcula como la suma de **residuos**:

$$x(n) = \frac{1}{2\pi i}\oint_C X(z)\,z^{n-1}\,dz = \sum_i \left[(z-z_i)\,X(z)\,z^{n-1}\right]_{z=z_i}$$

(válido para polos simples $z_i$). Recordatorios del teorema de Cauchy:

$$\frac{1}{2\pi i}\oint_C \frac{f(z)}{z-z_0}\,dz = \begin{cases} f(z_0), & z_0 \text{ dentro de } C \\ 0, & z_0 \text{ fuera de } C\end{cases}$$

$$\frac{1}{2\pi i}\oint_C \frac{f(z)}{(z-z_0)^k}\,dz = \frac{1}{(k-1)!}\,f^{(k-1)}(z_0)\quad (z_0 \text{ dentro de } C)$$

Ver [[S17-3 Tema 01 - Inversa por integral de inversion|Ej 2]] y [[S17-4 Tema 01 - Inversa por residuos|Ej 3]].

## 4. Transformada Z unilateral

- Se aplica a señales de **sistemas causales**: $X(z) = \sum_{n=0}^{\infty} x(n)z^{-n}$.
- Equivale a la bilateral para sistemas causales y satisface las mismas propiedades, **excepto la de desplazamiento en el tiempo**.

### Desplazamiento en el tiempo (unilateral)

Para un **retardo** $k$ ($x(n-k)$):

$$X(z) = x(-k) + z^{-1}x(-k+1) + \cdots + z^{-k+1}x(-1) + z^{-k}X(z),\quad k>0$$

Para un **adelanto** $k$ ($x(n+k)$):

$$X(z) = -x(0) + z^{k-1}x(1) - \cdots - z\,x(k-1) + z^{-k}X(z),\quad k>0$$

> [!tip] Clave para ecuaciones en diferencias
> La forma unilateral del desplazamiento (que **incorpora las condiciones iniciales** $x(0), x(1), \ldots$) es lo que permite resolver **ecuaciones en diferencias** con valores iniciales — análogo a lo que la transformada de derivadas hace en Laplace. Ver [[S17-5 Tema 01 - Ecuacion en diferencias con entrada|Ej 4]] y [[S17-6 Tema 01 - Ecuacion en diferencias homogenea|Ej 5]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
- Material del curso: [[T01-Lectura-transformada-z-p2.pdf|Lectura — Transformada Z (Parte 2)]].
