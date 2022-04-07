# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         arr[j + 1] = key
#
#     return arr
#
#
# test_array = [4, 2, 6, 1, 8, 9]
# print(test_array)
# print(insertion_sort(test_array))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


test_array = [4, 2, 6, 1, 8, 9]
print(test_array)
print(insertion_sort(test_array))