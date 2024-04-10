import random

# Função de aptidão (fitness)
def fitness(individual):
    target_pattern = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    score = 0
    for i in range(len(target_pattern)):
        if individual[i] == target_pattern[i]:
            score += 1
    return score

# Função para gerar população inicial
def generate_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        individual = [random.choice([0, 1]) for _ in range(chromosome_length)]
        population.append(individual)
    return population

# Função de seleção de pais (roleta)
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

# Função de crossover (ponto único)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Função de mutação (bit flip)
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

# Parâmetros do algoritmo genético
population_size = 100
chromosome_length = 12
mutation_rate = 0.001
generations = 100

# Gerar população inicial
population = generate_population(population_size, chromosome_length)

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
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        new_population.extend([child1, child2])
    
    # Substituir a população antiga pela nova geração
    population = new_population

# Encontrar o melhor indivíduo na última geração
best_individual = max(population, key=fitness)

# Imprimir o melhor indivíduo encontrado
print("Melhor indivíduo encontrado:", best_individual)
print("Aptidão:", fitness(best_individual))
