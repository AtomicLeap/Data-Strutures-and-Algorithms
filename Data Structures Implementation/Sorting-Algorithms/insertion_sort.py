# Insertion sort

def insertion_sort(arr: list[int]):
  N = len(arr)

  for i in range(1, N):
    current = arr[i]
    insert_idx = i
    for j in range(i - 1, -1, -1):
      if arr[j] > current:
       arr[j + 1] = arr[j]
       insert_idx = j
      else:
        break
    arr[insert_idx] = current
  return arr

print(insertion_sort([3, 2, 6, 1, 8, 3, 5, 8]))