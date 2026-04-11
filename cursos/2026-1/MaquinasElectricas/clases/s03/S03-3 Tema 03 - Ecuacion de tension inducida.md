---
title: Ecuacion de tension inducida
curso: "[[Motores MOC]]"
unidad: 1
semana: 3
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/fem-inducida
  - tema/ley-de-faraday
  - tema/maquina-sincrona
  - tema/transformador
date: 2026-04-11
---

En los devanados de las máquinas eléctricas se inducen f.e.m.s. debidas a las variaciones del flujo enlazado por los arrollamientos. Estos cambios son el resultado de:

- La variación con el tiempo de la magnitud del flujo, lo que da lugar a la llamada **f.e.m. de pulsación o de acción transformadora: $e_p$**.
- Del movimiento del circuito inducido, respecto del flujo, resultando una **f.e.m. de rotación, velocidad o movimiento: $e_r$**.
- De la combinación de los dos casos anteriores, apareciendo las f.e.m.s. **$e_p$ y $e_r$**.

## Modelo de máquina eléctrica elemental

El cálculo de la f.e.m. se realiza en cada caso, aplicando la [[S01-3 Tema 02 - Las leyes del electromagnetismo|ley de Faraday]], y para analizar este problema de generación se va a considerar el prototipo de máquina eléctrica que se indica en la figura, constituido por un devanado inductor 1, y un arrollamiento inducido 2, que consiste en un bobinado de $N_2$ espiras concentradas de paso diametral. Ambos devanados están situados en el estator y en el rotor, respectivamente, girando a una velocidad $\Omega$ rad/s.

![[Figura 1. Máquina eléctrica elemental con dos devanados.png]]
**Figura 1.** Máquina eléctrica elemental con dos devanados

### Hipótesis

- El flujo inductor $\phi_1$ varía de forma sinusoidal con el tiempo; para ello se introduce en el estator una corriente alterna de frecuencia $f_1$ y pulsación $\omega_1$.
- El flujo inductor se distribuye de forma sinusoidal por la periferia del entrehierro.
- El eje del devanado del rotor tiene una posición respecto del eje de flujo del estator, definido por la expresión $\alpha = \Omega \cdot t$, es decir, en $t = 0$ se tiene $\alpha = 0$ (**α** es el número de grados geométricos, $\Omega$ es la velocidad angular mecánica en rad/s).
- El bobinado del inducido está en circuito abierto, para considerar únicamente el efecto de generación de **f.e.m.**; la frecuencia de la señal obtenida se denominará $f_2$, que corresponde a una pulsación $\omega_2$.

## Deducción de la f.e.m. inducida

Al aplicar la ley de Hopkinson se obtendrá una expresión para el flujo distribuido en el entrehierro similar a la de la **f.m.m.**, es decir:

$$\phi_1 = \phi_m \cos \omega t \cos p\alpha$$

Donde $\phi_m$ expresa el valor máximo de flujo.

En consecuencia, la **f.e.m.** inducida será:

$$e_2 = -N_2 \frac{d\phi}{dt} = N_2 \omega_1 \phi_m \, \text{sen} \, \omega_1 t \cos p\alpha + N_2 p\Omega \phi_m \cos \omega_1 t \, \text{sen} \, p\alpha$$

El primer término del segundo miembro corresponde a la f.e.m. debida a la **pulsación de flujo**, mientras que el segundo término corresponde a la f.e.m. debida a la **rotación del inducido**.

Se puede escribir de la siguiente manera:

$$e_2 = \frac{N_2 \omega_1 \phi_m}{2} [\text{sen}(\omega_1 + p\Omega)t + \text{sen}(\omega_1 - p\Omega)t] + \frac{N_2 p\Omega \phi_m}{2} [\text{sen}(\omega_1 + p\Omega)t - \text{sen}(\omega_1 - p\Omega)t]$$

Expresión que responde a la forma general:

