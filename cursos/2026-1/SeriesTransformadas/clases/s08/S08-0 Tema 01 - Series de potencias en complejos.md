---
title: "Series de potencias en complejos — definiciones y criterio del cociente"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-potencias
  - tema/criterio-del-cociente
  - tema/radio-de-convergencia
date: 2026-05-11
---

## Idea central

Una **serie de potencias** en variable compleja es una suma infinita de términos donde cada uno es un múltiplo de una potencia creciente de $(z - z_0)$. Generaliza al plano complejo el concepto de serie de Taylor real.

> [!summary] Forma general
> $$y = \sum_{n=0}^{\infty} a_n\,(z - z_0)^n$$
> Donde:
> - $a_n$ son los **coeficientes** (números complejos en general).
> - $z_0$ es el **centro** de la serie.
> - $z$ es la variable compleja.

Cuando $z_0 = 0$ la serie se llama **serie de Maclaurin compleja**: $\sum_{n=0}^{\infty} a_n z^n$.

## Por qué importan

Las series de potencias permiten:

1. **Representar funciones complejas** como sumas infinitas (extensión analítica de Taylor/Maclaurin al plano $\mathbb{C}$).
2. **Aproximar valores** de funciones complicadas truncando la serie.
3. **Resolver integrales y ecuaciones diferenciales** sustituyendo la función por su serie.
4. **Caracterizar funciones analíticas**: toda función analítica en un disco admite desarrollo en serie de potencias allí (esto es la base de la Semana 9 — series de Taylor en complejos).

## Convergencia de series complejas

> [!info] Definición — Convergencia absoluta
> Una serie $\sum_{n=1}^{\infty} u_n$ **converge absolutamente** si la serie de los módulos converge:
> $$\text{Si } \sum_{n=1}^{\infty} |u_n| \text{ converge} \;\Longrightarrow\; \sum_{n=1}^{\infty} u_n \text{ converge}$$
>
> La convergencia absoluta implica convergencia ordinaria, pero **no** al revés.

## Criterio del cociente (test de D'Alembert)

> [!success] Criterio del cociente
> Sea $\sum u_n$ una serie de términos no nulos. Calcular:
> $$L = \lim_{n \to \infty} \left|\frac{u_{n+1}}{u_n}\right|$$
>
> - Si $L < 1$ → la serie **converge absolutamente**.
> - Si $L > 1$ → la serie **diverge**.
> - Si $L = 1$ → el criterio **no decide** (usar otro test).

## Aplicación a series de potencias

Para $\sum_{n=0}^\infty a_n (z - z_0)^n$ con $a_n \neq 0$, aplicando el criterio del cociente:

$$\lim_{n \to \infty} \left|\frac{a_{n+1}(z - z_0)^{n+1}}{a_n(z - z_0)^n}\right| = |z - z_0|\,\lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right| = |z - z_0|\,\lambda$$

Definimos:

$$\lambda = \lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right|$$

(El módulo $|z - z_0|$ **sale fuera del límite** porque no depende de $n$.)

## Radio de convergencia

> [!summary] Radio de convergencia $R$
> $$\boxed{\;R = \frac{1}{\lambda}\;}$$
>
> La serie de potencias **converge absolutamente** para todos los $z$ con $|z - z_0| < R$, y **diverge** para $|z - z_0| > R$. El comportamiento en $|z - z_0| = R$ debe analizarse caso por caso.

Casos límite:

| $\lambda$ | $R$ | Interpretación |
| --------- | --- | -------------- |
| $0$       | $\infty$ | Converge en **todo el plano** $\mathbb{C}$ |
| Finito $> 0$ | $1/\lambda$ | Converge en el **disco abierto** $\{z : \|z - z_0\| < R\}$ |
| $\infty$  | $0$ | Converge **solo en** $z = z_0$ |

## Procedimiento operativo

1. Escribir la serie en forma estándar $\sum a_n (z - z_0)^n$ identificando $a_n$.
2. Calcular $C_{n+1}$ sustituyendo $n \mapsto n+1$ en el término general.
3. Formar el cociente $\left|\dfrac{C_{n+1}}{C_n}\right|$ y simplificar (cancelando factoriales y potencias).
4. Separar el factor $|z - z_0|^k$ (no depende de $n$) del límite.
5. Calcular $\lambda$ (límite del cociente de coeficientes).
6. Determinar $R = 1/\lambda$ y la región de convergencia.

> [!warning] Convención del docente
> En el curso, el profesor define $\lambda$ como el **límite del cociente de los coeficientes** (extrayendo $|z - z_0|$ del módulo) — no incluye el factor $|z - z_0|$ dentro de $\lambda$. Así, $R = 1/\lambda$ da directamente el radio del disco de convergencia centrado en $z_0$.

## Ejercicios resueltos

| # | Serie | $\lambda$ | $R$ | Tipo |
| - | ----- | --------- | --- | ---- |
| [[S08-1 Tema 01 - Convergencia Ej1 - serie geometrica con (z+2)\|Ej 1]] | $\sum \dfrac{(z+2)^{n-1}}{(n+1)^3\,4^n}$ | $\tfrac{1}{4}$ | $4$ | centro $z_0 = -2$ |
| [[S08-2 Tema 01 - Convergencia Ej2 - serie del seno\|Ej 2]] | $\sum \dfrac{(-1)^{n-1} z^{2n-1}}{(2n-1)!}$ | $0$ | $\infty$ | serie del $\sin z$ |
| [[S08-3 Tema 01 - Convergencia Ej3 - exponencial alternante\|Ej 3]] | $\sum \dfrac{(-1)^{n+1} z^{3n}}{n!}$ | $0$ | $\infty$ | tipo exponencial |
| [[S08-4 Tema 01 - Convergencia Ej4 - polinomial n(n+1)\|Ej 4]] | $\sum n(n+1)\,z^n$ | $1$ | $1$ | polinomial creciente |

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — Capítulo 5 (Series).
- Apostol, T. M. (1980). *Análisis matemático* (2.ª ed.). Reverté — §9.3 (Series de potencias).
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Capítulo 6.
