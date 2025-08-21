# Array rotation (right rotate by k)

# A) Using modulo (simple, returns a new list)
def rotate_right(arr, k):
    n = len(arr)
    if n == 0: 
        return arr
    k %= n  # wrap k within [0, n)
    return [arr[(i - k) % n] for i in range(n)]

# B) In-place (no extra array)
def _rev(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1; r -= 1

def rotate_right_inplace(a, k):
    n = len(a)
    if n == 0: 
        return
    k %= n
    _rev(a, 0, n - 1)
    _rev(a, 0, k - 1)
    _rev(a, k, n - 1)



print(rotate_right(["a", "b", "c", "d", "e", "f"], 3))
print(rotate_right(["a", "b", "c", "d", "e", "f"], 28))
# ["c", "d", "e", "f"]