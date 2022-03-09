# When user enters a number, its factorial is displayed.

# code here

import math

# 5! = 120
number = int(input('Input your number: '))

print(math.factorial(number))
# O(n)
result = 1
if number != 0:
    for i in range(1, number + 1):
        result = result * i # result *= i


print(result)