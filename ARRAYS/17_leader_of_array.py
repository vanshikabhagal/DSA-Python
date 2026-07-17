class Solution:
    def leaders_present(self, arr):
        leader = []
        max_currently = arr[len(arr)-1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= max_currently:
                leader.append(arr[i])
                max_currently = arr[i]
        leader.reverse()
        return leader
    
nums = [16, 17, 4, 3, 5, 2]
s1 = Solution()
print(s1.leaders_present(nums))