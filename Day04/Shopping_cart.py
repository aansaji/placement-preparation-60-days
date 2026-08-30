cart=[]
cart.append("phone")
cart.append("headphone")
cart.append("charger")
cart.append("Mouse")

prices = [500, 1200, 300, 800]

total = 0

remove_index = cart.index("headphone")
cart.pop(remove_index)
prices.pop(remove_index)

highest = max(prices)
index = prices.index(highest)

for price in prices:
  total += price

print("Items:",cart)
print("Product Prices:",prices)
print ("Total price of cart:",total)
print("Most expensive:",cart[index])
print("Price:", highest)