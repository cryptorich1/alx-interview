#!/usr/bin/python3

""" Contains makeChange function"""

def makeChange(coins, total):
  """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
  if not coins or coins is None:
    return -1
  if total <= 0:
    return 0
  change = 0
  coins = sorted(coins)[::-1]
  for coin in coins:
    while coin <= total:
      total -= coin
      change += 1
    if (total == 0):
      return change
  return -1

# def makeChange(coins, total):
#     if total <= 0:
#         return 0

#     # Initialize a list to store the minimum number of coins needed for each total value
#     min_coin = [float('inf')] * (total + 1)
#     min_coin[0] = 0

#     # Iterate over each total value from 1 to 'total'
#     for i in range(1, total + 1):
#         for coin in coins:
#             if coin <= i:
#                 min_coin[i] = min(dp[i], dp[i - coin] + 1)

#     # If dp[total] is still infinity, then it's not possible to make change
#     if min_coin[total] == float('inf'):
#         return -1

#     return min_coin[total]
