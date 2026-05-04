---
title: Pérdidas magnéticas en el núcleo
curso: "[[Motores MOC]]"
unidad: 1
semana: 5
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/perdidas-nucleo
  - tema/perdidas-histeresis
  - tema/corrientes-foucault
  - tema/ciclo-histeresis
date: 2026-04-26
---

![[s05-t01-banner.jpg]]

## Introducción

Cuando los campos magnéticos asociados con núcleos ferromagnéticos se reducen, parte de la energía almacenada se devuelve a la fuente. Sin embargo, una porción de esa energía almacenada se disipa irreversiblemente en forma de calor en el núcleo. Esta pérdida de energía se atribuye a dos causas principales:

- **Pérdidas por histéresis**, que son características del material y están relacionadas con los ciclos de magnetización y desmagnetización.
- **Pérdidas por corrientes parásitas o corrientes de Foucault**, que se originan por corrientes inducidas en el núcleo.

Además, existen pérdidas de energía en núcleos sometidos a ciclos de magnetización y desmagnetización periódicos mediante excitaciones repetitivas.

![[s05-t01-fig1-laminas-foucault.png]]
*Figura 1. Disposición en láminas del núcleo ayuda a reducir las corrientes de Foucault.*

## Pérdidas por histéresis

La variación en la amplitud del campo magnético oscila entre $+H_m$ y $-H_m$, lo que equivale a cambios en la inducción entre $+B_m$ y $-B_m$. Si consideramos en un principio que la inducción en el núcleo se mueve desde $-B_R$ (punto **a**) hasta $B_m$ (punto **c**) siguiendo el tramo de la curva **abc**, experimentaremos un aumento en la inducción en el núcleo. Esto se traduce en la absorción de energía por parte del campo magnético, la cual es almacenada durante esta fase del ciclo.

$$W_{ac} = vol \int_{-B_r}^{B_m} H \cdot dB = vol \cdot w_1$$

La integral $w_1$ de la expresión anterior representará el área de la superficie **abcdea** de la figura 2. Si se considera ahora que la inducción se reduce desde $B_m$ (punto **c**) hasta $B_r$ (punto **e**), siguiendo el tramo **ce** de la curva de histéresis, entonces resultará una energía devuelta a la fuente (red) durante esta parte del ciclo porque es negativa, y cuyo valor es:

$$W_{ce} = vol \int_{B_m}^{B_r} H \cdot dB = vol \cdot w_2$$

![[s05-t01-fig2-energia-abce.png]]
*Figura 2. Energía disipada en el camino abce del ciclo de histéresis.*

Si se expone al núcleo a un aumento de la inducción desde $-B_r$ hasta $B_m$, siguiendo la trayectoria **abc**, seguido por una disminución de la inducción entre $B_m$ y $B_r$, a lo largo de la ruta **ce**, la superficie resultante **abcea** en la figura 2 reflejará la cantidad de energía absorbida por el núcleo ferromagnético durante este ciclo de excitación cíclica. Esta energía no se devuelve a la red, sino que se disipa en el núcleo en forma de calor.

De acuerdo con lo anterior, se puede afirmar que si las fluctuaciones en el campo magnético ocurren en el rango de $\pm H_m$, lo que corresponde a variaciones en la inducción de $\pm B_m$, la cantidad total de energía disipada en forma de calor en el núcleo durante este ciclo completo, denotada como $W_H$, se calculará de la siguiente manera:

$$W_H = (vol) \oint H \cdot dB$$

En la aplicación práctica, resulta más útil referirse a la pérdida de energía por unidad de tiempo en el núcleo (la potencia disipada por histéresis). Si el número de ciclos completos de magnetización es $f$ (donde $f$ representa la frecuencia de la corriente suministrada a la bobina), entonces la potencia perdida se calculará de la siguiente manera:

$$P_H = f \cdot W_H = f (vol) \oint H \cdot dB = f (vol) \cdot (\text{área del ciclo})$$

La única dependencia radica en la amplitud de la inducción, la frecuencia de la fuente de energía (red) y las propiedades intrínsecas del material magnético (representadas por el área del ciclo).

