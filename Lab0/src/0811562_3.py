#dynamic programming bottom up with tabulation

# define dp[i] = the min # of the coins to sum up to i
# base case: dp[0] = 0
# transition function: dp[i] = min(dp[currAmount], 1 + dp[currAmount - coin])
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1) # 0 ~ amount
    dp[0] = 0

    #calculate every value in dp array (bottom up)
    for currAmount in range(1, amount + 1):
        for c in coins:
            if currAmount - c >= 0:
                dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - c])

    return dp[amount] if dp[amount] != float('inf') else -1


n = int(input())

for i in range(n):
    coinsSize, amount = input().split(" ")
    amount = int(amount)
    coins = list(map(int, input().split(" ")))
    coins.sort()    #just to make sure the coins be sorted
    result = coinChange(coins, amount)
    print(result)