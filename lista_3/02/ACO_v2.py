import random
from Read_Berlin import read_tsp_file

class ACO:
    def __init__(self, distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate, Q):
        self.distance_matrix = distance_matrix
        self.num_cities = distance_matrix.shape[0]
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.Q = Q
        self.pheromone_matrix = np.ones((self.num_cities, self.num_cities)) / self.num_cities

    def run(self):
        shortest_path = None
        shortest_path_length = float('inf')

        for iteration in range(self.num_iterations):
            all_paths = self.construct_solutions()
            self.update_pheromones(all_paths)

            for path, path_length in all_paths:
                if path_length < shortest_path_length:
                    shortest_path = path
                    shortest_path_length = path_length

            print(f"Iteration {iteration+1}: Shortest path length: {shortest_path_length}")

        return shortest_path, shortest_path_length

    def construct_solutions(self):
        all_paths = []
        for _ in range(self.num_ants):
            path = []
            visited = set()
            current_city = random.randint(0, self.num_cities - 1)
            path.append(current_city)
            visited.add(current_city)

            while len(visited) < self.num_cities:
                next_city = self.choose_next_city(current_city, visited)
                path.append(next_city)
                visited.add(next_city)
                current_city = next_city

            path_length = self.calculate_path_length(path)
            all_paths.append((path, path_length))

        return all_paths

    def choose_next_city(self, current_city, visited):
        probabilities = []
        for city in range(self.num_cities):
            if city not in visited:
                tau = self.pheromone_matrix[current_city][city] ** self.alpha
                eta = (1.0 / self.distance_matrix[current_city][city]) ** self.beta
                probabilities.append(tau * eta)
            else:
                probabilities.append(0)

        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()
        next_city = np.random.choice(range(self.num_cities), p=probabilities)
        return next_city

    def calculate_path_length(self, path):
        path_length = 0
        for i in range(len(path) - 1):
            path_length += self.distance_matrix[path[i]][path[i+1]]
        path_length += self.distance_matrix[path[-1]][path[0]]
        return path_length

    def update_pheromones(self, all_paths):
        self.pheromone_matrix *= (1 - self.evaporation_rate)
        for path, path_length in all_paths:
            for i in range(len(path) - 1):
                self.pheromone_matrix[path[i]][path[i+1]] += self.Q / path_length
            self.pheromone_matrix[path[-1]][path[0]] += self.Q / path_length

# Parâmetros do ACO
num_ants = 52
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
Q = 100
file_path = "berlin52.tsp"
tsp_data = read_tsp_file(file_path)


list_of_cities = []
for city in tsp_data['coordinates']:
    list_of_cities.append((city[1],city[2]))


import numpy as np

# Exemplo de coordenadas de cidades
coordinates = np.array(list_of_cities)

# Calculando a matriz de distância
def calculate_distance_matrix(coords):
    num_cities = coords.shape[0]
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = np.linalg.norm(coords[i] - coords[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(coordinates)


# Executando o ACO
aco = ACO(distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate, Q)
shortest_path, shortest_path_length = aco.run()

print(f"Shortest path: {shortest_path}")
print(f"Shortest path length: {shortest_path_length}")

