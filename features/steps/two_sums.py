def find_pair(nums, target):
    if len(nums) == 2:
        return nums

    sum_set = set()

    for num in nums:
        target_element = target - num
        if target_element not in sum_set:
            sum_set.add(num)
        else:
            return [num, target_element]


test_list = [1, 3, 7, 8, 3, 11]
test_target = 8


print(find_pair(test_list, test_target))