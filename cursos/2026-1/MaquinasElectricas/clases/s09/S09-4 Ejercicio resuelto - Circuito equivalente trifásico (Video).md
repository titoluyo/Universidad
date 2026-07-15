---
title: Ejercicio resuelto - Circuito equivalente aproximado del transformador trifásico
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 4
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-trifasico
  - tema/circuito-equivalente
  - tema/analisis-por-fase
  - tema/impedancia-reflejada
  - tema/conexion-dY
  - tema/caida-tension-cc-porcentual
date: 2026-05-22
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de circuito equivalente del transformador trifásico" (Semana 09, Tema 02). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Se dispone de un transformador de **50 kVA**, conexión **Δ–Y**, relación de línea **15 000 / 380 V** con las siguientes tensiones relativas de cortocircuito:

- **Caída relativa de tensión en cortocircuito:** $\varepsilon_{cc} = 10\,\%$
- **Caída relativa de reactancia:** $\varepsilon_{X_{cc}} = 8\,\%$

El transformador alimenta por el secundario una **carga equilibrada en estrella** de **5 Ω con 0° de fase** (resistiva), a través de una línea de **impedancia $0{,}1 + j\,0{,}2$ Ω por hilo**.

Se solicita:
- **1)** Calcular **$R_{cc}$, $X_{cc}$ y $Z_{cc}$** del circuito equivalente aproximado del transformador **reducido al primario**.
- **2)** Si se aplica al primario una tensión trifásica equilibrada de **15 kV de línea** (lectura del voltímetro $V_1$), determinar las lecturas de los voltímetros $V_a$ (terminales del secundario del transformador) y $V_b$ (terminales de la carga).

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Potencia nominal | $S_n$ | 50 kVA |
| Conexión | — | Δ–Y |
| Tensión de línea primaria | $V_{LP}$ | 15 000 V |
| Tensión de línea secundaria | $V_{LS}$ | 380 V |
| Caída relativa de cortocircuito | $\varepsilon_{cc}$ | 10 % |
| Caída relativa reactiva | $\varepsilon_{X_{cc}}$ | 8 % |
| Impedancia por hilo de la línea | $\mathbf{Z}_{línea}$ | $0{,}1 + j\,0{,}2$ Ω |
| Impedancia de carga por fase (Y) | $\mathbf{Z}_L$ | $5\,\angle 0°$ Ω |

## 1) Parámetros del circuito equivalente

### Tensiones y corrientes por fase

**Primario (Δ):**
- Voltaje de fase: $V_{1f} = V_{LP} = 15\,000\,\text{V}$
- Corriente de fase: $I_{1f} = \dfrac{S_n}{3\,V_{1f}} = \dfrac{50\,000}{3 \cdot 15\,000} \approx 1{,}11\,\text{A}$

**Secundario (Y):**
- Voltaje de fase: $V_{2f} = \dfrac{V_{LS}}{\sqrt{3}} = \dfrac{380}{\sqrt{3}} \approx 219{,}4\,\text{V}$

### Relación de transformación (por fase)

$$m = \frac{V_{1f}}{V_{2f}} = \frac{15\,000}{219{,}4}$$

$$\boxed{m \approx 68{,}37}$$

### Impedancia de cortocircuito

De la [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real#Tensión de cortocircuito porcentual (\$\\varepsilon_{cc}\$)|definición de $\varepsilon_{cc}$]]:

$$\varepsilon_{cc} = \frac{Z_{cc} \cdot I_{1f}}{V_{1f}} \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} Z_{cc} = \frac{\varepsilon_{cc} \cdot V_{1f}}{I_{1f}}$$

$$Z_{cc} = \frac{0{,}10 \cdot 15\,000}{1{,}11} = \frac{1\,500}{1{,}11}$$

$$\boxed{Z_{cc} \approx 1\,350\,\Omega}$$

Reactancia de cortocircuito:

$$X_{cc} = \frac{\varepsilon_{X_{cc}} \cdot V_{1f}}{I_{1f}} = \frac{0{,}08 \cdot 15\,000}{1{,}11}$$

$$\boxed{X_{cc} \approx 1\,080\,\Omega}$$

Resistencia de cortocircuito (Pitágoras):

$$R_{cc} = \sqrt{Z_{cc}^{\,2} - X_{cc}^{\,2}} = \sqrt{1\,350^2 - 1\,080^2} = \sqrt{1\,822\,500 - 1\,166\,400} = \sqrt{656\,100}$$

$$\boxed{R_{cc} = 810\,\Omega}$$

#### Resumen del circuito equivalente (por fase, reducido al primario)

$$\mathbf{Z}_{cc} = R_{cc} + jX_{cc} = 810 + j\,1\,080\,\Omega$$

## 2) Lecturas $V_a$ y $V_b$

Trabajamos por fase, **todo referido al primario**, con $V_1 = 15\,000\,\text{V}$ (fase del primario en Δ = línea) como **referencia** $0°$.

### Impedancia de línea reflejada al primario

$$\mathbf{Z}'_{línea} = m^2 \cdot \mathbf{Z}_{línea} = 68{,}37^2 \cdot (0{,}1 + j\,0{,}2)$$

$$\mathbf{Z}'_{línea} = 4\,674{,}5 \cdot (0{,}1 + j\,0{,}2)$$

