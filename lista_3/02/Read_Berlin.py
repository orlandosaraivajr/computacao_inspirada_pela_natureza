import re

def read_tsp_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    name = ""
    dimension = 0
    edge_weight_type = ""
    node_coord_section = False
    coordinates = []

    for line in lines:
        line = line.strip()
        if line.startswith("NAME"):
            name = re.split(r'[:\s]+', line)[1]
        elif line.startswith("DIMENSION"):
            dimension = int(re.split(r'[:\s]+', line)[1])
        elif line.startswith("EDGE_WEIGHT_TYPE"):
            edge_weight_type = re.split(r'[:\s]+', line)[1]
        elif line.startswith("NODE_COORD_SECTION"):
            node_coord_section = True
        elif node_coord_section:
            if line == "EOF":
                break
            parts = re.split(r'[\s]+', line)
            coordinates.append((int(parts[0]), float(parts[1]), float(parts[2])))

    return {
        "name": name,
        "dimension": dimension,
        "edge_weight_type": edge_weight_type,
        "coordinates": coordinates
    }

# Usando a função para ler o arquivo berlin52.tsp
file_path = "berlin52.tsp"
tsp_data = read_tsp_file(file_path)

# Exibindo os dados lidos
print(f"Nome: {tsp_data['name']}")
print(f"Dimensão: {tsp_data['dimension']}")
print(f"Tipo de Peso de Borda: {tsp_data['edge_weight_type']}")
print("Coordenadas:")
for coord in tsp_data['coordinates']:
    print(f"  Cidade {coord[0]}: ({coord[1]}, {coord[2]})")

