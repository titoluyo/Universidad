---
title: Diagrama fasorial del transformador
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/diagrama-fasorial
  - tema/regulacion-tension
  - tema/factor-potencia
  - tema/transformador-real
date: 2026-05-11
---

> [!info] Fuente
> Esta nota desarrolla la **separata "Diagrama fasorial del transformador"** entregada por el docente — PDF embebido al final.

## ¿Para qué sirve el diagrama fasorial?

Es esencial entender las **pérdidas de voltaje internas** en un transformador para determinar su [[S08-2 Tema 02 - Eficiencia y regulación del transformador real#1. Regulación del transformador|regulación de voltaje]]. Para esto, se utiliza el **modelo simplificado** del transformador.

La manera más práctica de analizar cómo estas **impedancias y ángulos de fase** influyen en la regulación de voltaje del transformador es mediante la representación gráfica en un **diagrama fasorial**. Este diagrama ilustra visualmente los voltajes y corrientes fasoriales en el transformador.

> En todos los diagramas fasoriales se considera que el voltaje fasorial $\mathbf{V}_S$ se encuentra en una **fase angular de 0°** y se utiliza como **punto de referencia** para la comparación de todos los demás voltajes y corrientes.

## Modelo aproximado al lado secundario

El modelo aproximado (con la rama de excitación desplazada a la entrada del primario y reducida al secundario) tiene la siguiente forma:

```
        a·I_P     R_eqs       jX_eqs          I_s
   o─────→──────/\/\/\─────))(((──────→──o +
                                              │
   V_P/a   ⤓ R_Fe/a²   ⤓ jX_µ/a²            V_s
                                              │
   o─────────────────────────────────────o −

   R_eqs = R_p/a² + R_s        X_eqs = X_p/a² + X_s
```

*Imagen 1. Modelo aproximado del transformador al lado secundario.*

### Ecuación fundamental (2.ª ley de Kirchhoff)

Aplicando la ley de voltaje de Kirchhoff al circuito equivalente:

$$\boxed{\;\frac{\mathbf{V}_P}{a} = \mathbf{V}_S + R_{eq}\,\mathbf{I}_S + jX_{eq}\,\mathbf{I}_S\;}$$

El **diagrama fasorial** de un transformador es simplemente la **representación visual** de la ecuación anterior.

## Caso 1: Factor de potencia en retraso (carga inductiva)

```
                                          V_P/a
                                       ╱
                                  ╱
                             ╱   │ jX_eq I_S
                        ╱         │
                  ╱   V_S    R_eq I_S
        ╱  θ                
       I_S                       
```

*Imagen 2. Diagrama fasorial — factor de potencia en retraso.*

> [!summary] Caso inductivo
> $\dfrac{V_P}{a} > V_S$ para cargas en retraso → **la regulación de voltaje debe ser positiva**.
> 
> Se observa que el voltaje en el secundario es **menor** que el voltaje en el primario referido — la regulación es **positiva** y de magnitud importante.

## Caso 2: Factor de potencia unitario (carga resistiva)

```
                                      V_P/a
                                  ╱
                              ╱   │ jX_eq I_S
                          ╱       │
              ───────I_S──────  V_S   R_eq I_S
```

*Imagen 3. Diagrama fasorial — factor de potencia = 1.*

> [!summary] Caso resistivo
> $\dfrac{V_P}{a}$ sigue siendo mayor que $V_S$, pero la diferencia es **menor que en el caso inductivo**. La regulación es positiva pero más pequeña.

## Caso 3: Factor de potencia en adelanto (carga capacitiva)

```
                                              V_P/a
                                          ╱
                                      ╱   │ jX_eq I_S
                                  ╱       │
                 I_S                     R_eq I_S
        ─────────────────────────  V_S
```

*Imagen 4. Diagrama fasorial — factor de potencia en adelanto.*

> [!warning] Caso capacitivo — Regulación negativa
> Si la corriente secundaria está en **adelanto**, es posible que el **voltaje secundario sea incluso mayor que el voltaje primario referido**. Si esto ocurre, el transformador exhibirá una **regulación de voltaje negativa**.
> 
> Es decir: la tensión en el secundario **sube** por encima del valor nominal al cargar el transformador. Este efecto es análogo al **efecto Ferranti** en líneas de transmisión y debe controlarse para no dañar equipos sensibles a sobretensión.

## Resumen visual de los tres casos

| FP de la carga | $V_P/a$ vs $V_S$ | Regulación de voltaje |
| -------------- | ---------------- | --------------------- |
| Inductivo (retraso) | $V_P/a \gg V_S$ | **Positiva grande** |
| Resistivo ($\cos\theta = 1$) | $V_P/a > V_S$ | **Positiva moderada** |
| Capacitivo (adelanto) | $V_P/a \lessgtr V_S$ | **Pequeña o negativa** |

> [!tip] Conexión con el ejercicio
> El [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)|ejercicio de la semana]] ilustra exactamente estos tres casos numéricamente con un transformador de 15 kVA, 2 300/230 V: RV = 2,1 % / 1,28 % / ≈ −0,06 % para FP = 0,8 ind / 1 / 0,8 cap.

## Separata original

![[s08-t03-separata-diagrama-fasorial.pdf]]

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
