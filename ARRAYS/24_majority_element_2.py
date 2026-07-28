class Solution:
    def majority(self, nums):
        # n = len(nums)
        # nums.sort()
        # ans = []
        # count = 1
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #     else:
        #         if count > n//3 :
        #             ans.append(nums[i-1])
        #         count = 1
        # if count > n//3:
        #     ans.append(nums[len(nums)-1])
        # return ans

        #O(n) -- Boyre Moore --#
        res_1 = None
        res_2 = None 
        count_1 = 0
        count_2 = 0
        n = len(nums)
        res = []

        for element in nums:
            #counting frquency of element
            if res_1 == element:
                count_1 += 1
            elif res_2 == element:
                count_2 += 1
            #Setting element as result
            elif count_1 == 0:
                res_1 = element
                count_1 = 1
            elif count_2 == 0:
                res_2 = element
                count_2 = 1
            
            else:
                count_1 -= 1
                count_2 -= 1

        if nums.count(res_1) > n/3:
            res.append(res_1)
        if nums.count(res_2) > n/3:
            res.append(res_2)
        return res
                   


nums = [3,2,3,4,4,4,3]
s1 = Solution()
print(s1.majority(nums))