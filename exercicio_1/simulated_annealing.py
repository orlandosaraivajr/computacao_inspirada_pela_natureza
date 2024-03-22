import numpy as np
import logging
from funcao_g import g


def simulated_annealing(func, x_start, temp, cool_rate, max_iter):
    x_current = x_start
    y_current = func(x_current)
    best_solution = x_current
    best_score = y_current

    for i in range(max_iter):
        # Resfriamento da temperatura
        temp *= cool_rate

        # Gerando uma nova solução próxima à atual
        x_next = max(min(x_current + np.random.normal(0, 0.1), 1), 0)
        y_next = func(x_next)

        # Calculando a variação de energia (score)
        delta_e = y_next - y_current

        # Aceitando a nova solução se for melhor ou seguindo critério de probabilidade
        if delta_e < 0 or np.random.rand() < np.exp(-delta_e / temp):
            x_current = x_next
            y_current = y_next

        # Atualizando a melhor solução encontrada até agora
        if y_current > best_score:
            best_solution = x_current
            best_score = y_current
            logging.info('X = \t' + str(x_current) + '\t Y = \t' + str(y_current) )

    return best_solution, best_score

