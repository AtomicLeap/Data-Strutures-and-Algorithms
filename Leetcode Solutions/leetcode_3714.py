# Leetcode 3714. Longest Balanced Substring II

# https://leetcode.com/problems/longest-balanced-substring-ii/description/

def longest_balanced_substring(s: str) -> int:
    n = len(s)
    result = 1  # any single char substring is balanced

    # ---- 1) single-character: longest run ----
    run = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            run += 1
        else:
            result = max(result, run)
            run = 1
    result = max(result, run)

    # ---- helper for 2-char case inside segments that exclude 'bad' ----
    def best_two_chars(bad: str, plus: str, minus: str) -> int:
        best = 0
        diff = 0
        # earliest position (within current segment) where this diff occurred
        first = {0: 0}
        seg_pos = 0  # position index inside the current segment (0..len_seg)

        for ch in s:
            if ch == bad:
                # reset for next segment
                diff = 0
                first = {0: 0}
                seg_pos = 0
                continue

            seg_pos += 1
            if ch == plus:
                diff += 1
            elif ch == minus:
                diff -= 1
            # else: shouldn't happen in this segment, because bad is excluded and alphabet is 3 chars

            if diff in first:
                best = max(best, seg_pos - first[diff])
            else:
                first[diff] = seg_pos

        return best

    # ---- 2) exactly two distinct chars ----
    result = max(result, best_two_chars(bad='c', plus='a', minus='b'))  # only a,b
    result = max(result, best_two_chars(bad='b', plus='a', minus='c'))  # only a,c
    result = max(result, best_two_chars(bad='a', plus='b', minus='c'))  # only b,c

    # ---- 3) all three chars: a=b=c ----
    A = B = C = 0
    first = {(0, 0): 0}  # key -> earliest prefix index
    for i, ch in enumerate(s, 1):  # prefix index i
        if ch == 'a':
            A += 1
        elif ch == 'b':
            B += 1
        else:  # 'c'
            C += 1

        key = (A - B, A - C)
        if key in first:
            result = max(result, i - first[key])
        else:
            first[key] = i

    return result

# O(n) - Time complexity
# O(n) - Space complexity

print(longest_balanced_substring('abbac')) # 4
print(longest_balanced_substring('aabcc')) # 3
print(longest_balanced_substring('aba')) # 2
