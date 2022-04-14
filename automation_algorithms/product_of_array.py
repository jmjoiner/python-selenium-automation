# def product_of_array(nums):
#     result = [1] * len(nums)
#
#     for i in range(0, len(nums)):
#         for j in range(0, len(nums)):
#             if i != j:
#                 result[i] = result[i] * nums[j]
#
#     return result


def product_of_array(nums):
    result = [1] * len(nums)

    for i in range(0, len(nums) - 1):
        result[i + 1] = result[i] * nums[i]

    for i in range(0, len(nums) - 1):
        result[-1 - i] *= result[0]
        result[0] *= nums[-1 - i]

    return result


test_nums = [1, 2, 3, 4]
print(product_of_array(test_nums))