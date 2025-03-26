import numpy as np
import random
"""
0  55  55  86  20  
93  0  33  94  70  
35  53  0  13  32  
29  24  24  0  34  
98  24  73  14  0 
"""

# calcula a distancia da rota em questão, se rota = (1, 2, 3), irá ver a distancia na matriz de 1 até 2, 2 até 3 e 3 até o inicio, somando tudo
def calculate_distance(track, distance):
    return sum(distance[track[i], track[i+1]] for i in range(len(track)-1)) + distance[track[-1], track[0]]

def troca_rota(track, i, j):
    new_track = track[:i] + track[i:j+1][::-1] + track[j+1:]
    return new_track

def local_search(distance : list[list], track : list):
    best_track = track[:] #copia a lista
    best_distance = calculate_distance(best_track, distance)

    # --------------------------------------------------
    improve = True
    while improve:
        improve = False
        for i in range(1, len(track) - 1):
            for j in range(i + 1, len(track) - 1):
                new_track = troca_rota(best_track, i, j)
                new_distance = calculate_distance(new_track, distance)
                if new_distance < best_distance:
                    best_track, best_distance = new_track, new_distance
                    improve = True
                    break
            if improve:
                break
    #--------------------------------------------------------

    return best_track, best_distance



n_cities = 5  # numero de cidades
#create random distances between each city (0 for itself)
distances = np.random.randint(10, 100, (n_cities, n_cities))
np.fill_diagonal(distances, 0)

for i in range(n_cities):
    for j in range(n_cities):
        print(distances[i][j], " ", end="")
    print("")

start_track = list(range(n_cities))
random.shuffle(start_track)

best_track, best_distance = local_search(distances, start_track)

print("Melhor caminho encontrado:", best_track)
print("Melhor distância:", best_distance)

