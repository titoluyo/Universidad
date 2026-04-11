---
title: Obtencion de la curva de magnetizacion
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 7
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/magnetizacion
  - tema/histeresis
  - tema/materiales-ferromagneticos
date: 2026-03-28
---

## 1. Propiedades magnéticas macroscópicas

Las propiedades magnéticas macroscópicas de un material lineal, homogéneo e isótropo se definen en función de la susceptibilidad magnética $\chi_m$, coeficiente adimensional que representa la proporcionalidad entre la magnetización o imanación $M$ y la intensidad de [[S01-1 Tema 01 - Como se produce un campo magnético|campo magnético]] $H$, según la ecuación:

$$
M = \chi_m H
$$

## 2. La relación entre inducción magnética y variables magnéticas

La inducción magnética B está relacionada con estas dos variables:

$$
B = \mu_0(H + M) = \mu_0 H (1 + \chi_m) = \mu_0 \mu_r H = \mu H
$$

Siendo $\mu$ la permeabilidad magnética del medio, $\mu_0$ la permeabilidad magnética del vacío y $\mu_r$ la permeabilidad relativa, donde:

$$
\mu_r = 1 + \chi_m
$$

Dependiendo del valor de $\chi_m$, los materiales pueden clasificarse en los siguientes grupos:

- Diamagnéticos: $\mu_r \leq 1$, $\chi_m \sim -10^{-5}$.
- Paramagnéticos: $\mu_r \geq 1$, $\chi_m \sim 10^{-3}$.
- Ferromagnéticos: $\mu_r \gg 1$, $\chi_m$ de valor elevado.

A tomar en cuenta:

- Los materiales diamagnéticos son aquellos que presentan una débil repulsión frente a un campo magnético aplicado externamente.
- Los materiales paramagnéticos no retienen ninguna magnetización en ausencia de un campo magnético aplicado externamente.
- Los materiales ferromagnéticos atraen el campo magnético hacia su interior y son altamente permeables.

## 3. Curva de imanación o magnetización en materiales ferromagnéticos

Los materiales ferromagnéticos exhiben magnetizaciones significativas incluso cuando se encuentran expuestos a campos magnéticos de baja intensidad, y son comúnmente utilizados en aplicaciones tecnológicas. En estos materiales, las fuertes interacciones entre los momentos magnéticos atómicos conducen a su alineación paralela en áreas conocidas como dominios magnéticos, incluso en situaciones donde no hay un campo magnético externo presente.

Si aplicamos una intensidad de campo magnético o excitación magnética H creciente a una muestra de material ferromagnético, y representamos la inducción B en función de H, obtenemos la llamada curva de imanación o magnetización del material (Figura 1).

![[Pasted image 20260328235810.png]]
Figura 1. Curva de Imanación o magnetización

En la Figura 1 vemos que se pueden distinguir tres partes claramente diferenciadas en la curva de imanación. Se observan: una primera zona reversible, en la cual, si eliminamos el campo H exterior, la densidad de flujo también desaparece; una segunda zona irreversible; y una última parte, que representa la zona de saturación, en la cual la permeabilidad relativa es unitaria. El valor de B que se produce en un material ferromagnético debido a una determinada excitación magnética H no es una función uniforme, sino que depende del material. Si introducimos una muestra de material ferromagnético en el interior de una bobina y hacemos variar H modificando la corriente que circula por la bobina, obtenemos la siguiente curva:

![[Pasted image 20260328235831.png]]
Figura 2. Curva de histéresis 

Con respecto a la Figura 2, cuando $H = 0$ en el punto 3, aún existe una cierta magnetización $B = B_r$ que recibe el nombre de inducción remanente y constituye el estado de magnetización permanente de la muestra. Cuando $B = 0$, en el punto 4, $H$ presenta un valor de $H_c$ que se denomina campo coercitivo, que es el campo opuesto que es necesario aplicar para desmagnetizar la muestra. Si se continúa disminuyendo $H$ hasta alcanzar $H = -H_{\max}$, punto 5, y después invertimos el sentido de cambio de $H$, se llega a formar una curva cerrada, que recibe el nombre de ciclo de histéresis.

## 4. Ciclo de histéresis, pérdidas por histéresis y aplicaciones

El ciclo de histéresis es una representación gráfica de los diferentes estados por los que pasa el material ferromagnético a lo largo del ciclo de trabajo. Si la intensidad de campo $H$ varía entre $\pm H_{\max}$, el material ferromagnético describe dentro del plano de estado $B$-$H$ una gráfica, de modo que los valores que se obtienen aumentando $H$ no coinciden con los obtenidos al hacer disminuir $H$. Si partimos de un punto situado en la curva de histéresis, por ejemplo, el punto 2, y volvemos a dicho punto recorriendo un ciclo, nos encontraremos en la situación inicial, pero se ha disipado una energía que es proporcional al área encerrada bajo la curva $B$-$H$. Esta energía perdida se denomina pérdidas por histéresis. A su vez, la temperatura del material aumenta durante este proceso.

Los materiales ferromagnéticos se usan en electroimanes, núcleos de transformadores, motores y generadores, en los que se desea tener un campo magnético tan grande como sea posible con una corriente determinada. Ya que la histéresis disipa energía, los materiales que se utilizan en estas aplicaciones deben tener un ciclo de histéresis tan estrecho como sea posible. En los imanes permanentes por lo regular es deseable un ciclo de histéresis amplio, con una magnetización de campo cero intensa, y la necesidad de un campo inverso también intenso para desmagnetizar (figura 3).

![[Pasted image 20260328235855.png]]
Figura 3. Ciclos de histéresis y su posible uso en distintas aplicaciones.

---

## Bibliografía

- Calderón, A. (2015). _Guía de laboratorio I. Histéresis en materiales magnéticos_. Universidad de El Salvador.
- Carballo, L., y Gómez, R. (2007). _Medición del ciclo de histéresis de un material ferromagnético_. Universidad Favaloro. Recuperado de [https://www.fisicarecreativa.com/informes/infor_em/HisteresisUF2007.pdf](https://www.fisicarecreativa.com/informes/infor_em/HisteresisUF2007.pdf)
- HyperPhysics. (s.f.). _Variations in Hysteresis Curves._ Georgia State University. Recuperado de [http://hyperphysics.phy-astr.gsu.edu/hbase/Solids/hyst.html#c4](http://hyperphysics.phy-astr.gsu.edu/hbase/Solids/hyst.html#c4)
