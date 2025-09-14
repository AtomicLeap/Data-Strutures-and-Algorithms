# Binary Search

# Recursive solution
def binary_search_r(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    return _binary_search_helper(arr, target, left, right)

def _binary_search_helper(arr: list[int], target: int, left: int, right: int) -> int:
        if left > right:
             return -1 # Not found
        
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return _binary_search_helper(arr, target, mid + 1, right)
        else:
            return _binary_search_helper(arr, target, left, mid - 1)

# O(log n) Time complexity
# O(1) Space complexity

# Iterative solution
def binary_search_i(arr: list[int], target: int) -> int | None:
    left, right = 0, len(arr) - 1

    while left <= right:
         mid = (left + right) // 2
         if arr[mid] == target:
              return mid
         elif arr[mid] < target:
              left = mid + 1
         else:
            right = mid - 1
    return -1

# O(log n) Time complexity
# O(1) Space complexity

print(binary_search_r([1, 3, 5, 9, 11, 16, 21, 45, 78, 90], 45)) # 7
print(binary_search_r([1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 21], 3)) # 1
print(binary_search_r([1, 3, 5, 9, 11, 16, 21, 45, 78, 90], 3)) # 1
print(binary_search_r([1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 21], 21)) # 10
print('------------------------------------------------------')
print(binary_search_i([1, 3, 5, 9, 11, 16, 21, 45, 78, 90], 45)) # 1
print(binary_search_i([1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 21], 3)) # 1
print(binary_search_i([1, 3, 5, 9, 11, 16, 21, 45, 78, 90], 3)) # 1
print(binary_search_i([1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 21], 21)) # 10