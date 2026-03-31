---
title: Formulario - Motores Electricos Estaticos y Rotativos
curso: "[[Motores MOC]]"
tipo: formulario
tags:
  - curso/motores
  - tipo/formulario
date: 2026-03-28
---
# Formulario: Motores Eléctricos Estáticos y Rotativos

Este documento contiene las fórmulas y conceptos fundamentales desarrollados durante las primeras sesiones del curso.

## 1. Producción del Campo Magnético
Fuente: [[S01-1 Tema 01 - Como se produce un campo magnético|S01-1 Como se produce un campo magnetico]]

### Ley de Ampère
Establece la relación entre la corriente eléctrica y la intensidad del campo magnético.
$$\oint \vec{H} \cdot d\vec{l} = I_{\text{neta}}$$

Para un núcleo ferromagnético con longitud media $l_n$ y bobina de $N$ vueltas:
$$H \cdot l_n = N \cdot i$$

### Densidad de Flujo Magnético ($B$)
Relación con la intensidad de campo ($H$):
$$B = \mu H$$

Donde:
- $\mu = \mu_0 \mu_r$ (Permeabilidad del material)
- $\mu_0 = 4\pi \times 10^{-7} \, \mathrm{H/m}$ (Vacío)
- $\mu_r = \frac{\mu}{\mu_0}$ (Permeabilidad relativa)

### Flujo Magnético ($\phi$)
$$\phi = \int_A B \, dA$$
Si $B$ es constante y perpendicular al área $A$:
$$\phi = B \cdot A = \frac{\mu N i A}{l_n}$$

---

## 2. Circuitos Magnéticos
Fuente: [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2 Los circuitos magneticos]]

### Ley de Hopkinson (Análoga a la Ley de Ohm)
$$\phi = \frac{F}{\mathcal{R}}$$

### Fuerza Magnetomotriz (FMM)
$$F = N \cdot i$$

### Reluctancia ($\mathcal{R}$)
Oposición al flujo magnético. Para un núcleo uniforme:
$$\mathcal{R} = \frac{l_n}{\mu \cdot A}$$

**Asociación de Reluctancias:**
- **Serie:** $\mathcal{R}_{eq} = \mathcal{R}_1 + \mathcal{R}_2 + \dots$
- **Paralelo:** $\frac{1}{\mathcal{R}_{eq}} = \frac{1}{\mathcal{R}_1} + \frac{1}{\mathcal{R}_2} + \dots$

### Permeancia ($\mathcal{P}$)
Inverso de la reluctancia:
$$\mathcal{P} = \frac{1}{\mathcal{R}} \implies \phi = F \cdot \mathcal{P}$$

---

## 3. Leyes del Electromagnetismo
Fuente: [[S01-3 Tema 02 - Las leyes del electromagnetismo|S01-3 Las leyes del electromagnetismo]]

### Ley de Faraday-Lenz
Inducción de fuerza electromotriz (fem).
$$E = -N \cdot \frac{d\phi}{dt}$$
*El signo negativo indica que la fem se opone a la variación del flujo (Ley de Lenz).*

### Ley de Coulomb
Fuerza entre cargas eléctricas:
$$F = \frac{k \cdot q_1 \cdot q_2}{r^2}$$

### Fuerza de Lorentz
Fuerza total sobre una carga en movimiento dentro de campos eléctricos y magnéticos:
$$\vec{F} = q\vec{E} + q(\vec{v} \times \vec{B})$$

### Ley de Biot-Savart
Campo generado por un elemento de corriente:
$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \cdot d\vec{s} \times \hat{r}}{r^2}$$

---

## 4. Casos Específicos
Fuente: [[S01-5 Tema 04 - Campo magnetico de un toroide|S01-5 Campo magnetico de un toroide]]

### Campo en un Toroide
En el interior de un toroide de radio medio $r$:
$$B = \frac{\mu_0 NI}{2\pi r}$$

### Magnetización en Materiales
- **Magnetización ($M$):** $M = \chi_m H$
- **Relación de Inducción:** $B = \mu_0(H + M) = \mu H$
- **Permeabilidad Relativa:** $\mu_r = 1 + \chi_m$
  *Donde $\chi_m$ es la susceptibilidad magnética.*

---

## 5. Tabla de Unidades SI
Fuente: [[S01-4 Tema 03 - Sistema de unidades|S01-4 Sistema de unidades]]

| Magnitud | Símbolo | Unidad |
| :--- | :---: | :--- |
| Flujo Magnético | $\phi$ | Weber (Wb) |
| Densidad de Flujo (Inducción) | $B$ | Tesla (T) |
| Intensidad de Campo Magnético | $H$ | A-vuelta/m |
| Fuerza Magnetomotriz | $F$ | A-vuelta |
| Reluctancia | $\mathcal{R}$ | A-vuelta/Wb |
| Permeabilidad | $\mu$ | Henry/m (H/m) |
| Potencial Eléctrico | $V, E$ | Voltio (V) |
| Corriente Eléctrica | $I, i$ | Amperio (A) |
