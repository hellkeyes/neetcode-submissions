class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 0 in nums:
            return zero_res(nums, n)

        res = 1
        mylist = []
        for num in nums:
                res *= num 

        for i in nums:
                x = res // i
                mylist.append(x)

        return mylist

def zero_res(nums, n):  
    res = 1
    mylist = []
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
            if zero_count > 1:
                return [0] * n
            continue
        else:
            res *= num

    for i in nums:
        if i == 0:
            mylist.append(res)
        else:
            mylist.append(0)

    return mylist