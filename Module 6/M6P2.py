part_number = input("Enter part number: ")
quantity = int(input("Enter quantity: "))
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
    total_cost = quantity * unit_cost
    print(f"\nPart Number: {part_number}")
print(f"{'Description':<18}{'Amount':>12}")
print("-" * 30)
print(f"{'Cost Per Unit:':<18}${unit_cost:>11,.2f}")
print(f"{'Total Cost:':<18}${total_cost:>11,.2f}")