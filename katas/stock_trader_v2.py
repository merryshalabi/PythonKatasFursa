def max_profit(prices):
    """
    Finds the maximum profit that can be achieved by buying and selling the stock MULTIPLE times.

    O(n) is the best complexity

    Args:
        prices: a list of prices on each day

    Returns:
        the maximum profit, or 0 if no profit can be achieved
    """


    total_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit



if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 7

    # Additional test cases
    prices1 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 4

    prices2 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 0