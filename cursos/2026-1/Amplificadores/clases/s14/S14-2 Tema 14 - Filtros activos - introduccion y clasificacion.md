---
title: "Filtros activos: introducción, clasificación y análisis frecuencial"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/filtros-activos
  - tema/respuesta-en-frecuencia
  - tema/funcion-de-transferencia
  - tema/frecuencia-de-corte
  - tema/decibelio
  - tema/factor-q
date: 2026-06-22
---

## Contexto

Un **filtro** es un circuito que **deja pasar unas frecuencias y bloquea otras**. Un filtro es **activo** cuando, además de los componentes pasivos ($R$ y $C$), usa un **elemento activo** —típicamente un **amplificador operacional**— que aporta ganancia y aísla la entrada de la salida.

Esta nota es la aplicación directa de la [[S14-1 Tema 14 - Funcion de transferencia|función de transferencia $H(f)$]]: darle a $H(f)$ una forma concreta para que el circuito seleccione frecuencias. Es el contenido de las **sesiones 27–28** (filtros pasa bajo, pasa alto, pasa banda, supresor de banda y pasa todo) y la base de las semanas siguientes (Butterworth/Chebyshev/Bessel, primer y segundo orden, Sallen-Key).

> [!info] Toma de notas en clase
> Semana 14 — Sesiones 27–28. **Filtros activos: introducción y clasificación.** Qué son, por qué se prefieren a los pasivos, los cinco tipos por banda de paso y cómo se analizan en frecuencia (frecuencia de corte, pendiente por orden, ancho de banda y factor $Q$). El detalle de cada topología (primer orden, segundo orden, Sallen-Key) y las aproximaciones se ven en las notas/semanas siguientes.

---

## 1. ¿Qué es un filtro? Pasivo vs. activo

Todo filtro se describe por su [[S14-1 Tema 14 - Funcion de transferencia|función de transferencia]] $H(f)=Y(f)/X(f)$: su magnitud $|H(f)|$ dice cuánto pasa cada frecuencia.

| | **Filtro pasivo** | **Filtro activo** |
|---|---|---|
| Componentes | $R$, $L$, $C$ | $R$, $C$ + **amplificador (op-amp)** |
| Ganancia | $\le 1$ (solo atenúa) | **puede amplificar** ($>1$) |
| Inductores | sí (voluminosos, caros) | **no** ($L$ se "sintetiza" con op-amp + $RC$) |
| Impedancias | la carga afecta la respuesta | **aísla**: $Z_{in}$ alta, $Z_{out}$ baja |
| Cascada | las etapas se cargan entre sí | se conectan **sin interacción** |
| Frecuencia | sirve a muy alta frecuencia (RF) | limitado por el ancho de banda del op-amp |

> [!tip] Por qué activos en audio y baja frecuencia
> A bajas frecuencias, los inductores necesarios serían enormes. El op-amp permite **eliminar los inductores**, **dar ganancia** y, gracias a su baja impedancia de salida, **encadenar etapas** sin que una cargue a la otra. Por eso dominan en audio, instrumentación y acondicionamiento de señal.

## 2. Clasificación

### 2.1 Por banda de paso (los cinco tipos)

Es la clasificación principal. Según qué rango de frecuencias deja pasar:

```
 |H|                |H|                 |H|
  │▔▔▔▔▔▔▔▏          │      ▕▔▔▔▔▔        │    ▕▔▔▏
  │        ▏         │     ▕             │   ▕    ▏
  │         ▔▔▔      │ ▔▔▔▕             │▔▔▔      ▔▔▔
  └──────────► f     └──────────► f     └──────────► f
   Pasa BAJO          Pasa ALTO          Pasa BANDA

 |H|                       |H|
  │▔▔▏      ▕▔▔▔            │▔▔▔▔▔▔▔▔▔▔▔▔   (magnitud plana)
  │    ▏   ▕               │
  │     ▔▔▔                │
  └──────────► f           └──────────► f
   SUPRESOR de banda        PASA TODO (solo cambia la fase)
```

- **Pasa bajo (low-pass):** deja pasar frecuencias **por debajo** de $f_c$; atenúa las altas.
- **Pasa alto (high-pass):** deja pasar frecuencias **por encima** de $f_c$; atenúa las bajas.
- **Pasa banda (band-pass):** deja pasar una **franja** entre $f_{c1}$ y $f_{c2}$.
- **Supresor / rechaza banda (band-stop, notch):** **bloquea** una franja y deja pasar el resto.
- **Pasa todo (all-pass):** $|H(f)|=1$ en todas las frecuencias; **solo modifica la fase** (se usa para corregir retardos).

