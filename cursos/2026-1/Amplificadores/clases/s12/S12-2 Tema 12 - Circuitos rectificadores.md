---
title: "Circuitos rectificadores"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 12
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/rectificadores
  - tema/rectificador-de-media-onda
  - tema/rectificador-de-onda-completa
  - tema/puente-de-graetz
  - tema/diodo
date: 2026-06-08
---

## Contexto

Un **circuito rectificador** convierte una señal alterna (AC) en una unidireccional (pulsante), el paso central para obtener una fuente de **continua (DC)** a partir de la red. Es la etapa que precede al **filtro capacitivo** y al **rizado** que se analizó en [[S12-1 Tema 12 - Rectificador de pico y rizado]].

Cadena completa de una fuente lineal:

```
Red AC → Transformador → RECTIFICADOR → Filtro (C) → Regulador → DC estable
         (baja tensión)  (este tema)    (rizado V_r)
```

> [!info] Toma de notas en clase
> Topologías de rectificación: media onda, onda completa con derivación central y onda completa tipo puente. Se usa el **modelo ideal del diodo** (caída $V_D \approx 0$) salvo donde se indique.

---

## 1. Rectificador de media onda

Un **único diodo** en serie con la carga. Conduce solo durante el semiciclo positivo de la entrada; en el negativo queda en corte y la salida es nula.

$$v_O = \begin{cases} v_I & v_I > 0 \\ 0 & v_I \le 0 \end{cases} \qquad\Rightarrow\qquad v_O = \max(v_I,\,0)$$

- **Frecuencia de salida:** $f_{out} = f$ (un pulso por ciclo).
- **Valor medio (DC):** $\displaystyle V_{DC} = \frac{V_p}{\pi} \approx 0.318\,V_p$.
- **PIV** (tensión inversa de pico que soporta el diodo): $\text{PIV} = V_p$.

> [!warning] Desventaja
> Desaprovecha medio ciclo, el contenido de DC es bajo y, con filtro, el rizado es mayor (la descarga dura casi todo el periodo $T$ → recordar $V_r = V_p\,T/CR$).

## 2. Rectificador de onda completa con derivación central

Dos diodos y un transformador con **toma central** (*center-tapped*). Cada diodo conduce en un semiciclo, de modo que ambos semiciclos llegan a la carga con la **misma polaridad**.

- **Frecuencia de salida:** $f_{out} = 2f$ (dos pulsos por ciclo).
- **Valor medio (DC):** $\displaystyle V_{DC} = \frac{2V_p}{\pi} \approx 0.637\,V_p$ (**el doble** que media onda).
- **PIV:** $\text{PIV} = 2V_p$ (cada diodo soporta el doble).
- Requiere transformador con derivación central; solo se aprovecha la mitad del secundario por semiciclo.

## 3. Rectificador de onda completa tipo puente (Graetz)

**Cuatro diodos** en configuración de puente; no necesita toma central. En cada semiciclo conducen dos diodos en diagonal, encaminando siempre la corriente por la carga en el mismo sentido.

- **Frecuencia de salida:** $f_{out} = 2f$.
- **Valor medio (DC):** $\displaystyle V_{DC} = \frac{2V_p}{\pi} \approx 0.637\,V_p$.
- **PIV:** $\text{PIV} = V_p$ (ventaja frente al de toma central).
- Usa todo el secundario; es la topología **más empleada** en fuentes.

> [!note] Caída de diodos en el puente
> Como siempre conducen **dos** diodos en serie, la salida real pierde $2V_D \approx 1.4\ \text{V}$ respecto al pico ideal: $V_{O,\text{pico}} = V_p - 2V_D$.

---

## 4. Comparación de formas de onda

![[rectificadores_comparacion.png]]

| Característica          | Media onda      | Onda completa (puente)   |
| ---------------------- | --------------- | ------------------------ |
| N.º de diodos          | 1               | 4                        |
| $f_{out}$              | $f$             | $2f$                     |
| $V_{DC}$               | $V_p/\pi$       | $2V_p/\pi$               |
| PIV por diodo          | $V_p$           | $V_p$                    |
| Rizado (con filtro $C$)| Mayor           | **Menor** (mitad)        |
| Transformador          | Simple          | Simple (sin toma central)|

## 5. Conexión con el filtro y el rizado

Al colocar el condensador $C$ en paralelo con la carga se obtiene el **rectificador de pico** de [[S12-1 Tema 12 - Rectificador de pico y rizado]]. La frecuencia de salida determina el rizado:

- **Media onda:** la descarga dura $\approx T$ → $\displaystyle V_r = \frac{V_p}{f\,C\,R}$.
- **Onda completa:** al haber dos pulsos por ciclo, la descarga dura $\approx T/2$ → el rizado se **reduce a la mitad**:

$$\boxed{\,V_r^{\text{(onda completa)}} = \frac{V_p}{2\,f\,C\,R} = \frac{V_p\,T}{2\,CR}\,}$$

Esta es una razón clave para preferir la rectificación de onda completa: **mismo $C$, la mitad de rizado**.

---

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits*, cap. "Diodes" — rectificadores y filtro capacitivo.
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*, cap. "Aplicaciones del diodo".
