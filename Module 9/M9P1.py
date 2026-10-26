def compute_extended_price(qty, unit_price):
    total = qty * unit_price
    discount = 0.0
    if total > 10000.00:
        discount = total * 0.10
        total = total - discount
    return total, discount

def main_problem1():
    total_extended_price = 0.0
    keep_going = "yes"
    while keep_going.lower() in ["yes", "y"]:
        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter unit price: $"))
            ext_price, discount_amount = compute_extended_price(qty, price)
            total_extended_price += ext_price
            print(f"Qty: {qty} | Price: ${price:,.2f} | Discount Given: ${discount_amount:,.2f} | Extended Price: ${ext_price:,.2f}\n")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        keep_going = input("Do you want to enter another item? (yes/no): ")
    print(f"\nFinal total extended price for all items: ${total_extended_price:,.2f}")

if __name__ == "__main__":
    main_problem1()