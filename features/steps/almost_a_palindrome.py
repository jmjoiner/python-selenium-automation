# def is_almost_palindrome(s):
#     for i in range(len(s)):
#         s_temp = s[:i] + s[i + 1:]
#         if s_temp == s_temp[::-1]:
#             return True
#
#     return False
#
#
# str_pos = "radkar"
# str_neg = "radario"
# print(is_almost_palindrome(str_pos))
# print(is_almost_palindrome(str_neg))