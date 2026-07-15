---
title: Eficiencia y regulación del transformador real
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/regulacion-tension
  - tema/eficiencia-transformador
  - tema/perdidas-cobre
  - tema/perdidas-hierro
date: 2026-05-11
---

![[s08-t02-banner.png]]

## 1. Regulación del transformador

Dado que los transformadores reales contienen **impedancias en serie**, el voltaje de salida puede variar con la carga, incluso si el voltaje de entrada permanece constante. Para facilitar la comparación entre transformadores en este aspecto, se define una medida llamada **regulación de voltaje** (RV).

La regulación de voltaje **a plena carga** compara el voltaje de salida en vacío con el voltaje de salida a plena carga:

$$\boxed{\;RV = \frac{\dfrac{V_P}{a} - V_S}{V_S} \cdot 100\,\%\;}$$

**Donde:**
- $V_P$ es el voltaje nominal del primario.
- $V_S$ es el voltaje nominal del secundario (a plena carga).
- $a$ es la [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real#Relaciones entre las magnitudes secundarias|relación de transformación]].

> [!tip] Lectura física
> $V_P/a$ es lo que entregaría el secundario si **no hubiera caída de tensión interna** (transformador ideal); $V_S$ es lo que entrega realmente a plena carga. La diferencia entre ambos, normalizada, mide cuánto "se hunde" la tensión al cargar el transformador.

### Valor objetivo

Generalmente se busca tener una **regulación de voltaje lo más baja posible**:
- En un transformador **ideal**, la regulación de voltaje sería del **0 %**.
- Sin embargo, **no siempre es conveniente tener una baja RV**: a veces los transformadores con alta impedancia y alta regulación se utilizan de manera intencional para **limitar las fluctuaciones de corriente** en un circuito (p. ej. transformadores soldadores, transformadores de protección contra fallas).

> [!note] Conexión con la semana anterior
> La RV se relaciona directamente con la [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real#Tensión de cortocircuito porcentual (\$\\varepsilon_{cc}\$)|tensión de cortocircuito porcentual $\varepsilon_{cc}$]]: a mayor $\varepsilon_{cc}$, mayor caída interna y mayor RV. Los transformadores de distribución (1–6 % $\varepsilon_{cc}$) tienen RV bajas; los de gran potencia (6–13 % $\varepsilon_{cc}$) RV mayores pero ofrecen mejor protección contra cortocircuitos.

## 2. Eficiencia del transformador

A los transformadores también se les juzga y compara por su **eficiencia**:

$$\eta = \frac{P_{sal}}{P_{ent}} \cdot 100\,\% \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} \eta = \frac{P_{sal}}{P_{sal} + P_{perdida}} \cdot 100\,\%$$

Estas fórmulas son válidas tanto para **motores, generadores como transformadores**.

### Tres tipos de pérdidas

Los circuitos equivalentes simplifican los cálculos de eficiencia. En los transformadores se identifican **tres tipos de pérdidas**:

1. **Pérdidas en el cobre** ($I^2 R$) — disipadas en las resistencias $R_1$ y $R'_2$ de los devanados.
2. **Pérdidas por histéresis** — en el núcleo, asociadas al ciclo $B$–$H$ del material magnético (ver [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|pérdidas magnéticas]]).
3. **Pérdidas por corrientes parásitas (Foucault)** — modeladas por $R_{Fe}$ en la rama de magnetización.

> En la práctica las pérdidas 2 y 3 se agrupan como **pérdidas en el núcleo / pérdidas en el hierro** $P_{nucleo}$, que se obtienen del [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real#Ensayo de vacío|ensayo de vacío]] ($P_0 \approx P_{Fe}$). Las pérdidas 1 se obtienen del [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real#Ensayo de cortocircuito|ensayo de cortocircuito]] ($P_{cc} \approx P_{Cu}$).

### Cálculo con potencias

Para determinar la eficiencia con una carga específica, basta con sumar las pérdidas a cada resistencia del circuito equivalente. La potencia de salida es:

$$P_{sal} = V_S \, I_S \, \cos\theta_S$$

Por lo tanto, la **eficiencia del transformador** se expresa como:

$$\boxed{\;\eta = \frac{V_S \, I_S \, \cos\theta}{P_{Cu} + P_{nucleo} + V_S \, I_S \, \cos\theta} \cdot 100\,\%\;}$$

> [!success] Eficiencia alta = buen transformador
> Una **eficiencia del transformador a plena carga alta** significa que el transformador está convirtiendo eficazmente la mayoría de la energía de entrada en energía de salida — rendimiento óptimo y pérdida mínima de energía durante el proceso de transformación. Los transformadores de potencia industriales típicamente alcanzan $\eta > 98\,\%$.

## Resumen

| Magnitud | Fórmula | Datos necesarios |
| -------- | ------- | ---------------- |
| Regulación de voltaje | $RV = \dfrac{V_P/a - V_S}{V_S} \cdot 100\,\%$ | Tensión vacío, tensión plena carga |
| Eficiencia | $\eta = \dfrac{V_S I_S \cos\theta}{V_S I_S \cos\theta + P_{Cu} + P_{nucleo}} \cdot 100\,\%$ | $P_{cc}$ (cu), $P_0$ (núcleo), carga, $\cos\theta$ |

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
