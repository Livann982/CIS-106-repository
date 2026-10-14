student_count = 0

run_program = input("Do you want to run this program? (Yes/No): ").strip().lower()

while run_program == "yes" or run_program == "y":
    last_name = input("\nEnter student last name: ").strip()
    try:
        score1 = float(input("Enter exam score 1: "))
        score2 = float(input("Enter exam score 2: "))
        
        average = (score1 + score2) / 2
        student_count += 1
        
        print(f"\n{'Student':<15} {'Average Score':>15}")
        print("-" * 31)
        print(f"{last_name:<15} {average:>15.2f}")
        
    except ValueError:
        print("Invalid input. Scores must be numbers. Student data not counted.")
        
    run_program = input("\nDo you want to enter another student? (Yes/No): ").strip().lower()

print(f"\n{'Total Students Processed:':<26} {student_count:>5}")