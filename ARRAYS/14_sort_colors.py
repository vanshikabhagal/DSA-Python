class Solution(object):
    def sortColors(self, nums):
        count_red = 0
        count_white = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                count_red += 1
            elif nums[j] == 1:
                count_white += 1
        
        for i in range(len(nums)):
            if i<count_red:
                nums[i] = 0
            elif i>=(count_red+count_white):
                nums[i] = 2
            else:
                nums[i] = 1
        return nums
    
arr = [2, 1, 0, 0, 1, 2]
s1 = Solution()
print(s1.sortColors(arr))