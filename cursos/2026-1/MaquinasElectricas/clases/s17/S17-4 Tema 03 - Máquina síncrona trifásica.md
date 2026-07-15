---
title: "Tema 03 - Máquina síncrona trifásica"
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/motor-sincrono
  - tema/circuito-equivalente
  - tema/diagrama-fasorial
  - tema/curva-par-velocidad
date: 2026-07-13
---

![[S17-T03-01-S17-B1.png]]

El motor síncrono se ilustra en la Figura 1 con **dos polos**. La corriente de campo $I_f$ crea un campo magnético **estacionario** $B_R$. Al estator de la máquina se le aplica un conjunto de voltajes trifásicos, que genera una corriente trifásica circulando por los devanados. La interacción entre el campo del rotor y el campo del estator produce el par inducido:

$$\tau_{ind} = k\,B_R \times B_S$$

- $\tau_{ind}$ = par inducido.
- $k$ = constante que depende de la construcción de la máquina.
- $B_R$ = campo magnético del rotor (estacionario, creado por $I_f$).
- $B_S$ = campo magnético del estator (giratorio, creado por la corriente trifásica).

![[S17-T03-02-Figura-1-Motor-sincrono-con-dos-polos.png]]
> **Figura 1.** Motor síncrono con dos polos.

## Circuito equivalente de un motor síncrono

El circuito equivalente de un motor síncrono es **idéntico al de un generador síncrono**, salvo que la dirección de referencia de la corriente de armadura $I_A$ está **invertida**. En la Figura 2 se presenta el circuito equivalente completo resultante, mientras que en la Figura 3 se detalla el circuito equivalente **por fase**.

![[S17-T03-03-Figura-2-Circuito-equivalente-completo-de-un.png]]
> **Figura 2.** Circuito equivalente completo de un motor síncrono trifásico.

![[S17-T03-04-Figura-3-Circuito-equivalente-por-fase.png]]
> **Figura 3.** Circuito equivalente por fase.

La inversión de la dirección de $I_A$ conlleva un cambio en la ecuación de la **ley de voltajes de Kirchhoff** del circuito equivalente. La nueva ecuación es:

$$V_\phi = E_A + jX_S I_A + R_A I_A \qquad\text{o}\qquad E_A = V_\phi - jX_S I_A - R_A I_A$$

- $V_\phi$ = tensión de fase aplicada en bornes.
- $E_A$ = tensión interna generada (f.c.e.m.).
- $I_A$ = corriente de armadura (referencia invertida respecto al generador).
- $X_S$ = reactancia síncrona; $R_A$ = resistencia del devanado de armadura.

### Motores síncronos desde la perspectiva del campo magnético

En la Figura 4a se ilustra la operación como **motor**. La razón por la cual la cantidad $jX_S I_A$ apunta de $V_\phi$ a $E_A$ en el **generador** y de $E_A$ a $V_\phi$ en el **motor** es que se invirtió la dirección de referencia de $I_A$ en la definición del circuito equivalente del motor. La diferencia fundamental entre la operación como motor y como generador de las máquinas síncronas se refleja tanto en el **diagrama de campo magnético** como en el **diagrama fasorial**.

![[S17-T03-05-Figura-4-a-Diagrama-fasorial-de-un-motor-sinc.png]]
> **Figura 4.** a) Diagrama fasorial de un motor síncrono. b) Diagrama del campo magnético correspondiente.

## Curva característica par-velocidad de los motores síncronos

Los motores síncronos alimentan cargas que son mayormente **dispositivos de velocidad constante** y suelen formar parte de sistemas de potencia más grandes, dando la impresión de que operan conectados a **buses infinitos**.

La velocidad de un motor síncrono **permanece constante sin importar la carga**. Esta velocidad de rotación fija está determinada por:

$$n_m = \frac{120\,f_e}{P}$$

- $n_m$ = velocidad mecánica de rotación.
- $f_e$ = frecuencia eléctrica del estator.
- $P$ = número de polos del motor.

La Figura 5 muestra la curva característica par-velocidad. La velocidad del motor permanece constante desde el vacío hasta alcanzar el par máximo que puede suministrar, llamado **par máximo**. Por lo tanto, la **regulación de velocidad del motor es del 0 %**. La ecuación del par es:

$$\tau_{ind} = k\,B_R\,B_{net}\,\operatorname{sen}\delta$$

o bien:

$$\tau_{ind} = \frac{3\,V_\phi\,E_A\,\operatorname{sen}\delta}{\omega_m\,X_S}$$

- $B_{net}$ = campo magnético neto de la máquina.
- $\delta$ = ángulo de par (ángulo entre $E_A$ y $V_\phi$).
- $\omega_m$ = velocidad angular mecánica.

El par máximo del motor se presenta cuando $\delta = 90°$ y está dado por:

$$\tau_{max} = k\,B_R\,B_{net}$$

o bien:

$$\tau_{max} = \frac{3\,V_\phi\,E_A}{\omega_m\,X_S}$$

![[S17-T03-06-Figura-5-Caracteristica-par-velocidad-de-un-m.png]]
> **Figura 5.** Característica par-velocidad de un motor síncrono.

> [!summary] Idea central
> El motor síncrono comparte el circuito equivalente del generador salvo por la **inversión de $I_A$**, lo que cambia la LVK a $E_A = V_\phi - jX_S I_A - R_A I_A$ y hace que $jX_S I_A$ apunte de $E_A$ a $V_\phi$ en el diagrama fasorial. Su velocidad queda **fijada por la red**, $n_m = 120 f_e / P$, de modo que la **regulación de velocidad es 0 %** hasta el par máximo $\tau_{max} = 3 V_\phi E_A / (\omega_m X_S)$, alcanzado en $\delta = 90°$. Conviene contrastar este comportamiento con el del [[S17-1 Tema 01 - Curvas características del motor asíncrono y regulación de velocidad|motor asíncrono]], cuya velocidad sí depende de la carga a través del deslizamiento, y con su propia [[S17-5 Tema 04 - Principio de funcionamiento como generador|operación como generador]].

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
