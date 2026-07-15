---
title: "Tema 02 - Regulación de velocidad de un motor de corriente continua"
curso: "[[Motores MOC]]"
unidad: 3
semana: 14
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/regulacion-de-velocidad
  - tema/motor-shunt
  - tema/motor-serie
  - tema/motor-compuesto
  - tema/curvas-caracteristicas
date: 2026-06-22
---

![[S14 - B1.png]]

Para deducir analíticamente la característica $n = f(T)$ de los motores DC se parte de las **tres ecuaciones fundamentales** (suponiendo trabajo en la zona lineal de la curva de magnetización):

$$T = K_T\,\phi\,I_i \qquad V = E + R_i\,I_i \qquad E = K_E\,n\,\phi$$

- $T$ = par (torque) desarrollado.
- $V$ = tensión en bornes; $E$ = f.c.e.m.; $I_i$ = corriente del inducido.
- $\phi$ = flujo inductor; $n$ = velocidad; $K_T$, $K_E$ = constantes de la máquina.

## Regulación de velocidad de un motor shunt (derivación)

Despejando $I_i$ de la ecuación del inducido y sustituyendo:

$$I_i = \frac{V - K_E\,n\,\phi}{R_i}$$

se obtiene la **velocidad en función del par**:

$$n = \frac{V - R_i\,I_i}{K_E\,\phi} = \frac{1}{K_E\,\phi}\,V - \frac{R_i}{K_E\,K_T\,\phi^2}\,T$$

Esta recta tiene **ordenada en el origen** (velocidad de vacío) $n_0 = \dfrac{V}{K_E\,\phi}$ y **pendiente** $-\dfrac{R_i}{K_E K_T \phi^2}$. La regulación en los motores de derivación e independiente se logra de **tres formas**:

### 1) Variación de la tensión aplicada al inducido

Al **reducir** la tensión $V$, baja $I_i$ y con ella el par; la velocidad cae cuando el par desarrollado se vuelve menor que el resistente. **Aumentar** $V$ eleva la velocidad. Como $n_0 = V/(K_E\phi)$ cambia proporcionalmente con $V$ pero la **pendiente no se altera** (flujo y $R_i$ constantes), se obtienen **rectas paralelas** a la característica natural. Quedan **por debajo** de la natural porque la tensión se reduce respecto a la máxima (para no dañar los aislamientos).

![[T02 - Figura 1. Variacion de la tension aplicada.png]]
> **Figura 1.** Variación de la tensión aplicada: rectas paralelas que se desplazan con $V$.

### 2) Variación de la resistencia en serie con el inducido

Al **añadir una resistencia** (reóstato) en el circuito del inducido, **aumenta la pendiente** de la característica par-velocidad. Todas las rectas —llamadas **características artificiales o reostáticas**— pasan por el mismo punto de **velocidad de vacío $n_0$**, que solo depende de $V$ y $\phi$. Es un método **poco económico** (grandes pérdidas Joule en el reóstato por la elevada corriente de inducido), por lo que se usa solo en motores de pequeña potencia.

![[T02 - Figura 2. Variacion de la resistencia del inducido.png]]
> **Figura 2.** Variación de la resistencia del inducido: mismo $n_0$, mayor pendiente.

### 3) Variación de la resistencia en serie con el inductor (flujo)

Al introducir una resistencia ($R_s$) en el circuito **inductor**, disminuyen la corriente de excitación y el **flujo $\phi$**. Esto reduce la f.c.e.m., lo que **aumenta** la corriente del inducido; el par $T = K_T \phi I_i$ se mantiene porque la caída de flujo se compensa con el aumento de $I_i$, y **la velocidad sube**. Reducir el flujo eleva la velocidad de vacío

$$n_0 = \frac{1}{K_E\,\phi}\,V$$

y aumenta la pendiente $-\dfrac{R_i}{K_E K_T \phi^2}$; las rectas quedan **por encima** de la característica natural.

![[T02 - Figura 3. Motores con excitacion independiente y derivacion.png]]
> **Figura 3.** Motores con excitación independiente y derivación: inserción del reóstato $R_s$ en el inductor.

![[T02 - Figura 4. Variacion del flujo inductor.png]]
> **Figura 4.** Variación del flujo inductor: rectas por encima de la característica natural.

## Regulación de velocidad de un motor serie

En el motor serie el flujo depende de la corriente del inducido ($I = I_i$) y, por tanto, **de la carga**. De las ecuaciones básicas:

$$T = K_T\,\phi\,I_i \qquad V = E + R_i\,I_i \qquad E = K_E\,n\,\phi$$

![[T02 - Figura 5. Motor serie DC.png]]
> **Figura 5.** Esquema de conexiones del motor serie DC.

Suponiendo que **no está saturado**, se cumple la proporcionalidad $\phi = K_I\,I_i$, de donde:

$$T = K_T\,K_I\,I_i^{2} \quad\Longrightarrow\quad I_i = \sqrt{\frac{T}{K_T\,K_I}}$$

Y la **velocidad en función del par** resulta:

$$n = \frac{V - R_i\,I_i}{K_E\,\phi} = \frac{V}{K_E\,K_I\,I_i} - \frac{R_i}{K_E\,K_I} = \frac{1}{K_E}\sqrt{\frac{K_T}{K_I}}\;\frac{V}{\sqrt{T}} - \frac{R_i}{K_E\,K_I}$$

La dependencia $n \propto 1/\sqrt{T}$ explica la característica **hiperbólica** del motor serie: a poca carga la velocidad **se dispara**. Por eso, para cargas inferiores al ~25 % de la nominal la velocidad puede alcanzar niveles peligrosos, y **no se recomienda arrancar el motor serie en vacío o con carga mínima**. A diferencia del shunt, el modo eficiente de cambiar su velocidad es **variar la tensión en bornes**: al aumentar $V$ crece el primer término de la ecuación, dando mayor velocidad para cualquier par.

![[T02 - Figura 6. Curva Par-Velocidad de motor serie.png]]
> **Figura 6.** Curva par-velocidad del motor serie (forma hiperbólica).

También puede insertarse un resistor en serie con el motor, pero con **gran desperdicio de potencia**; se usa solo de forma intermitente durante el arranque.

## Regulación de velocidad de un motor compuesto (compound)

Las técnicas disponibles para el motor compuesto **acumulativo** son las mismas del motor en derivación:

- Cambio en la **resistencia de campo** (que regula el flujo).
- Cambio en el **voltaje del inducido**.

Su característica mecánica se sitúa **entre** las del motor de derivación y la del serie.

![[T02 - Figura 7. Curva Par-Velocidad de motor compuesto.png]]
> **Figura 7.** Curva par-velocidad del motor compuesto (entre la del shunt y la del serie).

> [!summary] Idea central
> La velocidad del motor DC se despeja de $E = K_E n \phi$: $\;n = \dfrac{V - R_i I_i}{K_E\,\phi}$. De ahí los **tres mandos de regulación**: la **tensión $V$** (desplaza $n_0$, rectas paralelas), la **resistencia del inducido** (aumenta la pendiente, mismo $n_0$) y el **flujo $\phi$** (subir velocidad debilitando el campo). En el **serie**, $\phi$ depende de la carga y $n \propto 1/\sqrt{T}$ → no arrancar en vacío. El **compuesto** queda entre shunt y serie. Estas curvas son la base de los procedimientos de [[S14-1 Tema 01 - Arranque, frenado e inversión del sentido de giro en motores DC|arranque y frenado]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
