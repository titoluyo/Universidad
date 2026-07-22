---
title: Examen Final (EXFN) - Desarrollo
curso: "[[Motores MOC]]"
unidad: 4
semana: 18
orden: 99
tipo: evaluacion
subtipo: exfn
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/exfn
  - tema/circuitos-magneticos
  - tema/transformadores
  - tema/maquinas-dc
  - tema/motor-asincrono
date: 2026-07-21
---

> [!info] Enunciado y contexto
> Enunciado convertido: [[EXAMEN DE MAQUINAS ELECTRICAS 4-FIN_TYYLNU]] · Consigna y rúbrica: [[S18-99 Evaluación Semana 18 - Examen Final (EXFN)]].
> Los bloques **✍️ A MANO** contienen lo que se transcribe al papel / documento de entrega. Todo lo que está **fuera** del marco es apoyo (explicación, lectura de curvas, verificación, referencias).

---

## Pregunta 1 — Circuito magnético · Hierro Fundido (3 pts)

**Estrategia.** Es un circuito magnético serie con un solo material. La cadena de cálculo es:
$$\Phi \xrightarrow{\;B=\Phi/A\;} B \xrightarrow{\;\text{curva } B\text{-}H\;} H \xrightarrow{\;\mathcal{F}=H\,l\;} \mathcal{F} \xrightarrow{\;\mathcal{F}=N I\;} I$$
El único paso no algebraico es leer $H$ en la **curva de magnetización** del *Cast Iron* (no vale $B=\mu_0 H$ porque el hierro está en zona no lineal).

**Lectura de la curva.** Con $B = 0{,}5\ \text{T}$, subimos hasta la curva inferior (*Cast Iron*) y bajamos al eje: $H \approx 2000\ \text{A·v/m}$.

![[S18-EXFN-P1-curva-magnetizacion.png]]

> [!example]+ ✍️ A MANO — Pregunta 1
> **Datos:** $\Phi = 0{,}1\times10^{-3}\ \text{Wb}$; $l = 0{,}25\ \text{m}$; $N = 500$; $A = 0{,}2\times10^{-3}\ \text{m}^2$; material *Cast Iron*.
>
> **1) Densidad de flujo:**
> $$B=\frac{\Phi}{A}=\frac{0{,}1\times10^{-3}}{0{,}2\times10^{-3}}=0{,}5\ \text{T}$$
>
> **2) Intensidad de campo (curva $B$-$H$, Cast Iron):**
> $$B=0{,}5\ \text{T}\;\Rightarrow\; H\approx 2000\ \text{A·v/m}$$
>
> **3) Fuerza magnetomotriz:**
> $$\mathcal{F}=H\,l=2000\times0{,}25=500\ \text{A·v}$$
>
> **4) Corriente:**
> $$\mathcal{F}=N\,I\;\Rightarrow\; I=\frac{\mathcal{F}}{N}=\frac{500}{500}=\boxed{1\ \text{A}}$$

> [!note] Por qué el resultado es "redondo"
> Que $I$ salga exactamente $1\ \text{A}$ confirma que la lectura $H\approx 2000\ \text{A·v/m}$ es la buscada. Si tu curva te da un $H$ algo distinto (p. ej. $1900$–$2100$), la corriente quedará en $\approx 0{,}95$–$1{,}05\ \text{A}$; redondea coherente con la precisión de la gráfica.

Teoría: [[S01-2 Tema 01 - Los circuitos magnéticos]] · [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion]].

---

## Pregunta 2 — Transformador monofásico ideal (3 pts)

**Idea clave.** En un transformador **ideal** la potencia aparente se conserva ($S_p = S_s$). Conviene calcular primero $S$ y de ahí sacar cada corriente como $I = S/V$.

$$S=\frac{P}{\cos\varphi}=\frac{600}{0{,}9}=666{,}67\ \text{VA}$$

