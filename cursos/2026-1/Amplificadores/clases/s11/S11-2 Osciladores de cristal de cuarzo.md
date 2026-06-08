---
title: "Osciladores de cristal de cuarzo"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 11
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/osciladores
  - tema/cristal-de-cuarzo
  - tema/piezoelectricidad
  - tema/estabilidad-en-frecuencia
  - tema/oscilador-pierce
date: 2026-06-02
---

## Contexto

En las sesiones anteriores estudiamos los osciladores senoidales basados en el criterio de Barkhausen, primero con redes $RC$ (Wien, desplazamiento de fase) y luego con tanques resonantes $LC$ (Colpitts, Hartley) en [[S09-2 Osciladores]]. Todos comparten una limitación común: la **frecuencia de oscilación depende directamente del valor de componentes pasivos** ($R$, $L$, $C$) que **derivan con la temperatura, el envejecimiento y la tolerancia de fabricación**.

Esta sesión responde a una pregunta de ingeniería muy concreta: *¿cómo se construye un oscilador cuya frecuencia sea tan estable que sirva de "reloj" para un microprocesador, un transmisor de radio o un GPS?* La respuesta es el **resonador de cristal de cuarzo**, y entender **por qué es tan importante** es el objetivo central de la nota.

> [!info] Enfoque de la nota
> El contenido se apoya en conocimientos generales de electrónica y fuentes confiables (no en el material del curso). Las cifras de $Q$, estabilidad y modelos provienen de la bibliografía y referencias técnicas citadas al final.

---

## 1. El problema de fondo: la estabilidad en frecuencia

Un oscilador $LC$ ideal oscila en $\omega_0 = 1/\sqrt{LC}$. Pero en la práctica esa frecuencia **se desplaza** por varias causas:

- **Tolerancia de componentes:** un capacitor $\pm 5\%$ y una bobina $\pm 10\%$ ya introducen un error de frecuencia de varios por ciento.
- **Deriva térmica:** el cobre del inductor, el dieléctrico del capacitor y los parámetros del transistor cambian con la temperatura.
- **Factor de calidad limitado:** una bobina real tiene $Q \approx 10$ a $200$. Como vimos en [[S09-2 Osciladores]], un $Q$ bajo significa una curva de reactancia poco pronunciada, de modo que **cualquier perturbación externa "jala" (pull) la frecuencia con facilidad**.

> [!question] ¿Qué tan buena es la estabilidad de un LC?
> Un buen oscilador $LC$ alcanza una estabilidad del orden de $10^{-3}$ a $10^{-4}$ (cientos a miles de ppm). Para un reloj digital eso significaría un error de **minutos por día** — inservible para comunicaciones o cómputo. El cuarzo lleva esta cifra a $10^{-6}$ o mejor.

La clave para mejorar la estabilidad es **maximizar el factor de calidad $Q$**: a mayor $Q$, más estrecho el ancho de banda, más empinada la pendiente de reactancia y menos "jalable" es el oscilador. Aquí es donde ningún circuito $LC$ puede competir con un resonador mecánico.

---

## 2. El efecto piezoeléctrico: un resonador mecánico

El cuarzo ($\text{SiO}_2$ cristalino) es **piezoeléctrico**: al deformarlo mecánicamente genera una tensión eléctrica entre sus caras, y a la inversa, al aplicarle una tensión se deforma físicamente.

Si tallamos una lámina de cuarzo y le aplicamos una señal alterna, la lámina **vibra mecánicamente**. Como todo cuerpo elástico, posee una **frecuencia natural de resonancia mecánica** que depende de su corte, espesor y geometría — y que es **extraordinariamente estable**, porque está fijada por las propiedades físicas del material y no por componentes eléctricos discretos.

> [!note] La idea central
> El cristal **convierte una resonancia mecánica (muy estable) en una resonancia eléctrica** que el circuito puede aprovechar. La frecuencia ya no la fija un $LC$ de cobre y dieléctrico, sino la vibración de una pieza de cuarzo.

El corte más usado en electrónica es el **corte AT**, porque su deriva con la temperatura sigue una curva cúbica muy plana alrededor de la temperatura ambiente.

---

## 3. Modelo eléctrico equivalente del cristal

Visto desde sus terminales, el cristal se comporta como un circuito $RLC$. La vibración mecánica se modela con una **rama móvil (motional)** serie, y el encapsulado/electrodos aportan una **capacitancia estática en paralelo** $C_0$:

```
              ┌────[ R1 ]──[ L1 ]──[ C1 ]────┐   ← rama móvil (motional)
   o──────────┤                              ├──────────o
              └──────────────[ C0 ]──────────┘   ← capacitancia estática (electrodos)
```

