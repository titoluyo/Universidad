---
title: "Analisis amplificador clase A en DC y AC"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 7
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-clase-a
  - tema/recta-de-carga
  - tema/punto-de-operacion
date: 2026-03-31
---

## Amplificador clase A

Un amplificador opera en clase A cuando el transistor trabaja **siempre en la region activa**. Esto implica que la corriente de colector fluye durante los **360°** del ciclo de alterna.

El disenador normalmente intenta colocar el punto Q en algun lugar proximo al **centro de la recta de carga**. De esta forma la senal puede oscilar en el maximo rango posible sin que el transistor llegue a la saturacion o el corte, lo cual distorsionaria la senal.

> [!important] Punto Q en gran senal vs pequena senal
> - **Pequena senal:** la posicion del punto Q no es critica
> - **Gran senal (potencia):** el punto Q **debe estar en el centro** de la recta de carga en AC para obtener maxima excursion de la senal de salida

## Amplificador de emisor comun

Circuito con divisor de voltaje ($R_1$, $R_2$), resistencia de colector $R_C$, resistencia de emisor $R_E$ con condensador de bypass $C_E$, condensadores de acoplo $C_S$ (entrada) y $C_O$ (salida), y carga $R_L$.

## Recta de carga DC

En analisis DC los condensadores se abren (circuito abierto). El circuito queda solo con $R_1$, $R_2$, $R_C$, $R_E$ y $V_{CC}$.

### Ecuacion de la recta de carga DC

$$V_{CC} = I_C R_C + I_E R_E + V_{CE}$$

Como $I_E \approx I_C$:

$$\boxed{V_{CC} = I_C(R_C + R_E) + V_{CE}}$$

**Punto de saturacion** ($V_{CE} = 0$):

$$I_{C(sat)} = \frac{V_{CC}}{R_C + R_E}$$

**Punto de corte** ($I_C = 0$):

$$V_{CE(corte)} = V_{CC}$$

La pendiente de la recta DC es $m_{DC} = -\dfrac{1}{R_C + R_E}$.

## Recta de carga AC

En analisis AC los condensadores se cortocircuitan y $V_{CC}$ se conecta a tierra. El circuito equivalente tiene $R_1 \parallel R_2$ en la entrada y $R_C \parallel R_L$ en la salida.

### Ecuacion de la recta de carga AC

$$v_{ce} + i_c R_{ac} = 0$$

Donde:

$$R_{ac} = R_C \parallel R_L = \frac{R_C \cdot R_L}{R_C + R_L}$$

Las variaciones de pequena senal se definen como:

$$i_c = \Delta I_C = I_C - I_{CQ}$$

$$v_{ce} = \Delta V_{CE} = V_{CE} - V_{CEQ}$$

Sustituyendo:

$$I_C - I_{CQ} = -\frac{V_{CE} - V_{CEQ}}{R_{ac}}$$

**Punto de saturacion AC** ($V_{CE} = 0$):

$$\boxed{i_{c(sat)} = I_{CQ} + \frac{V_{CEQ}}{R_{ac}}}$$

**Punto de corte AC** ($I_C = 0$):

$$\boxed{V_{CE(corte)} = V_{CEQ} + I_{CQ} \cdot R_{ac}}$$

> [!note] Diferencia entre rectas DC y AC
> La recta de carga AC tiene **mayor pendiente** que la DC porque $R_{ac} = R_C \parallel R_L < R_C + R_E$. Ambas rectas se cruzan en el punto Q.

### Grafica de la recta de carga AC

La recta de carga AC pasa por el punto Q con pendiente $-1/R_{ac}$. La senal de salida oscila a lo largo de esta recta. Para maxima excursion simetrica sin distorsion, el punto Q debe estar centrado en la recta AC.
