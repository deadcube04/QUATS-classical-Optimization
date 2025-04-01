import math
import random
def reorder(order : list, i : int, j : int):
    new_order =  order[:i] + order[i:j+1][::-1] + order[j+1:]
    return new_order

def target_function(x):
    return -(x ** 2) + 4 * x + 5 # quadradica Invertida (parabola invertida)

def simullated_annealing(function, low_limit, high_limit, start_temperature, cooling):#simulated annealing
    x = random.uniform(low_limit, high_limit) # gera x dentro dos limites
    temperature = start_temperature # temperatura = temperatura inicial -> define a aceitação de erro pelo algoritimo

    while temperature > 1e-6: #enquanto a temperatura n chegar no limite (10⁶)

        new_x = x + random.uniform(-0.1, 0.1) # gera um novo X, proximo do maximo atual

        new_x = max(low_limit, min(new_x, high_limit)) #garante q p nvo x esta dentro dos limites

        delta_e = function(new_x) - function(x) #calcula e variação de X

        if delta_e > 0 or random.random() < math.exp(delta_e / temperature): # se a variação for positiva aceita / ou se for pior maisestiver no começo do algoritimo
            x = new_x 
        temperature *= cooling

    return x

result = simullated_annealing(target_function, -10, 10, 100, 0.99)

print(f"best solution found: {result}")