- $R_1$ = **resistencia móvil** → modela las pérdidas mecánicas (fricción interna). Es muy pequeña.
- $L_1$ = **inductancia móvil** → modela la masa/inercia del cuarzo que vibra. Es enorme (¡decenas de henrios!).
- $C_1$ = **capacitancia móvil** → modela la elasticidad del cuarzo. Es minúscula (femto a pico faradios).
- $C_0$ = **capacitancia estática** → la del par de electrodos con el cuarzo como dieléctrico. Típicamente $C_0 \gg C_1$.

> [!tip] Por qué el Q es astronómico
> El factor de calidad de la rama móvil es $Q = \dfrac{\omega_s L_1}{R_1}$. Como $L_1$ es gigantesca y $R_1$ diminuta, el cociente alcanza valores de **$10^4$ a $10^6$**, frente a $\sim 10^2$ de un tanque $LC$. Es físicamente imposible fabricar una bobina con semejante $Q$.

---

## 4. Las dos frecuencias de resonancia

El modelo de dos ramas tiene **dos resonancias muy próximas entre sí**:

### 4.1. Resonancia serie $f_s$

La rama móvil $R_1 L_1 C_1$ entra en resonancia y su reactancia se anula; el cristal presenta su **impedancia mínima** (puramente resistiva $\approx R_1$):

$$
f_s = \frac{1}{2\pi\sqrt{L_1 C_1}}
$$

### 4.2. Resonancia paralelo (antirresonancia) $f_a$

A una frecuencia ligerísimamente mayor, la rama móvil se vuelve inductiva y **resuena con la capacitancia estática $C_0$**; el cristal presenta su **impedancia máxima**:

$$
f_a = f_s \sqrt{1 + \frac{C_1}{C_0}} \approx f_s\left(1 + \frac{C_1}{2C_0}\right)
$$

Como $C_1 \ll C_0$, ambas frecuencias distan apenas unos **pocos por mil** (0,1 % – 0,5 %). Entre $f_s$ y $f_a$ el cristal es **inductivo**, y es precisamente en esa estrecha ventana donde trabaja como inductor de altísimo $Q$ dentro del oscilador.

```
  Reactancia X(f)
        │        inductivo
        │        ╱│
        │       ╱ │
   ─────┼──────╱──┼──────────► f
        │  fs ╱   │ fa
        │    ╱    │
        │ capacitivo (fuera de la ventana)
```

> [!important] Estrechez = estabilidad
> Que $f_s$ y $f_a$ estén tan juntas implica una **pendiente de reactancia casi vertical**. El amplificador solo puede sostener oscilación dentro de esa ventana minúscula, así que la frecuencia queda "atrapada" allí. Una variación en los componentes del circuito activo mueve la frecuencia de forma despreciable — esto es la **baja "pullability"** y la raíz de la estabilidad del cuarzo.

---

## 5. ¿Por qué el cristal gana? Comparación directa

| Parámetro                  | Oscilador $LC$        | Oscilador a cristal de cuarzo        |
| -------------------------- | --------------------- | ------------------------------------ |
| Factor de calidad $Q$      | $\sim 10$ – $200$     | $\sim 10^4$ – $10^6$                 |
| Estabilidad en frecuencia  | $10^{-3}$–$10^{-4}$   | $10^{-6}$ o mejor                    |
| Deriva térmica             | Alta                  | Muy baja (corte AT casi plano)       |
| Frecuencia fijada por      | $L$ y $C$ discretos   | Vibración mecánica del cuarzo        |
| Ancho de banda             | Ancho                 | Extremadamente estrecho              |
| Ruido de fase              | Mayor                 | Muy bajo                             |

El criterio de Barkhausen ($|A\beta| \geq 1$ y fase $= 0°$, ver [[S09-1 Amplificadores con realimentacion positiva y osciladores]]) se cumple **solo dentro de la ventana $f_s$–$f_a$**, porque fuera de ella la fase del cristal cambia bruscamente y rompe la condición de oscilación. El cristal actúa así como un **filtro de banda ultraestrecha** que selecciona la frecuencia con una precisión inalcanzable para un $LC$.

---

## 6. Estabilidad: tolerancia, temperatura y envejecimiento

La estabilidad se especifica en **partes por millón (ppm)**: $1\ \text{ppm} = 10^{-6}$. Conviene distinguir tres conceptos:

- **Tolerancia de frecuencia:** desviación a $25\,°\text{C}$ respecto al nominal (proceso de fabricación).
- **Estabilidad térmica:** variación en todo el rango de temperatura de trabajo.
- **Envejecimiento (aging):** deriva lenta a lo largo de los años (típ. $< 5$ ppm/año), por relajación de tensiones y contaminación.

Según el grado de control, los productos comerciales son:

