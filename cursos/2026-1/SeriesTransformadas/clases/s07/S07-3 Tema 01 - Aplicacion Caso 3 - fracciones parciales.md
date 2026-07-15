---
title: "Aplicación del teorema de Cauchy — Caso 3: dos singularidades vía fracciones parciales"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/formula-integral-de-cauchy
  - tema/fracciones-parciales
date: 2026-05-04
---

## Enunciado

Calcular:

$$\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z - 1)(z - 2)}\,dz$$

donde $C: |z| = 3$ (circunferencia de radio 3 centrada en el origen).

## Paso 1: identificar los puntos singulares

Igualamos el denominador a cero:

$$(z - 1)(z - 2) = 0 \;\Longrightarrow\; z = 1,\; z = 2$$

Ambos son singularidades **simples** (multiplicidad 1).

## Paso 2: verificar que están dentro del contorno

$C: |z| = 3$ es una circunferencia de radio 3. Como $|1| = 1 < 3$ y $|2| = 2 < 3$, **ambos puntos quedan dentro de la curva** ✓.

![[T01-Caso3-Curva.png]]

## Paso 3 (opcional — simplificación errónea del guion): identidad trigonométrica

> [!warning] Inconsistencia en el guion del docente
> El guion plantea "emplear la propiedad $\sin\pi z^2 + \cos\pi z^2 = 1$" — **esto es incorrecto**: la identidad pitagórica es $\sin^2\theta + \cos^2\theta = 1$, no $\sin\theta + \cos\theta$. En general $\sin u + \cos u \neq 1$.
>
> En la práctica el guion **descarta** esta simplificación en los pasos siguientes y vuelve a la función original al aplicar la fórmula integral de Cauchy, por lo que el resultado final sigue siendo correcto. **Mejor omitir este paso**.

## Paso 4: descomposición en fracciones parciales

Para separar las dos singularidades, descomponemos:

$$\frac{1}{(z - 1)(z - 2)} = \frac{A}{z - 1} + \frac{B}{z - 2}$$

Resolviendo $A(z - 2) + B(z - 1) = 1$ con $z = 2 \Rightarrow B = 1$ y con $z = 1 \Rightarrow A = -1$:

$$\frac{1}{(z - 1)(z - 2)} = \frac{1}{z - 2} - \frac{1}{z - 1}$$

Aplicando esta descomposición al integrando original:

$$\frac{\sin\pi z^2 + \cos\pi z^2}{(z - 1)(z - 2)} = \frac{\sin\pi z^2 + \cos\pi z^2}{z - 2} - \frac{\sin\pi z^2 + \cos\pi z^2}{z - 1}$$

## Paso 5: integrar separando los dos términos

$$\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z-1)(z-2)}\,dz = \oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{z - 2}\,dz \;-\; \oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{z - 1}\,dz$$

Sea $g(z) = \sin\pi z^2 + \cos\pi z^2$. Aplicamos la fórmula integral de Cauchy $\oint \dfrac{g(z)}{z - z_0}\,dz = 2\pi i\,g(z_0)$ a cada uno:

### Para $z_0 = 2$

$$g(2) = \sin\pi (2)^2 + \cos\pi (2)^2 = \sin 4\pi + \cos 4\pi = 0 + 1 = 1$$

$$\oint_C \frac{g(z)}{z - 2}\,dz = 2\pi i \cdot 1 = 2\pi i$$

### Para $z_0 = 1$

$$g(1) = \sin\pi (1)^2 + \cos\pi (1)^2 = \sin\pi + \cos\pi = 0 + (-1) = -1$$

$$\oint_C \frac{g(z)}{z - 1}\,dz = 2\pi i \cdot (-1) = -2\pi i$$

## Paso 6: combinar resultados

$$\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z - 1)(z - 2)}\,dz = 2\pi i - (-2\pi i) = 4\pi i$$

> [!success] Resultado
> $$\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z - 1)(z - 2)}\,dz = 4\pi i$$

## Conclusión

Cuando un integrando tiene un **producto de factores lineales en el denominador** y **varias singularidades dentro del contorno**, conviene aplicar **fracciones parciales** para descomponerlo en sumandos del tipo $\dfrac{g(z)}{z - z_k}$, evaluar la fórmula integral de Cauchy en cada uno y sumar contribuciones — equivalente a usar el [[S06-6 Tema 06 - Teorema de extension de Cauchy|teorema de extensión de Cauchy]] sin construir explícitamente los contornos auxiliares.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §50, §52.
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Cap. 5, Problemas resueltos.
