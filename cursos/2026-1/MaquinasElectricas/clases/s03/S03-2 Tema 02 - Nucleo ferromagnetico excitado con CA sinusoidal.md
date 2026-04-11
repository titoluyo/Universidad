---
title: Nucleo ferromagnetico excitado con CA sinusoidal
curso: "[[Motores MOC]]"
unidad: 1
semana: 3
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/nucleo-ferromagnetico
  - tema/corriente-alterna
  - tema/circuito-equivalente
  - tema/corriente-excitacion
  - tema/perdidas-hierro
date: 2026-04-11
---

## 1. Núcleo ferromagnético

El núcleo ferromagnético es un componente común en dispositivos electromagnéticos, como transformadores y bobinas. Está hecho de un material [[S02-3 Tema 02 - Caracteristicas para crear un campo magnetico#Ferromagnetismo|ferromagnético]] que exhibe propiedades magnéticas especiales.

Cuando una corriente eléctrica fluye a través de una bobina que tiene un núcleo ferromagnético, el campo magnético generado por la corriente induce la magnetización en el núcleo. Esto refuerza el campo magnético y aumenta la inductancia de la bobina. Además, cuando se interrumpe la corriente, el núcleo ferromagnético ayuda a reducir la disminución rápida del campo magnético, lo que es beneficioso en aplicaciones como transformadores, donde se busca un flujo magnético constante.

![[Figura 1. Núcleo ferromagnético.png]]
**Figura 1.** Núcleo ferromagnético

**Los núcleos ferromagnéticos se utilizan para mejorar la eficiencia y las propiedades magnéticas de los dispositivos electromagnéticos al aumentar la inductancia y controlar el flujo magnético.**

---

## 2. Corriente alterna sinusoidal

En una función sinusoidal, por ejemplo, $v(t) = V_m \cos(\omega t + \phi_u)$ que representa una diferencia de potencial, podemos distinguir los siguientes parámetros:

- **Pulsación ($\omega$)**

Son los radianes recorridos por unidad de tiempo. Puesto que un ciclo son $2\pi$ radianes, y el periodo es la duración de un ciclo, la pulsación será el cociente entre ambos: $\omega = 2\pi \cdot \frac{1}{T} = 2\pi f$. La unidad de tiempo es (radianes/s).

- **Frecuencia**

Número de ciclos de la función sinusoidal en una unidad de tiempo, en segundos. Es por tanto el inverso del período $f = \frac{1}{T}$. La unidad es el Hertz (Hz).

- **Fase ($\phi_u$)**

Es el ángulo que establece el valor inicial en $t = 0$ de la señal.

![[Figura 2. Corriente alterna sinusoidal.png]]
**Figura 2.** Corriente alterna sinusoidal

- **Amplitud**

Es el valor máximo al que llega la función sinusoidal. La unidad es el Voltio (V).

- **Período**

Es la duración en tiempo de un ciclo completo. La unidad del tiempo, segundos (s).

---

## 3. Circuito eléctrico equivalente de una bobina con núcleo de hierro alimentada con c.a.

Para facilitar los cálculos, se considera que el circuito magnético es lineal, lo que equivale a suponer que el sistema tiene una [[S02-3 Tema 02 - Caracteristicas para crear un campo magnetico#Permeabilidad magnética|permeabilidad]] constante. Para determinar los circuitos equivalentes de una bobina con núcleo de hierro es preciso considerar dos situaciones:

- Que el núcleo no tenga pérdidas en el hierro
- Que el núcleo tenga pérdidas

### A. Núcleo sin pérdidas

Si consideramos que el núcleo magnético no tiene pérdidas y suponemos también despreciable la resistencia de la bobina, en esta situación la potencia activa absorbida (por la bobina) de la red será nula. De acuerdo con la [[S01-2 Tema 01 - Los circuitos magnéticos|ley de Hopkinson]], se tendrá:

$$\phi = \frac{F}{\mathcal{R}} = \frac{N \cdot i}{\dfrac{l}{\mu \cdot S}} = \mu \cdot \frac{N \cdot i}{l} \cdot S$$

![[Figura 3.png]]
**Figura 3.** Bobina con núcleo de hierro (sin pérdidas)

Donde:
- $i$ → corriente de excitación instantánea que circula por el devanado
- $l$ → longitud magnética media
- $S$ → sección transversal del núcleo
- $\mu$ → la permeabilidad, que suponemos constante

Se puede escribir:

$$v = N \frac{d\phi}{dt} = \frac{\mu \cdot N^2 \cdot S}{l} \cdot \frac{di}{dt}$$

Comparando con la tensión en una bobina de coeficiente de autoinducción $L$, llevando una corriente $i$:

$$v = L \frac{di}{dt}$$

Por lo tanto, el circuito equivalente de una bobina con núcleo de hierro puede representarse por una autoinducción cuya magnitud se expresa por:

$$L = \frac{\mu \cdot N^2 \cdot S}{l}$$

![[Figura 4. Circuito equivalente de una bobina con núcleo de hierro sin pérdidas.png]]
**Figura 4.** Circuito equivalente de una bobina con núcleo de hierro sin pérdidas

### B. Núcleo con pérdidas

En el caso de que el núcleo tenga pérdidas en el hierro, la corriente de excitación $I_{exc}$ no formará 90° con la tensión, ya que la potencia activa absorbida de la red debe vencer esas pérdidas, de tal forma que si denominamos $\phi_v$ al ángulo que forman $V$ e $I_{exc}$ y $P_{Fe}$ a las pérdidas en el hierro, se cumplirá:

$$P_{Fe} = V \cdot I_{exc} \cdot \cos \phi_v$$

El diagrama fasorial del sistema, donde puede observarse que $I_{exc}$ tiene dos componentes, una $I_{Fe}$ llamada **componente de pérdidas en el hierro** y otra $I_\mu$ llamada **corriente magnetizante**, que vienen expresadas por:

$$a) \quad I_{Fe} = I_{exc} \cdot \cos \phi_v$$

$$b) \quad I_\mu = I_{exc} \cdot \text{sen} \, \phi_v$$

$$c) \quad \vec{I_{exc}} = \vec{I_{Fe}} + \vec{I_\mu}$$

Y el diagrama fasorial de la Figura 5, permite obtener el llamado circuito equivalente de una bobina con núcleo de hierro (Figura 6).

![[Figura 5..png]]
**Figura 5.** Diagrama fasorial

![[Figura 6. Circuito.png]]
**Figura 6.** Circuito equivalente de una bobina con núcleo de hierro

En el **nodo A** de este circuito vemos que se cumple la ecuación:

$$\vec{I_{exc}} = \vec{I_{Fe}} + \vec{I_\mu}$$

Los valores de $R_{Fe}$ y $X_\mu$ serán:

$$R_{Fe} = \frac{V}{I_{Fe}} \qquad X_\mu = \frac{V}{I_\mu}$$

Las pérdidas $R_{Fe} \cdot I_{Fe}^2$ indicarán las pérdidas en el núcleo del sistema magnético, mientras que la corriente $I_\mu$ expresa, al igual que en el caso del núcleo sin pérdidas, la corriente necesaria para magnetizar el material.

---

## 4. Corriente de excitación en una bobina con núcleo de hierro alimentada con c.a.

En la práctica, la curva de imanación de un material ferromagnético es no lineal y el punto de trabajo normal en las máquinas eléctricas está en el codo de la curva de magnetización del material, lo que ejerce gran influencia en la forma de la curva de la corriente de excitación, que va a dejar de ser sinusoidal y teniendo que recurrir para su determinación a soluciones gráficas por ser imposible utilizar técnicas analíticas.

### Núcleo sin pérdidas

La relación en este caso, entre el flujo $\phi$ y la corriente de excitación $i_{exc}$, se obtiene gráficamente de la curva de magnetización del material, donde en vez de emplear el eje de ordenadas para inducciones $B$, se utiliza la magnitud proporcional $\phi = B \cdot S$, y donde en el eje de abscisas se empleaba $H = N \cdot \frac{i_{exc}}{l}$, se emplea ahora $i_{exc}$.

![[Figura 7. Curvas de imanación de diversos materiales.png]]
**Figura 7.** Curvas de imanación de diversos materiales

En el siguiente gráfico (Figura 8) podemos ver la corriente de excitación en una bobina con núcleo de hierro.

![[Figura 8. Corriente de excitación en una bobina con núcleo de hierro alimentada con c.a..png]]
**Figura 8.** Corriente de excitación en una bobina con núcleo de hierro alimentada con c.a.

En la siguiente figura (9) se muestra la curva de magnetización del material $\phi = f(i_{exc})$:

![[Figura 8.png]]
**Figura 9.** Curva de magnetización $\phi = f(i_{exc})$

En esta figura (10) se observa la forma sinusoidal de la tensión aplicada y la del flujo retrasado 90° respecto a $V$.

![[Figura 9.png]]
**Figura 10.** Tensión aplicada y flujo retrasado 90°

![[Figura 10.png]]
**Figura 10b.** Correspondencia entre curva de flujo y corriente de excitación

Al punto **A** de la curva b) de flujo le corresponde el punto **A'** en la curva de corrientes en virtud de la correspondencia $\phi - i_{exc}$; al punto **B** de la curva de flujo le corresponde **B'** en la de corriente, y así sucesivamente hasta obtener la forma completa de la curva de la corriente de excitación del núcleo.

