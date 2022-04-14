def contains_duplicate(nums):
    if len(nums) == 1:
        return True

    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False

    return True


test_list_pos = [1, 2, 3, 4, 5, 6, 2]
test_list_neg = [1, 2, 3, 4, 5, 6, 7]

print(contains_duplicate(test_list_pos))
print(contains_duplicate(test_list_neg))