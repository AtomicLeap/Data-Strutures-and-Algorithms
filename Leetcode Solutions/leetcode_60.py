# Leetcode 60. Permutation Sequence

# https://leetcode.com/problems/permutation-sequence/description/

# Tags -> Math, Backtracking

def get_permutation(n: int, k: int) -> str:
    # Precompute factorials
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i

    # Initialize the list of available numbers
    numbers = [str(i) for i in range(1, n + 1)]
    result = []

    # Adjust k to be zero-indexed
    k -= 1

    for remaining in range(n, 0, -1):
        # Calculate the index of the next number to add
        block_size = factorial[remaining - 1]
        index = k // block_size
        result.append(numbers.pop(index))
        k %= block_size

    return ''.join(result)

# O(n^2) Time complexity, where n is the input number
# O(n) Space complexity

print(get_permutation(3, 3)) # "213"
print(get_permutation(4, 9)) # "2314"
print(get_permutation(3, 1)) # "123"
