# Leetcode 121. Best Time to Buy and Sell Stock

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Sliding Window Approach/Two pointer approach
def buy_stock(prices: list[int]) -> int:
    buy_index, sell_index, n, max_profit = 0 , 1, len(prices), 0

    while sell_index < n:
        if prices[sell_index] > prices[buy_index]:
            profit = prices[sell_index] - prices[buy_index]
            max_profit = max(max_profit, profit)
        else:
            buy_index = sell_index
        sell_index += 1
    return max_profit

# n = len(prices)
# O(n) - Time complexity
# O(1) - Space complexity

print(buy_stock([7,1,5,3,6,4])) # 5
print(buy_stock([7,6,4,3,1])) # 0
print(buy_stock([3, 3])) # 0
print(buy_stock([2, 1, 4])) # 3

def buy_sell_stock(prices: list[int]) -> int:
    min_price, max_profit, n = float('inf'), 0, len(prices)

    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
    return max_profit

# n = len(prices)
# O(n) - Time complexity
# O(1) - Space complexity

# Brute-Force Approach
def sell_at_profit(prices: list[int]) -> int:
    max_profix = 0
    n = len(prices)

    for idx, price in enumerate(prices):
        for i in range(idx + 1, n):
            curr_profit = prices[i] - price
            if curr_profit > 0:
                max_profix = max(max_profix, curr_profit)
    return max_profix

# n = len(prices)
# O(n ^ 2) - Time complexity
# O(1) - Space complexity

print(buy_sell_stock([7,1,5,3,6,4])) # 5
print(buy_sell_stock([7,6,4,3,1])) # 0
print(buy_sell_stock([3, 3])) # 0
print(buy_sell_stock([2, 1, 4])) # 3

print(sell_at_profit([7,1,5,3,6,4])) # 5
print(sell_at_profit([7,6,4,3,1])) # 0
print(sell_at_profit([7, 9])) # 2