class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # what i think is we can find in which list the element exist by comparing the last element. And then when we find the list, we perform binary search.
        i = 0
        while i < len(matrix):
                n = matrix[i][len(matrix[i]) - 1]
                my_list = matrix[i]
                if n == target:
                    return True

                if n > target:
                    res = self.binary_search(my_list, target)
                    return res
                    
                elif n < target:
                    i += 1

        return False


    def binary_search(self, my_list, target):
        i = 0
        j = len(my_list) - 1
        
        while i <= j:
            mid = (i + j)//2
            if target == my_list[mid]:
                return True
            
            elif target > my_list[mid]:
                i = mid + 1

            else:
                j = mid - 1

        return False
        
        
        