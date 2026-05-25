---
title: "Relación del teorema de Cauchy y una integral — Lectura"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/teorema-de-cauchy
  - tema/formula-integral-de-cauchy
date: 2026-05-04
---

## Idea central

El [[S06-3 Tema 06 - Teorema de Cauchy|teorema de Cauchy]] establece que, si $f(z)$ es holomorfa en una región cerrada y simplemente conexa, entonces la integral a lo largo de cualquier curva cerrada contenida en esa región es cero:

$$\oint_C f(z)\,dz = 0$$

Pero esto solo aplica cuando la función es analítica en todo el interior. La **utilidad práctica** del teorema aparece cuando combinamos esta propiedad con la **fórmula integral de Cauchy**, que permite evaluar integrales sobre curvas cerradas que sí encierran **puntos singulares** de la función.

> [!summary] Conexión semana 6 → semana 7
> - **Semana 6:** Teorema de Cauchy "puro" — $\oint f(z)\,dz = 0$ cuando $f$ es analítica en toda la región.
> - **Semana 7:** Fórmula integral de Cauchy — calcular $\oint f(z)\,dz$ cuando $f$ tiene singularidades dentro del contorno, expresando el resultado en función de $f$ y sus derivadas evaluadas en esos puntos.

## Punto de singularidad

> [!info] Definición
> Un **punto de singularidad** de $f(z)$ es un valor $z_0$ donde la función **no es analítica**. En las funciones del tipo cociente, los puntos de singularidad ocurren donde el denominador se anula.

**Ejemplo.** Para $f(z) = \dfrac{z^3 + 1}{z^2 + 1}$, los puntos singulares se obtienen de $z^2 + 1 = 0$, es decir, $z = \pm i$.

## Fórmula integral de Cauchy

Sea $f(z)$ analítica dentro y sobre una curva cerrada simple $C$, y sea $z_0$ un punto interior a $C$. Entonces:

$$\oint_C \frac{f(z)}{z - z_0}\,dz = 2\pi i\,f(z_0)$$

Esta fórmula transforma una integral compleja en una **evaluación funcional**: basta calcular $f(z_0)$ para conocer el valor de la integral.

## Fórmula generalizada (derivadas de funciones analíticas)

Si $f(z)$ es analítica en una región, admite **derivadas de todos los órdenes** en cada punto interior, y todas son analíticas. La extensión de la fórmula integral de Cauchy para potencias del denominador es:

$$\boxed{\;\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz = \frac{2\pi i}{n!}\,f^{(n)}(z_0)\;}$$

Donde:
- $n = 0, 1, 2, \ldots$ es el orden de la derivada,
- $f^{(n)}(z_0)$ es la derivada $n$-ésima de $f$ evaluada en $z_0$,
- $z_0$ es el punto singular interior a $C$.

Para $n = 0$ se recupera la fórmula original ($f^{(0)} = f$, $0! = 1$).

## Procedimiento general para resolver $\oint_C \dfrac{g(z)}{h(z)}\,dz$

1. **Identificar los puntos singulares** resolviendo $h(z) = 0$.
2. **Graficar la curva** $C$ y verificar qué singularidades quedan **dentro** del contorno.
   - Si **ninguna** singularidad está dentro → la integral vale **0** (Teorema de Cauchy puro).
   - Si **una o varias** están dentro → aplicar la fórmula integral de Cauchy (paso 3).
3. **Reorganizar** el integrando como $\dfrac{f(z)}{(z - z_0)^{n+1}}$ identificando $f(z)$ y el orden $n+1$.
4. **Aplicar** la fórmula correspondiente:
   - Denominador simple $(z - z_0)$ → $2\pi i\,f(z_0)$.
   - Denominador con exponente $(z - z_0)^{n+1}$ → $\frac{2\pi i}{n!}\,f^{(n)}(z_0)$.
5. **Sumar las contribuciones** si hay varias singularidades dentro del contorno (consecuencia del [[S06-6 Tema 06 - Teorema de extension de Cauchy|teorema de extensión de Cauchy]]).

## Casos resueltos en la semana

| # | Forma del integrando | Singulares | Curva | Resultado |
| - | -------------------- | ---------- | ----- | --------- |
| [[S07-1 Tema 01 - Aplicacion Caso 1 - integral con factor lineal\|Caso 1]] | $\dfrac{z^2+1}{z(2z+1)}$ | $z=0,\ z=-\tfrac{1}{2}$ | $\|z\|=1$ | $-\dfrac{\pi i}{2}$ |
| [[S07-2 Tema 01 - Aplicacion Caso 2 - formula generalizada\|Caso 2]] | $\dfrac{z^2-3z}{(z+1)^2}$ | $z=-1$ (orden 2) | implícita | $-10\pi i$ |
| [[S07-3 Tema 01 - Aplicacion Caso 3 - fracciones parciales\|Caso 3]] | $\dfrac{\sin\pi z^2 + \cos\pi z^2}{(z-1)(z-2)}$ | $z=1,\ z=2$ | $\|z\|=3$ | $4\pi i$ |
| [[S07-4 Tema 01 - Aplicacion Caso 4 - formula generalizada e2z\|Caso 4]] | $\dfrac{e^{2z}}{(z+1)^4}$ | $z=-1$ (orden 4) | $\|z\|=3$ | $\dfrac{8\pi i}{3 e^2}$ |

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — Capítulo 4, "Integrales".
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Capítulo 5.
