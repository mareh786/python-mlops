"""
---------------------------------------------------------
Program: Best Time to Buy and Sell Stock (Brute Force)

Approach:
- Consider every possible pair of buying and selling days.
- Buy on day `i` and sell on every later day `j`.
- Calculate the profit for each pair.
- Keep track of the maximum profit obtained.
- Also store the corresponding buy and sell prices.
- Return the maximum profit along with the buy and sell prices.

Time Complexity:
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
  (Every pair of days is checked.)

Space Complexity:
- O(1)
  (Only a few extra variables are used.)

Key Learning:
- This is the brute-force solution.
- Every possible transaction is evaluated.
- An optimized solution exists with O(n) time complexity by
  tracking the minimum buying price seen so far.
---------------------------------------------------------
"""

from numpy import array


def stock_buy_sell(arr):
    # Initialize maximum profit
    max_profit = 0

    # Initialize buy and sell prices
    buy = -1
    sell = -1

    # Try every possible buying day
    for i in range(len(arr)):

        # Try every possible selling day after buying
        for j in range(i + 1, len(arr)):

            # Calculate the profit
            profit = arr[j] - arr[i]

            # Update maximum profit if a better transaction is found
            if profit > max_profit:
                max_profit = profit
                buy = arr[i]
                sell = arr[j]

    # Return maximum profit and transaction details
    return max_profit, buy, sell


# Driver Code
arr = array([7, 1, 5, 3, 6, 4])

profit, buy_price, sell_price = stock_buy_sell(arr)

print("Maximum Profit:", profit)
print("Buy Price:", buy_price)
print("Sell Price:", sell_price)
