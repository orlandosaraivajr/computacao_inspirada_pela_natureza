import numpy as np
import random
from funcao_g import g


# Parâmetros 
tam_populacao = 1000
taxa_crossover = 0.8
taxa_mutacao = 0.1
max_iter = 1000
minimo_x = 0
maximo_x = 10

# Função para criar uma população inicial
def criar_populacao(tam_populacao):
    return [random.uniform(minimo_x, maximo_x) for _ in range(tam_populacao)]

# Função de seleção de pais
def selecionar_pais(populacao, fitness):
    soma_fitness = sum(fitness)
    probabilidade = [f / soma_fitness for f in fitness]
    pais = []
    for _ in range(2):
        pai = random.choices(populacao, weights=probabilidade)[0]
        pais.append(pai)
    return pais

# Função de crossover
def crossover(pai1, pai2):
    return (pai1 + pai2) / 2

# Função de mutação com uma pequena perturbação aleatória
def mutacao(filho, taxa_mutacao):
    if random.random() < taxa_mutacao:
        filho += random.uniform(-0.1, 0.1)
    return filho


if __name__ == '__main__':
    populacao = criar_populacao(tam_populacao)
    for _ in range(max_iter):
        fitness = [g(x) for x in populacao]
        melhores = sorted(range(len(fitness)), key=lambda i: fitness[i], reverse=True)[:2]
        pais = [populacao[i] for i in melhores]
        filhos = [crossover(pais[0], pais[1]) for _ in range(tam_populacao)]
        populacao = [mutacao(filho, taxa_mutacao) for filho in filhos]
    melhor_idx = max(range(len(fitness)), key=lambda i: fitness[i])
    melhor_valor = fitness[melhor_idx]
    melhor_x = populacao[melhor_idx]

    print("Melhor valor encontrado:", melhor_valor)
    print("Valor de x correspondente:", melhor_x)
