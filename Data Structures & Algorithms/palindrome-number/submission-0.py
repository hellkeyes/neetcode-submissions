class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        integer = list(str(x)) 
        j = len(integer) - 1

        while i < j:
            if integer[i] == integer[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True

        