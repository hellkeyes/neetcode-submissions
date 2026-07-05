class Solution:
    def climbStairs(self, n: int) -> int:
        i = 1  # like fobonacci but we start from 1 here
        j = 1
        for x in range(n):
            if x > 0:
                result = i + j
                i = j
                j = result
        return j


        
        
