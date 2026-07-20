class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        for number in set(nums):
            count = 0
            for element in nums:
                if element == number:
                    count += 1
                    if count > n//2:
                        return number
    
array = [2,2,1,1,1,2,2]
s1 = Solution()
print(s1.majorityElement(array))