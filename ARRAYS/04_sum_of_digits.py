def sum(number):
    total = 0
    #convert the integer to a string for getting individual digits.
    for digit in str(number):
        #convert back the digit to integer for calculation.
        int(digit)
        total += int(digit)
    return total

n = 687
#it is supposed to be taken as '6', '7', '8'.

print(sum(n))