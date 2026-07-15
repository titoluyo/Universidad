---
title: Circuito equivalente exacto y aproximado del transformador real
curso: "[[Motores MOC]]"
unidad: 2
semana: 7
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-real
  - tema/circuito-equivalente
  - tema/flujo-dispersion
  - tema/reduccion-al-primario
  - tema/impedancia-cortocircuito
date: 2026-05-04
---

![[s07-t01-banner.png]]

## Funcionamiento de un transformador real

En los transformadores reales, la **aparición de resistencia** es inherente a la constitución de los devanados con hilo conductor. En la figura 1 se muestra el circuito del transformador donde se han considerado las resistencias $R_1$ y $R_2$ de los arrollamientos.

En el transformador real también se observa que, de todo el flujo producido por los devanados, **solo existe una parte común a ambos** y representada por $\Phi$, como se muestra en la figura 1.

![[s07-t01-fig1-trafo-real-dispersion.png]]
*Figura 1. Transformador real con resistencias eléctricas y flujos de dispersión.*

### Flujos totales y flujos de dispersión

Si denominamos $\Phi_1$ y $\Phi_2$ a los flujos totales que atraviesan los devanados primario y secundario, y $\Phi_{d1}$, $\Phi_{d2}$ a los **flujos de dispersión** respectivos, se cumple:

$$\Phi_1 = \Phi + \Phi_{d1} \hspace{0.5cm};\hspace{0.5cm} \Phi_2 = \Phi + \Phi_{d2}$$

![[s07-t01-fig2-trafo-bobinas-ideales.png]]
*Figura 2. Transformador real con bobinas ideales en el núcleo.*

En la figura 2 se han indicado con $L_{d1}$ y $L_{d2}$ los **coeficientes de autoinducción** de estas bobinas adicionales (con núcleo de aire), cuyos valores son:

$$L_{d1} = N_1 \, \frac{d\Phi_{d1}}{di_1} \hspace{0.5cm};\hspace{0.5cm} L_{d2} = N_2 \, \frac{d\Phi_{d2}}{di_2}$$

Que dan lugar a las **reactancias de dispersión** $X_1$ y $X_2$ de ambos devanados:

$$X_1 = L_{d1} \, \omega \hspace{0.5cm};\hspace{0.5cm} X_2 = L_{d2} \, \omega$$

### Aplicación de la 2ª ley de Kirchhoff

La aplicación de la 2ª ley de Kirchhoff a los circuitos primario y secundario de la figura 2 da:

$$v_1 = e_1 + R_1 \, i_1 + L_{d1} \, \frac{di_1}{dt} \hspace{0.5cm};\hspace{0.5cm} e_2 = v_2 + R_2 \, i_2 + L_{d2} \, \frac{di_2}{dt}$$

Donde los valores de $e_1$ y $e_2$ vienen expresados por las ecuaciones:

$$e_1 = N_1 \, \frac{d\Phi}{dt} \hspace{0.5cm};\hspace{0.5cm} e_2 = N_2 \, \frac{d\Phi}{dt}$$

Y sus valores eficaces son:

$$E_1 = 4{,}44 \cdot f \cdot N_1 \cdot \Phi_m$$
$$E_2 = 4{,}44 \cdot f \cdot N_2 \cdot \Phi_m$$

Donde $\Phi_m$ es el **flujo común máximo** que circula por el circuito magnético. En forma compleja:

$$\mathbf{V}_1 = \mathbf{E}_1 + R_1 \, \mathbf{I}_1 + jX_1 \, \mathbf{I}_1 \hspace{0.5cm};\hspace{0.5cm} \mathbf{V}_2 = \mathbf{E}_2 - R_2 \, \mathbf{I}_2 - jX_2 \, \mathbf{I}_2$$

## El circuito equivalente de un transformador

**Steinmetz**, a principios del siglo XX, sentó las bases científicas de la tecnología eléctrica. La utilidad de desarrollar **circuitos equivalentes** para máquinas eléctricas radica en la capacidad de aprovechar todo el potencial de la **teoría de redes eléctricas** para anticipar la respuesta de una máquina en condiciones específicas de funcionamiento.

En el contexto del transformador, la creación de un circuito equivalente comienza al **igualar el número de espiras en ambos devanados**. Por lo general, se ajusta el devanado secundario al número de espiras del primario, lo que implica reemplazar el transformador original con otro que tenga el mismo devanado primario con $N_1$ espiras y un nuevo devanado secundario con $N'_2 = N_1$ espiras.

