import random
import math

def test_payment(new_order : list, price : int):
    new_payment = []
    for coin in new_order:
        while price >= coin[1]:
            price = price - coin[1]
            new_payment.append(coin[0])
    return new_payment


def simullated_annealing_trade(coins : dict, price : int, cooling_factor : float) -> list:
    
    coins_list = list(coins.items())
    
    

    random.seed()
    random.shuffle(coins_list)

    best_order = coins_list[:]
    best_payment = test_payment(best_order, price)
    
    annealing_factor = 100
    while annealing_factor > 0:
        new_order = best_order[:]
        random.shuffle(new_order)

        new_payment = test_payment(new_order, price)

        delta_e = len(best_payment) - len(new_payment)


        if delta_e > 0 or random.random() < math.exp(delta_e / annealing_factor):
            best_order = new_order[:]
            best_payment = new_payment[:]

        annealing_factor -= cooling_factor
    return best_payment

    
                



price = 1283
coins_available = { "copper" : 1, "silver" : 10, "gold" : 100, "platinum" : 500}  # platinum, gold, silver and copper coins

result = simullated_annealing_trade(coins_available, price, 0.01)    
print(f"total Platinum coins: {result.count('platinum')}")
print(f"total gold coins: {result.count('gold')}")
print(f"total silver coins: {result.count('silver')}")
print(f"total copper coins: {result.count('copper')}")
