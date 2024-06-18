import random
from Read_Berlin import read_tsp_file
from ACO_v1 import calculate_distance_matrix
from ACO_v1 import ACO

# Parâmetros do ACO
num_ants = 20
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
Q = 100
file_path = "berlin52.tsp"
tsp_data = read_tsp_file(file_path)


list_of_cities = []
X = []
y = []
for city in tsp_data['coordinates']:
    list_of_cities.append((city[1],city[2]))
    X.append(city[1])
    y.append(city[2])

import numpy as np

# Exemplo de coordenadas de cidades
coordinates = np.array(list_of_cities)

distance_matrix = calculate_distance_matrix(coordinates)

# Executando o ACO
aco = ACO(distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate, Q)
shortest_path, shortest_path_length = aco.run()

print(f"Shortest path: {shortest_path}")
print(f"Shortest path length: {shortest_path_length}")

