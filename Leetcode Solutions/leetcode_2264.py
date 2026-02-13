# Leetcode 2264. Largest 3-Same-Digit sber in String

def solution_1(s: str) -> str:
  result = None
  for i in range(len(s) - 2):
    if s[i] == s[i+1] == s[i+2]:
      if result is None or s[i] > result:
        result = s[i]
  return "" if result is None else result * 3

def solution_2(s: str) -> str:
  for digit in "9876543210":
    result = digit * 3
    if result in s:
      return result
  return ""

print(solution_2("6777133339"))
print(solution_2("2300019"))
print(solution_2("42352338"))