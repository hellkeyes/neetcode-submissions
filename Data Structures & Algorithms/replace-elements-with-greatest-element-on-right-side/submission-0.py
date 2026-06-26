class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            max_value = 0
            for j in range(i + 1, len(arr)):
                print(j)
                if arr[j] > max_value:
                    max_value = arr[j]
            
            arr[i] = max_value
        arr[-1] = -1

        return arr