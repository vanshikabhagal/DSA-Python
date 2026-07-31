class Solution():
    def maximumValue(self, arr):
        max_1 = arr[0]+0
        min_1 = arr[0]+0
        max_2 = arr[0]+0
        min_2 = arr[0]+0

        for i in range(len(arr)):
            val_1 = arr[i]+i
            val_2 = arr[i]-i

            if val_1>max_1:
                max_1 = val_1 
            if val_1<min_1:
                min_1 = val_1

            if val_2>max_2:
                max_2 = val_2 
            if val_2<min_2:
                min_2 = val_2

        ans_1 = max_1 - min_1
        ans_2 = max_2 - min_2
        if ans_1>ans_2:
            return ans_1
        return ans_2
    
nums = [1,2,3,1]
s1 = Solution()
print(s1.maximumValue(nums))
