def get_student_averages(grades_dict):
    student_averages = []
    for name, grades in grades_dict.items():
        avg = sum(grades) / len(grades)
        student_averages.append([name, avg])
    return student_averages

def get_class_grade_averages(grades_dict):
    num_students = len(grades_dict)
    grade1_total = 0
    grade2_total = 0
    grade3_total = 0

    for grades in grades_dict.values():
        grade1_total += grades[0]
        grade2_total += grades[1]
        grade3_total += grades[2]

    return [
        grade1_total / num_students,
        grade2_total / num_students,
        grade3_total / num_students
    ]

def main():
    student_grades = {
        "Alice": [92.5, 88.0, 95.0],
        "Bob": [84.0, 79.5, 85.0],
        "Charlie": [78.5, 82.0, 80.0],
        "Diana": [95.0, 96.5, 94.0],
        "Evan": [88.0, 91.0, 89.5]
    }

    student_avgs = get_student_averages(student_grades)
    print(f"{'Student Name':<15} {'Average':>10}")
    print("-" * 26)
    for name, avg in student_avgs:
        print(f"{name:<15} {avg:>10.2f}")

    print()

    class_avgs = get_class_grade_averages(student_grades)
    print(f"{'Assessment':<15} {'Class Avg':>10}")
    print("-" * 26)
    for i, avg in enumerate(class_avgs, start=1):
        print(f"{f'Grade {i}':<15} {avg:>10.2f}")

if __name__ == "__main__":
    main()
