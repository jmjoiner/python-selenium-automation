# def buy_and_sell_stock(prices):
#     max_sum = 0
#     curr_sum = 0
#
#     for i in range(len(prices) - 1):
#         curr_sum = curr_sum + prices[i + 1] - prices[i]
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#         if curr_sum < 0:
#             curr_sum = 0
#
#     return max_sum
#
#
# test_prices = [7, 1, 5, 3, 6, 4]
# print(buy_and_sell_stock(test_prices))