> [!example]+ ✍️ A MANO — Pregunta 2
> **Datos:** $V_p=400\ \text{V}$, $V_s=230\ \text{V}$; $P=600\ \text{W}$ a $230\ \text{V}$; ideal; $\cos\varphi=0{,}9$ (inductivo).
>
> **a) Relación de transformación:**
> $$a=\frac{V_p}{V_s}=\frac{N_p}{N_s}=\frac{400}{230}\approx \boxed{1{,}74}$$
>
> **Potencia aparente** (se conserva por ser ideal):
> $$S=\frac{P}{\cos\varphi}=\frac{600}{0{,}9}=666{,}67\ \text{VA}$$
>
> **b) Corriente en el secundario (la que entrega a la carga):**
> $$I_s=\frac{S}{V_s}=\frac{666{,}67}{230}\approx \boxed{2{,}90\ \text{A}}$$
>
> **c) Corriente en el primario:**
> $$I_p=\frac{S}{V_p}=\frac{666{,}67}{400}\approx \boxed{1{,}67\ \text{A}}\qquad\left(=\frac{I_s}{a}=\frac{2{,}90}{1{,}74}\right)$$

> [!check] Verificación
> $\dfrac{I_s}{I_p}=\dfrac{2{,}90}{1{,}67}\approx 1{,}74 = a$ ✔ — coincide con la relación de vueltas del esquema $\dfrac{V_p}{V_s}=\dfrac{I_s}{I_p}=\dfrac{N_p}{N_s}$.

![[S18-EXFN-P2-transformador-monofasico.png]]

Fórmulas: [[Formulario - Motores Eléctricos Estáticos y Rotativos]].

---

## Pregunta 3 — Transformadores trifásicos · preguntas cerradas (4 pts)

Cuatro respuestas cortas. Van directo al documento de entrega.

> [!example]+ ✍️ A MANO — Pregunta 3
> **1.** La mayoría de los sistemas de generación y distribución funcionan con **corriente alterna (CA)**, en configuración **trifásica**.
>
> **2.** Primer método: conectar **tres transformadores monofásicos** formando un **banco trifásico**.
>
> **3.** Segundo método: usar **un solo transformador trifásico**, con los tres devanados sobre un **núcleo común** (de tres columnas).
>
> **4.** Los 4 tipos de conexión de los devanados trifásicos:
> - **Estrella–Estrella (Y–Y)**
> - **Estrella–Triángulo (Y–Δ)**
> - **Triángulo–Estrella (Δ–Y)**
> - **Triángulo–Triángulo (Δ–Δ)**

> [!note] Apoyo
> La CA trifásica se impuso porque permite transporte a alta tensión con bajas pérdidas y produce campos giratorios en las máquinas. En el banco de tres monofásicos cada unidad se puede reemplazar por separado; el transformador trifásico único es más compacto y económico. Notación habitual: la letra mayúscula es el lado de alta tensión y la minúscula el de baja (p. ej. `Dyn`).

---

## Pregunta 4 — Máquina DC · espira giratoria entre caras polares (6 pts)

**Modelo.** Es la *espira rotatoria simple* (análogo rotativo de la máquina lineal). Con ambos lados de la espira bajo los polos, las relaciones son:
$$e_{ind}=2\,r\,l\,B\,\omega \qquad\qquad \tau_{ind}=2\,r\,l\,B\,i$$
y la malla eléctrica cumple $V_B = e_{ind} + i\,R$ (la espira es un **motor**: $V_B$ vence a la fem inducida).

Calculamos una constante útil (para ambos apartados):
$$2\,r\,l\,B = 2\,(0{,}5)(1)(0{,}25)=0{,}25$$

