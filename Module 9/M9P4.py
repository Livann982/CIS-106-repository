def determine_pay_rate(job_code):
    code = job_code.upper()
    if code == 'L':
        return 25.00
    elif code == 'A':
        return 30.00
    elif code == 'J':
        return 50.00
    else:
        return 0.00

def main_problem4():
    total_gross_pay = 0.0
    keep_going = "yes"
    while keep_going.lower() in ["yes", "y"]:
        last_name = input("Enter employee's last name: ")
        job_code = input("Enter job code (L, A, J): ")
        try:
            hours = float(input("Enter hours worked: "))
            rate = determine_pay_rate(job_code)
            if rate == 0.0:
                print("Warning: Invalid job code. Pay rate set to $0.00.")
            if hours > 40:
                regular_pay = 40 * rate
                overtime_hours = hours - 40
                overtime_pay = overtime_hours * (rate * 1.5)
                gross_pay = regular_pay + overtime_pay
                print(f"Employee: {last_name} | Regular Pay: ${regular_pay:,.2f} | Overtime Pay: ${overtime_pay:,.2f} | Gross Pay: ${gross_pay:,.2f}\n")
            else:
                gross_pay = hours * rate
                print(f"Employee: {last_name} | Regular Pay: ${gross_pay:,.2f} | Overtime Pay: $0.00 | Gross Pay: ${gross_pay:,.2f}\n")
            total_gross_pay += gross_pay
        except ValueError:
            print("Invalid input. Please enter numbers for hours.")
            continue
        keep_going = input("Do you want to enter another employee? (yes/no): ")
    print(f"\nTotal of all gross pay: ${total_gross_pay:,.2f}")

if __name__ == "__main__":
    main_problem4()