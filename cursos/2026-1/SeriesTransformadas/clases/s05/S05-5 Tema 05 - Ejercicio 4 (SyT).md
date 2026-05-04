---
title: "Ejercicio 4 - Probar que sen^2(z) + cos^2(z) = 1 en complejos"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 5
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-trigonometrica-compleja
  - tema/identidades-trigonometricas
date: 2026-04-26
---

## Enunciado

Probar que para todo $z \in \mathbb{C}$:

$$\text{sen}^2 z + \cos^2 z = 1$$

usando las definiciones exponenciales del seno y coseno complejos.

## Referencia teorica

Ver [[S05-1 Tema 05 - Funciones complejas elementales#4. Funciones trigonometricas e hiperbolicas|definiciones trigonometricas]]:

$$\text{sen}\,z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}$$

## Paso 1: Sustituir en la expresion

$$\text{sen}^2 z + \cos^2 z = \left(\frac{e^{iz} - e^{-iz}}{2i}\right)^2 + \left(\frac{e^{iz} + e^{-iz}}{2}\right)^2$$

## Paso 2: Desarrollar el primer cuadrado

Aplicando $(A - B)^2 = A^2 - 2AB + B^2$ con $A = e^{iz}$, $B = e^{-iz}$:

$$\left(\frac{e^{iz} - e^{-iz}}{2i}\right)^2 = \frac{(e^{iz})^2 - 2\,e^{iz}\,e^{-iz} + (e^{-iz})^2}{(2i)^2}$$

Como $e^{iz}\cdot e^{-iz} = e^{0} = 1$ y $(2i)^2 = -4$:

$$= \frac{e^{2iz} - 2 + e^{-2iz}}{-4} = \frac{-e^{2iz} + 2 - e^{-2iz}}{4} = \frac{2 - e^{2iz} - e^{-2iz}}{4}$$

## Paso 3: Desarrollar el segundo cuadrado

Aplicando $(A + B)^2 = A^2 + 2AB + B^2$:

$$\left(\frac{e^{iz} + e^{-iz}}{2}\right)^2 = \frac{e^{2iz} + 2 + e^{-2iz}}{4}$$

## Paso 4: Sumar ambos terminos

$$\text{sen}^2 z + \cos^2 z = \frac{2 - e^{2iz} - e^{-2iz}}{4} + \frac{e^{2iz} + 2 + e^{-2iz}}{4}$$

$$= \frac{(2 - e^{2iz} - e^{-2iz}) + (e^{2iz} + 2 + e^{-2iz})}{4}$$

Los terminos $-e^{2iz}$ con $+e^{2iz}$ se cancelan. Igual con $-e^{-2iz}$ y $+e^{-2iz}$:

$$= \frac{2 + 2}{4} = \frac{4}{4} = 1$$

## Conclusion

$$\boxed{\text{sen}^2 z + \cos^2 z = 1, \quad \forall z \in \mathbb{C}}$$

> [!success] Generalizacion
> La identidad pitagorica trigonometrica se mantiene **identica** en el plano complejo, aunque las funciones $\text{sen}\,z$ y $\cos z$ ya no estan acotadas (a diferencia del caso real, donde $|\text{sen}\,x| \le 1$). Esta es una propiedad notable de la generalizacion exponencial.
