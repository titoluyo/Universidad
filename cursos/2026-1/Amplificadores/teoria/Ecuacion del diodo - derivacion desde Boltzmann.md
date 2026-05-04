---
title: "Ecuacion del diodo - derivacion desde Boltzmann"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
tipo: referencia
tags:
  - curso/amplificadores
  - tipo/referencia
  - tema/diodo
  - tema/ecuacion-de-shockley
  - tema/distribucion-de-boltzmann
  - tema/union-pn
  - tema/voltaje-termico
date: 2026-04-27
---

## Objetivo

Demostrar que el voltaje directo de un diodo PN se relaciona con la corriente que lo atraviesa por la formula:

$$\boxed{V_f = \frac{kT}{q} \ln\left(\frac{I_f}{I_R}\right)}$$

Donde:
- $V_f$ = voltaje en directa del diodo
- $I_f$ = corriente que circula por el diodo
- $I_R$ = corriente inversa de saturacion (parametro fisico del diodo)
- $k$ = constante de Boltzmann ($1.381 \times 10^{-23}$ J/K)
- $T$ = temperatura absoluta (K)
- $q$ = carga del electron ($1.602 \times 10^{-19}$ C)

La derivacion parte de la **distribucion de Maxwell-Boltzmann** aplicada a los portadores de carga en semiconductores y termina en la ecuacion de Shockley (ecuacion ideal del diodo).

---

## 1. Distribucion de Maxwell-Boltzmann

En un sistema en equilibrio termico a temperatura $T$, la probabilidad de que una particula clasica (no degenerada) ocupe un estado con energia $E$ es:

$$f_{MB}(E) = A \, e^{-E / kT}$$

Donde $A$ es una constante de normalizacion.

En semiconductores **no degenerados** (la mayoria de uso practico), los portadores en las bandas de conduccion y valencia siguen esta distribucion respecto al **nivel de Fermi** $E_F$:

$$f(E) \approx e^{-(E - E_F)/kT} \quad \text{(para electrones, con } E - E_F \gg kT)$$

> [!note] Por que Boltzmann y no Fermi-Dirac
> La estadistica exacta para electrones es Fermi-Dirac. Pero cuando los estados estan **lejos** del nivel de Fermi (mas de $\sim 3 \, kT$), la Fermi-Dirac se aproxima a Maxwell-Boltzmann. En semiconductores no degenerados los electrones de la banda de conduccion y los huecos de la valencia cumplen esta condicion.

---

## 2. Concentraciones de portadores en un semiconductor

### Electrones en la banda de conduccion

Integrando la densidad de estados $g_c(E)$ por la probabilidad de Boltzmann:

$$n = \int_{E_C}^{\infty} g_c(E) \, e^{-(E - E_F)/kT} \, dE = N_C \, e^{-(E_C - E_F)/kT}$$

### Huecos en la banda de valencia

$$p = N_V \, e^{-(E_F - E_V)/kT}$$

Donde:
- $N_C$ = densidad efectiva de estados en la banda de conduccion
- $N_V$ = densidad efectiva de estados en la banda de valencia
- $E_C$ = borde inferior de la banda de conduccion
- $E_V$ = borde superior de la banda de valencia
- $E_F$ = nivel de Fermi

### Producto $np$ (ley de accion de masas)

Multiplicando ambas expresiones:

$$np = N_C N_V \, e^{-(E_C - E_V)/kT} = N_C N_V \, e^{-E_g/kT}$$

Donde $E_g = E_C - E_V$ es la **energia de banda prohibida** (gap).

En **semiconductor intrinseco** $n = p = n_i$:

$$\boxed{np = n_i^2 = N_C N_V \, e^{-E_g/kT}}$$

Esta es la **ley de accion de masas**: en equilibrio termico, el producto $np$ es constante, independiente del nivel de dopaje. Para Si a 300 K: $n_i \approx 1.5 \times 10^{10}$ cm$^{-3}$.

---

## 3. Union PN en equilibrio

Al unir un semiconductor tipo P (alto $p_p$) con uno tipo N (alto $n_n$):

```
   region P             |  region N
   p_p = N_A            |  n_n = N_D
   n_p = n_i^2/N_A      |  p_n = n_i^2/N_D
                        |
   (huecos              |   (electrones
    mayoritarios)       |    mayoritarios)
                        |
              <-- union -->
                  |
            zona de carga
              espacial
```

Los electrones difunden de N → P y los huecos de P → N. Esta difusion crea una **carga espacial** (iones donadores y aceptores ya no compensados) que genera un **campo electrico interno** que se opone a la difusion. En equilibrio se alcanza un balance entre **drift** (arrastre por campo) y **difusion**.

