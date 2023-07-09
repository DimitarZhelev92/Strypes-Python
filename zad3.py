def to_number(digits):
 
    # initialize an empty string
    digit = ""
 
    # traverse in the string
    for i in digits:
        digit += str(i)
 
    # return string
    return digit
 
 
# Driver code
digits = [2,6,12,6]
print(to_number(digits))