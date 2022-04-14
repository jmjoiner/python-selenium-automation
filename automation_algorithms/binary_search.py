def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == x:
            return mid
        if guess > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1


test_list = [3, 7, 92, 143, 744, 900, 1490, 4398, 109872]
test_x_pos = 92
test_x_neg = 976

print(binary_search(test_list, test_x_pos))
print(binary_search(test_list, test_x_neg))
