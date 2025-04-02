import random

# Definição de parâmetros
POPULACAO_TAMANHO = 10
GERACOES = 50
MUTACAO_TAXA = 0.1

# Função de aptidão (fitness)
def fitness(x):
    return x ** 2

# Criar população inicial (valores inteiros entre -10 e 10)
populacao = [random.randint(-10, 10) for _ in range(POPULACAO_TAMANHO)]

for geracao in range(GERACOES):
    # Avaliação da população
    populacao = sorted(populacao, key=fitness, reverse=True)

    # Seleção dos melhores indivíduos (50% superiores)
    pais = populacao[: POPULACAO_TAMANHO // 2]

    # Reprodução (crossover)
    nova_populacao = []
    while len(nova_populacao) < POPULACAO_TAMANHO:
        pai = random.choice(pais)
        mae = random.choice(pais)
        filho = (pai + mae) // 2  # Média dos pais
        nova_populacao.append(filho)

    # Mutação
    for i in range(len(nova_populacao)):
        if random.random() < MUTACAO_TAXA:
            nova_populacao[i] += random.choice([-1, 1])  # Pequena variação

    populacao = nova_populacao

# Melhor solução encontrada
melhor_solucao = max(populacao, key=fitness)
print("Melhor solução encontrada:", melhor_solucao)
