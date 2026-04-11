---
title: "Amplificador Push-Pull Clase B"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 6
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/amplificador-clase-b
  - tema/push-pull
  - tema/distorsion-de-cruce
date: 2026-04-07
---

## Concepto

El Push-Pull es una configuracion que usa **dos transistores complementarios** (NPN y PNP) que trabajan **alternadamente**, cada uno conduciendo un semiciclo de la senal:

- **Push (empujar):** el transistor NPN conduce durante el semiciclo **positivo**, entregando corriente a la carga
- **Pull (jalar):** el transistor PNP conduce durante el semiciclo **negativo**, absorbiendo corriente de la carga

## ¿Por que se necesita?

Un amplificador **Clase B** solo conduce medio ciclo. Con un solo transistor se pierde la otra mitad de la senal. La solucion es usar **dos transistores en Push-Pull** que entre ambos reconstruyen la senal completa.

## Circuito basico (simetria complementaria)

```
        +Vcc
         |
        NPN (Q1)  ← conduce semiciclo positivo
         |
Vin -----+------→ Vout (carga RL a GND)
         |
        PNP (Q2)  ← conduce semiciclo negativo
         |
        -Vcc
```

### Funcionamiento

1. Cuando $V_{in} > 0$ → Q1 (NPN) conduce, Q2 esta en corte
2. Cuando $V_{in} < 0$ → Q2 (PNP) conduce, Q1 esta en corte
3. La carga recibe la senal **completa**

## Distorsion de cruce (crossover)

> [!warning] Zona muerta
> Cuando la senal pasa por **0 V**, ninguno de los dos transistores conduce (necesitan $\approx 0.7\,V$ para activarse). Esto produce una **zona muerta** en la salida.

$$V_{in} \in [-0.7\,V,\; +0.7\,V] \implies \text{ningun transistor conduce}$$

La forma de onda de salida presenta una deformacion alrededor del cruce por cero, introduciendo **armonicos no deseados**.

## Solucion: Clase AB

Se agrega una pequena polarizacion (con diodos o resistencias) para que ambos transistores esten *ligeramente* encendidos cerca de 0 V:

- Se colocan **dos diodos** (o un multiplicador $V_{BE}$) entre las bases de Q1 y Q2
- Esto proporciona una caida de $\approx 1.4\,V$ que mantiene ambos transistores al borde de conduccion
- Elimina la zona muerta con minimo impacto en la eficiencia

## Eficiencia

$$\boxed{\eta_{max} = \frac{\pi}{4} \approx 78.5\%}$$

Mucho mayor que la [[S02-3 Amplificadores de potencia - Clase A|Clase A]] (25-50%).

## Ventajas del Push-Pull

- **Alta eficiencia** ($\sim 78.5\%$) comparado con Clase A
- **Cancela armonicos pares** por la simetria del circuito
- **Sin corriente de reposo** en Clase B pura → sin disipacion cuando no hay senal
- Ideal como **etapa de salida** en amplificadores de audio y de potencia

## Desventajas

- **Distorsion de cruce** en Clase B pura (se resuelve con Clase AB)
- Requiere **transistores complementarios** con caracteristicas similares (matched pair)
- Mayor complejidad de circuito comparado con Clase A

## Comparacion de clases

| Clase | Conduccion | $\eta_{max}$ | Distorsion | Uso tipico |
| ----- | ---------- | ------------- | ---------- | ---------- |
| **A** | Ciclo completo | 25-50% | Baja | Pre-amplificadores, audio hi-fi |
| **B** | Medio ciclo | 78.5% | Cruce | Etapas de potencia (con AB) |
| **AB** | >Medio ciclo | 50-78.5% | Muy baja | Etapas de salida en la practica |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
