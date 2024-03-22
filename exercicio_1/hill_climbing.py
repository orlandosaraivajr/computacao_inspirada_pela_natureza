import logging
from funcao_g import g


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
