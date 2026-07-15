---
title: "Tema 02 - El motor de corriente continua (curvas características)"
curso: "[[Motores MOC]]"
unidad: 3
semana: 13
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/motor-dc
  - tema/curvas-caracteristicas
  - tema/motor-serie
  - tema/motor-shunt
  - tema/motor-compuesto
  - tema/regulacion-de-velocidad
date: 2026-06-15
---

> [!info] Material original
> Manual del docente: [s13-manual-motor-dc.pdf](attachments/s13-manual-motor-dc.pdf) (UTP, Semana 13).

## El motor de corriente continua

Un motor de c.c. convierte **energía eléctrica en energía mecánica**. Por el **principio de reciprocidad** (Faraday-Lenz), la misma máquina puede funcionar como **generador** o como **motor**. Al absorber la corriente $I_i$ de la red, aplicando el segundo lema de Kirchhoff al inducido:

$$V = E + R_i\,I_i + V_{esc}$$

donde $E$ es la **fuerza contraelectromotriz** (f.c.e.m.): cuando $E$ supera la tensión $V$, la corriente se invierte y la máquina pasa a operar como **generador**.

### Balance de potencias

Multiplicando por $I_i$:

$$V\,I_i = E\,I_i + R_i\,I_i^2 + V_{esc}\,I_i$$

| Término | Significado |
| --- | --- |
| $P_i = V\,I_i$ | Potencia eléctrica absorbida por el inducido |
| $P_{esc} = V_{esc}\,I_i$ | Pérdidas en los contactos de las escobillas |
| $P_{cui} = R_i\,I_i^2$ | Pérdidas en el cobre del inducido |
| $P_a = E\,I_i$ | Potencia electromagnética desarrollada |

$$P_i = P_a + P_{cui} + P_{esc}$$

El **par interno** desarrollado por la máquina:

$$T = \frac{E\,I_i}{2\pi\frac{n}{60}} = K_T\,\phi\,I_i$$

La **potencia útil** en el árbol $P_2$ resulta de restar a $P_a$ las pérdidas en el hierro $P_{Fe}$ y mecánicas $P_m$; el **rendimiento** es $\eta = P_2/P_1$.

## Regulación de velocidad

Partiendo de $V = E + R_i\,I_i$ y de la expresión de la f.e.m.:

$$E = \frac{n}{60}\,Z\,\phi\,\frac{p}{c} = K_E\,n\,\phi$$

se despeja la **velocidad**:

$$\boxed{n = \frac{V - R_i\,I_i}{K_E\,\phi}}$$

La velocidad de un motor DC puede regularse controlando tres variables:

- **a) El flujo por polo (corriente de excitación):** disminuir el flujo **aumenta** la velocidad. ⚠️ Arrancar sin excitación puede provocar el **embalamiento** del motor.
- **b) La tensión de alimentación $V$:** reducir/aumentar $V$ disminuye/aumenta la velocidad.
- **c) La resistencia del circuito del inducido:** un reóstato en serie con el inducido permite controlar la velocidad (aumentar $R$ → disminuye la velocidad). *Poco práctico por las pérdidas que genera.*

## Curvas características $n = f(T)$

### Motor con excitación independiente y derivación (shunt)

Con la curva de magnetización en zona lineal ($\phi$ constante, fijado por la excitación):

$$T = K_T\,\phi\,I_i \quad;\quad V = E + R_i\,I_i \quad;\quad E = K_E\,n\,\phi$$

$$I = \frac{V - K_E\,n\,\phi}{R_i} \quad\Longrightarrow\quad n = \frac{V - R_i\,I_i}{K_E\,\phi} = \frac{1}{K_E\,\phi}\,V - \frac{R_i}{K_E\,K_T\,\phi^2}\,T$$

La curva $n$–$T$ es una **recta** ligeramente descendente → **característica natural** de la máquina. Al aumentar el par resistente, baja un poco la f.c.e.m., sube la corriente y el par se iguala con la carga: la velocidad es **casi constante**.

![[T02 - Figura 5. Caracteristica n-T motor derivacion.png]]
> **Figura 5.** Característica par/velocidad de motores con excitación independiente y derivación: recta de pendiente suave ($n_0 = V/(K_E\phi)$ en vacío).

> [!note] Aplicaciones del motor derivación
> Velocidad casi constante e independiente de la carga → ventiladores, bombas centrífugas, cintas transportadoras, máquinas herramienta.

### Motor con excitación serie

El **flujo depende de la corriente del inducido** ($I = I_i$), por lo que depende de la carga. Sin saturación, $\phi = K_I\,I_i$:

$$T = K_T\,K_I\,I_i^2 \quad\Longrightarrow\quad I_i = \sqrt{\frac{T}{K_T\,K_I}}$$

$$n = \frac{V - R_i\,I_i}{K_E\,\phi} = a\,\frac{V}{\sqrt{T}} - b \;\approx\; a\,\frac{V}{\sqrt{T}} \quad\Longrightarrow\quad \boxed{n^2\,T = a\,V = \text{constante}}$$

con $a = \dfrac{1}{K_E}\sqrt{\dfrac{K_T}{K_I}}$ y $b = \dfrac{R_i}{K_E\,K_I}$.

La curva $n$–$T$ es una **hipérbola**: el **par de arranque es muy elevado**, pero ⚠️ **en vacío la velocidad tiende a infinito** (embalamiento). En saturación, al duplicar el par la corriente sube ~140 % y la velocidad cae a ~70 % del valor inicial.

![[T02 - Figura 7. Curva n-T motor serie.png]]
> **Figura 7.** Curva par/velocidad de un motor serie: hiperbólica, con par de arranque muy alto y embalamiento en vacío.

> [!note] Aplicaciones del motor serie
> Alto par de arranque y velocidad muy variable con la carga → tracción eléctrica (trenes, tranvías), grúas, donde se necesitan **altas pares con arranque de carga pesada**. **No** se debe arrancar en vacío.

![[T02 - Figura 6. Motor con excitacion serie (esquema).png]]
> **Figura 6.** Esquema del motor con excitación en serie (inductor de pocas espiras en serie con el inducido).

### Motor con excitación compuesta

Combina un devanado **en derivación** (flujo casi constante) y otro **en serie** (flujo que aumenta con la carga). Su característica mecánica es **intermedia** entre la del motor derivación y la del serie.

![[T02 - Figura 8. Motor con excitacion compuesta (esquema).png]]
> **Figura 8.** Esquema del motor con excitación compuesta (devanados serie + derivación).

![[T02 - Figura 9. Curva par-velocidad de los motores DC.png]]
> **Figura 9.** Comparación de las curvas par-velocidad: **Paralelo (shunt)** casi horizontal, **Serie** hiperbólica, **Compuesto** intermedia.

> [!summary] Comparación de los tres motores
> | Motor | Curva $n$–$T$ | Velocidad con carga | Par de arranque | Aplicación típica |
> | --- | --- | --- | --- | --- |
> | **Derivación (shunt)** | recta plana | casi constante | moderado | ventiladores, bombas |
> | **Serie** | hipérbola | muy variable | **muy alto** | tracción, grúas |
> | **Compuesto** | intermedia | intermedia | alto | compromiso par/velocidad |
>
> Verifica estas tendencias en los ejercicios resueltos: [[S13-3 Ejercicio resuelto - Motor con excitación serie (Video)|serie]], [[S13-4 Ejercicio resuelto - Motor con excitación shunt (Video)|shunt]] y [[S13-5 Ejercicio resuelto - Motor con excitación compuesta (Video)|compuesto]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
