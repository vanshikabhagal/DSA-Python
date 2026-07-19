class Solution:
    def rearrangeBySign(self, nums):
        #creating a list with *same length*
        answer = [None]*len(nums)

        #taking 2 pointers to track index in new list
        positive = 0
        negative = 1

        #filling indices as per the condition
        for element in nums:
            if element >= 0:
                answer[positive] = element
                positive += 2
            else:
                answer[negative] = element
                negative += 2
        return answer
    
array = [3,-2,1,-5,2,-4]
s1 = Solution()
print(s1.rearrangeBySign(array))