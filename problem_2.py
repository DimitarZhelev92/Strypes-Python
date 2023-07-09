def sum_of_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)

print(sum_of_divisors(1000))