$$\boxed{\mathbf{Z}'_{línea} \approx 467{,}45 + j\,934{,}9\,\Omega}$$

### Impedancia de carga reflejada al primario

$$\mathbf{Z}'_L = m^2 \cdot \mathbf{Z}_L = 4\,674{,}5 \cdot 5\,\angle 0°$$

$$\boxed{\mathbf{Z}'_L \approx 23\,372{,}6\,\angle 0°\,\Omega}$$

### Corriente $\mathbf{I}'_2$

La impedancia total vista desde el primario:

$$\mathbf{Z}_{total} = \mathbf{Z}_{cc} + \mathbf{Z}'_{línea} + \mathbf{Z}'_L$$

$$\mathbf{Z}_{total} = (810 + 467{,}45 + 23\,372{,}6) + j(1\,080 + 934{,}9 + 0)$$

$$\mathbf{Z}_{total} = 24\,650 + j\,2\,014{,}9 \approx 24\,732\,\angle 4{,}67°\,\Omega$$

Corriente del secundario referida al primario:

$$\mathbf{I}'_2 = \frac{\mathbf{V}_1}{\mathbf{Z}_{total}} = \frac{15\,000\,\angle 0°}{24\,732\,\angle 4{,}67°}$$

$$\boxed{\mathbf{I}'_2 \approx 0{,}6066\,\angle(-4{,}67°)\,\text{A}}$$

### Tensiones fasoriales (referidas al primario, por fase)

**$V'_{Af}$** — tensión por fase en los **terminales del transformador** (punto A, antes de la línea):

$$\mathbf{V}'_{Af} = (\mathbf{Z}'_{línea} + \mathbf{Z}'_L) \cdot \mathbf{I}'_2$$

$$\mathbf{V}'_{Af} = [(23\,372{,}6 + 467{,}45) + j\,934{,}9] \cdot 0{,}6066\,\angle(-4{,}67°)$$

$$\mathbf{V}'_{Af} \approx 23\,858\,\angle 2{,}24° \cdot 0{,}6066\,\angle(-4{,}67°)$$

$$\boxed{\mathbf{V}'_{Af} \approx 14\,472\,\angle(-2{,}43°)\,\text{V}}$$

**$V'_{Bf}$** — tensión por fase en los **terminales de la carga** (punto B, después de la línea):

$$\mathbf{V}'_{Bf} = \mathbf{Z}'_L \cdot \mathbf{I}'_2 = 23\,372{,}6 \cdot 0{,}6066\,\angle(-4{,}67°)$$

$$\boxed{\mathbf{V}'_{Bf} \approx 14\,178\,\angle(-4{,}67°)\,\text{V}}$$

### Conversión a tensiones reales de línea en el secundario (Y)

Para regresar al lado real del secundario, se **divide entre $m$** (fase) y se **multiplica por $\sqrt{3}$** (porque el secundario está en Y, $V_L = \sqrt{3} \cdot V_\phi$):

$$V_a = \frac{|V'_{Af}|}{m} \cdot \sqrt{3} = \frac{14\,472}{68{,}37} \cdot \sqrt{3} = 211{,}7 \cdot \sqrt{3}$$

$$\boxed{V_a \approx 366{,}3\,\text{V}}$$

$$V_b = \frac{|V'_{Bf}|}{m} \cdot \sqrt{3} = \frac{14\,178}{68{,}37} \cdot \sqrt{3} = 207{,}4 \cdot \sqrt{3}$$

$$\boxed{V_b \approx 359{,}2\,\text{V}}$$

> [!note] Caída de tensión por la línea
> La diferencia $V_a - V_b \approx 7{,}1\,\text{V}$ representa la **caída de tensión a lo largo de la línea de alimentación** (la línea entre el trafo y la carga, no la línea del transformador). $V_b$ es la tensión efectiva en bornes de la carga.

## Resumen de resultados

| Magnitud | Valor |
| -------- | ----- |
| Relación de transformación $m$ | $68{,}37$ |
| Corriente nominal de fase primaria $I_{1f}$ | $1{,}11\,\text{A}$ |
| $R_{cc}$ (al primario) | $810\,\Omega$ |
| $X_{cc}$ (al primario) | $1\,080\,\Omega$ |
| $Z_{cc}$ (al primario) | $1\,350\,\Omega$ |
| $\mathbf{Z}'_{línea}$ | $467{,}45 + j\,934{,}9\,\Omega$ |
| $\mathbf{Z}'_L$ | $23\,372{,}6\,\Omega$ |
| $\mathbf{I}'_2$ | $0{,}6066\,\angle(-4{,}67°)\,\text{A}$ |
| $V_a$ (terminales del trafo) | $\approx 366{,}3\,\text{V}$ |
| $V_b$ (terminales de la carga) | $\approx 359{,}2\,\text{V}$ |
| Caída de tensión en la línea | $\approx 7{,}1\,\text{V}$ |

> [!tip] Procedimiento general para problemas de circuito equivalente trifásico
> 1. Calcular $m$ con voltajes **de fase** y corriente nominal $I_{1f}$ con $S/(3 V_{1f})$.
> 2. Pasar $\varepsilon_{cc}$ y $\varepsilon_{X_{cc}}$ a valores absolutos en Ω.
> 3. Reflejar todas las impedancias externas (línea, carga) al primario multiplicando por $m^2$.
> 4. Resolver el circuito **por una fase** como si fuera monofásico.
> 5. Convertir las tensiones del lado primario al lado real del secundario dividiendo entre $m$ y multiplicando por $\sqrt{3}$ si la conexión del secundario es Y, o dejando igual si es Δ.

## Guion del video

![[s09-t02-ej-guion-circuito-equivalente-trifasico.pdf]]

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
