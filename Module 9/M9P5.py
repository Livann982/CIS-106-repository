def compute_tuition(credit_hours, district_code):
    code = district_code.upper()
    if code == 'I':
        return credit_hours * 250
    elif code == 'O':
        return credit_hours * 550
    else:
        return 0

def main_problem5():
    total_tuition_owed = 0.0
    keep_going = "yes"
    while keep_going.lower() in ["yes", "y"]:
        last_name = input("Enter student's last name: ")
        try:
            hours = int(input("Enter credit hours: "))
            district_code = input("Enter district code (I/O): ")
            tuition = compute_tuition(hours, district_code)
            total_tuition_owed += tuition
            print(f"Student: {last_name} | Tuition Owed: ${tuition:,.2f}\n")
        except ValueError:
            print("Invalid input. Credit hours must be an integer.")
            continue
        keep_going = input("Do you want to enter another student? (yes/no): ")
    print(f"\nTotal of all tuition owed: ${total_tuition_owed:,.2f}")

if __name__ == "__main__":
    main_problem5()
