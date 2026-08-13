# 16. Item prices calculations
prices = (120.50, 250.00, 75.50, 310.00, 180.00)

total = sum(prices)
average = total / len(prices)
highest = prices[0]
lowest = prices[0]

for price in prices[1:]:
    if price > highest:
        highest = price
    if price < lowest:
        lowest = price

print("Prices:", prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)