Se observa que la forma de $i_{exc}$ no es sinusoidal y por desarrollo en serie de Fourier puede demostrarse que aparecen **armónicos impares: 1, 3, 5, etc**. En la Figura 11 **a)** se muestra la curva acampanada de la corriente, que aparece como suma de una onda fundamental y un tercer armónico. En la Figura **b)** se muestra la curva $v(t)$ y la corriente $i_{exc}(t)$, que van desfasadas 90°.

![[Figura 11. Corriente de vacío y sus armónicos. Ondas de tensión y corriente.png]]
**Figura 11.** a) Corriente de vacío y sus armónicos. b) Ondas de tensión y corriente.

### Núcleo con pérdidas

Suponiendo que el núcleo solo tenga pérdidas por [[S02-4 Tema 03 - Lazo de histeresis|histéresis]], se obtiene la composición gráfica de la figura, donde se ha superpuesto la curva $i_{exc}$ con la del flujo para observar que aparte de la deformación de la curva de vacío de la corriente, esta va desfasada del flujo debido a las pérdidas del núcleo.

![[Figura 13.png]]
**Figura 12.** Composición gráfica con pérdidas por histéresis

![[Figura 12. Deformación de la corriente de excitación de una bobina con núcleo con pérdidas.png]]
**Figura 13.** Deformación de la corriente de excitación de una bobina con núcleo con pérdidas

