# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
#
# test_array = [6, 3, 8, 1, 9, 2]
# print(test_array)
# print(selection_sort(test_array))
from audioop import reverse


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(len(arr) - 1, i, - 1):
            if arr[j] > arr[min_index]:
                min_index = j

        if (min_index != i):
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


test_array = [6, 3, 8, 1, 9, 2]
print(test_array)
print(selection_sort(test_array))