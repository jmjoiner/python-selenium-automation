list1 = [7, 3, 5, 6, 4, 10, 3, 2]

only_even = [num for num in list1 if num % 2 == 0]
only_odd = [num for num in list1 if num % 2 == 1]

even_first = (only_even + only_odd)
print(even_first)


