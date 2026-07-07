# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        if n == 0:
            return pairs

        final_list = []
        final_list.append(pairs.copy())
        for i in range(1, n):
            element = pairs[i]
            pointer = pairs[i].key
            j = i - 1

            while j >= 0 and pointer < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            
            pairs[j + 1] = element
            ss = pairs.copy()
            final_list.append(ss)

        return final_list
        


        