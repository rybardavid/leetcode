def run(prices: list[int]) -> int:
    lowestIdx = 0
    highestIdx = 0
    highestProfit = 0

    for idx, price in enumerate(prices):
        if price < prices[lowestIdx]:
            lowestIdx = idx
            highestIdx = idx
        elif price > prices[lowestIdx]:
            highestIdx = idx

        profit = prices[highestIdx] - prices[lowestIdx]
        if profit > highestProfit:
            highestProfit = profit

    return highestProfit