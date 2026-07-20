class Solution:
    def majorityElement(self, nums):
        # Came up by myself #
        # n = len(nums)
        # for number in set(nums):
        #     count = 0
        #     for element in nums:
        #         if element == number:
        #             count += 1
        #             if count > n//2:
        #                 return number
    
        # Optimised #
        # n = len(nums)
        # list.sort(nums)
        # return nums[n//2]

        # Boyer - Moore Vooting algorithm #
        freq = 0
        result = 0
        for numbers in nums:
            if freq == 0:
                result = numbers
            if result == numbers:
                freq += 1
            else:
                freq -= 1
        return result
    
array = [2,2,1,1,1,2,2]
s1 = Solution()
print(s1.majorityElement(array))