Puede demostrarse que la existencia de las pérdidas por corrientes de Foucault hace que se ensanche más el ciclo de pérdidas obligando a un nuevo desfase de las curvas de $i_{exc} - \phi$, lo cual está en correspondencia con el diagrama vectorial de la figura.

---

## 5. Ejercicio: Núcleo ferromagnético y sus pérdidas

Considerar el núcleo magnético de la figura, donde la longitud de la trayectoria magnética media es de 50 cm y la sección del núcleo es de 10 $\text{cm}^2$. El número de espiras es 300 y la tensión eficaz aplicada es $\frac{150}{\sqrt{2}}$ V. La resistencia de la bobina se supone despreciable y la curva de magnetización del material responde a la expresión:

$$B = \frac{2{,}2 \times 10^{-2} H}{1 + 10^{-2} H} \qquad B: \text{Tesla}; \quad H: \text{A.v/m}$$

![[Figura 3.png]]
**Figura 14.** Bobina con núcleo de hierro

**A tomar en cuenta:** la frecuencia de la tensión es de 60 Hz y las pérdidas en el hierro con la tensión aplicada son de 20 W.

**Calcular:**

1. Las corrientes $I_{Fe}$, $I_\mu$, $I_{exc}$ y el ángulo de desfase $\phi_v$.
2. Parámetros $R_{Fe}$ y $X_\mu$ del circuito equivalente de la bobina.

### Resolución

**1.** El valor del flujo máximo es:

$$\phi_m = \frac{V}{4{,}44 \cdot f \cdot N} = \frac{\frac{150}{\sqrt{2}}}{4{,}44 \times 60 \times 300} = 1{,}99 \times 10^{-3} \, \text{Wb}$$

Que corresponde a una densidad de flujo $B_m$:

$$B_m = \frac{\phi_m}{S} = \frac{1{,}99 \times 10^{-3}}{10 \times 10^{-4}} = 1{,}99 \, \text{Teslas}$$

Con la curva de imanación del material, se obtiene:

$$B_m = 1{,}99 = \frac{2{,}2 \times 10^{-2} H_m}{1 + 10^{-2} H_m} \quad \longrightarrow \quad H_m = 947{,}6 \, \text{A.v/m}$$

Suponiendo que la curva de $H_m$ fuera sinusoidal, el valor eficaz de $H$ sería:

$$H = \frac{H_m}{\sqrt{2}} = \frac{947{,}9}{\sqrt{2}} = 670 \, \text{A.v/m}$$

Y como $H = \frac{N \cdot I_\mu}{l}$, quedaría:

$$I_\mu = \frac{H \cdot l}{N} = \frac{670 \times 0{,}5}{300} = 1{,}12 \, \text{A}$$

Por otra parte, las pérdidas en el hierro son de 20 W y se tiene:

$$20 = \frac{150}{\sqrt{2}} \cdot I_{exc} \cdot \cos \phi_v = \frac{150}{\sqrt{2}} \cdot I_{Fe} \quad \Longrightarrow \quad I_{Fe} = 0{,}19 \, \text{A}$$

De acuerdo con el diagrama fasorial se cumple:

$$I_{exc} = \sqrt{I_{Fe}^2 + I_\mu^2} = \sqrt{0{,}19^2 + 1{,}12^2} = 1{,}136 \, \text{A}$$

$$\cos \phi_v = \frac{I_{Fe}}{I_{exc}} = \frac{0{,}19}{1{,}136} = 0{,}167 \quad \Longrightarrow \quad \phi_v = 80{,}4°$$

![[Figura 5..png]]
**Figura 15.** Diagrama fasorial del ejercicio

**2.** Los valores de $R_{Fe}$ y $X_\mu$ pueden obtenerse de las ecuaciones:

$$R_{Fe} = \frac{V}{I_{Fe}} = \frac{\frac{150}{\sqrt{2}}}{0{,}19} = 558{,}24 \, \Omega$$

$$X_\mu = \frac{V}{I_\mu} = \frac{\frac{150}{\sqrt{2}}}{1{,}12} = 94{,}7 \, \Omega$$

---

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
