def BalancedNumber(n):
 
    Leftsum = 0
    Rightsum = 0
 
    
    for i in range(0, int(len(n) / 2)):
        Leftsum = Leftsum + int(n[i])
        Rightsum = (Rightsum + int(n[len(n) - 1 - i]))
 
    if (Leftsum == Rightsum):
        print("True", end = '\n')
    else:
        print("False", end = '\n')
 
BalancedNumber("12321")