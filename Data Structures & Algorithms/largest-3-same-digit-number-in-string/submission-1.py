class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = set()
        for i in range(len(num) - 2):
            chunk = num[i:i+3]

            if chunk[0] == chunk[1] == chunk[2]:
                good.add(chunk)

        if good:
            return max(good)
        return ""

        