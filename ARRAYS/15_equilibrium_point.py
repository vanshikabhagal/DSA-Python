class Solution:
    def eqPoint(self, arr):    
        for index in range(len(arr)):
            sum_left = 0
            sum_right = 0
            for i in range(index):
                sum_left += arr[i]
            for j in range(index+1,len(arr)):
                sum_right += arr[j]
            if sum_left == sum_right:
                return index
        return -1
arr = [1,2,0,3]
s1 = Solution()
print(s1.eqPoint(arr))