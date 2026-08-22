class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mylist = []
        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = (i + 1)
            k = len(nums) - 1

            while j < k:
                ans = nums[i] + nums[j] + nums[k]

                if ans == 0:
                    mylist.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1


                elif ans < 0:
                    j += 1
                
                else:
                    k -= 1


        return mylist
                    


                

                

                    


            