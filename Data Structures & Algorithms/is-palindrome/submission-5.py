import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = "".join(s).lower()
        i = 0
        j = len(s) - 1

        while i <= j:

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True