class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        i = 1
        j = 1

        while i < len(nums):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                counter = 1
                i += 1
                j += 1

            else:
                counter += 1
                if counter <= 2:
                    nums[j] = nums[i]
                    j += 1
                i += 1
                    

        return j

            







