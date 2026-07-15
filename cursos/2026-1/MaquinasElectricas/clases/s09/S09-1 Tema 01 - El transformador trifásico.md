---
title: El transformador trifásico - construcción y conexiones
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-trifasico
  - tema/conexion-YY
  - tema/conexion-Yd
  - tema/conexion-dY
  - tema/conexion-dd
  - tema/banco-trifasico
  - tema/desplazamiento-30-grados
date: 2026-05-18
---

![[s09-t01-banner.png]]

## ¿Por qué trifásico?

La mayoría de los sistemas principales de **generación y distribución de energía** en el mundo actual funcionan utilizando **corriente alterna trifásica**. Existen dos métodos de fabricación de transformadores trifásicos:

### Método 1: tres monofásicos en arreglo trifásico (banco)

Usando **tres transformadores monofásicos** conectados en un arreglo trifásico.

![[s09-t01-fig1-banco-3-mono.png]]
*Figura 1. Banco trifásico compuesto con 3 transformadores independientes.*

### Método 2: tres devanados sobre un único núcleo

Construyendo transformadores trifásicos con **tres grupos de devanados** enrollados alrededor de un **único núcleo** de tres columnas.

![[s09-t01-fig2-trafo-3-columnas.png]]
*Figura 2. Transformador trifásico construido con un núcleo de 3 columnas.*

> [!info] Ventaja del núcleo único
> Menor tamaño, peso y costo de materiales para la misma potencia. El banco de 3 monofásicos se usa cuando se requiere **redundancia** (si una unidad falla se reemplaza solo esa) o cuando los transformadores ya existen en el inventario.

## Conexiones del transformador trifásico

Un transformador trifásico se compone de tres transformadores (separados o combinados en un solo núcleo). Los **devanados primarios y secundarios** de cualquier transformador trifásico pueden conectarse de forma **independiente** en configuración **estrella (Y)** o **triángulo / delta (Δ)**. Esto resulta en un total de **cuatro opciones**:

### 1. Y–Y (estrella–estrella)

![[s09-t01-fig3-conexion-YY.png]]
*Figura 3. Conexión estrella–estrella.*

- $V_{\phi P} = V_{LP}/\sqrt{3}$ (voltaje de fase = voltaje de línea / $\sqrt{3}$).
- $V_{LS} = \sqrt{3} \cdot V_{\phi S}$.
- Relación de voltaje de línea a línea:

$$\boxed{\;\frac{V_{LP}}{V_{LS}} = \frac{\sqrt{3} \cdot V_{\phi P}}{\sqrt{3} \cdot V_{\phi S}} = a\;}$$

> [!warning] Dos desafíos significativos de Y–Y
> 1. **Cargas desbalanceadas** → si las cargas no están balanceadas, los voltajes en las fases pueden **desequilibrarse considerablemente**.
> 2. **Voltajes de tercer armónico** pueden ser significativos.

### 2. Y–Δ (estrella–delta)

![[s09-t01-fig4-conexion-Yd.png]]
*Figura 4. Conexión estrella–delta.*

- Primario: $V_{LP} = \sqrt{3} \cdot V_{\phi P}$.
- Secundario: $V_{LS} = V_{\phi S}$.
- Relación de voltaje de fase: $V_{\phi P}/V_{\phi S} = a$.
- Relación global entre voltajes de línea:

$$\boxed{\;\frac{V_{LP}}{V_{LS}} = \frac{\sqrt{3} \cdot V_{\phi P}}{V_{\phi S}} = \sqrt{3} \cdot a\;}$$

> [!success] Ventajas Y–Δ
> - **No tiene inconvenientes con el tercer armónico** — los componentes de tercer armónico se absorben en una **corriente circulante** en el lado Δ.
> - Es **más resistente a desequilibrios de carga** — el delta redistribuye parcialmente cualquier desequilibrio.

> [!warning] Inconveniente — desfase de 30°
> Debido a la conexión, el **voltaje secundario se desfasa 30°** con respecto al voltaje primario. Esta diferencia de fase puede ocasionar problemas al intentar poner **en paralelo los secundarios** de dos bancos de transformadores que tengan distintas conexiones.

### 3. Δ–Y (delta–estrella)

![[s09-t01-fig5-conexion-dY.png]]
*Figura 5. Conexión delta–estrella.*

- Primario: $V_{LP} = V_{\phi P}$.
- Secundario: $V_{LS} = \sqrt{3} \cdot V_{\phi S}$.
- Relación de voltaje de línea a línea:

$$\boxed{\;\frac{V_{LP}}{V_{LS}} = \frac{V_{\phi P}}{\sqrt{3} \cdot V_{\phi S}} = \frac{a}{\sqrt{3}}\;}$$

> Esta configuración presenta las **mismas ventajas y el mismo desfase de 30°** que la Y–Δ.

### 4. Δ–Δ (delta–delta)

![[s09-t01-fig6-conexion-dd.png]]
*Figura 6. Conexión delta–delta.*

- Primario: $V_{LP} = V_{\phi P}$.
- Secundario: $V_{LS} = V_{\phi S}$.
- Relación de voltaje de línea a línea:

$$\boxed{\;\frac{V_{LP}}{V_{LS}} = \frac{V_{\phi P}}{V_{\phi S}} = a\;}$$

> [!success] Δ–Δ — robusta y sin desfase
> - **No tiene desplazamiento de fase** asociado.
> - **No tiene problemas** con cargas desequilibradas ni con armónicos.

## Tabla resumen

| Conexión | $V_{LP}/V_{LS}$ | Desfase | Tercer armónico | Cargas desbalanceadas |
| -------- | ---------------- | ------- | --------------- | --------------------- |
| **Y–Y**   | $a$              | 0°      | Problemático    | Problemático |
| **Y–Δ**   | $\sqrt{3} \cdot a$ | 30°     | OK              | Buena |
| **Δ–Y**   | $a/\sqrt{3}$     | 30°     | OK              | Buena |
| **Δ–Δ**   | $a$              | 0°      | OK              | OK |

## Diagramas fasoriales por conexión

![[s09-t01-fig7-fasorial-YY.png]]
*Figura 7. Conexión Y–Y.*

![[s09-t01-fig9-fasorial-Yd.png]]
*Figura 9. Conexión Y–Δ — observa el desfase de 30°.*

![[s09-t01-fig8-fasorial-dY.png]]
*Figura 8. Conexión Δ–Y — también con desfase de 30°.*

![[s09-t01-fig10-fasorial-dd.png]]
*Figura 10. Conexión Δ–Δ — sin desfase.*

## Análisis por fase

> [!tip] Técnica fundamental para resolver problemas
> La técnica fundamental para analizar un banco trifásico implica **observar cada transformador del banco individualmente**. Cada transformador del banco opera de manera similar a los transformadores monofásicos previamente estudiados.
>
> Los cálculos relacionados con la **impedancia, regulación de voltaje, eficiencia y otros aspectos** de los transformadores trifásicos se realizan considerando un **enfoque por fase**.

Esto se aprovecha en [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico|el circuito equivalente aproximado del trifásico]] para reutilizar todo el marco del [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|transformador monofásico real]].

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
