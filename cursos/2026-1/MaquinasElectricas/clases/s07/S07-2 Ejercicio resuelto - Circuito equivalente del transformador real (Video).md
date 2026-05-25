---
title: Ejercicio resuelto - Circuito equivalente del transformador real
curso: "[[Motores MOC]]"
unidad: 2
semana: 7
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-real
  - tema/circuito-equivalente
  - tema/ensayo-vacio
  - tema/ensayo-cortocircuito
  - tema/parametros-transformador
date: 2026-05-04
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de circuito equivalente exacto y aproximado del transformador real" (Semana 07, Tema 01). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Considere un transformador monofásico de **50 kVA**, con tensiones nominales de **13 200 V / 220 V**, que se sometió a una prueba donde se ubicaron los **instrumentos de medición en el primario** y se obtuvieron los siguientes resultados:

| Prueba | $V$ | $I$ | $P$ |
| ------ | --- | --- | --- |
| **Circuito abierto** (vacío) | 13 200 V | 0,32 A | 900 W |
| **Cortocircuito** | 850 V | 3,79 A | 380 W |

Se solicita:
- **Determinar las resistencias y reactancias** del transformador, referidas al primario.
- **Dibujar el diagrama** con los valores obtenidos.

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Potencia aparente nominal | $S_n$ | 50 kVA |
| Tensión nominal primaria | $V_{1n}$ | 13 200 V |
| Tensión nominal secundaria | $V_{2n}$ | 220 V |
| Ensayo vacío — tensión aplicada | $V_0$ | 13 200 V |
| Ensayo vacío — corriente medida | $I_0$ | 0,32 A |
| Ensayo vacío — potencia activa | $P_0$ | 900 W |
| Ensayo cortocircuito — tensión | $V_{cc}$ | 850 V |
| Ensayo cortocircuito — corriente | $I_{cc}$ | 3,79 A |
| Ensayo cortocircuito — potencia | $P_{cc}$ | 380 W |

## Desarrollo

### a) Relación de transformación

$$\frac{E_1}{E_2} = \frac{V_{1n}}{V_{2n}} = a$$

$$a = \frac{13\,200}{220}$$

$$\boxed{a = 60}$$

### b) Del ensayo de cortocircuito

Como en el cortocircuito la tensión aplicada $V_{cc}$ es muy pequeña, la corriente $I_0$ por la rama paralela es despreciable y solo queda la rama serie del circuito equivalente aproximado.

**Impedancia de cortocircuito:**

$$Z_{cc} = \frac{V_{cc}}{I_{cc}} = \frac{850}{3{,}79}$$

$$\boxed{Z_{cc} \approx 224{,}27\,\Omega}$$

> Todos los valores están referidos al primario (que es donde se midió). Los explicitamos llamando $\mathbf{Z}_{cc}$ a esta impedancia.

**Resistencia de cortocircuito** (a partir de la potencia disipada):

$$R_{cc} = \frac{P_{cc}}{I_{cc}^{\,2}} = \frac{380}{3{,}79^{2}} = \frac{380}{14{,}36}$$

$$\boxed{R_{cc} \approx 26{,}45\,\Omega}$$

**Reactancia de cortocircuito:**

$$X_{cc} = \sqrt{Z_{cc}^{\,2} - R_{cc}^{\,2}} = \sqrt{224{,}27^{2} - 26{,}45^{2}} = \sqrt{50\,297 - 700}$$

$$\boxed{X_{cc} \approx 222{,}7\,\Omega}$$

### Reparto entre primario y secundario (referidos al primario)

Suponiendo un **reparto igualitario** entre primario y secundario (criterio habitual cuando no se dan más datos):

$$R_1 = R'_2 = \frac{R_{cc}}{2} = \frac{26{,}45}{2}$$

