class Solution:
    def missing_number(self,arr):
        for number in range(len(arr)+1):
            if (number not in arr):
                return number
            
array = [0,3,1]
s1 = Solution()
print(s1.missing_number(array))

#Better Approach
# class Solution:
#     def missing_numbers_addition(self,arr):
#         n = len(arr)
#         actual = sum(arr)
#         expected = n*(n+1)//2
#         return expected - actual