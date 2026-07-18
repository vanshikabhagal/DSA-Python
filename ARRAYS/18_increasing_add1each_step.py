class Solution:
    def arrange_in_increasing(self, arr):
        moves = 0
        for index in range(len(arr)-1):
            if arr[index]>arr[index+1]:
                #Optimal
                moves += arr[index] - arr[index+1]
                arr[index+1] = arr[index]
                #Brute Force
                # while arr[index] != arr[index+1]: 
                #     arr[index+1] += 1 
                #     moves += 1
        return moves
    
nums = [3, 2, 5, 1, 7]
s1 = Solution()
print(s1.arrange_in_increasing(nums))