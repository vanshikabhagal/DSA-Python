def Alternate(array):
    result = []
    for index in range(0, len(array), 2)):
        result.append(array[index])
    return result

test = [1,2,3,4,5,6,7]
print(Alternate(test))
