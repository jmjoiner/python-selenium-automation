# When the user enters a year, the code detects if its a leap year or not.

# A leap year is exactly divisible by 4, except for century years (years ending with 00).
# The centry year is a leap year only if it is perfectly divisible by 400. For example...

# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year
# 2000 is a leap year


# code here
year = int(input('Input a year: '))

# O(1)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year:')
        else:
            print(f'{year} is not a leap year:')
    else:
        print(f'{year} is a leap year:')
else:
    print(f'{year} is not a leap year:')