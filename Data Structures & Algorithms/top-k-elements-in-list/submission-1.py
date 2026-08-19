class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1

        sorted_list = sorted(mydict, key=mydict.get, reverse=True)

        return sorted_list[:k]
                