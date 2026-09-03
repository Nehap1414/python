# Store item prices in a tuple and calculate total bill, average, highest and lowest price.
prices = (100, 250, 150, 300, 200)

total = sum(prices)
average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)