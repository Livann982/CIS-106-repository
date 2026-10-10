quantity = int(input("Enter the quantity of the item: "))
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
print("\n--- Order Summary ---")
print(f"Quantity: {quantity:,}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:,.2f}")
print(f"Tax (7%): ${tax:,.2f}")
print(f"Total Cost: ${total:,.2f}")