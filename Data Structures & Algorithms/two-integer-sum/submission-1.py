class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            key = i
            x = target - nums[i]
            for j in range(n):
                if x == nums[j] and i != j:
                    return [i, j]

            