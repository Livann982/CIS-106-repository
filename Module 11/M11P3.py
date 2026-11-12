def compute_sales_metrics(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    
    next_year_target = sales * 0.05
    return commission, next_year_target

def main():
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter total sales: "))

    commission, next_year_target = compute_sales_metrics(sales)

    print(f"\nSalesperson: {last_name}")
    print(f"Commission: ${commission:,.2f}")
    print(f"Next Year's Target: ${next_year_target:,.2f}")

if __name__ == "__main__":
    main()
