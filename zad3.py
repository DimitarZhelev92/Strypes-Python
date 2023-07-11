def to_number(digits):
 
    digit = ""
    for i in digits:
        digit += str(i)
    return digit
 
digits = [2,6,12,6]
print(to_number(digits))