Para que este nuevo transformador sea equivalente al original, es esencial **conservar las condiciones energéticas** de la máquina — las potencias activa y reactiva — así como su distribución entre los distintos elementos del circuito secundario.

![[s07-t01-fig3-circuito-equivalente.png]]
*Figura 3. Circuito equivalente de un transformador.*

### Relaciones entre las magnitudes secundarias

**En el transformador real** se cumple:

$$\frac{E_1}{E_2} = \frac{N_1}{N_2} = a \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} E_2 = \frac{E_1}{a}$$

**En el transformador equivalente** ($N'_2 = N_1$):

$$\frac{E_1}{E'_2} = \frac{N_1}{N'_2} = 1 \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} E'_2 = E_1 = a \, E_2$$

**Potencia aparente** (se conserva entre ambos secundarios):

$$S_2 = E_2 \, I_2 = E'_2 \, I'_2 \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} \boxed{\;I'_2 = \frac{I_2}{a}\;}$$

> [!note] Lectura
> La corriente $I'_2$ del nuevo secundario es **$a$ veces menor** que la corriente $I_2$ que existía en el transformador real.

**Resistencia reflejada** (igualando la potencia activa disipada):

$$R_2 \, I_2^2 = R'_2 \, I'^{2}_2 \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} \boxed{\;R'_2 = a^2 \, R_2\;}$$

**Reactancia reflejada** (igualando la potencia reactiva):

$$X_2 \, I_2^2 = X'_2 \, I'^{2}_2 \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} \boxed{\;X'_2 = a^2 \, X_2\;}$$

**Impedancia de carga reflejada:**

$$\mathbf{Z}'_L = a^2 \, \mathbf{Z}_L$$

Demostración:

$$\mathbf{Z}_L = \frac{\mathbf{V}_2}{\mathbf{I}_2} \hspace{0.3cm}\Longrightarrow\hspace{0.3cm} \mathbf{Z}'_L = \frac{\mathbf{V}'_2}{\mathbf{I}'_2} = \frac{a\,\mathbf{V}_2}{\dfrac{\mathbf{I}_2}{a}} = \frac{a^2 \, \mathbf{V}_2}{\mathbf{I}_2} = a^2 \, \mathbf{Z}_L$$

> [!summary] Regla general de reducción al primario
> Para llevar una magnitud del secundario al lado primario:
> - **Tensiones:** se multiplican por $a$.
> - **Corrientes:** se dividen entre $a$.
> - **Impedancias/Resistencias/Reactancias:** se multiplican por $a^2$.

## Circuito equivalente exacto y aproximado

### Circuito equivalente exacto

Las figuras 4 y 5 reflejan de manera precisa el comportamiento del transformador real — por eso se llama **circuito equivalente exacto**. Se considera un **núcleo con pérdidas**, representado por la **rama en paralelo** por la que circula la **corriente de vacío $I_0$** (esta rama contiene la resistencia $R_{Fe}$ que modela las [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|pérdidas en el hierro]] y la reactancia magnetizante $X_\mu$).

![[s07-t01-fig4-equivalente-exacto-primario.png]]
*Figura 4. Circuito equivalente exacto reducido al primario.*

![[s07-t01-fig5-equivalente-exacto-secundario.png]]
*Figura 5. Circuito equivalente exacto reducido al secundario.*

### Circuito equivalente aproximado

En la práctica, debido al **valor reducido de $I_0$** en comparación con las corrientes $I_1$ e $I_2$, comúnmente se emplea un **circuito equivalente aproximado**. Este se obtiene **desplazando la rama en paralelo** donde se deriva la corriente de vacío a los **terminales de entrada del primario**.

Aunque este circuito aproximado no introduce errores significativos en los cálculos, simplifica considerablemente el análisis de la máquina. Además, es posible simplificar aún más el esquema al observar la **conexión en serie** formada por las ramas primaria y secundaria reducida:

![[s07-t01-fig6-equivalente-aproximado.png]]
*Figura 6. Circuito equivalente aproximado reducido al primario.*

### Impedancia de cortocircuito

Al agrupar las ramas serie del circuito aproximado se obtienen los **parámetros de cortocircuito**:

$$\boxed{\;R_{CC} = R_1 + R'_2 \;:\; \text{resistencia de cortocircuito}\;}$$

$$\boxed{\;X_{CC} = X_1 + X'_2 \;:\; \text{reactancia de cortocircuito}\;}$$

> [!tip] Transformadores grandes
> En transformadores de gran tamaño, donde $X_{CC}$ es considerablemente mayor que $R_{CC}$, es posible emplear **exclusivamente la reactancia serie $X_{CC}$** para representar el circuito equivalente del transformador.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
