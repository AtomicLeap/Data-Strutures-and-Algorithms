# Leetcode 3. Longest Substring Without Repeating Characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def solution(s: str) -> int:
  count = 0
  final_count = 0
  left = 0
  right = 0
  result = {}
  n = len(s)

  while right < n:
    if s[right].isspace():
      if "space" in result:
        left = max(result["space"] + 1, left)
        result["space"] = right
      else:
        result["space"] = right
    elif s[right] in result:
      left = max(result[s[right]] + 1, left)
      result[s[right]] = right
    else:
      result[s[right]] = right
    
    count = right - left + 1
    final_count = max(final_count, count)
    right += 1
    
  return final_count

# O(n) - Time complexity
# O(n) - Space complexity

print(solution("abcabcbb")) # 3
print(solution("bbbbb")) # 1
print(solution("pwwk  ew"))
print(solution("    eeee  "))
print(solution(" "))


