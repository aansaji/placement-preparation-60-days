a=548
b=67

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

price = int(input("Enter the price of the item: "))
quantity = int(input("Enter the qunatity:")) 
print(price * quantity)

ticke_price = 180
quant = int(input("Enter the qunatity of tickets: "))
if (quant > 5):
    print("You qualify for group bookings.")
    print(180 * quant)
else:
    print(180 * quant)
