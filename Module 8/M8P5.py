total_tuition = 0.0   
student_count = 0     

print(f"{'Last Name':<12} {'Credits':<10} {'Tuition Owed':<12}")
print("-" * 38)

with open("students.txt", "r") as file:
    while True:
        last_name_line = file.readline()
        
        if not last_name_line or last_name_line.strip() == "":
            break
            
        district_code_line = file.readline()
        credits_line = file.readline()
        
        student_last_name = last_name_line.strip()
        district_code = district_code_line.strip().upper()
        
        credits_text = credits_line.strip()
        credits_taken = int(credits_text)
        
        if district_code == 'I':
            cost_per_credit = 250.00
        else:
            cost_per_credit = 500.00
            
        tuition_owed = credits_taken * cost_per_credit
        
        total_tuition += tuition_owed
        student_count += 1
        
        print(f"{student_last_name:<12} {credits_taken:<10} ${tuition_owed:,.2f}")

print("-" * 38)
print(f"Total Tuition Owed:  ${total_tuition:,.2f}")
print(f"Total Students:      {student_count}")