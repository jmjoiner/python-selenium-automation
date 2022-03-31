# Our code grneratesa random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.


# code here
# from random import randint

# random_number = randint(100, 999)
# print(f'The random number is: {random_number}')

# result = 0
# Soultion A
# O(n)
# for digit in str(random_number):
#    result = result + int(digit)

# Solution B
# O(n)
# Random number = 321; Expected result = 6
#while random_number != 0: # 3
#    result = result + (random_number % 10) # 6
#    random_number = random_number // 10


#print(f'Result {result}:')