arr = [10, 20, 30, 40, 50]
index = int(input("Which index value do you want? "))

#for error handling
if(index>len(arr)):
    print("Invalid index.")
#output
else:
    print(f"The value of arr[{index}] is {arr[index]}.")