total = 0.0
tax = 0.0

def compute_total_and_tax(qty, unit_price):
    global total, tax
    total = qty * unit_price
    tax = total * 0.07

def main():
    qty = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    compute_total_and_tax(qty, unit_price)

    print(f"\nTotal: ${total:,.2f}")
    print(f"Tax (7%): ${tax:,.2f}")

if __name__ == "__main__":
    main()
