
def main():
    student_grades = {
        "Alice": 92.5,
        "Bob": 84.0,
        "Charlie": 78.5,
        "Diana": 95.0,
        "Evan": 88.0
    }

    print(f"{'Student Name':<15} {'Grade':>10}")
    print("-" * 26)

    total_grade = 0
    for name, grade in student_grades.items():
        print(f"{name:<15} {grade:>10.2f}")
        total_grade += grade

    class_average = total_grade / len(student_grades)
    print("-" * 26)
    print(f"{'Class Average':<15} {class_average:>10.2f}")

if __name__ == "__main__":
    main()