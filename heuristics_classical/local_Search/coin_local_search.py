import random
def reorder(order : list, i : int, j : int):
    new_order =  order[:i] + order[i:j+1][::-1] + order[j+1:]
    return new_order

def test_payment(new_order : list, price : int):
    new_payment = []
    for coin in new_order:
        while price >= coin[1]:
            price = price - coin[1]
            new_payment.append(coin[0])
    return new_payment


def local_search_trade(coins : dict, price : int) -> list:

    coins_list = list(coins.items())
    random.seed()
    random.shuffle(coins_list)
    best_order = coins_list[:]
    best_payment = test_payment(best_order, price)

    improve = True
    while improve:
        improve = False
        for i in range(len(best_order)-1):
            for j in range(i+1, len(best_order)):
                new_order = reorder(best_order, i, j)
                new_payment = test_payment(new_order, price)
                if len(new_payment) < len(best_payment):
                    best_order, best_payment = new_order, new_payment
                    improve = True
                    break
            if improve:
                break
    return best_payment
                



price = 1283
coins_available = { "copper" : 1,"silver" : 10, "gold" : 100, "platinum" : 500}  # platinum, gold, silver and copper coins

result = local_search_trade(coins_available, price)
print(f"total Platinum coins: {result.count('platinum')}")
print(f"total gold coins: {result.count('gold')}")
print(f"total silver coins: {result.count('silver')}")
print(f"total copper coins: {result.count('copper')}")
