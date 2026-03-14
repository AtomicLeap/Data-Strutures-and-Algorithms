# Leetcode 1415. The k-th Lexicographical String of All Happy Strings of Length n

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

# Tags -> String, Backtracking


# Backtracking solution
def get_happy_string(n: int, k: int) -> str:
    results = []

    def dfs(path):
        if len(path) == n:
            results.append("".join(path))
            return
        for ch in ['a', 'b', 'c']:
            if not path or path[-1] != ch:
                path.append(ch)
                dfs(path)
                path.pop()

    dfs([])
    return results[k - 1] if k <= len(results) else ""

# O(n · 2^n) - Time complexity
# O(n) - Space complexity

def get_happy_string_a(n: int, k: int) -> str:
    total = 3 * (1 << (n - 1))
    if k > total:
        return ""

    res = []
    prev = None

    for i in range(n):
        candidates = [ch for ch in ['a', 'b', 'c'] if ch != prev]

        # After choosing current character, remaining positions = n - i - 1
        # Number of valid completions for each choice:
        # 2^(remaining_positions - 1) * 2? Simpler:
        # if remaining_positions == 0 => 1
        # else => 2^(remaining_positions)
        remaining = n - i - 1
        count_per_choice = 1 if remaining == 0 else (1 << remaining)

        for ch in candidates:
            if k > count_per_choice:
                k -= count_per_choice
            else:
                res.append(ch)
                prev = ch
                break

    return "".join(res)

# O(n) - Time complexity
# O(n) - Space complexity

print(get_happy_string(1, 3)) # c
print(get_happy_string(1, 4)) # ""
print(get_happy_string(3, 9)) # cab

print(get_happy_string_a(1, 3)) # c
print(get_happy_string_a(1, 4)) # ""
print(get_happy_string_a(3, 9)) # cab