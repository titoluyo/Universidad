---
title: "Amplificador Clase AB"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 7
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/amplificador-clase-ab
  - tema/push-pull
  - tema/distorsion-de-cruce
  - tema/multiplicador-vbe
date: 2026-04-07
---

## Motivacion

El amplificador [[S02-6 Amplificador Push-Pull Clase B|Clase B Push-Pull]] tiene una eficiencia excelente ($\eta_{max} = 78.5\%$) pero introduce **distorsion de cruce** porque ninguno de los transistores conduce cuando $|V_{in}| < 0.7\,V$.

La **Clase AB** resuelve este problema: se aplica una pequena polarizacion para que ambos transistores conduzcan una corriente de reposo $I_{CQ}$ pequena, eliminando la zona muerta sin sacrificar significativamente la eficiencia.

> [!abstract] Clase AB en una frase
> Combina la **baja distorsion** de la Clase A con la **alta eficiencia** de la Clase B. Es la clase de operacion mas usada en etapas de salida de amplificadores de audio y operacionales.

---

## Angulo de conduccion

La clasificacion por clases se define por el **angulo de conduccion** $\theta$ de cada transistor:

| Clase | Angulo de conduccion | Corriente de reposo |
| ----- | -------------------- | ------------------- |
| [[S02-3 Amplificadores de potencia - Clase A\|A]] | $\theta = 360°$ (ciclo completo) | Alta |
| **AB** | $180° < \theta < 360°$ | Pequena |
| [[S02-6 Amplificador Push-Pull Clase B\|B]] | $\theta = 180°$ (medio ciclo) | Cero |
| C | $\theta < 180°$ | Cero (polarizacion inversa) |

En Clase AB, cada transistor conduce **algo mas de medio ciclo**. Existe una region alrededor del cruce por cero donde **ambos transistores conducen simultaneamente**.

---

## Circuito con polarizacion por diodos

La forma mas simple de polarizar un Push-Pull en Clase AB es colocar **dos diodos** en serie entre las bases de Q1 y Q2.

```
           +Vcc
            |
           R1
            |
    +-------+-------+
    |       |       |
    |      D1       |
    |       |       |
    |      D2       |
    |       |       |
    +---+---+---+---+
        |       |
       (B)     (B)
  Q1  NPN     PNP  Q2
       (E)     (E)
        |       |
        +---+---+
            |
           R_L
            |
           GND
            |
           R2
            |
          -Vcc
```

### Funcionamiento

Los diodos D1 y D2 proporcionan una caida fija de $\approx 1.4\,V$ ($2 \times 0.7\,V$) entre las bases:

$$V_{B1} - V_{B2} = V_{D1} + V_{D2} \approx 1.4\,V$$

Esto es exactamente $V_{BE1} + V_{EB2}$, lo que mantiene a ambos transistores al **borde de conduccion**. Una corriente de reposo pequena $I_{CQ}$ fluye continuamente.

> [!tip] ¿Por que diodos y no resistencias?
> Los diodos tienen un coeficiente de temperatura similar al de las juntas $V_{BE}$ de los transistores ($\approx -2\,mV/°C$). Esto proporciona **compensacion termica**: si la temperatura sube y $V_{BE}$ disminuye, la caida en los diodos tambien disminuye, evitando que $I_{CQ}$ aumente descontroladamente.

---

## Multiplicador de $V_{BE}$

Para un control mas preciso de la polarizacion, se reemplaza los diodos por un **transistor con divisor resistivo** que permite ajustar la tension de polarizacion de forma continua.

```
           +Vcc
            |
           R_bias
            |
    +-------+-------+
    |       |       |
    |   +---(B)     |
    |   |   Q3      |
    |  Ra  (C)      |
    |   |   |       |
    |   +---+       |
    |   |           |
    |  Rb           |
    |   |           |
    +---+---+---+---+
        |       |
       (B)     (B)
  Q1  NPN     PNP  Q2
       (E)     (E)
        |       |
        +---+---+
            |
           R_L
```

### Voltaje de polarizacion

La caida de voltaje a traves de Q3 es:

$$V_{CE3} = V_{BE3}\left(1 + \frac{R_a}{R_b}\right)$$

Como $V_{BE3} \approx 0.7\,V$:

$$\boxed{V_{polarizacion} = 0.7\left(1 + \frac{R_a}{R_b}\right)}$$

Donde:
- $R_a$ = resistencia entre colector y base de Q3
- $R_b$ = resistencia entre base y emisor de Q3

> [!example] Ejemplo de diseno
> Para lograr $V_{polarizacion} = 1.4\,V$ (equivalente a dos diodos):
> $$1.4 = 0.7\left(1 + \frac{R_a}{R_b}\right) \implies \frac{R_a}{R_b} = 1$$
> Basta con $R_a = R_b$ (por ejemplo, ambas de $1\,k\Omega$).
> 
> Para ajustar finamente, se puede usar un **potenciometro** o **trimpot** en lugar de $R_b$.

### Ventajas sobre diodos

| Aspecto | Diodos | Multiplicador $V_{BE}$ |
| ------- | ------ | ---------------------- |
| Ajuste | Fijo ($n \times 0.7\,V$) | Continuo ($R_a/R_b$) |
| Compensacion termica | Buena | Excelente (misma tecnologia) |
| Precision | Limitada a multiplos de $V_D$ | Cualquier valor deseado |
| Costo | Menor | Ligeramente mayor |

