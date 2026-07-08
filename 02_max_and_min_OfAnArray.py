def maximum(arr):
    largest = arr[0]
    for index in range(len(arr)):
        if (largest < arr[index]):
            largest = arr[index]
    return largest

def minimum(arr):
    smallest = arr[0]
    for index in range(len(arr)):
        if(smallest > arr[index]):
            smallest = arr[index]
    return smallest

numbers = [4, 8, 9, 1, 16, 5]

print(f"The maximum element is {maximum(numbers)}.")
print(f"The minimum element is {minimum(numbers)}.")