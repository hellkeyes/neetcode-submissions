class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        s = s.lower()
        allowed = "abcdefghijklmnopqrstuvwxyz1234567890"

        while i <= j:
            while i < j and s[i] not in  allowed:
                i += 1

            while i < j and s[j] not in allowed:
                j -= 1

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True