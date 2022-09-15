#dynamic programming
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for currAmount in range(1, amount + 1):
            if currAmount >= coin:
                dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - coin])

    return dp[amount] if dp[amount] != float('inf') else -1


n = int(input())

for i in range(n):
    coinsSize, amount = input().split(" ")
    amount = int(amount)
    coins = list(map(int, input().split(" ")))
    result = coinChange(coins, amount)
    print(result)