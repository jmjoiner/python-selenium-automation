# # def find_missing_element(list_1, list_2):
# #     list_1.sort()
# #     list_2.sort()
# #
# #     for num_1, num_2 in zip(list_1, list_2):
# #         if num_1 != num_2:
# #             return num_1
# #
# #     return list_1[-1]
# import collections
#
#
# def find_missing_element(list_1, list_2):
#     dict = collections.defaultdict(int)
#
#     for num in list_2:
#         dict[num] += 1
#
#     for num in list_1:
#         if dict[num] == 0:
#             return num
#         else:
#             dict[num] -= 1
#
# test_list_1 = [1, 2, 3, 4, 5, 6, 7]
# test_list_2 = [3, 7, 2, 1, 4, 6]
#
# print(str(find_missing_element(test_list_1, test_list_2)) + " is the missing number")