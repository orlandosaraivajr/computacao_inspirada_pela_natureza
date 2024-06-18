import matplotlib.pyplot as plt
import numpy as np
from Read_Berlin import read_tsp_file
from ACO_v1 import calculate_distance_matrix
from ACO_v1 import ACO

# Parâmetros do ACO
num_ants_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
Q = 100
file_path = "berlin52.tsp"
tsp_data = read_tsp_file(file_path)

list_of_cities = []
cities = {}
for city in tsp_data['coordinates']:
    list_of_cities.append((city[0], city[1], city[2]))
    cities[city[0]] = (city[1],city[2])


# Exemplo de coordenadas de cidades
coordinates = np.array(list_of_cities)
distance_matrix = calculate_distance_matrix(coordinates)

for num_ants in num_ants_list:
    aco = ACO(distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate, Q)
    shortest_path, shortest_path_length = aco.run()
    shortest_path_length = round(shortest_path_length, 2)
    
    print(f"Shortest path: {shortest_path}")
    print(f"Shortest path length: {shortest_path_length}")
    
    
    X = []
    y = []
    for point in shortest_path:
        X.append([cities[point + 1][0]])
        y.append([cities[point + 1][1]])

    plt.title("Número formigas:" + str(num_ants) + "  Menor caminho:" + str(shortest_path_length))
    plt.plot(X, y, marker='x')
    plt.grid(True)
    plt.savefig('ACO_' + str(num_ants) +  '.png')
    plt.clf()

