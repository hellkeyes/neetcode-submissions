class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while j > i:
            k = numbers[i] + numbers[j]

            if k == target:
                return [i+1, j+1]

            if k > target:
                j -= 1
            else:
                i += 1
