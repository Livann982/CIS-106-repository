def compute_assessed_value(county, market_value):
    co = county.strip().lower()
    if co == "cook":
        percent = 0.90
    elif co == "dupage":
        percent = 0.80
    elif co == "mchenry":
        percent = 0.75
    elif co == "kane":
        percent = 0.60
    else:
        percent = 0.70
    return market_value * percent

def main():
    total_market = 0.0
    total_assessed = 0.0
    while True:
        run_program = input("Do you want to value a home property? (Yes or No): ").strip().lower()
        if run_program != "yes":
            break
        county = input("Enter IL County name: ").strip()
        market_value = float(input("Enter Home Market Value: $"))
        assessed_val = compute_assessed_value(county, market_value)
        total_market += market_value
        total_assessed += assessed_val
        print(f"Assessed Home Value: ${assessed_val:,.2f}\n")
    print(f"\n--- Cumulative Summary ---")
    print(f"Total Market Value of all properties: ${total_market:,.2f}")
    print(f"Total Assessed Value of all properties: ${total_assessed:,.2f}")

if __name__ == "__main__":
    main()
