class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        mystring = []
        i = 0

        while i < len(s):
            if s[i] in mystring:
                longest = max(longest, len(mystring))
                myindex = mystring.index(s[i]) 
                del mystring[0:myindex + 1]
                
            mystring.append(s[i])
            i += 1

        longest = max(longest, len(mystring))

        return longest
