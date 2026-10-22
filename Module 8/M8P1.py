principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
total_interest = 0.0
print("\nFormatted output")
print(f"{'Year':<5} {'Beginning':<12} {'Ending':<12}")
print(f"{'':<5} {'Balance':<12} {'Balance':<12}")
for year in range(1, 6):
    beg_balance = principal
    interest = beg_balance * rate
    end_balance = beg_balance + interest
    total_interest += interest
    principal = end_balance  # Ending balance becomes next year's principal
    print(f"{year:<5} ${beg_balance:,.2f}  ${end_balance:,.2f}")
    print(f"Total interest earned: ${total_interest:,.2f}")
