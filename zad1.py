def sum_of_num(n):
    
    num = 0
    for digit in str(n): 
      num += int(digit)      
    return num
   
input_number = input("Enter the number: ")
sum_of_num = sum_of_num(input_number)
print(sum_of_num)