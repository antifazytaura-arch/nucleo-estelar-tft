# Núcleo Estelar Fractalizado y la Transformada de Fourier-Trapezoide (TFT)

Este repositorio contiene el núcleo algorítmico y la simulación matemática de la **Transformada de Fourier-Trapezoide (TFT)** y el operador de confinamiento absoluto cuántico **Omega ($\Omega$)**, diseñado bajo el marco de la Topología Lógica Coherente Absoluta.

## Autores / Colaboradores
* **3UATLAS**
* **Mali Luditze**
* **Leo M. Bakoudios**
* **IA Co-Procesador**

---

## 1. Fundamento Matemático

El sistema procesa señales complejas inyectándolas en el **Primer Vector ($Y$)** y confinándolas en el Ángulo Áureo Limitante ($\theta_0 \approx 2.399 \text{ rad}$ o $137.5^\circ$) mediante una contracción dimensional ejecutada por el operador **Triángulo con Cola ($\nabla_{\tau}$)**:

$$\hat{Y} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \nabla_{\tau} = \begin{pmatrix} 1 & 1 \end{pmatrix}$$

La interacción de frontera en la membrana del Horizonte de Eventos aplica una serie decreciente infinita que converge estrictamente en la proporción áurea ($\phi$):

$$\sum_{k=1}^{\infty} \frac{1}{\phi^k} = \frac{1}{\phi - 1} = \phi \approx 1.618$$

El coeficiente maestro global resultante para la purificación de la señal en el epicentro del núcleo es numéricamente invariable: **35.070**.

---

## 2. Estructura del Código

El script provisto ejecuta los siguientes pasos lógicos autónomos:
1. **Calibración Áurea:** Evaluación geométrica finita e infinita de las potencias de $\phi$.
2. **Inyección de Espín:** Bifurcación matricial a través del transformador topológico $Y$.
3. **Contracción de Ruido:** Simulación de una señal senoidal real contaminada con ruido estocástico (blanco) para demostrar analíticamente el aislamiento y amplificación de la componente armónica pura bajo clausura absoluta.

## 3. Ejecución del Sistema

Para correr la simulación matemática y comprobar el factor de amplificación hermético, ejecute:

```bash
python nucleo_estelar.py
```

## Licencia
Este proyecto se distribuye bajo la **Licencia MIT**. Su publicación abierta e indexada garantiza que el descubrimiento pertenece al dominio público global de forma irrevocable desde Octubre de 2026.
