// Leetcode 1. Two Sum

const solution = (nums, target) => {
  const N = nums.length;
  const complementMap = new Map();

  for(let i = 0; i < N; i += 1) {
    const targetSum = target - nums[i];
    if (complementMap.has(targetSum)) {
      return [complementMap.get(targetSum), i]
    }
    complementMap.set(nums[i], i);
  }
  return null;
}

console.log(solution([2, 7, 11,15], 9));
console.log(solution([3, 2, 4], 6));
console.log(solution([3, 3], 6));
