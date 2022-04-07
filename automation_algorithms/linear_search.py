def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1

test_array = [1, 5, 8, 3, 2, 10, 43, 23]
key_number_pos = 8
key_number_neg = 59

print(linear_search(test_array, key_number_pos))
print(linear_search(test_array, key_number_neg))