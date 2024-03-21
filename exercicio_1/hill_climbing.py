import logging
from funcao_g import g

logging.basicConfig(filename='hill_climbing.log',  filemode='w',  level=logging.DEBUG)

logging.info('So should this')

def hill_climbing(func, x_start, step_size, max_iter):
    x_current = x_start
    for _ in range(max_iter):
        y_current = func(x_current)
        x_next = x_current + step_size
        y_next = func(x_next)
        if y_next > y_current:
            x_current = x_next
            logging.info('X = \t' + str(x_current) + '\t Y = \t' + str(y_current) )
        else:
            break
    return x_current, func(x_current)

# Parâmetros iniciais
# x_start = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]  # Pontos iniciais
x_start = [0.05, 0.15, 0.25, 0.35,  0.45, 0.55]
step_size = 0.0001  # Tamanho do passo
max_iter = 10000  # Número máximo de iterações


# possible_x 
parciais = {}


for x in x_start:
    logging.warning('Busca com X = \t' + str(x) )
    x_optimal, y_optimal = hill_climbing(g, x, step_size, max_iter)
    print(f'Ponto ótimo local em x = {x_optimal}, y = {y_optimal}')
    parciais[y_optimal] = x_optimal

print(40 *'-')
logging.warning(f'Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')
print(f'Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')

