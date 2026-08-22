class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1

        while i < len(nums):
            if nums[i - 1] == nums[i]:
                i += 1

            else:
                nums[j] = nums[i]
                i += 1
                j += 1

        return j
                

           
