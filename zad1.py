def sum_of_digits(n):
    num = 0
    for digit in str(n): 

      num += int(digit)      
    return num
   
input_number = input("Enter the number: ")
sum_of_digits = sum_of_digits(input_number)
print(sum_of_digits)