$$e_2 = \frac{N_2 \phi_m}{2} [(\omega_1 + p\Omega) \, \text{sen}(\omega_1 + p\Omega)t + (\omega_1 - p\Omega) \, \text{sen}(\omega_1 - p\Omega)t]$$

La ecuación anterior indica que la **f.e.m.** inducida en el rotor, $e_2$, contiene pulsaciones de valor $\omega_2$ que responden a la expresión general:

$$\boxed{\omega_2 = \omega_1 \pm p\Omega}$$

Y teniendo en cuenta que:

$$\omega_1 = 2\pi f_1 ; \quad \omega_2 = 2\pi f_2 ; \quad \Omega = 2\pi \frac{n}{60}$$

La siguiente es una ecuación muy importante que relaciona las frecuencias de los circuitos inductor e inducido con la velocidad del rotor y el número de polos:

$$\boxed{f_2 = f_1 \pm \frac{n \cdot p}{60}}$$

Además, permite analizar los dos casos particulares siguientes:

---

## Caso 1: Inducido fijo. Flujo variable.

En este caso **Ω** = 0, ya que el devanado del rotor es estacionario, y de acuerdo con la f.e.m. resultante, debida a la pulsación del flujo, será:

$$e_2 = N_2 \omega_1 \phi_m \, \text{sen} \, \omega_1 t \cos p\alpha$$

Se observa que cuando $p\alpha = \frac{\pi}{2}$ la **f.e.m.** resultante es nula, lo cual puede comprobarse en la figura 1, ya que el rotor no abraza ningún flujo.

Cuando $p\alpha = 0$. El valor eficaz de la f.e.m. será:

$$E_2 = \frac{N_2 \omega_1 \phi_m}{\sqrt{2}}$$

Que da lugar a:

$$\boxed{E_2 = \frac{2\pi}{\sqrt{2}} N_2 f_1 \phi_m = 4{,}44 \cdot N_2 \cdot f_1 \cdot \phi_m}$$

> [!important] Expresión importante
> Esta expresión se empleará en el estudio de los **transformadores**.

---

## Caso 2: Inducido móvil. Flujo constante.

En este caso $\omega_1 = 0$, lo que indica que el devanado inductor está alimentado por una c.c.; de acuerdo con la expresión general, la f.e.m. resultante, debida al **movimiento** del inducido, será:

$$e_2 = N_2 p\Omega \phi_m \, \text{sen} \, p\alpha$$

Teniendo en cuenta que $\alpha = \Omega t$:

$$e_2 = N_2 p\Omega \phi_m \, \text{sen} \, p\Omega t$$

Que expresa una **f.e.m.** de valor eficaz:

$$E_2 = \frac{N_2 p\Omega \phi_m}{\sqrt{2}}$$

Y cuya pulsación vale:

$$\omega_2 = p\Omega \quad \Rightarrow \quad f_2 = \frac{n \cdot p}{60}$$

Las máquinas que responden a estas consideraciones se denominan **síncronas**, y deben su nombre a que, según la ecuación anterior, la frecuencia del inducido es proporcional a la velocidad del rotor (las máquinas de c.c. pertenecen también a esta clasificación, pero debido a la rectificación mecánica del colector de delgas, la expresión de la f.e.m. difiere de la expresada aquí).

La expresión $E_2 = \frac{N_2 p\Omega \phi_m}{\sqrt{2}}$ de la f.e.m. para las máquinas síncronas puede tomar otra forma si se tiene en cuenta que $\Omega = \frac{2\pi n}{60}$, resultando:

$$E_2 = \frac{2\pi}{\sqrt{2}} \cdot \frac{pn}{60} \cdot N_2 \cdot \phi_m = 4{,}44 \cdot \frac{pn}{60} \cdot N_2 \cdot \phi_m$$

Teniendo en cuenta la ecuación $f_2 = \frac{np}{60}$, resulta:

$$\boxed{E_2 = 4{,}44 \cdot N_2 \cdot f_2 \cdot \phi_m}$$

---

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
