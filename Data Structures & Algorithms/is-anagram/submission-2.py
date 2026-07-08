class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = find_total_char(s)
        t_freq = find_total_char(t)

        return s_freq == t_freq

def find_total_char(my_string):
    freq = {}
    for ch in my_string:
        if ch not in freq:
            freq[ch] = 1
        else:
            value = freq[ch]
            value = value + 1
            freq[ch] = value
    return freq

#first solution was done using counters
# in this one i make the dict with count of each character in thw string and then compare it