### Fórmula empírica de Steinmetz

Experimentalmente, **C. P. Steinmetz** propuso en 1892 una fórmula empírica para definir el cálculo de la pérdida por histéresis, la cual indica:

$$P_H = k_H \cdot f \cdot (vol) \cdot B_m^{\alpha}$$

Donde:
- $k_H$ = coeficiente de Steinmetz
- $\alpha$ = exponente de Steinmetz
- Ambos dependen de la naturaleza del núcleo ferromagnético.
- El exponente $\alpha$ varía entre 1,5 y 2,5, siendo un valor frecuente $\alpha = 1{,}6$, mientras que $k_H$ varía, en el caso de acero al silicio, entre 100 y 200.

## Pérdidas por corrientes de Foucault

En el gráfico se muestra una bobina arrollada sobre un núcleo de hierro macizo, el cual, al ser alimentado con corriente alterna, se producirá un campo magnético alterno de inducción $B_z = B_z \cos \omega t$ que atravesará toda la masa de hierro en el sentido del eje Z.

Aparecerán en el material unas f.e.m.s. inducidas que darán lugar a unas corrientes parásitas que circularán por el material si este es conductor, llamadas **corrientes de Foucault**.

Estas corrientes pueden generar pérdidas y calentamiento de los núcleos.

Para prevenir estas pérdidas, el hierro empleado en los circuitos magnéticos suele estar laminado, en forma de chapas magnéticas de pequeño espesor, con capas externas aislantes para evitar la circulación de corriente de una chapa a otra.

![[s05-t01-fig3-areas-histeresis.png]]
*Figura 3. Áreas del ciclo de histéresis.*

![[s05-t01-fig4-nucleo-laminado.png]]
*Figura 4. Núcleo de hierro laminado.*

### Deducción de la potencia disipada

Si el campo es uniforme en la sección transversal de la chapa, el flujo que atraviesa la espira sombreada es:

$$\phi = 2 b y B_m \cos \omega t$$

Por la ley de Faraday:

$$e = 2 \omega b y B_m \, \text{sen} \, \omega t$$

El cual produce una corriente en la espira y se obtiene una resistencia de:

$$R = \frac{2b}{\sigma \cdot dy}$$

Donde:
- $\sigma$ = conductividad del material
- $y$ = espesor de la chapa magnética, varía entre $0$ y $\frac{a}{2}$

La potencia instantánea en la espira será:

$$dP_F = R \cdot i^2 = \frac{e^2}{R} = \frac{4 \omega^2 \cdot b^2 \cdot y^2 \cdot B_m^2 \cdot \sigma \cdot \text{sen}^2 \omega t \cdot dy}{2b}$$

Y su valor medio:

$$dP_F = \omega^2 \cdot b \cdot y^2 \cdot B_m^2 \cdot \sigma \cdot dy$$

Con una potencia disipada total:

$$P_F = \int_0^{a/2} \omega^2 B_m^2 b \sigma y^2 \, dy = \frac{\omega^2}{24} B_m^2 \cdot a^3 \cdot b \cdot \sigma$$

Y por unidad de volumen:

$$\frac{P_F}{vol} = \pi^2 f^2 B_m^2 a^2 \frac{\sigma}{6} = k_F \cdot f^2 \cdot B_m^2 \cdot a^2 \cdot \sigma$$

> [!info] Frecuencia y espesor de chapa
> Si hay frecuencia elevada, se deben utilizar chapas más delgadas.

### Pérdidas totales en el hierro

Por lo tanto, las pérdidas totales en el hierro son la suma de las pérdidas por histéresis y por corrientes de Foucault:

$$P_{Fe} = P_H + P_F = k_H \cdot f \cdot B_m^{\alpha} + k_F \cdot f^2 \cdot B_m^2 \cdot a^2 \cdot \sigma$$

El fabricante del material magnético suministra las curvas donde se muestran las pérdidas totales en función de **B**, a frecuencia constante.

![[s05-t01-fig5-curvas-perdidas-hierro.png]]
*Figura 5. Curvas de pérdidas en el hierro.*

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
