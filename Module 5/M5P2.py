item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price
print("\n--- Pricing Breakdown ---")
print(f"Item Type: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:,.2f}")