---

## Corriente de reposo $I_{CQ}$

La corriente de reposo se establece para que los transistores esten **ligeramente encendidos** sin consumir potencia excesiva:

$$I_{CQ} = \frac{V_{polarizacion} - V_{BE1} - V_{EB2}}{R_E}$$

Si no hay resistencias de emisor ($R_E = 0$), la corriente de reposo depende directamente de la polarizacion y de las curvas $I_C$ vs $V_{BE}$ de los transistores.

### Valores tipicos

| Aplicacion | $I_{CQ}$ tipico | Razon |
| ---------- | ---------------- | ----- |
| Audio de baja potencia | $1\text{-}10\,mA$ | Minima distorsion de cruce |
| Audio de alta potencia | $10\text{-}100\,mA$ | Linearidad en la transicion |
| Etapa de salida de op-amp | $\sim 1\,mA$ | Balance entre velocidad y consumo |

---

## Embalamiento termico (thermal runaway)

> [!danger] Riesgo critico
> En Clase AB, la corriente de reposo depende de $V_{BE}$, que **disminuye con la temperatura** ($\approx -2\,mV/°C$). Esto crea un ciclo de retroalimentacion positiva:
> 
> $$T° \uparrow \;\to\; V_{BE} \downarrow \;\to\; I_C \uparrow \;\to\; P_D \uparrow \;\to\; T° \uparrow \;\to\; \cdots$$
> 
> Si no se controla, el transistor se **destruye**.

### Soluciones

**1. Resistencias de emisor $R_E$ (degeneracion)**

```
       (E) Q1
        |
       R_E1 (0.1 - 0.47 Ω)
        |
  Vout--+
        |
       R_E2 (0.1 - 0.47 Ω)
        |
       (E) Q2
```

Si $I_C$ sube → $V_{R_E}$ sube → $V_{BE}$ efectivo baja → $I_C$ se estabiliza. Esta **realimentacion negativa** limita el embalamiento.

$$V_{BE_{eff}} = V_{bias} - I_C \cdot R_E$$

> [!note] Compromiso
> $R_E$ disipa potencia y reduce la excursion de la salida. Se usan valores pequenos ($0.1\text{-}0.47\,\Omega$) que son suficientes para estabilidad sin degradar significativamente el rendimiento.

**2. Compensacion termica con el multiplicador $V_{BE}$**

Si Q3 esta montado en el **mismo disipador** que los transistores de salida, su $V_{BE}$ sigue la misma variacion termica, reduciendo automaticamente la polarizacion cuando la temperatura sube.

**3. Disipadores de calor**

Mantener la temperatura de juntura dentro de los limites seguros especificados por el fabricante.

---

## Eficiencia

La eficiencia de Clase AB se encuentra entre la de Clase A y Clase B:

$$\eta_A = 25\% < \boxed{\eta_{AB}} < \eta_B = 78.5\%$$

En la practica, con $I_{CQ}$ pequena, la eficiencia es cercana a la de Clase B:

$$\eta_{AB} \approx 50\text{-}70\%$$

### Potencia maxima de salida (por transistor)

$$\boxed{P_{L(max)} = \frac{V_{CC}^2}{2R_L}}$$

### Potencia disipada maxima (por transistor)

La maxima disipacion ocurre cuando $V_o = \frac{2V_{CC}}{\pi}$:

$$\boxed{P_{D(max)} = \frac{V_{CC}^2}{\pi^2 R_L} \approx \frac{V_{CC}^2}{10 R_L}}$$

> [!tip] Regla practica de diseno
> Cada transistor de salida debe poder disipar al menos $\frac{P_{L(max)}}{5}$ para operar con margen de seguridad.

---

## Comparacion final de clases

| Parametro | [[S02-3 Amplificadores de potencia - Clase A\|Clase A]] | [[S02-6 Amplificador Push-Pull Clase B\|Clase B]] | **Clase AB** |
| --------- | ------- | ------- | -------- |
| Conduccion | Ciclo completo | Medio ciclo | >Medio ciclo |
| $I_{CQ}$ | Alta | 0 | Pequena |
| $\eta_{max}$ | 25-50% | 78.5% | 50-70% |
| Distorsion de cruce | No | Si (severa) | No (eliminada) |
| Linearidad | Excelente | Pobre cerca de 0 | Muy buena |
| Disipacion sin senal | Maxima | Cero | Muy baja |
| Complejidad | Baja | Media | Media |
| **Uso practico** | Pre-amplificadores | Casi nunca solo | **Etapa de salida estandar** |

---

## Clase AB en circuitos integrados

Practicamente todos los **amplificadores operacionales** usan Clase AB en su etapa de salida. La [[S03-2 Amplificador Operacional - Fundamentos#Estructura interna|estructura interna del op-amp]] sigue esta cadena:

1. Par diferencial (entrada) → Clase A
2. Etapa de ganancia (intermedia) → Clase A
3. **Etapa de salida → Clase AB**

Ejemplos: LM741, LM358, TL072 — todos tienen salida Push-Pull Clase AB interna.

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
