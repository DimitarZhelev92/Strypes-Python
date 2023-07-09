def to_digits(n):
    c = str(n)
    int_list = []
    for i in range(len(c)):
        int_list.append(int(c[i]))
    return int_list
input_number = input("Enter the number: ")
to_digits = to_digits(input_number)
print(to_digits)