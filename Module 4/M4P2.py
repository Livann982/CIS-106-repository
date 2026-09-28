exam1 = purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = int(input("Enter the quantity of stock: "))
value_change = (current_price - purchase_price) * quantity
if value_change >= 0:
    print(f"Value Increase: ${value_change:,.2f}")
else:
    print(f"Value Decrease: -${abs(value_change):,.2f}")
