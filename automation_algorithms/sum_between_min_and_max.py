def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return -1

    min_value = max_value = arr[0]
    min_index = max_index = 0
    i = 1

    while i < len(arr):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]
        if arr[i] < min_value:
            min_index = i
            min_value = arr[i]
        i += 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test_list_1 = [1, 5, 9, 3, 11, 27, 25]
print(sum_between_min_and_max(test_list_1))

test_list_2 = [34, 8, 27, 91, 22, 9, 2]
print(sum_between_min_and_max(test_list_2))