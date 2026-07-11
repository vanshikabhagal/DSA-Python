class Solution:
    def removeDuplicates(self,nums):
        write = 1
        for read in range(1, len(nums)):
            if(nums[read] != nums[write - 1]):
                nums[write] = nums[read]
                write += 1
        return write

nums = [0,1,1,2,3,3,3,4,4]

s1 = Solution()
k = s1.removeDuplicates(nums)

print(k)
print(nums[:k])