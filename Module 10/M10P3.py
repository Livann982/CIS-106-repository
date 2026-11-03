def compute_out_the_door_price(msrp, make, model, ev_code):
    if make.lower() == "honda" and model.lower() == "accord":
        discount_percent = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount_percent = 0.15
    elif ev_code.upper() == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05
    discounted_msrp = msrp * (1 - discount_percent)
    return discounted_msrp * 1.07  

def main():
    sum_msrp = 0.0
    sum_sales_price = 0.0
    while True:
        run_program = input("Do you want to process an automobile? (Yes or No): ").strip().lower()
        if run_program != "yes":
            break
        make = input("Enter vehicle make: ").strip()
        model = input("Enter vehicle model: ").strip()
        ev_code = input("Is it an electric vehicle? (Y or N): ").strip().upper()
        msrp = float(input("Enter vehicle MSRP: $"))
        final_price = compute_out_the_door_price(msrp, make, model, ev_code)
        sum_msrp += msrp
        sum_sales_price += final_price
        print(f"Out the door price: ${final_price:,.2f}\n")
    print(f"\n--- Cumulative Summary ---")
    print(f"Sum of all MSRPs: ${sum_msrp:,.2f}")
    print(f"Sum of all Sales Prices: ${sum_sales_price:,.2f}")

if __name__ == "__main__":
    main()
