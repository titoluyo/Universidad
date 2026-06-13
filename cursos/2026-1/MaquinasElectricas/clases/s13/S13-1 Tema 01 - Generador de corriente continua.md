---
title: "Tema 01 - Generador de corriente continua"
curso: "[[Motores MOC]]"
unidad: 3
semana: 13
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/generador-dc
  - tema/dinamo
  - tema/balance-de-potencias
  - tema/tipos-de-excitacion
date: 2026-06-15
---

![[S13 - B1.png]]

## El generador de corriente continua (dinamo)

Los **generadores de corriente continua** (c.c.), también conocidos como **dinamos**, transforman la **energía mecánica en energía eléctrica** en forma de corriente continua. Han sido reemplazados en gran medida por **rectificadores de silicio**, que convierten c.a. en c.c. de manera estática y más eficiente.

Desde el punto de vista del circuito, las máquinas de c.c. tienen un **inductor** en el estátor y un **inducido giratorio** con colector de delgas. El inductor, alimentado con c.c., produce un campo magnético que induce una **fuerza electromotriz $E$** en el inducido. Al conectar una carga, circula una corriente $I_i$ que provoca una caída de tensión en el inducido (resistencia total del inducido $R_i$, que incluye el devanado y los contactos escobillas-colector). Aplicando el **segundo lema de Kirchhoff** al circuito del inducido:

$$E = V + R_i\,I_i + V_{esc}$$

Donde $V$ es la tensión terminal en bornes y $V_{esc}$ la caída de tensión en las dos escobillas. (Si la máquina tiene polos auxiliares para anular la reacción del inducido, sus resistencias se incluyen en $R_i$ por estar en serie con el inducido.)

![[T01 - Figura 1. Generador de cc o dinamo.png]]
> **Figura 1.** Generador de c.c. o dinamo: circuito inductor (excitación) e inducido con su f.e.m. $E$ y resistencia $R_i$.

## Balance de potencias

De la figura 1 se tienen las ecuaciones de circuito:

- **Inductor:** $\;V_e = R_e\,I_e$
- **Inducido:** $\;E = V + R_i\,I_i + V_{esc}$

Multiplicando la ecuación del inducido por $I_i$:

$$E\,I_i = V\,I_i + R_i\,I_i^2 + V_{esc}\,I_i$$

Cuyos términos representan:

| Término | Significado |
| --- | --- |
| $P_2 = V\,I_i$ | Potencia eléctrica de salida suministrada por el generador |
| $P_{cui} = R_i\,I_i^2$ | Pérdidas en el cobre del inducido |
| $P_{esc} = V_{esc}\,I_i$ | Pérdidas en los contactos de las escobillas |
| $P_a = E\,I_i$ | Potencia electromagnética desarrollada por la máquina |

El **balance de potencias en el inducido**:

$$P_a = P_2 + P_{cui} + P_{esc}$$

Para la **potencia mecánica de entrada** $P_1$ hay que sumar a $P_a$ las demás pérdidas:

- Pérdidas en el cobre del arrollamiento de excitación: $\;P_{exc} = V_e\,I_e = R_e\,I_e^2$
- Pérdidas mecánicas $P_m$ (rozamiento y ventilación).
- Pérdidas en el hierro $P_{Fe}$ (en el apilamiento del rotor, por magnetización cíclica al girar).

$$P_1 = P_{exc} + P_m + P_{Fe} + P_a$$

![[T01 - Figura 2. Balance de potencias en el generador de cc.png]]
> **Figura 2.** Balance de potencias en el generador de c.c.: de la potencia mecánica de entrada $P_1$ se descuentan las pérdidas hasta la potencia eléctrica de salida $P_2$.

## Tipos de generadores de corriente continua

La forma de conexión entre los devanados **inductor** e **inducido** determina el comportamiento de la máquina:

### Máquinas con excitación independiente

El devanado inductor está **separado** del inducido y es alimentado por una **fuente externa** (p. ej. una batería).

![[T01 - Figura 3. Excitacion independiente.png]]
> **Figura 3.** Excitación independiente.

### Máquinas autoexcitadas

El inductor se alimenta de la **propia corriente** de la máquina. Se subdividen en:

**Serie** — el inductor está **en serie** con el inducido; devanado de **pocas espiras de hilo grueso** (lleva la corriente total).

![[T01 - Figura 4. Excitacion serie.png]]
> **Figura 4.** Excitación serie.

**Derivación o shunt** — el inductor se conecta **en paralelo** con el inducido; devanado de **muchas espiras de hilo delgado**.

![[T01 - Figura 5. Excitacion shunt.png]]
> **Figura 5.** Excitación shunt (derivación).

**Compuesta (compound)** — la excitación se divide entre un devanado **en serie** (pocas espiras, hilo grueso) y otro **en paralelo** (muchas espiras, hilo delgado). Según dónde se conecte la derivación se obtienen máquinas de **corta** o **larga derivación**.

![[T01 - Figura 6. Excitacion compuesta (compound).png]]
> **Figura 6.** Excitación compuesta (compound).

> [!summary] Idea central
> En el generador, $E = V + R_i I_i + V_{esc}$: la f.e.m. inducida se reparte entre la tensión de salida y las caídas internas. El **balance de potencias** $P_1 = P_a + P_{exc} + P_m + P_{Fe}$ describe la conversión mecánica→eléctrica. Los **tipos de excitación** (independiente, serie, shunt, compuesta) son los mismos que definen las [[S13-2 Tema 02 - El motor de corriente continua|curvas características del motor]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
