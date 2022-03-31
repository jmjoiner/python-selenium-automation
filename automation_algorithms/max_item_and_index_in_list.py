def find_max_item_and_index(arr):
    max_value = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return [max_index, max_value]


test_list = [1, 45, 33, 76, 9, 10]
print(find_max_item_and_index(test_list))