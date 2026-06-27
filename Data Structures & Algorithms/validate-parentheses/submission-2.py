class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        pairs =  {  #dic to keep track of pairs
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:  # we get the brackets one by one
            if i in pairs:  # we find the pair by key and append value in ans
                ans.append(pairs[i])
            else:  # this means they are closing bracket
                if not ans:   # to check cases where only closing brackets are there
                    return False

                if ans[-1] == i:  #if closind bracket is equal to the last value of ans
                    ans.pop()
                else:
                    return False
                


        if ans == []:
            return True
        else:
            return False

        