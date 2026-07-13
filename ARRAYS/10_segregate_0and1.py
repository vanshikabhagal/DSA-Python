class Solution:
    def segregate_0and1(self,arr):
        #getting the total number of 0s 
        count_0 = 0
        for element in arr:
            if element == 0:
                count_0 += 1
        
        #rearranging the array
        for index in range(len(arr)):
            if index < count_0:
                arr[index] = 0
            else:
                arr[index] = 1
        return arr
        
number = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
s1 = Solution()

print(s1.segregate_0and1(number))