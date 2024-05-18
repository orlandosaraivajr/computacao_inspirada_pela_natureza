import numpy as np
import matplotlib.pyplot as plt
import pyswarms as ps

# Definição da função de Rosenbrock
def rosenbrock_function(x):
    return (1 - x[:, 0])**2 + 100 * (x[:, 1] - x[:, 0]**2)**2

# Configurações do PSO
options = {'c1': 0.05, 'c2': 0.03, 'w': 0.09}
bounds = (np.array([-5, -5, -5]), np.array([5, 5, 5]))

# Inicializando o otimizador
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=3, options=options, bounds=bounds)

# Executando a otimização
cost, pos = optimizer.optimize(rosenbrock_function, iters=1000)

# Extraindo a história dos valores de custo
cost_history = optimizer.cost_history
mean_cost_history = np.array([np.mean(optimizer.swarm.best_cost) for i in range(1000)])

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
plt.savefig('PSO.png')
