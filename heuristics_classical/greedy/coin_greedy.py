def greedy_trade(coins : dict, price : int) -> list:
    payment = []
    reverse_sorterd_coins = sorted(coins.items(), key=lambda x : x[1], reverse=True)
    for coin in reverse_sorterd_coins:
        while price >= coin[1]:
            price = price - coin[1]
            payment.append(coin[0])
    return payment


price = 1283
coins_available = { "copper" : 1,"silver" : 10, "gold" : 100, "platinum" : 500}  # platinum, gold, silver and copper coins
result = greedy_trade(coins_available, price)

print(f"total Platinum coins: {result.count('platinum')}")
print(f"total gold coins: {result.count('gold')}")
print(f"total silver coins: {result.count('silver')}")
print(f"total copper coins: {result.count('copper')}")
