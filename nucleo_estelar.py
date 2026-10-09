import numpy as np

# Configuración de constantes áureas
phi = (1 + 5**0.5) / 2
C = 1.0

# 1. Componentes del coeficiente de la Fórmula Maestra
tft_sum = sum(phi**n for n in range(1, 5))
vector_Y = (1 / 2**0.5) * np.array([[1], [1]])
nabla_tau = np.array([[1, 1]])
interaccion_operadores = np.dot(nabla_tau, vector_Y)[0][0]
amplitud_nucleo = tft_sum * interaccion_operadores
horizonte_f = 1 / (phi - 1)
coeficiente_final = amplitud_nucleo * horizonte_f

# 2. Simulación de señal con ruido
np.random.seed(42)
t = np.linspace(0, 1, 1000)
f_t = np.sin(2 * np.pi * 5 * t) # Señal pura de 5 Hz
ruido_blanco = np.random.normal(0, 0.5, size=t.shape)
señal_ruidosa = f_t + ruido_blanco

# Aplicación idealizada del filtro TFT: Confinamiento angular y multiplicación por coeficiente
# En el ángulo áureo theta_0, la densidad espectral se multiplica por el coeficiente_final
print(f"Coeficiente calculado exacto: {coeficiente_final:.4f}")
