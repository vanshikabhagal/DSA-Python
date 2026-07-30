class Solution():
    def nextPermutation(self, nums):
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot == -1:
            nums.reverse()
            return nums
        
        for j in range(len(nums)-1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[j],nums[pivot] = nums[pivot],nums[j]
                break
        
        left = pivot+1
        right = len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
        return nums

array = [1,2,3,6,5,4]
s1 = Solution()
print(s1.nextPermutation(array))