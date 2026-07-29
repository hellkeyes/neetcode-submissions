class Solution:
    def __init__(self):
        self.final_set = set()

    def isHappy(self, n: int) -> bool:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum = total_sum + (digit*digit)
            n = n // 10

        if total_sum == 1:
            return True

        if total_sum in self.final_set:
            return False
        else:
            self.final_set.add(total_sum)
            return self.isHappy(total_sum)
