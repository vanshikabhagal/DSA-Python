class Solution:
    def sort(self,nums):
        def swap(arr,x,y):
            swap = arr[x]
            arr[x] = arr[y]
            arr[y] = swap
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    swap(nums,i,i+1)
            else:
                if nums[i] < nums[i+1]:
                    swap(nums,i,i+1)
        return nums

array = [1,3,2,2,3,1]
blwh = Solution()
print(blwh.sort(array))  