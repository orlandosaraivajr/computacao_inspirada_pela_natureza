import numpy as np

y_start = -10
x_start = -10
y_end = 10
x_end = 10

'''
Função de aptidão (fitness)
'''
def fitness(individual):
    x, y = individual
    return (1 - x)**2 + 100 * (y - x**2)**2



if __name__ == '__main__':
    coordenates = []
    fitness_scores = []
    for axis_y in np.arange(x_start, x_end, 0.1):
        for axis_y in np.arange(y_start, y_end, 0.1):
            individual = (axis_y, axis_y)
            coordenates.append(individual)
            fitness_scores.append(fitness(individual))
            dicionario = dict(zip(fitness_scores, coordenates))
        
    best_individual = min(fitness_scores)

    # Imprimir o melhor indivíduo encontrado
    print("Melhor indivíduo encontrado:", dicionario[best_individual])
    print("Valor mínimo encontrado:", best_individual)
