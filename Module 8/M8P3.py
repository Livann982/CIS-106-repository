
total_bonuses = 0.0

print(f"{'Name':<10} {'Salary':<12} {'Bonus':<12}")
print("-" * 36)
with open("employees.txt", "r") as file:
    while True:
        # Read two lines at a time (Name then Salary)
        name = file.readline().strip()
        salary_str = file.readline().strip()
        if not name or not salary_str:
            break      
        salary = float(salary_str)
        if salary >= 100000.00:
            rate = 0.20
        elif salary >= 50000.00:
            rate = 0.15
        else:
            rate = 0.10
        bonus = salary * rate
        total_bonuses += bonus

        print(f"{name:<10} ${salary:,.2f}   ${bonus:,.2f}")
print("-" * 36)
print(f"Total interest earned: ${total_bonuses:,.2f}")