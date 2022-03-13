# The equation for the fibonacci sequence:
# *** How do I type the fibonacci sequence? ***

# The task is to display all the numbers from start to n of the Fibonacci sequence

# Equation:
# FO = O
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

# 1 1 2 3 5 8 13 ...

# code here
# O(n)
#def fibonacci(n):
#    if n < 0:
#        return 'Not a valid value'
#    if n == 0:
#        return 0
#    if n == 1:
#        return [1]
#    if n == 2:
#        return [1, 1]

#    fib_1 = 1
#    fib_2 = 1
#    result = [1, 1]
#    index = 3

#    while index <= n:
#        result.append(result[-1] + result[-2])
     #   fib_1, fib_2 = fib_2, fib_1 + fib_2
#        index = index + 1

#    return result

# print(fibonacci(5)) #1 1 2 3 5
# print(fibonacci(7)) #1 1 2 3 5 8 13
