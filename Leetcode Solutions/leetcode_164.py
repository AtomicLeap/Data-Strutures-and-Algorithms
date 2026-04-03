# Leetcode 164. Maximum Gap

# https://leetcode.com/problems/maximum-gap/

# Tags -> Array, Sorting, Bucket Sort, Radix Sort

# Idea -> Bucket-based Pigeonhole Principle principle
"""
To find the maximum gap between successive elements in a sorted form of 
the array, we can use a bucket-based approach based on the pigeonhole principle.
1. Find the minimum and maximum values in the array.
2. Calculate the bucket size and the number of buckets needed to cover 
    the range from min to max.
3. Distribute the numbers into the appropriate buckets based on their value.
4. Each bucket will store the minimum and maximum value of the numbers 
    that fall into it.
5. The maximum gap will be the maximum difference between the minimum 
    value of the current bucket and the maximum value of the previous 
    non-empty bucket.
This approach allows us to find the maximum gap in linear time, O(n), 
since we are only iterating through the array and the buckets once.

"""

def maximum_gap(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0

    min_num, max_num = min(nums), max(nums)
    if min_num == max_num:
        return 0

    n = len(nums)
    bucket_size = max(1, (max_num - min_num) // (n - 1))
    bucket_count = (max_num - min_num) // bucket_size + 1

    buckets = [[None, None] for _ in range(bucket_count)]

    for num in nums:
        idx = (num - min_num) // bucket_size
        if buckets[idx][0] is None:
            buckets[idx][0] = num
            buckets[idx][1] = num
        else:
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

    max_gap = 0
    previous_max = None

    for bucket in buckets:
        if bucket[0] is not None:
            if previous_max is not None:
                max_gap = max(max_gap, bucket[0] - previous_max)
            previous_max = bucket[1]

    return max_gap

# O(n) Time complexity
# O(n) Space complexity

print(maximum_gap([3,6,9,1])) # 3
print(maximum_gap([10])) # 0
