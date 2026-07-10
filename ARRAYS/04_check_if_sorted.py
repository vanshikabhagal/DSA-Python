def Sorted(arr):
    for index in range(len(arr)-1):
        if (arr[index]>arr[index+1]):
            return False
    return True

test = [10 ,20, 30, 40, 50]
print(Sorted(test))