# Leetcode 1268. Search Suggestions System

# https://leetcode.com/problems/search-suggestions-system/description/

# Tags -> Array, String

def suggested_products(products: list[str], search_word: str) -> list[list[str]]:
    products.sort()
    prefix = ""
    suggestions = []

    for char in search_word:
        prefix += char
        results = list(filter(lambda x: x.startswith(prefix), products))
        suggestions.append(results[:3])
    return suggestions

# Let m, n, k = len(search_word), len(products), prefix comparison cost
# O(m * n * k) - Time complexity
# O(n) - Space complexity

print(suggested_products(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")) #
print(suggested_products(["havana"], "havana"))