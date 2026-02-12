import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import (bernoulli, binom, geom, nbinom, 
                         hypergeom, poisson, randint)

# Configuraci0n de la figura (3 filas, 3 columnas)
fig, axs = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Distribuciones de Probabilidad Discretas', fontsize=20)

# 1. Uniforme Discreta (Dado de 6 caras)
x1 = np.arange(1, 7)
axs[0, 0].bar(x1, randint.pmf(x1, 1, 7), color='skyblue')
axs[0, 0].set_title('Uniforme Discreta (1-6)')

# 2. Bernoulli (p=0.3)
x2 = [0, 1]
axs[0, 1].bar(x2, bernoulli.pmf(x2, 0.3), color='salmon', width=0.4)
axs[0, 1].set_title('Bernoulli (p=0.3)')
axs[0, 1].set_xticks([0, 1])

# 3. Binomial (n=10, p=0.5)
x3 = np.arange(0, 11)
axs[0, 2].bar(x3, binom.pmf(x3, 10, 0.5), color='lightgreen')
axs[0, 2].set_title('Binomial (n=10, p=0.5)')

# 4. Geometrica (p=0.4)
x4 = np.arange(1, 11)
axs[1, 0].bar(x4, geom.pmf(x4, 0.4), color='gold')
axs[1, 0].set_title('Geométrica (p=0.4)')

# 5. Binomial Negativa (n=3, p=0.5)
x5 = np.arange(0, 15)
axs[1, 1].bar(x5, nbinom.pmf(x5, 3, 0.5), color='orchid')
axs[1, 1].set_title('Binomial Negativa (r=3, p=0.5)')

# 6. Hipergeometrica (M=20, n=7, N=12)
# M: total, n: exitos en total, N: muestra
x6 = np.arange(0, 8)
axs[1, 2].bar(x6, hypergeom.pmf(x6, 20, 7, 12), color='coral')
axs[1, 2].set_title('Hipergeométrica (20, 7, 12)')

# 7. Poisson (λ=4)
x7 = np.arange(0, 15)
axs[2, 0].bar(x7, poisson.pmf(x7, 4), color='teal')
axs[2, 0].set_title('Poisson (λ=4)')

# Eliminamos los espacios vacios (los dos ultimos cuadros)
axs[2, 1].axis('off')
axs[2, 2].axis('off')

# Ajuste estetico
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()