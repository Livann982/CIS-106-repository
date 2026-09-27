make = input("Enter the auto make: ")
model = input("Enter the auto model: ")
msrp = float(input("Enter the MSRP amount: "))
discount_pct = float(input("Enter the discount percent (as a decimal, e.g., 0.15): "))
amount_off = msrp * discount_pct
discounted_price = msrp - amount_off
print(f"\nMake: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:,.2f}")
print(f"Discount Percent: {discount_pct:.2f}")
print(f"Amount Off: ${amount_off:,.2f}")
print(f"Discounted Price: ${discounted_price:,.2f}")