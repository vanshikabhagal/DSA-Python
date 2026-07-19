class Solution:
    def rotate(self, arr):
        temp = arr[len(arr)-1]
        for i in range(len(arr)-1, 0 ,-1):
            arr[i] = arr[i-1]
        arr[0] = temp
        return arr
    
array = [8, 7, 6, 5, 4, 9]
s1 = Solution()
print(s1.rotate(array))