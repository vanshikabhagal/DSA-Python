class Solution:
    def reverse(self, x):
        neg = False
        if x<0:
            neg = True 
            x = -1*x
        ans = 0
        digit = 0
        while x != 0:
            digit = x % 10 
            ans = (ans*10) + digit
            x = x//10
        if neg==True:
            ans = -1*ans
        if ans>=2**31 or ans <-2**31:
            return 0
        return ans
        
            
a = -123
s1 = Solution()
print(s1.reverse(a))