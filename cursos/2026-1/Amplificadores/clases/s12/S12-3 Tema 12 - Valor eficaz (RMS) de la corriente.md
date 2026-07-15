---
title: "Valor eficaz (RMS) de la corriente"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 12
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/corriente-eficaz
  - tema/valor-rms
  - tema/potencia
date: 2026-06-08
---

## Contexto

El **valor eficaz** o **RMS** (*Root Mean Square*) de una corriente alterna es el valor de corriente **continua** que disiparía la **misma potencia** en una resistencia. Es la magnitud que miden los amperímetros/voltímetros de AC y la base del cálculo de potencia en los [[S12-2 Tema 12 - Circuitos rectificadores|circuitos rectificadores]].

> [!info] Toma de notas en clase
> Definición del valor eficaz y desarrollo de la integral para una corriente senoidal hasta obtener $I_{ef}=I_m/\sqrt{2}$.

---

## 1. Definiciones de partida

$$i(t) = I_m\,\sin\omega t \qquad\qquad \omega = 2\pi f = \frac{2\pi}{T}$$

- $i(t)$ = corriente instantánea
- $I_m$ = corriente de pico (amplitud)
- $\omega$ = frecuencia angular [rad/s]
- $T$ = periodo

El valor eficaz se define como la **raíz de la media del cuadrado** sobre un periodo:

$$I_{ef} = \sqrt{\frac{1}{T}\int_{0}^{T} \big(i(t)\big)^{2}\,dt}$$

> [!note] ¿Por qué "raíz de la media del cuadrado"?
> La potencia en una resistencia es $p(t) = i^2(t)\,R$. La potencia **media** es $P = \overline{i^2}\,R$. Para que una continua $I_{ef}$ disipe esa misma potencia debe cumplir $I_{ef}^2 R = \overline{i^2}\,R$, de donde $I_{ef} = \sqrt{\overline{i^2}}$.

---

## 2. Desarrollo de la integral

**1. Sustituir** $i(t) = I_m\sin\omega t$ y sacar la constante $I_m^2$:

$$I_{ef}^{2} = \frac{1}{T}\int_{0}^{T} I_m^{2}\sin^{2}\omega t\,dt = \frac{I_m^{2}}{T}\int_{0}^{T}\sin^{2}\omega t\,dt$$

**2. Linealizar** $\sin^2$ con la identidad del ángulo doble $\sin^{2}x = \dfrac{1-\cos 2x}{2}$:

$$I_{ef}^{2} = \frac{I_m^{2}}{T}\int_{0}^{T}\frac{1-\cos 2\omega t}{2}\,dt = \frac{I_m^{2}}{2T}\left[\int_{0}^{T}dt \;-\; \int_{0}^{T}\cos 2\omega t\,dt\right]$$

**3. Evaluar cada integral:**

$$\int_{0}^{T}dt = T$$

$$\int_{0}^{T}\cos 2\omega t\,dt = \left.\frac{\sin 2\omega t}{2\omega}\right|_{0}^{T} = \frac{1}{2\omega}\big[\sin(2\omega T) - \sin 0\big] = 0$$

ya que $\omega T = 2\pi \Rightarrow 2\omega T = 4\pi$ y $\sin 4\pi = 0$. (El coseno completa un número entero de ciclos en $[0,T]$, su área neta es cero.)

**4. Reemplazar:**

$$I_{ef}^{2} = \frac{I_m^{2}}{2T}\,\big[\,T - 0\,\big] = \frac{I_m^{2}}{2}$$

**5. Tomar raíz cuadrada:**

$$\boxed{\,I_{ef} = \frac{I_m}{\sqrt{2}} \approx 0.707\,I_m\,}$$

> [!important] Resultado
> Solo válido para forma de onda **senoidal**. El factor $1/\sqrt{2}$ no aplica a otras formas (cuadrada, triangular, rectificada), donde hay que rehacer la integral.

---

## 3. Interpretación gráfica

![[corriente_eficaz.png]]

- La curva roja $\sin^2\omega t$ es **siempre $\ge 0$** y oscila al **doble** de frecuencia ($2\omega$) entre 0 y 1.
- Su **media** sobre un periodo es exactamente $\tfrac{1}{2}$ (línea morada): el área por encima de $\tfrac12$ compensa la de abajo.
- El valor eficaz es la **raíz** de esa media: $I_{ef}/I_m = \sqrt{1/2} = 1/\sqrt2 \approx 0.707$ (línea verde).

---

## 4. Relación con otros valores

Para la senoide pura, partiendo de $I_m$:

| Valor                    | Expresión        | Factor    |
| ------------------------ | ---------------- | --------- |
| Pico                     | $I_m$            | $1$       |
| Eficaz (RMS)             | $I_m/\sqrt{2}$   | $0.707$   |
| Medio (sobre medio ciclo)| $2I_m/\pi$       | $0.637$   |
| Medio (ciclo completo)   | $0$              | $0$       |

> [!note] Conexión con rectificadores
> Tras rectificar **onda completa**, $\overline{i^2}$ no cambia (elevar al cuadrado elimina el signo), por lo que el **valor eficaz sigue siendo $I_m/\sqrt2$**, mientras que el **valor medio** sí pasa de $0$ a $2I_m/\pi$. Ver [[S12-2 Tema 12 - Circuitos rectificadores]].

---

## Bibliografía

- Sadiku, M. *Fundamentos de Circuitos Eléctricos*, cap. "Análisis de potencia en AC" — valor RMS.
- Boylestad, R. *Introducción al Análisis de Circuitos* — valores eficaces y medios.
