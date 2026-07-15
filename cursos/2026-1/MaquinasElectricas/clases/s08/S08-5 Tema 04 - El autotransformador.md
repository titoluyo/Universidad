---
title: El autotransformador
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 5
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/autotransformador
  - tema/devanado-comun
  - tema/devanado-serie
  - tema/elevador-reductor
date: 2026-05-15
---

![[s08-t04-banner.png]]

## ¿Cuándo se usa un autotransformador?

En algunas situaciones, puede ser necesario **ajustar los niveles de voltaje en una pequeña cantidad**. Estos incrementos pequeños pueden ser necesarios debido a una **caída de voltaje en un sistema de potencia** que está distante de los generadores.

En tales casos, sería **ineficiente y costoso** fabricar un transformador con dos devanados completos diseñados para voltajes casi idénticos. En su lugar, se recurre a un tipo especial de transformador llamado **autotransformador**.

> [!info] Diferencia con el transformador convencional
> Mientras que un [[S06-4 Tema 02 - El transformador monofásico ideal|transformador convencional]] tiene **dos devanados eléctricamente aislados**, el autotransformador tiene **un único devanado** dividido en dos secciones: hay **conexión galvánica** entre primario y secundario. Esto elimina el aislamiento entre los dos lados pero **reduce drásticamente el tamaño y costo** del equipo cuando la relación $V_H/V_L$ está cerca de 1.

## Devanado común y devanado en serie

- **Devanado común** ($N_C$): su voltaje **aparece en ambos lados** del transformador.
- **Devanado en serie** ($N_{SE}$): es el **más pequeño**, conectado en serie con el devanado común.

![[s08-t04-fig1-autotransformador-elevador.png]]
*Figura 1. Autotransformador elevador.*

## Autotransformador reductor

![[s08-t04-fig2-autotransformador-reductor.png]]
*Figura 2. Autotransformador reductor.*

En esta configuración:
- El **voltaje de entrada** es la **suma** de los voltajes en el devanado en serie y en el devanado común.
- El **voltaje de salida** es solo el voltaje en el **devanado común**.

## Ecuaciones del autotransformador

### Voltajes y corrientes en las bobinas (relación de espiras)

Como ambos devanados comparten el mismo flujo magnético, se cumple la relación clásica:

$$\boxed{\;\frac{V_C}{V_{SE}} = \frac{N_C}{N_{SE}} \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} N_C \, I_C = N_{SE} \, I_{SE}\;}$$

**Donde:**
- $V_C$, $V_{SE}$ — voltajes en los devanados común y en serie (V).
- $N_C$, $N_{SE}$ — número de espiras de cada devanado.
- $I_C$, $I_{SE}$ — corrientes en los devanados común y en serie (A).

### Voltajes terminales

Los voltajes en las bobinas están relacionados con los voltajes en los terminales mediante:

$$V_L = V_C \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} V_H = V_C + V_{SE}$$

**Donde:**
- $V_L$ — voltaje en el **lado de baja** (low) tensión del autotransformador.
- $V_H$ — voltaje en el **lado de alta** (high) tensión.

### Corrientes terminales

Las corrientes en las bobinas están relacionadas con las corrientes en los terminales mediante:

$$I_L = I_C + I_{SE} \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} I_H = I_{SE}$$

**Donde:**
- $I_L$ — corriente en el lado de baja tensión.
- $I_H$ — corriente en el lado de alta tensión.

> [!summary] Síntesis de las relaciones
> | Lado | Voltaje | Corriente |
> | ---- | ------- | --------- |
> | Baja (L) | $V_L = V_C$ | $I_L = I_C + I_{SE}$ |
> | Alta (H) | $V_H = V_C + V_{SE}$ | $I_H = I_{SE}$ |

> [!tip] Ventaja del autotransformador
> Una parte de la potencia se transfiere **por conducción eléctrica directa** entre primario y secundario (no por acoplamiento magnético). Esto permite que el devanado en serie maneje solo una **fracción** de la potencia total aparente — el resto se transfiere a través de la conexión común sin pasar por el núcleo.
> 
> Por eso, **un autotransformador es mucho más compacto y económico** que un transformador convencional de la misma potencia nominal, **siempre que la relación de transformación esté cerca de 1**.

> [!warning] Desventajas
> - **No hay aislamiento galvánico**: una falla en el devanado puede transmitir directamente la alta tensión al lado de baja.
> - Para relaciones muy distintas de 1 (p. ej. 10:1), el ahorro de cobre desaparece y deja de ser ventajoso frente al transformador convencional.

## Aplicaciones típicas

- **Compensación de caída de tensión** en líneas largas.
- **Arrancadores suaves** de motores trifásicos (reducen la tensión durante el arranque).
- **Reguladores de tensión** automáticos.
- **Conexión entre sistemas** con tensiones próximas (p. ej. 220/110 V doméstico).

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
