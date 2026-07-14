class Solution:
    def check_palindrome(self,nums):
        for element in nums:
            element = str(element)
            start = 0
            end = len(element) - 1
            while start < end:
                if element[start] == element[end]:
                    start += 1
                    end -= 1
                else:
                    return False
        return True

array = [111, 222, 333, 444, 5656 ]
s1 = Solution()
print(s1.check_palindrome(array))