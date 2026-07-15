---
title: Circuito equivalente aproximado del transformador trifásico (por fase) e índice horario
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-trifasico
  - tema/circuito-equivalente
  - tema/analisis-por-fase
  - tema/indice-horario
  - tema/grupo-conexion
date: 2026-05-22
---

> [!info] Fuente
> Esta nota desarrolla la **separata "Circuito equivalente de un transformador trifásico"** entregada por el docente — PDF embebido al final.

## Análisis por fase

En el análisis del **transformador trifásico** es necesario considerar **cada conjunto de devanados como si fuera un transformador monofásico independiente**. Esto implica expresar los ensayos, modelos equivalentes, etc., en términos de **valores de fase**.

Con este enfoque, se pueden aplicar las mismas técnicas de análisis utilizadas en el estudio de los [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|transformadores monofásicos]].

> [!tip] Cálculo de la relación de transformación
> La relación de transformación se calcula como el **cociente entre el número de espiras por fase** del devanado primario y el número de espiras por fase del devanado secundario, lo cual coincide con la **relación entre las f.e.m. por fase** entre el primario y el secundario:
>
> $$a = \frac{N_{\phi P}}{N_{\phi S}} = \frac{E_{\phi P}}{E_{\phi S}}$$

## Circuito equivalente por fase

El circuito equivalente del transformador trifásico es **el mismo del monofásico real**, aplicado a una sola fase:

```
        I₁     R_cc      X_cc                    I'₂
   o─────→────/\/\/\─────))(((───────────────→─────o +
                                                    │
                  ↓ I₀                              │
              ┌──┴──┐                               │
        V₁    │ I_Fe + I_µ │                       V'₂
              │     │      │                        │
              R_Fe  X_µ                             │
              │     │                               │
   o──────────┴─────┴───────────────────────────────o −
```

*Circuito equivalente en una fase (Fraile Mora, 2008).*

Como se vio en la [[S08-1 Tema 01 - Determinación de los parámetros del transformador|determinación de parámetros]] y en la [[S08-2 Tema 02 - Eficiencia y regulación del transformador real|eficiencia y regulación]], los parámetros son:

- $R_{cc} = R_1 + R'_2$ — resistencia equivalente de cortocircuito por fase
- $X_{cc} = X_1 + X'_2$ — reactancia equivalente de cortocircuito por fase
- $R_{Fe}$ — resistencia de pérdidas en el hierro por fase
- $X_\mu$ — reactancia magnetizante por fase

> Una vez resuelto el circuito por una fase, las **magnitudes de línea** se obtienen con los factores $\sqrt{3}$ apropiados según la conexión (Y / Δ).

## Índice horario (grupo de conexión)

El **índice horario** indica el **desfase angular** entre la tensión del primario y la del secundario, expresado como múltiplo de **30°** (el equivalente a una "hora" en un reloj de 12 posiciones).

Notación: **`Xy<n>`** donde:
- Primera letra: conexión primaria — **D** = Delta, **Y** = Estrella (mayúscula = alta tensión).
- Segunda letra: conexión secundaria — **d** = delta, **y** = estrella (minúscula = baja tensión).
- Número $n$: desfase = $n \times 30°$ (el primario "marca las 12", el secundario marca la hora $n$).

### Tipos comunes de acoplamiento

| Índice horario | Símbolo | Desfase | Conexión |
| -------------- | ------- | ------- | -------- |
| **0** (0°) | **Dd0** | 0° | Δ primario, Δ secundario, sin desfase |
| **0** (0°) | **Yy0** | 0° | Y primario, Y secundario, sin desfase |
| **5** (150°) | **Dy5** | 150° | Δ primario, Y secundario |
| **5** (150°) | **Yd5** | 150° | Y primario, Δ secundario |
| **6** (180°) | **Dd6** | 180° | Δ–Δ con inversión |
| **6** (180°) | **Yy6** | 180° | Y–Y con inversión |
| **11** (330°) | **Dy11** | 330° (= −30°) | Δ primario, Y secundario |
| **11** (330°) | **Yd11** | 330° (= −30°) | Y primario, Δ secundario |

**Donde:**
- **A.T.** = Alta Tensión
- **B.T.** = Baja Tensión

### Resumen visual de los 8 acoplamientos típicos

Las dos columnas muestran la conexión y el diagrama fasorial:

| 0° | 180° |
| -- | ---- |
| **Dd0** — ambos delta, alineados | **Dd6** — ambos delta, invertidos |
| **Yy0** — ambos estrella, alineados | **Yy6** — ambos estrella, invertidos |

| 150° | 330° (≡ −30°) |
| ---- | ------------- |
| **Dy5** — delta / estrella | **Dy11** — delta / estrella |
| **Yd5** — estrella / delta | **Yd11** — estrella / delta |

### Importancia del índice horario

> [!warning] Compatibilidad para puesta en paralelo
> Cuando se ponen **dos bancos de transformadores en paralelo** alimentando una misma carga, **deben tener el mismo índice horario**. De lo contrario, la diferencia de fase produce una **fuerte corriente circulante** entre los secundarios que puede dañar los devanados.
>
> Por eso, los fabricantes especifican el grupo de conexión (Dy11, Yd5, etc.) en la placa de características del transformador.

> [!tip] Las conexiones más comunes en distribución
> - **Dy5** y **Dy11** son las más usadas en transformadores de **distribución** (MT/BT) — la conexión en delta del primario maneja bien los armónicos triple, y la estrella del secundario permite **tomar neutro** para cargas monofásicas.
> - **Yy0** se usa en transformadores grandes de **subtransmisión** donde la conmutación entre tensiones nominales debe ser fácil.

## Separata original

![[s09-t02-separata-circuito-equivalente.pdf]]

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
