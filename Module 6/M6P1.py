quantity = int(input("Enter the quantity of widgets: "))
if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30
    extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax
print(f"\n{'Description':<18}{'Amount':>12}")
print("-" * 30)
print(f"{'Extended Price:':<18}${extended_price:>11,.2f}")
print(f"{'Tax (7%):':<18}${tax:>11,.2f}")
print(f"{'Total:':<18}${total:>11,.2f}")