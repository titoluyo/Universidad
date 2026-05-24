---
title: "Osciladores"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 9
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/osciladores
  - tema/circuitos-tanque
  - tema/resonancia-lc
date: 2026-05-19
---

## Contexto

En esta sesión continuamos el estudio de los **osciladores senoidales**, enfocándonos en las topologías que operan en alta frecuencia utilizando **circuitos tanque resonantes $LC$**. Analizaremos cómo se comporta un circuito tanque real (con pérdidas), cómo se compensan estas pérdidas para sostener la oscilación según el criterio de Barkhausen, y estudiaremos las topologías clásicas: **Colpitts** y **Hartley**.

---

## 1. El Circuito Tanque como Resonador LC

Para entender los osciladores de radiofrecuencia (RF), primero debemos analizar el **circuito tanque** ($LC$ resonante), el cual actúa como el "péndulo" que fija la frecuencia de oscilación.

```
           ┌───────┬───────┐
           │       │       │
          [ ] C   ( ) L    │
           [ ]     ( )     │
           │       │       │
           └───────┴───────┘
```

### 1.1. Tanque Ideal
A la frecuencia de resonancia $\omega_0$, las reactancias inductiva y capacitiva son iguales en magnitud pero opuestas en fase:

$$
X_L = \omega_0 L = X_C = \frac{1}{\omega_0 C} \quad\Rightarrow\quad \omega_0 = \frac{1}{\sqrt{LC}}
$$

*   **Impedancia ideal:** $Z_p(j\omega_0) \to \infty$. El circuito no demanda corriente de la fuente externa para mantener la oscilación interna.
*   **Fase de la impedancia:** $0^\circ$ (resistivo puro).

### 1.2. Tanque Real (Con Pérdidas)
En el mundo real, el inductor posee una **resistencia parásita en serie** ($R_s$) debida al devanado de cobre. 

```
           ┌───────────┬───────┐
           │           │       │
          [ ] C       ( ) L    │
           [ ]         ( )     │
           │           │       │
           │          [ ] Rs   │
           │          [_]      │
           │           │       │
           └───────────┴───────┘
```

El **Factor de Calidad ($Q$)** a la resonancia mide qué tan selectivo es el tanque:

$$
Q_0 = \frac{\omega_0 L}{R_s} = \frac{1}{\omega_0 C R_s}
$$

### 1.3. Conversión de Modelo Serie a Paralelo
Para facilitar el análisis de osciladores, transformamos la rama serie real ($R_s + j\omega L$) en una rama paralelo equivalente ($R_p \parallel j\omega L_p$) válida en resonancia:

$$
R_p \approx Q_0^2 R_s = \frac{(\omega_0 L)^2}{R_s} = \frac{L}{R_s C}
$$

$$
L_p \approx L
$$

De esta forma, en resonancia, las reactancias de $L_p$ y $C$ se anulan y la impedancia del tanque real queda limitada por la resistencia paralelo $R_p$:

$$
Z_0 = R_p = Q_0 \cdot X_{L0} = \frac{L}{R_s C}
$$

---

## 2. Anotaciones de la pizarra (Clase en vivo)

> [!note] Desarrollo en vivo
> *Espacio reservado para las ráfagas de conceptos, ecuaciones y esquemas que se dicten hoy en clase sobre Osciladores.*

### 1. Clasificación por rango de frecuencias: RC vs LC

El profesor comenzó delimitando el uso físico de los componentes según la frecuencia de operación:

*   **Osciladores RC (Baja Frecuencia: $f < 100\text{ kHz}$):**
    *   Para frecuencias bajas, **se evita el uso de bobinas (inductores)**.
    *   *Razón física:* Como $\omega_0 = \frac{1}{\sqrt{LC}}$, si $\omega_0$ es muy pequeño, el producto $LC$ debe ser extremadamente grande. Si utilizáramos inductores, requeriríamos valores de inductancia gigantescos (del orden de Henrios). Un inductor de ese tamaño necesitaría miles de vueltas de cobre, lo que lo haría físicamente enorme, pesado, muy costoso y, críticamente, tendría una **resistencia parásita en serie ($R_s$) sumamente alta**. Esto haría que su factor de calidad $Q = \omega L / R_s$ fuera paupérrimo, impidiendo la oscilación selectiva.
    *   *Solución:* Se utilizan redes de resistencias y condensadores ($RC$) como el **Puente de Wien** o **Desplazamiento de fase**.

