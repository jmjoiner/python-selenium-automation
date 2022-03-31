def delete_duplicates(arr):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    return write_index


test_list = [1, 3, 4, 4, 5, 8, 9, 9, 11]
print(test_list)

print(delete_duplicates(test_list))
print(test_list)