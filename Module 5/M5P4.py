appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: $"))
if appliance_cost > 1000.00:
    warranty_cost = appliance_cost * 0.10
else:
    warranty_cost = appliance_cost * 0.05

total_cost = appliance_cost + warranty_cost
print(f"Appliance: {appliance_name}")
print(f"Appliance Cost: ${appliance_cost:,.2f}")
print(f"Warranty Cost: ${warranty_cost:,.2f}")
print(f"Total Price: ${total_cost:,.2f}")