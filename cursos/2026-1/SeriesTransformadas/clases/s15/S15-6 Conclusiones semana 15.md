---
title: "Conclusiones — Semana 15: Transformada de Fourier"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 6
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-de-fourier
date: 2026-06-29
---

## Conclusiones de la semana

> [!abstract] Síntesis
> La **transformada de Fourier** generaliza la serie de Fourier al límite $T\to\infty$, permitiendo analizar señales **no periódicas** en el dominio de la frecuencia mediante un **espectro continuo**. Es una herramienta central en procesamiento de señales, comunicaciones e ingeniería.

## Ideas clave

- **Definición:** $F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t}dt$ y su inversa $f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)e^{i\omega t}d\omega$.
- **Propiedades:** linealidad, escalado, traslación en el tiempo ($e^{-i\omega a}$) y derivada ($i\omega$).
- **Transformadas notables:** $\delta(t)\to 1$; constante $\to 2\pi\delta(\omega)$; $\cos/\sin\to$ deltas en $\pm\omega_0$; escalón $\to \pi\delta(\omega)+\frac{1}{i\omega}$; pulso rectangular $\to$ sinc.
- **Dualidad tiempo–frecuencia:** lo concentrado en un dominio se dispersa en el otro (pulso ↔ sinc, delta ↔ constante).
- **Teoría de muestreo:** una señal de banda limitada se reconstruye a partir de muestras espaciadas $< 1/f_M$.

## Mapa de la semana

```
Serie de Fourier compleja (Cn)  --[T→∞]-->  Transformada de Fourier F(ω)
   │                                              │
   ├─ Espectro de línea (discreto)                ├─ Espectro continuo
   └─ Coef. por diferenciación                    ├─ Propiedades (lineal, escala, traslación, derivada)
                                                  ├─ TF elementales (δ, 1, sen/cos, escalón, periódica)
                                                  └─ Aplicación: teoría de muestreo
```

## Siguiente semana

La Unidad 3 continúa en la **Semana 16** con la **Transformada Z** (Parte 1) y el programa **Octave**.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