> [!example]+ ✍️ A MANO — Pregunta 4
> **Datos:** $r=0{,}5\ \text{m}$; $l=1\ \text{m}$; $R=0{,}3\ \Omega$; $B=0{,}25\ \text{T}$; $V_B=120\ \text{V}$.
>
> **a) Al cerrar el interruptor:**
> En el instante inicial $\omega=0\Rightarrow e_{ind}=0$, así que $V_B$ solo se opone a $R$ y circula una corriente grande. Esa corriente, dentro del campo $B$, produce un **par inducido** $\tau_{ind}=2rlB\,i$ que hace **girar la espira (acción de motor)**. Al acelerar aparece $e_{ind}=2rlB\,\omega$ que se opone a $V_B$ y va **reduciendo la corriente**, hasta alcanzar el equilibrio.
>
> **b) Corriente de arranque** ($\omega=0,\ e_{ind}=0$):
> $$i_{arr}=\frac{V_B}{R}=\frac{120}{0{,}3}=\boxed{400\ \text{A}}$$
>
> **Velocidad angular en vacío (estado estacionario):** sin carga $\tau_{ind}=0\Rightarrow i=0$, luego $V_B=e_{ind}$:
> $$V_B=2rlB\,\omega\;\Rightarrow\;\omega=\frac{V_B}{2rlB}=\frac{120}{0{,}25}=\boxed{480\ \text{rad/s}}$$

> [!note] Apoyo y verificación
> - En vacío la corriente tiende a $0$ porque no hay par de carga que sostener; toda la tensión de la batería la equilibra la fem inducida.
> - En rpm: $n=\omega\cdot\dfrac{60}{2\pi}=480\cdot 9{,}549\approx 4584\ \text{rpm}$.
> - Coherencia dimensional de la constante: $[\,2rlB\,]=\text{m·m·T}=\text{Wb}$, y $\text{Wb}\cdot\text{rad/s}=\text{V}$ ✔; $\text{Wb}\cdot\text{A}=\text{N·m}$ ✔.

Teoría: [[S13-2 Tema 02 - El motor de corriente continua]] · [[S13-1 Tema 01 - Generador de corriente continua]] · [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua]].

---

## Pregunta 5 — Motores asíncronos · preguntas cerradas (4 pts)

> [!example]+ ✍️ A MANO — Pregunta 5
> **1.** La corriente de campo del rotor se suministra **por inducción electromagnética**: el campo magnético giratorio del estator induce corriente en el rotor **a través del entrehierro** (no por una fuente/conexión externa como en las síncronas).
>
> **2.** También se les conoce como **máquinas de inducción**.
>
> **3.** Cuando el rotor está en cortocircuito, se le llama **rotor de jaula de ardilla**.
>
> **4.** Cuando el rotor se conecta mediante un reóstato de arranque (anillos rozantes), se le llama **rotor devanado (rotor bobinado)**.

> [!note] Apoyo
> El nombre "asíncrona/de inducción" viene justamente de que el rotor NO se alimenta directamente: la corriente aparece por inducción, y para que haya inducción el rotor debe girar más lento que el campo (existe **deslizamiento** $s>0$). Jaula de ardilla = barras cortocircuitadas por anillos (robusto, sin mantenimiento); rotor devanado = bobinas accesibles por anillos rozantes que permiten insertar resistencia externa para mejorar el arranque.

Teoría: [[S15-1 Tema 01 - Máquinas de corriente alterna]] · [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas]] · [[S17-1 Tema 01 - Curvas características del motor asíncrono y regulación de velocidad]].

---

## Resumen de respuestas

| # | Tema | Respuesta |
| - | ---- | --------- |
| 1 | Circuito magnético | $B=0{,}5\ \text{T}$, $H\approx2000\ \text{A·v/m}$, $\mathcal{F}=500\ \text{A·v}$, $I=\mathbf{1\ A}$ |
| 2 | Transformador monofásico | $a\approx\mathbf{1{,}74}$; $I_s\approx\mathbf{2{,}90\ A}$; $I_p\approx\mathbf{1{,}67\ A}$ |
| 3 | Transf. trifásicos | CA trifásica · banco de 3 monofásicos · 1 transformador trifásico · Y-Y, Y-Δ, Δ-Y, Δ-Δ |
| 4 | Máquina DC | Actúa como motor · $i_{arr}=\mathbf{400\ A}$ · $\omega_{vacío}=\mathbf{480\ rad/s}$ ($\approx4584$ rpm) |
| 5 | Motores asíncronos | Inducción (entrehierro) · máquinas de inducción · jaula de ardilla · rotor devanado |

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill. [Circuitos magnéticos, cap. 1; espira rotatoria y máquina DC, cap. 8; máquinas de inducción, cap. 7].
