# Leetcode 2573. Find the String with LCP

# https://leetcode.com/problems/find-the-string-with-lcp/description

# Tags -> String, Greedy

def find_the_string(lcp: list[list[int]]) -> str:
    n = len(lcp)
    letters = [0] * n
    current_letter = 1

    for r in range(n):
        if letters[r]:
            continue
        if current_letter > 26:
            return ""
        for c in range(r, n):
            if lcp[r][c]:
                letters[c] = current_letter
        current_letter += 1

    for r in range(n):
        for c in range(n):
            if letters[r] != letters[c]:
                expected_lcp = 0
            else:
                expected_lcp = (lcp[r + 1][c + 1] if r < n - 1 and c < n - 1 else 0) + 1
            if expected_lcp != lcp[r][c]:
                return ""
    results = ""
    for letter in letters:
        results += chr(ord('a') - 1 + letter)
    return results


# O(n^2) Time complexity
# O(n) Space complexity

# Examples
print(find_the_string([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]])) # "abab"
print(find_the_string([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]])) # "aaaa"
print(find_the_string([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]])) # ""  