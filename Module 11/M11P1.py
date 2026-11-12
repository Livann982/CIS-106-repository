def compute_discount(qty, price, disc_rate):
    extended_price = qty * price
    disc_amount = extended_price * disc_rate
    disc_price = extended_price - disc_amount
    return disc_amount, disc_price

def main():
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))
    disc_rate = float(input("Enter discount rate (as a decimal, e.g., 0.10): "))

    disc_amount, disc_price = compute_discount(qty, price, disc_rate)

    print(f"\nQuantity: {qty}")
    print(f"Unit Price: ${price:,.2f}")
    print(f"Discount Amount: ${disc_amount:,.2f}")
    print(f"Discounted Price: ${disc_price:,.2f}")

if __name__ == "__main__":
    main()
