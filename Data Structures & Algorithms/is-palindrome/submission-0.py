class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        mystring = ''
        for i in s:
            if str(i) in "abcdefghijklmnopqrstuvwxyz0123456789":
                mystring += i
            else:
                continue

        reverse_string = mystring[::-1]

        if reverse_string == mystring:
            return True
        return False



# not the optimized one, can apply two pointers
