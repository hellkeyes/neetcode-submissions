class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_strs = 0

        for num in set_nums:        # iterate in a set
            if (num - 1) not in set_nums:     # check if they are a part of sequence and no previous number means new sequence
                strs = 1

                while (num + strs) in set_nums:    
                    strs += 1
            
                max_strs = max(strs, max_strs)   # compare the max and store it 

        return max_strs



 
