class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0 #initiate a pointer write with value 0

        for i in range(len(nums)): # so i scans every element
            if nums[i] != val:    # if not same as our val we overwrite it 
                nums[write] = nums[i]  # write pointer
                write += 1   # increase the counter here

        return write

# We use two pointers: i (read pointer) and write (write pointer). The i pointer scans every element in the array. Whenever nums[i] is not equal to val, we copy that element to nums[write] and increment write. If nums[i] is equal to val, we simply skip it and continue scanning. By the end of the traversal, the first write elements of the array contain all the elements that are not equal to val, and write is the number of valid elements.