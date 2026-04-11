---
title: Lazo de histeresis
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/histeresis
  - tema/perdidas-magneticas
  - tema/steinmetz
  - tema/corrientes-parasitas
date: 2026-04-11
---

Cuando un material magnético se somete a un flujo magnético variable en el tiempo, hay un calentamiento que se debe a la **histéresis magnética** del material y a **corrientes parásitas o de Foucault** que circulan en él.

La histéresis magnética es un fenómeno que ocurre en algunos materiales magnéticos al exponerse a un campo magnético variable en el tiempo. Esta propiedad describe la tendencia de un material magnético a retener parte de su magnetización incluso después de que la intensidad del campo aplicado haya cambiado.

Si aplicamos una fuente de tensión variable en el tiempo (con forma sinusoidal) a la bobina en el [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|circuito magnético]] de la figura 1, la corriente que fluye a través de la bobina experimentará variaciones en el tiempo. Esto provoca la repetición del ciclo de histéresis para corriente continua, en el cual el valor se modifica mediante una resistencia variable y la polaridad de la fuente. La frecuencia de la fuente determinará la frecuencia con la que se repite este ciclo por unidad de tiempo.

![[Figura 1. Circuito magnético alimentado por tensión alterna senoidal .png]]
**Figura 1.** Circuito magnético alimentado por tensión alterna senoidal

## Deducción de la energía del ciclo de histéresis

Como la resistencia óhmica de la bobina es nula y todo el flujo magnético que origina se establece en el núcleo, la energía que la fuente suministra es la siguiente:

$$dE = e \cdot i \cdot dt = u \cdot i \cdot dt$$

La fuerza electromotriz inducida en la bobina está dada por la [[S01-3 Tema 02 - Las leyes del electromagnetismo|ley de Faraday]] y su valor es:

$$e = N \frac{d\phi}{dt} = u \qquad d\phi = S \cdot dB$$

Con lo que nos queda:

$$e = N \cdot S \frac{dB}{dt}$$

Reemplazando en la ecuación inicial:

$$dE = e \cdot i \cdot dt = N \cdot S \cdot I \cdot dB = S \cdot L_m \cdot H \cdot dB$$

![[Figura 2. Ciclo de histéresis.jpg]]
**Figura 2.** Ciclo de histéresis

## Interpretación energética

Esto nos indica que la energía proporcionada por la fuente es el resultado de multiplicar el volumen del circuito magnético $S \cdot L_m$ (producto de la sección transversal, representada por $S$, y la longitud magnética, representada por $L_m$) por el área comprendida entre la curva de magnetización y el eje vertical. Esta energía es absorbida por el núcleo cuando la intensidad del campo magnético está en aumento y se devuelve a la fuente cuando está disminuyendo, como se ilustra en la figura 2.

![[Figura 3. Sentido de la energía de acuerdo a la variación del campo magnético .png]]
**Figura 3.** Sentido de la energía de acuerdo a la variación del campo magnético

Se puede observar que el área delimitada por el ciclo de histéresis es directamente proporcional a la energía acumulada en el núcleo por unidad de volumen y por cada ciclo. Cuando el material se ve forzado a completar "$f$" ciclos de histéresis por segundo, la energía por unidad de tiempo se convierte en la potencia disipada en forma de calor.

## Fórmula de Steinmetz — Pérdidas por histéresis

Las pérdidas de la potencia mencionada anteriormente están relacionadas con la frecuencia de la corriente excitadora, el volumen del material magnético y el área del ciclo de histéresis, considerando el valor máximo alcanzado por la inducción magnética. Las pérdidas magnéticas por histéresis se calculan mediante la **fórmula empírica de Steinmetz**, cuyo valor es el siguiente:

$$P_H = K_H \cdot f \cdot B^{n}_{\max} \quad \left[\frac{\text{W}}{\text{kg}}\right]$$

El valor de la constante $K_H$ depende del tipo de chapa magnética, y el valor de "$n$" está comprendido entre 1,7 y 2,3 pudiendo adoptarse un valor igual a 2. Así, a los efectos prácticos podemos utilizar la siguiente expresión:

$$P_H = K_H \cdot f \cdot B^{2}_{\max} \quad \left[\frac{\text{W}}{\text{kg}}\right]$$

Donde:
- $P_H$ = pérdidas por histéresis $[\text{W/kg}]$
- $K_H$ = constante que depende del tipo de chapa magnética
- $f$ = frecuencia de la corriente excitadora $[\text{Hz}]$
- $B_{\max}$ = valor máximo de la inducción magnética $[\text{T}]$
- $n$ = exponente entre 1,7 y 2,3 (se adopta $n = 2$ en la práctica)

## Reducción de pérdidas

Para poder disminuir las pérdidas, se debe buscar chapas magnéticas cuyo ciclo de histéresis sea lo más delgado posible. Esto se logra con cierto tipo de aleaciones con silicio y orientando el grano del material mediante un proceso adecuado.

---

## Bibliografía

- Álvarez (2007). *Circuitos magnéticos*. [enlace](https://elprofesorvirtual.com.ar/wp-content/uploads/2017/03/CircuitosMagneticos1.pdf)
