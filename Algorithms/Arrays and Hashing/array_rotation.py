# Array rotation (right rotate by k)

# A) Using modulo (simple, returns a new list)
def rotate_right(arr, k):
    n = len(arr)
    if n == 0: 
        return arr
    k %= n  # wrap k within [0, n]
    return [arr[(i - k) % n] for i in range(n)]

# O(n) Time complexity
# O(n) Space complexity

# B) In-place (no extra array)
def _rev(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1; r -= 1

def rotate_right_inplace(arr, k):
    n = len(arr)
    if n == 0: 
        return arr
    k %= n # Normalize rotation count
    _rev(arr, 0, n - 1) # Step 1: reverse entire array
    _rev(arr, 0, k - 1) # Step 2: reverse first k elements
    _rev(arr, k, n - 1) # Step 3: reverse the rest

    return arr

# O(n) Time complexity
# O(1) Space complexity

print(rotate_right(["a", "b", "c", "d", "e", "f"], 3)) # ['d', 'e', 'f', 'a', 'b', 'c']
print(rotate_right(["a", "b", "c", "d", "e", "f"], 28)) # ['c', 'd', 'e', 'f', 'a', 'b']

print(rotate_right_inplace(["a", "b", "c", "d", "e", "f"], 3)) # ['d', 'e', 'f', 'a', 'b', 'c']
print(rotate_right_inplace(["a", "b", "c", "d", "e", "f"], 28)) # ['c', 'd', 'e', 'f', 'a', 'b']
