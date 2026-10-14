total_gross_pay = 0.0
employee_count = 0
run_program = input("Do you want to run the payroll program? (Yes/No): ").strip().lower()

while run_program == "yes" or run_program == "y":
    last_name = input("\nEnter employee last name: ").strip()
    try:
        hours = float(input("Enter hours worked: "))
        pay_rate = float(input("Enter rate of pay: $"))
        if hours > 40:
            regular_pay = 40 * pay_rate
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (pay_rate * 1.5)
            gross_pay = regular_pay + overtime_pay
        else:
            gross_pay = hours * pay_rate
            
        total_gross_pay += gross_pay
        employee_count += 1
        print(f"\n{'Employee':<15} {'Gross Pay':>15}")
        print("-" * 31)
        print(f"{last_name:<15} ${gross_pay:>14,.2f}")
        
    except ValueError:
        print("Invalid data entered. Please use numeric numbers for hours and rate.")
        run_program = input("\nDo you want to enter another employee? (Yes/No): ").strip().lower()
        if employee_count > 0:
            average_pay = total_gross_pay / employee_count
else:
    average_pay = 0.0

print(f"\n{'Payroll Final Summary':<25} {'Value':>15}")
print("-" * 41)
print(f"{'Total Employees:':<25} {employee_count:>15}")
print(f"{'Total Gross Payroll:':<25} ${total_gross_pay:>14,.2f}")
print(f"{'Average Gross Pay:':<25} ${average_pay:>14,.2f}")
