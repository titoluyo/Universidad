---
title: Ejercicio resuelto - Metodos de analisis Ej1 (Video)
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 6
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/circuito-magnetico
  - tema/curva-imanacion
  - tema/metodo-grafico
date: 2026-04-11
---

> [!info] Fuente
> Video: [Semana 2 - Desarrollo de ejercicios de circuitos ferromagnéticos - Ejercicio 1](https://www.youtube.com/watch?v=FyKr7cBJQxU) — Aprendizaje Virtual UTP (6:25)

## Enunciado

Utilizando la gráfica de las características de inducción magnética $B$ e intensidad de campo magnético $H$ del material (ya sea del gráfico correspondiente o de una tabla de valores), calcular el flujo $\phi$ del circuito magnético de la figura.

![[video2-datos.png]]
**Figura 1.** Circuito magnético del ejercicio con datos

### Datos

- $I = 2{,}5 \, \text{A}$
- $S = 4 \, \text{cm}^2$
- $N = 30$ vueltas
- $l = 20 \, \text{cm}$

---

## Resolución

### Paso 1: Aplicar la [[S01-2 Tema 01 - Los circuitos magnéticos|Ley de Kirchhoff]] para circuitos magnéticos

Recordemos las leyes de Kirchhoff:
- **Primera ley:** toda corriente que ingresa a un nodo debe salir de ese nodo con la misma magnitud
- **Segunda ley:** las caídas de tensiones en un lazo cerrado deben ser igual a cero

Calculamos la fuerza magnetomotriz:

$$N \cdot I = 30 \times 2{,}5 = 75 \, \text{A} \cdot \text{v}$$

![[video2-resultado-NI.png]]
**Figura 2.** Cálculo de $N \cdot I$

Y esto es igual a nuestra [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|fuerza magnetomotriz]], que es igual a la intensidad del campo magnético por la longitud:

$$F = N \cdot I = H \cdot l$$

### Paso 2: Confeccionar tabla $\phi$ vs $F_{mm}$

A partir de la curva de densidad de flujo magnético $B$ vs intensidad de campo magnético $H$, se confecciona una tabla usando las relaciones:

$$\phi = B \cdot S \qquad \text{y} \qquad F_{mm} = H \cdot l$$

![[video2-tabla.png]]
**Figura 3.** Tabla confeccionada a partir de la curva $B = f(H)$

| $\phi \times 10^{-5}$ [Wb] | $B$ [Wb/m²] | $H$ [A/m] | $H \cdot l$ [A.v] |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 25 | 0,625 | 75 | 15 |
| 30 | 0,750 | 100 | 20 |
| 35 | 0,875 | 140 | 28 |
| 40 | 1,000 | 200 | 40 |
| 45 | 1,125 | 330 | 66 |
| 50 | 1,250 | 620 | 124 |

### Paso 3: Obtener el gráfico $\phi$ vs $F_{mm}$ y leer el resultado

Con la tabla se construye el gráfico $\phi$ vs $F_{mm}$:

![[video2-grafico-flujo.png]]
**Figura 4.** Gráfico $\phi$ vs $F_{mm}$ y fórmulas auxiliares

Para $H \cdot l = 75$ A.v, entramos al gráfico y determinamos el valor aproximado del flujo:

![[video2-resultado-final.png]]
**Figura 5.** Lectura del resultado en el gráfico

$$\boxed{\phi \approx 46 \times 10^{-5} \, \text{Wb}}$$

### Verificación por interpolación lineal

De la misma forma se puede determinar dicho valor a partir de la tabla por **interpolación lineal**. Observando que el valor de $H \cdot l = 75$ A.v debe encontrarse entre los valores de la tabla correspondientes a $\phi = 45 \times 10^{-5}$ Wb ($H \cdot l = 66$) y $\phi = 50 \times 10^{-5}$ Wb ($H \cdot l = 124$):

$$\phi \approx 45{,}8 \times 10^{-5} \, \text{Wb}$$

---

## Resultado

$$\boxed{\phi \approx 46 \times 10^{-5} \, \text{Wb} = 0{,}46 \, \text{mWb}}$$

Tanto el método gráfico como la interpolación lineal dan resultados consistentes.
