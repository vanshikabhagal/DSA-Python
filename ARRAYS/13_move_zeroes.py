class Solution:
    def moving_zeroes(self, nums):
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
        return nums
    
arr = [0, 8, 0, 3, 12]
s1 = Solution()
print(s1.moving_zeroes(arr))