| Tipo   | Nombre                                      | Estabilidad típica    |
| ------ | ------------------------------------------- | --------------------- |
| XO     | Oscilador de cristal simple                 | $\pm 50$ a $\pm 100$ ppm |
| TCXO   | Compensado en temperatura                   | $\pm 0{,}5$ a $\pm 5$ ppm |
| OCXO   | Controlado por horno (oven-controlled)      | $\pm 0{,}01$ a $\pm 0{,}1$ ppb |

> [!example] Intuición de magnitud
> $\pm 20$ ppm en un reloj de $32{,}768\ \text{kHz}$ equivale a un error máximo de **~1,7 segundos por día**. Un OCXO de $0{,}01$ ppb erra menos de **1 segundo en varios años**. Ningún $LC$ se acerca a esto.

---

## 7. Topologías de oscilador a cristal

Las topologías $LC$ vistas en [[S09-2 Osciladores]] se "transplantan" sustituyendo el inductor del tanque por el cristal, que trabaja en su ventana inductiva.

### 7.1. Oscilador Pierce

Es la topología **más usada** en relojes de microcontroladores y sistemas digitales por su simplicidad, bajo consumo y mínimo número de componentes. El cristal va entre la salida y la entrada de un inversor/amplificador, con dos capacitores de carga ($C_{L1}$, $C_{L2}$) a masa:

```
        ┌──────[ XTAL ]──────┐
        │                    │
   ─────┤  >──── inversor ───┤─────
        │                    │
       ═╪═ CL1              ═╪═ CL2
        │                    │
       GND                  GND
```

El amplificador aporta la ganancia y el desfase necesarios; el cristal fija la frecuencia. La **capacitancia de carga** $C_L$ que "ve" el cristal define con qué precisión opera entre $f_s$ y $f_a$ (los cristados en modo paralelo se especifican para un $C_L$ dado, p. ej. 18 pF).

### 7.2. Colpitts a cristal

Equivalente al Colpitts $LC$, reemplazando la bobina por el cristal en la rama inductiva. Se usa cuando se requiere una salida senoidal limpia en RF.

> [!note] Series vs. paralelo
> - Un cristal **modo serie** se diseña para oscilar en $f_s$ (baja impedancia); el circuito no añade capacitancia de carga.
> - Un cristal **modo paralelo** se diseña para una $C_L$ específica y oscila entre $f_s$ y $f_a$. **Usar un cristal en el modo equivocado desplaza la frecuencia** fuera de tolerancia.

---

## 8. Importancia y aplicaciones

La estabilidad del cuarzo lo convirtió en el **patrón de tiempo y frecuencia de toda la electrónica moderna**. Sin él no existirían:

- **Cómputo digital:** el *clock* de todo microprocesador, microcontrolador y bus de datos. La sincronización de millones de transistores depende de un reloj estable.
- **Relojería:** el reloj de cuarzo de $32{,}768\ \text{kHz}$ ($=2^{15}$ Hz, fácil de dividir hasta 1 Hz) desplazó al reloj mecánico por su precisión y bajo costo.
- **Comunicaciones y RF:** generación de portadoras y referencias de frecuencia en radios, celulares y Wi-Fi; el ancho de canal exige que el transmisor no se salga de su banda asignada.
- **GPS y navegación:** la trilateración exige referencias de tiempo extremadamente estables (TCXO/OCXO) — un error de microsegundos se traduce en cientos de metros de error de posición.
- **Instrumentación y metrología:** bases de tiempo de frecuencímetros, osciloscopios y patrones de calibración.
- **RTC (Real-Time Clock):** mantienen fecha y hora en equipos aun apagados, con consumo ínfimo.

> [!important] Síntesis de "por qué importa"
> El cristal de cuarzo resuelve el talón de Aquiles de los osciladores: la **estabilidad**. Su $Q$ de hasta $10^6$ y su frecuencia anclada a una vibración mecánica permiten precisiones de ppm o mejores, baratas y reproducibles en masa. Por eso es, literalmente, el **latido de tiempo de casi todo dispositivo electrónico**.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson. (Capítulo de osciladores: oscilador a cristal y modelo equivalente.)
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press. (Resonadores de cuarzo y osciladores Pierce/Colpitts.)
- *Crystal oscillator* — Wikipedia. https://en.wikipedia.org/wiki/Crystal_oscillator
- *Quartz Crystal Oscillator and Crystal Oscillation Fundamentals* — Electronics Tutorials. https://www.electronics-tutorials.ws/oscillator/crystal.html
- *Characterizing Frequency Deviations of Quartz Crystals* — All About Circuits. https://www.allaboutcircuits.com/technical-articles/characterizing-frequency-deviations-of-quartz-crystals-frequency-tolerance-frequency-stability-and-aging/
- *Specifying Quartz Crystals* / *Design a Crystal Oscillator to Match Your Application* — Analog Devices. https://www.analog.com/en/resources/technical-articles/specifying-quartz-crystals.html
