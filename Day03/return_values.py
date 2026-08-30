def add_balance(balance, deposit):
    return balance + deposit

total = add_balance(1000, 500)

print("Total Balance:", total)

gst = total*0.018

print("GST:", gst)