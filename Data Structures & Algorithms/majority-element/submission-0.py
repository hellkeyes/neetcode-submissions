class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0)+1

        for key, value in mydict.items():
            if value >= (len(nums)/2):
                return key
                