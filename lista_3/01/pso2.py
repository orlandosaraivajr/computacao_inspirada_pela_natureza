import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyswarms as ps

# Definindo a função de Rosenbrock
def rosenbrock_function(x):
    return (1 - x[:, 0])**2 + 100 * (x[:, 1] - x[:, 0]**2)**2

# Configurações do PSO
options = {'c1': 0.015, 'c2': 0.003, 'w': 0.09}
bounds = (np.array([-5, -5]), np.array([5, 5]))

# Inicializando o otimizador
# Documentação em https://pyswarms.readthedocs.io/en/latest/api/pyswarms.single.html
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=2, options=options, bounds=bounds)

# Variáveis para armazenar a trajetória
position_history = []

# Função de callback para armazenar a trajetória
def record_position(history):
    position_history.append(history.swarm.position)

# Executando a otimização
cost, pos = optimizer.optimize(rosenbrock_function, iters=1000, verbose=False)

# Extraindo a história dos valores de custo
cost_history = optimizer.cost_history
mean_cost_history = np.array([np.mean([rosenbrock_function(p) for p in pos]) for pos in position_history])

# Imprimindo os resultados
print(f"Melhor valor encontrado: {cost}")
print(f"Melhor posição encontrada: {pos}")

# Plotando os valores mínimos e médios ao longo das iterações
plt.figure(figsize=(10, 5))
plt.plot(cost_history, label='Valor Mínimo')
plt.plot(mean_cost_history, label='Valor Médio')
plt.xlabel('Iterações')
plt.ylabel('Valor da Função')
plt.title('Convergência do PSO')
plt.legend()
plt.grid(True)
plt.savefig('PSO2.png')

# Plotando os pontos no plano 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Criando os dados para a superfície
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock_function(np.array([X.ravel(), Y.ravel()]).T).reshape(X.shape)

# Superfície da função de Rosenbrock
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='k')

# Adicionando os pontos da trajetória do enxame
for i in range(len(position_history)):
    particles = position_history[i]
    ax.scatter(particles[:, 0], particles[:, 1], rosenbrock_function(particles), color='red', marker='o', s=10)

ax.set_title("Função de Rosenbrock com Trajetória do Enxame PSO")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig('PSO3.png')
