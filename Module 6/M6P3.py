principal = float(input("Enter the principal amount of the CD: $"))
years = int(input("Enter years to maturity: "))
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
    first_year_interest = principal * interest_rate
    print(f"\n{'Description':<22}{'Value':>12}")
print("-" * 34)
print(f"{'Principal Amount:':<22}${principal:>11,.2f}")
print(f"{'Interest Rate:':<22}{interest_rate * 100:>11.1f}%")
print(f"{'First Year Interest:':<22}${first_year_interest:>11,.2f}")