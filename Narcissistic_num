def narcissistic( value ):
    str_digits = list(str(value))
    int_digits = str_digits.copy()
    # int => string => split => int => NUMBER[Digit_0, Digit_1, ...]
    i = 0
    for digit in int_digits:
        int_digits[i] = int(digit)
        i += 1
    j = 0
    sum = 0
    print(int_digits)
    #  for each Digit in NUMBER[] : Digit ** len(NUMBER[])
    for digit in int_digits:
        int_digits[j] = digit ** len(int_digits)
        sum += int_digits[j]
    if sum == value:
        return True
    else:
        return False
