# Leetcode 271 Encode and Decode Strings

# https://leetcode.com/problems/encode-and-decode-strings/

# https://neetcode.io/problems/string-encode-and-decode

class Codec:
    def encode(self, strs: list[str]) -> str:
        # length-in-characters + '#' + string
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> list[str]:
        result, i, n = [], 0, len(s)
        while i < n:
            # read length up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            result.append(s[j:j+length])
            i = j + length
        return result

# O(n) Time complexity
# O(n) Space complexity

codec = Codec()

print(codec.encode(["leet","code","love","you"])) # 4#leet4#code4#love3#you
print(codec.encode(["we","say",":","yes"])) # 2#we3#say1#:3#yes
print(codec.decode('4#leet4#code4#love3#you')) # ["leet","code","love","you"]
print(codec.decode('2#we3#say1#:3#yes')) # ["we","say",":","yes"]
