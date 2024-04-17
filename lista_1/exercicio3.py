import random
import math

# Parâmetros
population_size = 1000
x_boundaries = (-10, 10)
y_boundaries = (-10, 10)
mutation_rate = 0.1
generations = 5000


'''
Função de aptidão (fitness)
'''
def fitness(individual):
    x, y = individual
    return (1 - x)**2 + 100 * (y - x**2)**2


'''
Função para gerar população inicial
'''
def generate_population(population_size, x_boundaries, y_boundaries):
    population = []
    for _ in range(population_size):
        x = random.uniform(*x_boundaries)
        y = random.uniform(*y_boundaries)
        population.append([x, y])
    return population


'''
# Função de seleção de pais (roleta)
'''
def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = []
    for _ in range(2):
        r = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(probabilities):
            cumulative_prob += prob
            if r <= cumulative_prob:
                parents.append(population[i])
                break
    return parents


'''
Função de crossover (ponto único)
'''
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


'''
Função de mutação (mutação gaussiana)
'''
def mutate(individual, mutation_rate, x_boundaries, y_boundaries):
    mutated_individual = individual[:]
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            if i == 0:
                mutated_individual[i] += random.gauss(0, (x_boundaries[1] - x_boundaries[0]) * 0.1)
            else:
                mutated_individual[i] += random.gauss(0, (y_boundaries[1] - y_boundaries[0]) * 0.1)
            mutated_individual[i] = max(min(mutated_individual[i], y_boundaries[1]), y_boundaries[0])
    return mutated_individual



if __name__ == '__main__':
    # População inicial
    population = generate_population(population_size, x_boundaries, y_boundaries)

    # Executar as gerações
    for generation in range(generations):
        # Calcular a aptidão de cada indivíduo na população
        fitness_scores = [fitness(individual) for individual in population]
        
        # Selecionar pais
        parents = select_parents(population, fitness_scores)
        
        # Realizar crossover e mutação para gerar nova geração
        new_population = []
        while len(new_population) < population_size:
            child1, child2 = crossover(parents[0], parents[1])
            child1 = mutate(child1, mutation_rate, x_boundaries, y_boundaries)
            child2 = mutate(child2, mutation_rate, x_boundaries, y_boundaries)
            new_population.extend([child1, child2])
        
        # Substituir a população antiga pela nova geração
        population = new_population

    # Encontrar o melhor indivíduo na última geração
    best_individual = min(population, key=fitness)

    # Imprimir o melhor indivíduo encontrado
    print("Melhor indivíduo encontrado:", best_individual)
    print("Valor mínimo encontrado:", fitness(best_individual))
