---
title: "Simulación LTspice — LE2 Realimentación negativa (teoría vs simulación)"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 9
orden: 97
tipo: ejercicio
tags:
  - curso/amplificadores
  - tipo/ejercicio
  - tema/realimentacion-negativa
  - tema/transresistencia
  - tema/respuesta-en-frecuencia
  - tema/simulacion
  - tema/ltspice
  - tema/2n2222
date: 2026-06-02
---

> [!info] De qué trata
> Simulación del circuito **real del LE2** ([[S09-99 Laboratorio - LE2 Realimentacion negativa|guía]]) en **LTspice** (motor SPICE, modo batch), para contrastar con los cálculos teóricos. Se corren dos casos: **S1 abierto** (con realimentación) y **S1 cerrado** (sin realimentación).
>
> Archivos: [`le2_s1abierto.cir`](le2_s1abierto.cir) · [`le2_s1cerrado.cir`](le2_s1cerrado.cir) · parser [`parse_raw.py`](parse_raw.py) · gráfico [`plot_rm.py`](plot_rm.py).

## Método de medición (igual que la guía)

Se excita con $V_g$ senoidal (AC, magnitud 1 V) y se define $I_g$ = corriente por $R_1$. Entonces, directamente:

$$R_m=\frac{V_o}{I_g}=\frac{V(c)}{I(R_1)}\qquad Z_i=\frac{V_g}{I_g}=\frac{1}{I(R_1)}$$

Barrido `.ac dec 50 10Hz 200kHz`; punto de operación con `.op`. Modelo Gummel-Poon estándar del **2N2222**.

## 1. Punto de operación DC (`.op`)

Idéntico en ambos casos (el condensador $C_2$ bloquea DC, así que S1 no altera el bias):

| Nodo / magnitud | Simulación |
| --------------- | ---------- |
| $V_B$ | 1.513 V |
| $V_C$ | 3.718 V |
| $V_E$ | 0.813 V |
| $V_{BE}$ | 0.700 V ✔ |
| $V_{CE}$ | 2.905 V |
| $I_{CQ}$ | **8.08 mA** |
| $I_B$ | 45.6 µA |
| $\beta_{DC}=I_C/I_B$ | ≈ 177 |

De aquí salen los parámetros de pequeña señal usados en la teoría:
$$g_m=\frac{I_{CQ}}{V_T}=\frac{8.08\,\text{mA}}{25.85\,\text{mV}}=0.313\,\text{S}\qquad r_\pi=\frac{\beta}{g_m}=\frac{177}{0.313}\approx566\,\Omega$$

> El bias es por **realimentación de colector** ($R_3{+}R_4$ de colector a base + $R_2$ a tierra). En el laboratorio físico, este $I_{CQ}$ se obtiene midiendo las tensiones de nodo (paso 2 de la guía).

## 2. Respuesta en frecuencia de la transresistencia

![[le2_respuesta_frecuencia.png]]
*$|R_m|$ vs frecuencia. Rojo: sin realimentación (S1 cerrado) — gana ~123 kΩ pero la curva sube y se curva (banda angosta). Azul: con realimentación (S1 abierto) — plana en ~10.4 kΩ, pegada a la línea ideal $R_f=11.2\,\text{k}\Omega$ (banda ancha y estable).*

### Tabla de datos simulada (frecuencias de la guía)

| f [Hz] | $\lvert R_m\rvert$ SIN realim. [kΩ] | $\lvert R_{mf}\rvert$ CON realim. [kΩ] | $\lvert Z_i\rvert$ SIN [kΩ] | $\lvert Z_{if}\rvert$ CON [kΩ] |
| ------ | ------ | ------ | ------ | ------ |
| 20     | 19.04  | 8.53   | 12.15  | 11.00 |
| 100    | 26.49  | 8.94   | 12.76  | 10.79 |
| 200    | 35.53  | 9.52   | 12.71  | 10.51 |
| 1 K    | 94.88  | 10.31  | 11.56  | 10.08 |
| 2 K    | 114.0  | 10.35  | 10.92  | 10.05 |
| 5 K    | 122.1  | 10.36  | 10.60  | 10.04 |
| 10 K   | 123.4  | 10.37  | 10.54  | 10.04 |
| 20 K   | 123.4  | 10.37  | 10.53  | 10.04 |
| 50 K   | 121.3  | 10.37  | 10.50  | 10.04 |
| 70 K   | 119.2  | 10.36  | 10.49  | 10.04 |
| 100 K  | 114.6  | 10.36  | 10.45  | 10.04 |
| 150 K  | 105.2  | 10.35  | 10.38  | 10.04 |

