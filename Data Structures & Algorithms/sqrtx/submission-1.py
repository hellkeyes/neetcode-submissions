class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2

        if x == 0 or x == 1:
            return x

        while low <= high:
            mid = (low + high) // 2
            guess = mid*mid

            if guess == x:
                return mid
            elif guess > x:
                high = mid - 1
            else:
                low = mid + 1

        return high