# Take qty and price and display net amount after a discount of 20%

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty
discount = amount * 20 // 100
net_amount = amount - discount

print(f"Amount     : {amount:6}")
print(f"- Discount : {discount:6}")
print(f"Net Amount : {net_amount:6}")