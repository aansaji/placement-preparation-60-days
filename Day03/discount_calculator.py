def calculate_discount(price, discount):
    discount_amount = (price * discount) / 100
    return price - discount_amount

ans = calculate_discount(2000, 10)

print(ans)