def contains_digit(number, digit):
    num_list = list(map(int, str(number)))
    dig = num_list.count(digit)

    if dig > 0:
        print("True")
    else:
        print("False")
contains_digit(12346789, 5)