$$\boxed{R_1 = R'_2 \approx 13{,}22\,\Omega}$$

$$X_1 = X'_2 = \frac{X_{cc}}{2} = \frac{222{,}7}{2}$$

$$\boxed{X_1 = X'_2 \approx 111{,}35\,\Omega}$$

### Valores reales del secundario (referidos al secundario)

Aplicando las [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real#Relaciones entre las magnitudes secundarias|relaciones de reducción]] $R_2 = R'_2/a^2$ y $X_2 = X'_2/a^2$:

$$R_2 = \frac{R'_2}{a^2} = \frac{13{,}22}{60^{2}} = \frac{13{,}22}{3\,600}$$

$$\boxed{R_2 \approx 0{,}0037\,\Omega}$$

$$X_2 = \frac{X'_2}{a^2} = \frac{111{,}35}{3\,600}$$

$$\boxed{X_2 \approx 0{,}031\,\Omega}$$

### c) Del ensayo de vacío — Rama paralela (rama de magnetización)

En el ensayo de vacío las corrientes $I_1$ e $I'_2$ del circuito equivalente son cero (no hay carga), por lo que **solo se considera la rama en paralelo**. La resistencia de pérdidas en el hierro es:

$$R_{Fe} = \frac{V_{0}^{\,2}}{P_0} = \frac{13\,200^{2}}{900} = \frac{174\,240\,000}{900}$$

$$\boxed{R_{Fe} \approx 193\,600\,\Omega = 193{,}6\,\text{k}\Omega}$$

> [!note] Significado físico
> $R_{Fe}$ representa la resistencia equivalente que disipa la **potencia de pérdidas en el hierro** (histéresis + Foucault) a tensión nominal. Como $V_0 = V_{1n}$ y la corriente en el cobre es despreciable, todo $P_0$ se va al hierro.

### Reactancia magnetizante (cálculo complementario)

Aunque el guion no lo desarrolla, completamos el modelo:

Corriente de pérdidas en el hierro:
$$I_{Fe} = \frac{V_0}{R_{Fe}} = \frac{13\,200}{193\,600} \approx 0{,}068\,\text{A}$$

Corriente magnetizante:
$$I_\mu = \sqrt{I_0^{\,2} - I_{Fe}^{\,2}} = \sqrt{0{,}32^{2} - 0{,}068^{2}} \approx 0{,}313\,\text{A}$$

Reactancia magnetizante:
$$X_\mu = \frac{V_0}{I_\mu} = \frac{13\,200}{0{,}313}$$

$$\boxed{X_\mu \approx 42{,}2\,\text{k}\Omega}$$

## Resumen de parámetros (referidos al primario)

| Parámetro | Valor | Lado |
| --------- | ----- | ---- |
| Relación de transformación $a$ | $60$ | — |
| $R_1$ | $13{,}22\,\Omega$ | Primario |
| $X_1$ | $111{,}35\,\Omega$ | Primario |
| $R'_2$ | $13{,}22\,\Omega$ | Sec. reducido al primario |
| $X'_2$ | $111{,}35\,\Omega$ | Sec. reducido al primario |
| $R_{Fe}$ | $193{,}6\,\text{k}\Omega$ | Rama paralela |
| $X_\mu$ | $42{,}2\,\text{k}\Omega$ | Rama paralela |
| $R_2$ (valor real) | $0{,}0037\,\Omega$ | Secundario |
| $X_2$ (valor real) | $0{,}031\,\Omega$ | Secundario |

> [!tip] Interpretación
> - $Z_{cc} \gg$ impedancia interna del transformador en operación nominal → buena regulación de tensión.
> - $R_{Fe}$ muy alta y $X_\mu$ relativamente alta → la rama paralela toma una corriente muy pequeña en comparación con la corriente nominal ($I_0 \ll I_{1n}$), lo que justifica el uso del **circuito equivalente aproximado** (ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real#Circuito equivalente aproximado|teoría]]).

## Diagrama final (circuito equivalente aproximado, ref. al primario)

```
                    R₁ = 13.22 Ω   X₁ = 111.35 Ω    R'₂ = 13.22 Ω   X'₂ = 111.35 Ω
   o────[ R_Fe ]──┬─[──/\/\──]──[──))(──]──[──/\/\──]──[──))(──]──o
   │              │
   V₁             X_μ                                              V'₂ → Carga
   │              │
   o──────────────┴────────────────────────────────────────────────o

   R_Fe = 193.6 kΩ     X_μ ≈ 42.2 kΩ
```

## Guion del video

![[s07-t01-ej-guion-circuito-equivalente-real.pdf]]

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
