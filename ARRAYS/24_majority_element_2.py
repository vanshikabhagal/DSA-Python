class Solution:
    def majority(self, nums):
        n = len(nums)
        nums.sort()
        ans = []
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if count > n//3 :
                    ans.append(nums[i-1])
                count = 1
        if count > n//3:
            ans.append(nums[len(nums)-1])
        return ans

nums = [3,2,3]
s1 = Solution()
print(s1.majority(nums))