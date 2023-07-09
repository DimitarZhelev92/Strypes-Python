def sum_of_num(n):
    
    num = 0
    for digit in str(n): 
      num += int(digit)      
    return num
   
n = 569
print(sum_of_num(n))