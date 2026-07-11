class SecondLargest:
    def largest(self,arr):
        largest = arr[0]
        for element in arr:
            if(largest < element):
                largest = element
        return largest
    
    def second_largest(self,arr):
        largest = self.largest(arr)
        second_largest = -1
        new_arr =[]
        for element in arr:
            if(element != largest(arr)):
                new_arr.append(element)
        
        if(new_arr == []):
            return -1
        
        for element in new_arr:
            if(second_largest < element):
                second_largest = element
        return second_largest

obj1 = [12, 35, 1, 10, 34, 1]
obj2 = [10, 5, 10]
obj3 = [10 ,10, 10]

solution = SecondLargest()
print(solution.second_largest(obj1))
print(solution.second_largest(obj2))
print(solution.second_largest(obj3))