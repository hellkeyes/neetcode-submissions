class Solution:
    def firstUniqChar(self, s: str) -> int:
        # mydict = {}
        # for i in s:
        #     mydict[i] = mydict.get(i, 0)+1

        # for i, v in enumerate(mydict.values()):
        #     if v == 1:
        #         return i
        c = Counter(s)

        for i, char in enumerate(s):
            if c[char] == 1:
                return i
        
        return -1