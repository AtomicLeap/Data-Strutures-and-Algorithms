# Leetcode 706. Design HashMap

# https://leetcode.com/problems/design-hashmap/description

# Tags -> Design, Hash Table

class MyHashMap:
    def __init__(self):
        self.size = 1009  # prime number helps distribute keys better
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # update existing key
                return

        bucket.append((key, value))        # insert new key

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
            
# Time Complexity
"""
Let n be the number of stored keys.
Average case: put: O(1), get: O(1), remove: O(1)

Worst case
If many keys collide into the same bucket:
put: O(n), get: O(n), remove: O(n)
"""

# Space Complexity
# O(n + b), where b is the number of buckets