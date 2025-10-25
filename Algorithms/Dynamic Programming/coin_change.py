# Leetcode 322. Coin Change

# https://leetcode.com/problems/coin-change/description/

# Iterative solution (Tabulation)
def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    table = [None for _ in range(amount + 1)]
    table[0] = [] # base case

    for i in range(amount + 1):
        if table[i] != None:
            for num in coins:
                if i + num < amount + 1:
                    if not table[i + num]:
                        table[i + num] = table[i] + [num]
                    else:
                        combination = table[i] + [num]
                        if len(combination) < len(table[i + num]):
                            table[i + num] = combination
    return len(table[amount]) if table[amount] else -1
# n = len(coins), m = size of amount
# O(m * n) Time complexity
# O(m) Space complexity

# Faster Iterative solution
def coin_change_f(coins, amount):
    # Initialize dp array with infinity (unreachable)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case

    # Build up dp from 1 to amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount is unreachable, return -1
    return dp[amount] if dp[amount] != float('inf') else -1

# n = len(coins), m = size of amount
# O(m * n) Time complexity
# O(m) Space complexity


print(coin_change([1,2,5], 11)) # 3
print(coin_change([2], 3)) # -1
print(coin_change([1], 0)) # 0
print(coin_change([2], 1)) # -1

print(coin_change_f([1,2,5], 11)) # 3
print(coin_change_f([2], 3)) # -1
print(coin_change_f([1], 0)) # 0
print(coin_change_f([2], 1)) # -1

