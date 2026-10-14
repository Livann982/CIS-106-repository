last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: $"))
job_level = int(input("Enter job level: "))
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10
bonus = salary * bonus_rate
print(f"\nEmployee Last Name: {last_name}")
print(f"{'Description':<18}{'Amount':>12}")
print("-" * 30)
print(f"{'Salary:':<18}${salary:>11,.2f}")
print(f"{'Bonus Rate:':<18}{bonus_rate * 100:>11.1f}%")
print(f"{'Bonus Amount:':<18}${bonus:>11,.2f}")