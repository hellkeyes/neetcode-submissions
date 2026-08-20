class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_strs = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                strs = 1

                while (num + strs) in set_nums:
                    strs += 1
            
                max_strs = max(strs, max_strs)

        return max_strs



 
