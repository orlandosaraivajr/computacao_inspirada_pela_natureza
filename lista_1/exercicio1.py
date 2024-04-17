import random
import numpy as np


# Definindo o alvo (target)
target = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]

# Definindo o tamanho da população e o número máximo de gerações
population_size = 100
max_generations = 1000

# Definindo as taxas de crossover e mutação
crossover_rate = 0.08
mutation_rate = 0.01

# Função para inicializar a população com indivíduos aleatórios
def initialize_population(population_size, target_length):
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(target_length)]
        population.append(individual)
    return population

# Função para calcular o fitness de um indivíduo
def calculate_fitness(individual, target):
    fitness = sum([1 for i, j in zip(individual, target) if i == j])
    return fitness

# Função para selecionar os pais com base no fitness
def select_parents(population, target):
    parents = []
    total_fitness = sum([calculate_fitness(individual, target) for individual in population])
    while len(parents) < 2:
        candidate = random.choice(population)
        if random.uniform(0, 1) < calculate_fitness(candidate, target) / total_fitness:
            parents.append(candidate)
    return parents

# Função para realizar o crossover
def crossover(parents):
    point = random.randint(1, len(parents[0]) - 1)
    child1 = parents[0][:point] + parents[1][point:]
    child2 = parents[1][:point] + parents[0][point:]
    return child1, child2

# Função para realizar a mutação
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.uniform(0, 1) < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

# Algoritmo genético
def genetic_algorithm(target, population_size, max_generations, crossover_rate, mutation_rate):
    population = initialize_population(population_size, len(target))
    generation = 0
    while generation < max_generations:
        population.sort(key=lambda x: calculate_fitness(x, target), reverse=True)
        best_individual = population[0]
        if best_individual == target:
            return generation
        new_population = [best_individual]
        while len(new_population) < population_size:
            parents = select_parents(population, target)
            if random.uniform(0, 1) < crossover_rate:
                offspring = crossover(parents)
                new_population.extend(offspring)
            else:
                new_population.extend(parents)
        population = [mutate(individual, mutation_rate) for individual in new_population]
        generation += 1
    return max_generations

# Executando várias simulações para testar diferentes taxas de crossover e mutação
num_simulations = 100
results = []

for _ in range(num_simulations):
    
    generations_needed = genetic_algorithm(target, population_size, max_generations, crossover_rate, mutation_rate)
#    print(generations_needed)
    results.append(generations_needed)


print("Número de Simulações: \t\t" + str(num_simulations))
print("Taxa de CrossOver: \t\t" +  str(crossover_rate))
print("Taxa de Mutação: \t\t " +  str(mutation_rate))
print("Número médio de gerações necessárias: ", np.mean(results))