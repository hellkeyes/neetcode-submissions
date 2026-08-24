class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        i = 0
        j = len(nums) - 1

        for i in range(len(nums)):
            k = target - nums[i]

            if k in mydict:
                return [mydict[k], i]
            
            mydict[nums[i]] = i


            



