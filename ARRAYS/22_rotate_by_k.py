class Solution:
    def rotating(self, nums, k):
        # BEST CASE (reversal) #
        n = len(nums)
        k %= n
        
        def reverse(left,right):
            while left<right:
                swap = nums[left]
                nums[left] = nums[right]
                nums[right] = swap
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return nums

        # Optimised #
        # arr = [0]*len(nums)
        # # if k > length of array, we need to optimize.
        # k %= len(nums)
        # for i in range(len(nums)):
        #     arr[(k+i) % len(nums)] = nums[i]
        # return arr

        # Solved in 1st go #
        # round = 0
        # while round < k:
        #     temp = nums[len(nums)-1]
        #     for i in range(len(nums)-1, 0, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = temp
        #     round += 1
        # return nums
        
# :rtype: None Do not return anything, modify nums in-place instead.

arr = [1,2,3,4,5,6,7]
p = 3
s1 = Solution()
print(s1.rotating(arr, p))