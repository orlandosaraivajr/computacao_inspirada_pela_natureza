import numpy as np
import logging
from funcao_g import g
from simulated_annealing import simulated_annealing
from hill_climbing import hill_climbing

def subida_colina():
    parciais = {}
    x_start = [0.05, 0.15, 0.25, 0.35,  0.45, 0.55]
    # x_start = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    step_size = 0.01
    max_iter = 10000

    for x in x_start:
        logging.warning('Busca com X = \t' + str(x) )
        x_optimal, y_optimal = hill_climbing(g, x, step_size, max_iter)
        print(f'Ponto ótimo local em x = {x_optimal}, y = {y_optimal}')
        parciais[y_optimal] = x_optimal

    print(40 *'-')
    logging.warning((80 *'-'))
    logging.warning(f'Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')
    print(f'Hill Climbing: Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')


def subida_colina2():
    parciais = {}
    x_start = [0.05, 0.15, 0.25, 0.35,  0.45, 0.55]
    # x_start = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    step_size = 0.001  # Passos Menores
    max_iter = 10000

    for x in x_start:
        logging.warning('Busca com X = \t' + str(x) )
        x_optimal, y_optimal = hill_climbing(g, x, step_size, max_iter)
        print(f'Ponto ótimo local em x = {x_optimal}, y = {y_optimal}')
        parciais[y_optimal] = x_optimal


    logging.warning((80 *'-'))
    logging.warning(f'Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')
    print(40 *'-')
    print(f'Hill Climbing: Ponto ótimo global em x = {parciais[max(parciais.keys())]}, y = {max(parciais.keys())}')


def recozimento_simulado():
    # Parâmetros do Recozimento Simulado
    x_start = 0.005  # Ponto inicial
    temp = 100.0  # Temperatura inicial
    cool_rate = 0.99  # Taxa de resfriamento
    max_iter = 10000  # Número máximo de iterações

    x_optimal, y_optimal = simulated_annealing(g, x_start, temp, cool_rate, max_iter)
    logging.warning((80 *'-'))
    logging.warning(f'Simulated Annealing: Ponto ótimo encontrado em x = {x_optimal}, y = {y_optimal}')
    print(f'Simulated Annealing: Ponto ótimo encontrado em x = {x_optimal}, y = {y_optimal}')

def main():
    logging.basicConfig(filename='eventos.log',  filemode='w',  level=logging.DEBUG)
    recozimento_simulado()
    subida_colina()
    subida_colina2()

if __name__ == "__main__":
    main()