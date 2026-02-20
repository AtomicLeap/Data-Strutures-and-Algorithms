# Leetcode 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/

def solution(str_list: list[str]) -> str:
    prefix_str = ""
    if not str_list:
        return prefix_str
    
    for chars in zip(*str_list):
        if len(set(chars)) > 1:
            break
        prefix_str += chars[0]
        
    return prefix_str

def solution_1(str_list: list[str]) -> str:
    prefix_str = ""

    if not str_list:
        return prefix_str
    
    m = len(str_list)
    common = str_list[0]
    for i in range(m):
        common = str_list[i] if len(str_list[i]) < len(common) else common
    n = len(common)
    
    for i in range(n):
        for j in range(1, m):
            if str_list[j][i] != common[i]:
                return prefix_str
        prefix_str += common[i]
    return prefix_str

def solution_2(strs_list: list[str]) -> str:
    if not strs_list:
        return ""
    prefix = strs_list[0]
    for s in strs_list[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(solution(["flower","flow","flight"]))
print(solution(["dog","racecar","car"]))
print(solution([]))
print(solution_1(["flower","flow","flight"]))
print(solution_1(["dog","racecar","car"]))
print(solution_1([]))