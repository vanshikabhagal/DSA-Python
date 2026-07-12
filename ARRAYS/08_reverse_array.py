class Solution:
    def reverse_using_python(self, arr):
        self.arr = arr
        arr.reverse()
        return arr
    
    def reverse(self,arr):
        read = len(arr)-1
        for write in range(len(arr)):
            if(write >= read):
                break
            swap = arr[write] 
            arr[write] = arr[read]
            arr[read] = swap
            read -= 1
        return arr
    
array = [1,2,3,4,5]
s1 = Solution()
print(s1.reverse(array))