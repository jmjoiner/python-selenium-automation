# def is_mountain_array(arr):
#     if len(arr) < 3:
#         return False
#
#     i = 1
#     while i < len(arr) and arr[i] > arr[i - 1]:
#         i += 1
#
#     if i == len(arr):
#         return False
#
#     while i < len(arr) and arr[i] < arr[i - 1]:
#         i += 1
#
#     return i == len(arr)
#
#
# test_list_pos = [1, 3, 5, 11, 9, 2]
# test_list_neg_1 = [1, 4, 7]
# test_list_neg_2 = [1, 4, 7, 2, 3]
#
# print(is_mountain_array(test_list_neg_1))
# print(is_mountain_array(test_list_pos))
# print(is_mountain_array(test_list_neg_2))