### Potencial de contacto $V_{bi}$

En equilibrio, la corriente neta es cero. Para electrones:

$$J_n = \underbrace{q \mu_n n E}_{\text{drift}} + \underbrace{q D_n \frac{dn}{dx}}_{\text{difusion}} = 0$$

Donde $\mu_n$ es la movilidad y $D_n$ el coeficiente de difusion. Despejando $E$:

$$E = -\frac{D_n}{\mu_n} \frac{1}{n} \frac{dn}{dx}$$

Por la **relacion de Einstein**:

$$\frac{D_n}{\mu_n} = \frac{kT}{q}$$

Sustituyendo:

$$E = -\frac{kT}{q} \cdot \frac{1}{n} \cdot \frac{dn}{dx}$$

El campo electrico es el negativo del gradiente del potencial $V$, $E = -dV/dx$. Integrando entre los lados de la union:

$$\int_{V_p}^{V_n} dV = \frac{kT}{q} \int_{n_p}^{n_n} \frac{dn}{n}$$

$$V_n - V_p = \frac{kT}{q} \ln\left(\frac{n_n}{n_p}\right) = V_{bi}$$

Usando $n_n = N_D$, $n_p = n_i^2/N_A$:

$$\boxed{V_{bi} = \frac{kT}{q} \ln\left(\frac{N_A N_D}{n_i^2}\right)}$$

> [!important] Primera aparicion del logaritmo
> El potencial de contacto **ya** tiene la forma $V = (kT/q) \ln(\text{cociente de concentraciones})$. La ecuacion del diodo es la generalizacion de esta relacion bajo polarizacion.

Para Si a 300 K con dopajes tipicos: $V_{bi} \approx 0.7$ V (coincide con la "caida tipica del diodo").

---

## 4. Polarizacion: ley de la union

Cuando se aplica un voltaje externo $V$ (positivo para directa: P+ N-) la barrera de potencial se reduce a $V_{bi} - V$. La condicion de equilibrio se rompe y la difusion supera al drift.

### Concentracion de minoritarios en el borde de la zona

Aplicando el balance modificado, la concentracion de **minoritarios inyectados** en cada lado del borde de la zona de carga espacial es:

$$\boxed{n_p(x_p) = n_{p0} \, e^{V/V_T} \quad ; \quad p_n(x_n) = p_{n0} \, e^{V/V_T}}$$

Donde $V_T = kT/q$. Esta es la **ley de la union** o relacion de Boltzmann para el diodo polarizado.

> [!example] Interpretacion fisica
> - $V > 0$ (directa): la barrera disminuye, mas portadores cruzan, $n_p \uparrow$ y $p_n \uparrow$ exponencialmente
> - $V = 0$: $n_p = n_{p0}$, $p_n = p_{n0}$ (concentraciones de equilibrio)
> - $V < 0$ (inversa): la barrera aumenta, $n_p \to 0$ y $p_n \to 0$ (casi cero)

### Excesos de minoritarios (con respecto al equilibrio)

$$\Delta n_p(x_p) = n_{p0}(e^{V/V_T} - 1)$$

$$\Delta p_n(x_n) = p_{n0}(e^{V/V_T} - 1)$$

---

## 5. Corrientes de difusion: ecuacion de Shockley

Los excesos de minoritarios difunden alejandose de la union y se recombinan. Resolviendo la **ecuacion de difusion** en estado estacionario:

$$\frac{d^2 \Delta n}{dx^2} = \frac{\Delta n}{L_n^2}$$

Con $L_n = \sqrt{D_n \tau_n}$ (longitud de difusion). Las soluciones son exponenciales decrecientes desde el borde de la zona.

La densidad de corriente de difusion en el borde de la zona es:

$$J_n = q D_n \left.\frac{d \Delta n}{dx}\right|_{x_p} = \frac{q D_n n_{p0}}{L_n}(e^{V/V_T} - 1)$$

Analogamente para huecos:

$$J_p = \frac{q D_p p_{n0}}{L_p}(e^{V/V_T} - 1)$$

### Densidad total y corriente

$$J = J_n + J_p = \underbrace{q\left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right)}_{J_S} \cdot (e^{V/V_T} - 1)$$

Multiplicando por el area $A$ de la union:

$$\boxed{I_D = I_S \left(e^{V_D / V_T} - 1\right)} \qquad \text{(ecuacion de Shockley)}$$

Donde:

$$I_S = q A \left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right) = q A n_i^2\left(\frac{D_n}{L_n N_A} + \frac{D_p}{L_p N_D}\right)$$

$I_S$ es la **corriente inversa de saturacion** (en bibliografia tambien aparece como $I_R$, $I_0$ o $I_{ES}$). Es el parametro fisico que caracteriza el diodo: depende de geometria, dopaje, temperatura y material.

