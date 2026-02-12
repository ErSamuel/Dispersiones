import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Distribuciones continuas
# Formato: "tecla": [Nombre, Objeto_SciPy, Lista_Nombres_Parametros]
continuas = {
    "1": ["Uniforme Continua", st.uniform, ["Inicio (a)", "Ancho (b-a)"]],
    "2": ["Normal", st.norm, ["Media (μ)", "Desv. Estándar (σ)"]],
    "3": ["Exponencial", st.expon, ["λ (1/λ)"]],
    "4": ["Gama", st.gamma, ["α (forma)","Loc", "λ"]],
    "5": ["Beta", st.beta, ["Parámetro a", "Parámetro b"]],
    "6": ["Weibull", st.weibull_min, ["c (forma)","Loc", "λ"]],
    "7": ["Ji-cuadrada", st.chi2, ["Grados de libertad (n)"]],
    "8": ["t de Student", st.t, ["Grados de libertad (n)"]],
    "9": ["F de Fisher", st.f, ["dfn (numerador)", "dfd (denominador)"]]
}

print("--- Comparativa de Distribuciones Superpuestas ---")
try:
    n_a_graficar = int(input("¿Cuatas distribuciones quieres superponer? "))
except ValueError:
    print("Ingresa un número entero.")
    exit()

seleccionadas = []

# Captura de datos del usuario
for i in range(n_a_graficar):
    print(f"\n--- Configuracion para la Curva {i+1} ---")
    for k, v in continuas.items():
        print(f"[{k}] {v[0]}")
    
    op = input("Selecciona el numero de distribucion: ")
    if op in continuas:
        nombre, func, nombres_params = continuas[op]
        params_usuario = []
        print(f"Configurando {nombre}:")
        for p_nombre in nombres_params:
            if p_nombre=="Loc":
                val=0
            else:
                val = float(input(f"  > {p_nombre}: "))
            params_usuario.append(val)
        
        # Ajuste tecnico para Exponencial (SciPy usa scale = 1/λ)
        if nombre == "Exponencial":
            params_usuario = [ 1/params_usuario[0]]
            
        seleccionadas.append([nombre, func, params_usuario])

# Creacien del grafico unico
plt.figure(figsize=(12, 7))

# Determinamos un rango de X que intente cubrir todas las selecciones
# Rango generico inicial que luego se puede ajustar
x = np.linspace(-5, 40, 1000) 

for nombre, func, params in seleccionadas:
    # Ajustes de rango especificos para que la curva no se vea cortada o vacia
    if nombre == "Beta":
        x_plot = np.linspace(0, 1, 300)
    elif nombre == "Uniforme Continua":
        # Se grafica un poco antes y despues del rango [a, a+ancho]
        inicio = params[0]
        ancho = params[1]
        x_plot = np.linspace(inicio - 1, inicio + ancho + 1, 400)
    elif nombre == "Normal":
        mu, sigma = params[0], params[1]
        x_plot = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)
    else:
        x_plot = x

    # Calculo de la densidad
    y = func.pdf(x_plot, *params)
    
    # Graficar
    plt.plot(x_plot, y, lw=3, label=f"{nombre} (Parametros: {params})", alpha=0.8)
    plt.fill_between(x_plot, y, alpha=0.15)

# Estetica del grafico
plt.title("Distribuciones de Probabilidad Superpuestas", fontsize=16)
plt.xlabel("Valor de la Variable (X)", fontsize=12)
plt.ylabel("Densidad de Probabilidad (PDF)", fontsize=12)
plt.legend(loc='best', fontsize=9)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', lw=1.5) # Eje X resaltado
plt.tight_layout()

print("\nGenerando gráfico... cerciórate de cerrar la ventana del gráfico para terminar.")
plt.show()