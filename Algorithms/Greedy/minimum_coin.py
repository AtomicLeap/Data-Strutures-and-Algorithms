# minimum number of coin - Greedy Coin Changing

"""
For a given set of denominations, you are asked to find the minimum 
number of coins with which a given amount of money can be paid. That 
problem can be approached by a greedy algorithm that always selects 
the largest denomination not exceeding the remaining amount of money 
to be paid. As long as the remaining amount is greater than zero, 
the process is repeated.
"""
# Brute-Force solution -- Using Dynamic Programming
def greedy_coin_changingr(coins: list[int], target_sum: int) -> list[int] | None:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    greedy_coins = None
    
    for coin in coins:
        remainder = target_sum - coin
        results = greedy_coin_changingr(coins, remainder)
        if results != None:
           coins_list = results + [coin]
           if not greedy_coins or greedy_coins and len(coins_list) < len(greedy_coins):
                greedy_coins = coins_list
    return greedy_coins

# m = size of target
# n = len(coins) -> number of coin denominations
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

# Optimized (recursive) solution -- Using Dynamic Programming
def greedy_coin_changingo(coins: list[int], target_sum: int) -> list[int] | None:
    memo = {}
    return _greedy_change_helper(coins, target_sum, memo)

def _greedy_change_helper(coins: list[int], target_sum: int, memo: dict[str, int]) -> list[int] | None:
    if str(target_sum) in memo:
        return memo[str(target_sum)]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    best_combination = None
    
    for coin in coins:
        remainder = target_sum - coin
        results = _greedy_change_helper(coins, remainder, memo)
        if results != None:
            combination = results + [coin]
            if not best_combination or best_combination and len(combination) < len(best_combination):
                best_combination = combination
    memo[str(target_sum)] = best_combination
    return best_combination

# m = size of target
# n = len(coins) -> number of coin denominations
# O(m * n) Time complexity
# O(m * m) => O(m^2) Space complexity

# Tabulation solution -- -- Using Dynamic Programming
def greedy_coin_changingi(coins: list[int], target_sum: int) -> list[int] | None:
    table = [None for _ in range(target_sum + 1)]
    table[0] = [] # base case - we need no coin to generate a target sum of zero

    for i in range(target_sum + 1):
        if table[i] != None:
            for coin in coins:
                if i + coin < target_sum + 1:
                    combination = table[i] + [coin]
                    if not table[i + coin] or len(table[i + coin]) > len(combination):
                        table[i + coin] = combination
    return table[target_sum]

# m = size of target
# n = len(coins) -> number of coin denominations
# O(n * m) Time complexity
# O(m * m) => O(m^2) Space complexity => size of the table and created array


# print(greedy_coin_changingo([1, 2, 3, 4, 5], 9)) # [4, 5]
# print(greedy_coin_changingo([1, 2, 3, 4], 6)) # [3, 3]
# print(greedy_coin_changingo([1, 2, 3, 7], 11)) # [2, 2, 7]
# print(greedy_coin_changingo([1, 2, 3, 4, 5, 7, 11], 23)) # [1, 11, 11]
# print('------------------------------------------------')
# print(greedy_coin_changingr([1, 2, 3, 4, 5], 9)) # [4, 5]
# print(greedy_coin_changingr([1, 2, 3, 4], 6)) # [3, 3]
# print(greedy_coin_changingr([1, 2, 3, 7], 11)) # [2, 2, 7]
# print(greedy_coin_changingr([1, 2, 3, 4, 5, 7, 11], 23)) # [1, 11, 11]
# print('------------------------------------------------')
print(greedy_coin_changingi([1, 2, 3, 4, 5], 9)) # [4, 5]
print(greedy_coin_changingi([1, 2, 3, 4], 6)) # [3, 3]
print(greedy_coin_changingi([1, 2, 3, 7], 13)) # [2, 2, 7]
print(greedy_coin_changingi([1, 2, 3, 4, 5, 7, 11], 23)) # [1, 11, 11]