> [!note] Comportamiento limite
> - $V_D \to +\infty$ (directa fuerte): $I_D \to I_S e^{V_D/V_T}$ (exponencial)
> - $V_D \to -\infty$ (inversa fuerte): $I_D \to -I_S$ (corriente inversa de saturacion)
> - $V_D = 0$: $I_D = 0$

---

## 6. Despeje de $V_f$ en directa

En polarizacion directa con $V_D \gg V_T$ (~26 mV), o equivalentemente $V_D \gtrsim 4 V_T \approx 100$ mV, el termino $-1$ es despreciable comparado con $e^{V_D/V_T}$:

$$I_f \approx I_R \, e^{V_f/V_T}$$

Donde se ha sustituido $V_D \to V_f$, $I_D \to I_f$ e $I_S \to I_R$ usando la notacion del enunciado.

Despejando la exponencial:

$$\frac{I_f}{I_R} = e^{V_f / V_T}$$

Tomando logaritmo natural en ambos lados:

$$\ln\left(\frac{I_f}{I_R}\right) = \frac{V_f}{V_T}$$

Despejando $V_f$:

$$\boxed{V_f = V_T \, \ln\left(\frac{I_f}{I_R}\right) = \frac{kT}{q} \, \ln\left(\frac{I_f}{I_R}\right)}$$

**Q.E.D.**

---

## 7. Verificacion numerica

Para un diodo de silicio a $T = 300$ K con $I_R = 10^{-12}$ A:

| $I_f$ | $I_f / I_R$ | $\ln(I_f/I_R)$ | $V_f = V_T \ln(\cdot)$ |
| ----- | ----------- | -------------- | ----------------------- |
| 1 nA | $10^3$ | 6.91 | 180 mV |
| 1 uA | $10^6$ | 13.82 | 359 mV |
| 1 mA | $10^9$ | 20.72 | 539 mV |
| 10 mA | $10^{10}$ | 23.03 | 599 mV |
| 100 mA | $10^{11}$ | 25.33 | 659 mV |

→ La caida directa "tipica" de 0.6-0.7 V para corrientes de mA-cientos de mA emerge naturalmente de la ecuacion. Por **cada decada** de aumento en $I_f$, $V_f$ sube **~60 mV** (el factor $\ln(10) \cdot V_T \approx 60$ mV).

---

## 8. Consideraciones reales

La ecuacion de Shockley es ideal. Diodos reales agregan correcciones:

### Factor de idealidad $\eta$

$$I_D = I_S\left(e^{V_D / (\eta V_T)} - 1\right)$$

Con $\eta \in [1, 2]$:
- $\eta = 1$: pura inyeccion-difusion (BJT diode-connected, diodos de baja recombinacion)
- $\eta \approx 2$: dominada por recombinacion en la zona de carga espacial (diodos rapidos, LEDs, baja corriente)

### Resistencia serie $R_S$

A altas corrientes la resistencia ohmica del semiconductor neutro y los contactos hace que:

$$V_{aplicado} = V_D + I_D R_S$$

→ La curva real "se inclina" en lugar de seguir la exponencial pura.

### Generacion-recombinacion en la zona

Agrega un termino adicional a la corriente inversa, especialmente en diodos de Si modernos. Para nuestra derivacion la ignoramos.

### Ruptura inversa

Para $V_D < -V_{BR}$ (Zener o avalancha) la corriente inversa crece bruscamente. La ecuacion de Shockley **no** captura este efecto.

---

## 9. Importancia para amplificadores

Esta ecuacion es la base teorica de:

- [[S06-1 Amplificadores lineales y no lineales#5. Amplificador logaritmico|Amplificador logaritmico]] — usa $V_f = V_T \ln(I_f/I_R)$ directamente
- [[S06-1 Amplificadores lineales y no lineales#6. Amplificador antilogaritmico (exponencial)|Amplificador antilogaritmico]] — usa la forma inversa $I_f = I_R e^{V_f/V_T}$
- **Multiplicadores y divisores analogicos** (combinando log y antilog)
- **Modelo del BJT** — la union B-E sigue la misma ecuacion: $I_C = I_S e^{V_{BE}/V_T}$
- **Caracteristica I-V de cualquier union PN** — diodos rectificadores, Zener, LEDs, fotodiodos

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press. Cap. 3 (PN Junction).
- Pierret, R. F. *Semiconductor Device Fundamentals*. Addison-Wesley. Cap. 5-6.
- Sze, S. M. & Ng, K. K. *Physics of Semiconductor Devices*. Wiley. Cap. 2.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson. Cap. 1.
