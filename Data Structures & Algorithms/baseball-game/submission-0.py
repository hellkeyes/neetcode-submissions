class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []   #we are gonna save score here

        for n in operations: # to get values 
            if n == 'C':   # we remove the last value in ans
                last = len(ans) - 1 
                ans.pop(last) 
            elif n == 'D':  # we double the last value in ans and append it
                x = int(ans[-1]) * 2
                ans.append(x)
            elif n == '+':    #we add last two values in ans
                y = int(ans[-1]) + int(ans[-2])
                ans.append(y)
            else:     # if we encounter any digits
                z = int(n)
                ans.append(z)

        return sum(ans)  # final sum of the ans 
        