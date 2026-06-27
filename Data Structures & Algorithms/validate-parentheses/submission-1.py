class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        pairs =  {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in s:
            if i in pairs:
                ans.append(pairs[i])
            else:
                if not ans:
                    return False

                if ans[-1] == i:
                    ans.pop()
                else:
                    return False
                


        if ans == []:
            return True
        else:
            return False

        