---
title: Campo magnetico de un toroide
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 5
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/toroide
  - tema/ley-de-ampere
date: 2026-03-28
---

## 1. ¿Qué es un toroide?

Cuando hablamos de un toroide nos referimos a una figura geométrica tridimensional que se asemeja a una donut. Se genera al girar un círculo en el espacio alrededor de un eje que no pasa por su centro, creando así una figura anular con una cavidad en el medio.

Para nuestra materia, un toroide alude a configuración de un conductor eléctrico enrollado en forma de anillo o espira cerrada. Este diseño tiene ventajas prácticas frente a otras configuraciones, como solenoides o bobinas rectangulares, ya que las líneas de campo magnético se mantienen más confinadas y no se dispersan en el espacio circundante.

## 2. El campo magnético de un toroide

En un toroide, la corriente eléctrica circula por los alambres enrollados alrededor del toroide, generando un campo magnético que circula por el interior del toroide. Dado que el toroide es una estructura cerrada, el campo magnético fuera de esta forma es casi nulo.

![[Pasted image 20260328231533.png]]

## 3. La [[S01-1 Tema 01 - Como se produce un campo magnético|ley de Ampère]]

Para calcular el valor del campo magnético dentro de un toroide, consideremos un toroide con $N$ vueltas de alambre y una corriente $I$ fluyendo a través de cada vuelta. La corriente total enlazada por una trayectoria amperiana es $NI$. Usando la ley de Ampère, podemos expresar el campo magnético en función de la corriente y el número de vueltas:

$$
\oint \vec{B} \cdot d\vec{l} = \mu_0 NI
$$

Si asumimos que el campo magnético es tangencial y aproximadamente constante a lo largo de una circunferencia de radio medio $r$, entonces:

$$
B(2\pi r) = \mu_0 NI
$$

Por lo tanto, el campo magnético en el interior del toroide viene dado por:

$$
B = \frac{\mu_0 NI}{2\pi r}
$$

Donde:

- $r$ es el radio medio del toroide.
- $B$ es el campo magnético.
- $\mu_0$ es la permeabilidad del vacío.
- $N$ es el número de vueltas.
- $I$ es la corriente eléctrica que circula por el devanado.

A partir de esta relación, se puede deducir que el campo magnético dentro del toroide es proporcional al número de vueltas y a la corriente que circula por ellas. Además, varía inversamente con el radio del toroide.

---

## Bibliografía

- Rodríguez, M. (2014). _Materiales y circuitos magnéticos_. Universidad de Cantabria.