*(Fase de $R_m$ en banda media ≈ ±180° en ambos casos → amplificador inversor, $R_{mf}\approx-R_f$.)*

## 3. Comparación teoría vs simulación (banda media)

Teoría con $g_m=0.313$ S, $r_\pi=566\,\Omega$ (de la simulación):

| Magnitud | Fórmula | **Teoría** | **Simulación** | Δ |
| -------- | ------- | ---------- | -------------- | - |
| $R_m$ (sin realim.) | $-g_m(R_C\!\parallel\!R_4)(R_2\!\parallel\!R_3\!\parallel\!r_\pi)$ | −129.6 kΩ | −123.4 kΩ | ~5 % |
| $R_{mf}$ (con realim.) | $\dfrac{A}{1+A\beta}$, $A{=}{-}146.6$k, $A\beta{=}13.1$ | **−10.4 kΩ** | **−10.37 kΩ** | <1 % |
| $R_{mf}$ (límite ideal) | $-R_f=-(R_3{+}R_4)$ | −11.2 kΩ | −10.37 kΩ | 7 % (lazo finito) |
| $Z_i$ (sin realim.) | $R_1+(R_2\!\parallel\!R_3\!\parallel\!r_\pi)$ | 10.49 kΩ | 10.50 kΩ | <1 % |
| $Z_{if}$ (con realim.) | $R_1+\dfrac{R_2\!\parallel\!R_f\!\parallel\!r_\pi}{1+A\beta}$ | 10.04 kΩ | 10.04 kΩ | ✔ |
| Nodo base $Z_{if}$ (sin $R_1$) | $\dfrac{511\,\Omega}{1+13.1}$ | 36 Ω | — | — |

**La teoría predice la simulación con error < 1 % en los valores con realimentación.** Las pequeñas diferencias en lazo abierto vienen de aproximar $\beta$ y de efectos de segundo orden del modelo (Early, $r_o$ finito en el modelo real).

## 4. Conclusiones (lo que demuestra el experimento)

1. **La realimentación negativa reduce la transresistencia** ~12× (123 kΩ → 10.4 kΩ) y la **fija** cerca de $-R_f=-11.2\,\text{k}\Omega$, casi independiente del transistor. La ganancia de lazo medida es $1+A\beta=\frac{123.4}{10.37}\approx 11.9$.
2. **Aplana y ensancha la respuesta en frecuencia**: la curva azul es plana en toda la banda; la roja (sin realim.) tiene más ganancia pero se curva y rueda antes (compromiso ganancia–ancho de banda).
3. **Baja la impedancia de entrada del nudo** (mezcla en paralelo): $Z_{if}$ del nodo base cae de ~489 Ω a ~36 Ω. *Vista desde $V_g$* el efecto queda enmascarado porque $R_1=10\,\text{k}\Omega$ domina ($Z_i\approx R_1$ en ambos casos).
4. El **bias DC no cambia** al conmutar S1 (lo garantiza $C_2$): mismo $I_{CQ}=8.08$ mA → comparación AC justa.

> [!check] Veredicto
> Simulación y teoría **coinciden**. El circuito se comporta como un **amplificador de transresistencia con realimentación tensión-paralelo (shunt-shunt)**, tal como se anticipó en [[S09-99 Laboratorio - LE2 Realimentacion negativa|la guía]] y [[S09-98 Resolucion teorica - Realimentacion negativa (problema serie-serie)|la resolución teórica]].

## Cómo reproducir

```powershell
$lt = "$env:LOCALAPPDATA\Programs\ADI\LTspice\LTspice.exe"
& $lt -b -ascii "le2_s1abierto.cir"
& $lt -b -ascii "le2_s1cerrado.cir"
uv run --with matplotlib python plot_rm.py   # tabla + grafico
```
