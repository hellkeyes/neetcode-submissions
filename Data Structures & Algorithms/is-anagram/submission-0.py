from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Count characters in a string
        s_counter = Counter(s)
        t_counter = Counter(t)

        if s_counter == t_counter:
           return True
        return False