### 2.2 Por orden (pendiente de caída)

El **orden** $n$ del filtro lo fija el número de elementos reactivos ($C$) y determina **qué tan brusca** es la transición entre banda de paso y banda de rechazo:

$$\text{pendiente} = n \times 20\ \tfrac{\text{dB}}{\text{década}} = n\times 6\ \tfrac{\text{dB}}{\text{octava}}$$

- **1.er orden:** $-20\ \text{dB/década}$ (caída suave).
- **2.º orden:** $-40\ \text{dB/década}$ (más selectivo; base del Sallen-Key).
- A mayor orden, más se parece al filtro **ideal** (corte vertical), a costa de más componentes.

### 2.3 Por aproximación (forma de la respuesta)

Cómo se "diseña" la curva en la banda de paso y la transición (se desarrollan en la semana 16):

- **Butterworth:** banda de paso **lo más plana** posible (*maximally flat*).
- **Chebyshev:** transición **más abrupta** a cambio de **rizado** en la banda de paso.
- **Bessel:** prioriza la **fase lineal** (retardo constante, no deforma la señal).

## 3. Análisis frecuencial

Analizar un filtro = estudiar su $H(f)$ con estos parámetros.

### 3.1 Frecuencia de corte $f_c$ (criterio de $-3\ \text{dB}$)

Es la frecuencia que marca el **límite** de la banda de paso: donde la salida cae a $\tfrac{1}{\sqrt2}\approx 0{,}707$ de su valor máximo, es decir **$-3\ \text{dB}$** (la potencia cae a la mitad).

$$\boxed{\,|H(f_c)| = \dfrac{|H|_{\max}}{\sqrt{2}} \;\Leftrightarrow\; -3\ \text{dB}\,}$$

Para un filtro $RC$ de primer orden:

$$\boxed{\,f_c = \dfrac{1}{2\pi RC}\,}$$

- $f_c$ = frecuencia de corte (Hz)
- $R$ = resistencia ($\Omega$)
- $C$ = capacitancia (F)

### 3.2 Respuesta de un pasa bajo de 1.er orden (ejemplo base)

$$H(f) = \dfrac{A_0}{1 + j\,\dfrac{f}{f_c}}\qquad |H(f)| = \dfrac{A_0}{\sqrt{1+\left(\frac{f}{f_c}\right)^2}}$$

- $A_0$ = ganancia en la banda de paso ($f\ll f_c$).
- En $f=f_c$: $|H|=A_0/\sqrt2$ → $-3\ \text{dB}$.
- En $f\gg f_c$: cae $-20\ \text{dB/década}$.

> [!example] Diseño rápido
> Para $f_c = 1\ \text{kHz}$ con $C = 10\ \text{nF}$:
> $$R = \frac{1}{2\pi f_c C} = \frac{1}{2\pi(1000)(10\times10^{-9})} \approx 15{,}9\ \text{k}\Omega$$

### 3.3 Ancho de banda y factor $Q$ (pasa banda)

En un pasa banda, entre las dos frecuencias de corte $f_{c1}$ y $f_{c2}$:

$$\text{BW} = f_{c2}-f_{c1} \qquad f_0 = \sqrt{f_{c1}\,f_{c2}}\qquad \boxed{\,Q = \dfrac{f_0}{\text{BW}}\,}$$

- $f_0$ = frecuencia central (media **geométrica**).
- $\text{BW}$ = ancho de banda ($-3\ \text{dB}$).
- $Q$ = **factor de calidad**: alto $Q$ → banda **estrecha y selectiva**; bajo $Q$ → banda ancha.

### 3.4 Diagrama de Bode

La herramienta estándar para representar $|H(f)|$ (en dB) y la fase $\phi(f)$ frente a $\log f$. Permite leer de un vistazo $f_c$, la pendiente y el ancho de banda. Se desarrolla en la **semana 15**.

## 4. Gráfica

Respuesta en magnitud (en dB) de los cuatro filtros básicos de 2.º orden con la misma frecuencia de corte / central $f_c = 1\ \text{kHz}$. Se ve el criterio de $-3\ \text{dB}$ en cada $f_c$ y cómo cada tipo selecciona su banda.

![[filtros_activos_respuesta.png]]

Script: [`plot_filtros_activos.py`](plot_filtros_activos.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_filtros_activos.py`.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — cap. de filtros activos y respuesta en frecuencia.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — filtros activos, función de transferencia y factor $Q$.
- Coughlin, R. & Driscoll, F. *Amplificadores Operacionales y Circuitos Integrados Lineales*. Pearson — filtros activos con op-amp.
