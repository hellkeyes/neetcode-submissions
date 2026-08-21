class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mydict = {}
        for i in nums:
            mydict[i] = mydict.get(i, 0)+1

        for v in mydict.values():
            if v % 2 == 1:
                return False
        return True

        
        