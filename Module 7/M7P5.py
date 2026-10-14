total_discounts_applied = 0.0

run_program = input("Do you want to run the order discount program? (Yes/No): ").strip().lower()

while run_program == "yes" or run_program == "y":
    try:
        quantity = int(input("\nEnter item quantity: "))
        price = float(input("Enter item price: $"))
        
        extended_price = quantity * price
        
        if extended_price > 10000.00:
            discount_rate = 0.25
        else:
            discount_rate = 0.10
            
        discount_amount = extended_price * discount_rate
        total_price = extended_price - discount_amount
        
        total_discounts_applied += discount_amount
        
        print(f"\n{'Order Metric':<20} {'Amount':>15}")
        print("-" * 36)
        print(f"{'Extended Price:':<20} ${extended_price:>14,.2f}")
        print(f"{'Discount Amount:':<20} ${discount_amount:>14,.2f}")
        print(f"{'Total Order Cost:':<20} ${total_price:>14,.2f}")
        
    except ValueError:
        print("Invalid numerical inputs. Try again.")
        
    run_program = input("\nDo you want to process another order? (Yes/No): ").strip().lower()

print(f"\n{'Summary Metric':<25} {'Total Amount':>15}")
print("-" * 41)
print(f"{'Sum of All Discounts:':<25} ${total_discounts_applied:>14,.2f}")