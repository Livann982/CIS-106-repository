total_inventory_value = 0.0

print(f"{'Item':<12} {'Quantity':<10} {'Price':<10} {'Total Value':<12}")
print("-" * 50)

with open("inventory.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if len(data) < 3:
            continue
            
        item = data[0]
        quantity = int(data[1])
        price = float(data[2])
        item_total = quantity * price
        total_inventory_value += item_total
        
        print(f"{item:<12} {quantity:<10} ${price:,.2f}    ${item_total:,.2f}")

print("-" * 51)
print(f"Total Order/Inventory Value: ${total_inventory_value:,.2f}")