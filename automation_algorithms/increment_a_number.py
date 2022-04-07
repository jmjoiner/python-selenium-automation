# def inc_a_num(digits):
#
#     index = len(digits) - 1
#
#     while (index >= 0 and digits[index] == 9):
#         digits[index] = 0
#         index -= 1
#
#     if (index < 0):
#
#         digits.insert(0, 1)
#
#     else:
#         digits[index] += 1
#
#
# digits = [1, 2, 9]
#
# inc_a_num(digits)
#
# for digit in digits:
#     print(digit, end=' ')