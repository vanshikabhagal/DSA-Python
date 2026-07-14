class Solution:
    def consecutive_ones(self, arr):
        count = 0
        count_max = 0
        for element in arr:
            if element == 1:
                count += 1
            elif element == 0:
                if count_max < count:
                    count_max = count
                    count = 0
                else:
                    count = 0
            if count_max < count:
                count_max = count
        return count_max
    
num = [1,1,0,1,1,1]
n1 = Solution()
print(n1.consecutive_ones(num))