*   **Osciladores LC (Alta Frecuencia: $f > 100\text{ kHz}$):**
    *   A frecuencias altas (cientos de kHz a MHz), las bobinas requeridas son físicamente muy pequeñas (micro Henrios o mili Henrios).
    *   Es posible fabricar bobinas compactas, ligeras y con bajas pérdidas ($R_s$ mínima), garantizando un **factor de calidad $Q$ elevado**.
    *   El tanque resonante $LC$ ofrece una selectividad excepcional para obtener ondas senoidales puras y es fácil de sintonizar variando una capacitancia.

---

### 2. Análisis de Estabilidad y Polos en el Dominio de Laplace

El profesor introdujo el uso de la **Transformada de Laplace ($s = \sigma + j\omega$)** para modelar matemáticamente el comportamiento dinámico de los osciladores y justificar cómo arranca y se estabiliza el circuito.

La función de transferencia en lazo cerrado en el dominio de Laplace se expresa como:

$$
A_f(s) = \frac{A(s)}{1 - A(s)\beta(s)}
$$

Los polos del sistema (que determinan la respuesta temporal) son las raíces de la **ecuación característica**:

$$
1 - A(s)\beta(s) = 0
$$

El profesor graficó en la pizarra la ubicación de los polos en el **plano complejo $s$** y su correspondencia en el tiempo:

```
        PlanoComplejo s (s = σ + jω)                 Respuesta Temporal v(t)
        
                ^ jω                                        v(t) ^
                │                                                │      /\
         *      │     *  (Polos en semiplano derecho,            │     /  \  /\
                │         σ > 0: Arranque)                       │    /    \/  \
        ────────┼────────> σ                                     └────┴──────────> t
         *      │     *                                             (Exponencial creciente)
                │
                
                ^ jω                                        v(t) ^
                │                                                │   _  _  _  _
         x      │        (Polos en eje imaginario,               │  / \/ \/ \/ \
        ────────┼────────> σ                                     │ /  /\  /\  /\
         x      │        (σ = 0: Régimen permanente)             └─┴──┴──┴──┴──┴─> t
                │                                                   (Sustentado)
```

#### Los tres escenarios de polos en el plano $s$

1. **Polos en el Semiplano Izquierdo ($\sigma < 0$): Oscilación Amortiguada**
   *   *Ubicación:* $s = -\sigma \pm j\omega_0$.
   *   *Respuesta temporal:* $v(t) = V_m e^{-\sigma t} \sin(\omega_0 t)$.
   *   *Efecto:* Las pérdidas del circuito tanque dominan. Si el circuito recibe un impulso, la oscilación se atenúa exponencialmente hasta extinguirse. **No hay oscilación sostenida.**

2. **Polos en el Semiplano Derecho ($\sigma > 0$): Condición de Arranque**
   *   *Ubicación:* $s = +\sigma \pm j\omega_0$.
   *   *Respuesta temporal:* $v(t) = V_m e^{+\sigma t} \sin(\omega_0 t)$.
   *   *Efecto:* Para asegurar que el oscilador arranque solo a partir del ruido térmico ambiental, diseñamos de modo que $|A\beta| > 1$. Los polos inician en el semiplano derecho, lo que genera una **oscilación que crece de manera exponencial**.

3. **Polos sobre el Eje Imaginario ($\sigma = 0$): Régimen Permanente**
   *   *Ubicación:* $s = \pm j\omega_0$ (imaginarios puros).
   *   *Respuesta temporal:* $v(t) = V_m \sin(\omega_0 t)$ (amplitud constante).
   *   *Efecto:* A medida que la señal crece exponencialmente, el circuito activo (transistor u OPAM) comienza a saturarse no linealmente (o actúa un lazo de control AGC). Esta no linealidad reduce la ganancia efectiva del amplificador $A$ hasta que $|A\beta| = 1$ exacto. En ese instante, los polos se desplazan hacia la izquierda y **se estacionan en el eje imaginario**, estabilizando la oscilación en amplitud constante.

---

### 3. Osciladores LC y Compensación de Pérdidas

*(Esperando la explicación de cómo compensa el circuito activo las pérdidas del tanque real...)*
