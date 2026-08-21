class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        mynums = []

        for num in nums1:
            if num in nums2:
                mynums.append(num)
                
        return mynums

        