---
title: Caracteristicas para crear un campo magnetico
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/permeabilidad-magnetica
  - tema/entrehierro
  - tema/ferromagnetismo
  - tema/paramagnetismo
  - tema/diamagnetismo
date: 2026-04-11
---

Los materiales ferromagnéticos que forman los campos magnéticos tienen ciertas características. En esta ocasión, profundizaremos en dos que son muy importantes: la **permeabilidad magnética** y el **entrehierro**.

## Permeabilidad magnética

El concepto de permeabilidad surge debido a que en numerosos materiales (y en el vacío), se establece una relación directa entre los campos magnéticos $H$ y $B$, en cualquier lugar o momento. Esta relación implica que ambos campos son proporcionalmente equivalentes entre sí:

$$B = \mu \cdot H$$

En este contexto, el coeficiente de proporcionalidad ***μ*** representa la permeabilidad, la cual es variable según el material en cuestión. La permeabilidad del vacío, también llamada permeabilidad del espacio libre, se considera una constante física y se denota como $\mu_0$.

### Permeabilidad relativa y susceptibilidad magnética

La permeabilidad relativa, denotada por el símbolo $\mu_r$, es la relación entre la permeabilidad de un medio específico y la permeabilidad del vacío $\mu_0$:

$$\mu_r = \frac{\mu}{\mu_0}$$

Donde:
- $\mu_0 = 4\pi \cdot 10^{-7} \, \frac{\text{H}}{\text{m}}$ es la permeabilidad magnética del vacío.
- En términos de permeabilidad relativa, la susceptibilidad magnética es: $\chi_m = \mu_r - 1$.
- El número $\chi_m$ es una cantidad adimensional.

### Permeabilidad relativa comparación entre materiales

Para comparar entre sí los materiales, se entiende la permeabilidad magnética absoluta $(\mu)$ como el producto entre la permeabilidad magnética relativa $(\mu_r)$ y la permeabilidad magnética de vacío $(\mu_0)$:

$$\mu = \mu_r \cdot \mu_0$$

Los materiales se pueden clasificar según su permeabilidad magnética relativa en:

- **Ferromagnéticos**, cuyo valor de permeabilidad magnética relativa es muy superior a 1.
- **Paramagnéticos**, o no magnéticos, cuya permeabilidad relativa es aproximadamente 1 (se comportan como el vacío).
- **Diamagnéticos**, de permeabilidad magnética relativa inferior a 1.

![[Figura 1. Diamagnetismo, paramagnetismo y ferromagnetismo.png]]
**Figura 1.** Diamagnetismo, paramagnetismo y ferromagnetismo

#### Paramagnetismo

A diferencia de los ferromagnetos, los paramagnetos no conservan ninguna magnetización en ausencia de un campo magnético externo, ya que el movimiento térmico causa que los espines se orienten de manera aleatoria sin dicho campo. Por lo tanto, la magnetización total disminuirá a cero cuando se elimine el campo externo aplicado. Solo se produce una pequeña magnetización inducida debido a que solo una fracción mínima de los espines se alinea con el campo magnético. Esta fracción es proporcional a la intensidad del campo, lo que explica la relación lineal observada. En contraste, la atracción experimentada por los ferromagnetos es no lineal y significativamente más fuerte, lo que se evidencia fácilmente, por ejemplo, en los imanes de nevera.

#### Diamagnetismo

El diamagnetismo es una manifestación de magnetismo que se presenta únicamente cuando una sustancia está expuesta a un campo magnético externo. En términos generales, este fenómeno suele ser relativamente débil en la mayoría de los materiales, aunque los superconductores exhiben un efecto significativo.

#### Ferromagnetismo

Los materiales ferromagnéticos atraen el campo magnético hacia su interior. Son altamente permeables, pueden ser inducidos magnéticamente sin hacer mucho trabajo magnético sobre ellos, utilizando electroimanes. Es por esta razón que se utilizan materiales ferromagnéticos para crear imanes permanentes.

---

## Entrehierro

En los [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|circuitos magnéticos]] que se utilizan en la técnica existen los denominados **entrehierros**, que son tramos en los cuales el flujo magnético se establece en el aire.

En la figura 2 podemos ver un núcleo de material magnético el cual tiene un entrehierro. Experimentalmente puede demostrar que las líneas de inducción se expanden, como puede verse en la figura que sigue, para tres valores distintos de entrehierro *𝛿*.

![[Figura 2. Núcleo de material magnético.png]]
**Figura 2.** Núcleo de material magnético

Existen fórmulas empíricas para tener en cuenta la deformación del flujo en los entrehierros como es:

$$S_\delta = (a + \delta)(b + \delta)$$

![[Figura 3. Entrehierro.png]]
**Figura 3.** Entrehierro

Donde:
- $a$ y $b$ = lados de la sección del hierro
- $\delta$ = valor de la longitud del entrehierro

Como se podrá apreciar en el punto de problemas resueltos, el entrehierro es un factor desfavorable en un circuito magnético.

---

## Bibliografía

- Ferro, G. (2016). *Circuitos Magnéticos*. En *Electrotecnia*. Universidad Nacional de Mar del Plata. Recuperado de [enlace](http://www3.fi.mdp.edu.ar/dtoelectrica/files/electrotecnia/e_im_9_circuitos_magneticos.pdf)
- Cernicharo, J. (5 de enero de 2022). Diamagnetismo, paramagnetismo y ferromagnetismo. *SalonFermi*. [enlace](https://mundo-vivo.com/salonfermi/diamagnetico-paramagnetico-ferromagnetico/)
