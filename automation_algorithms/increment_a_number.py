def AddOne(digits):

    index = len(digits) - 1

    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1

    if (index < 0):

        digits.insert(0, 1)

    else:
        digits[index] += 1


digits = [1, 2, 9]

AddOne(digits)

for digit in digits:
    print(digit, end=' ')