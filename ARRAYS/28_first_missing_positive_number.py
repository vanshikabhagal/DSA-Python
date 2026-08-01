class Solution:
    def missingnumber(self, nums):
        n = len(nums)
        for i in range(n):
             while (1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]):
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]
        #first index where the value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

array = [3,2,-1,1]
s1 = Solution()
print(s1.missingnumber(array))