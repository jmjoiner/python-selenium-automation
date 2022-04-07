# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
#
#
# test_array = [5, 6, 2, 9, 11, 3]
# print(test_array)
# print(bubble_sort(test_array))


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_array = [5, 6, 2, 9, 11, 3]
print(test_array)
print(bubble_sort(test_array))
