def display_parallel(names, scores):
    print("--- Student Scores ---")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")

def display_parallel_reverse(names, scores):
    print("\n--- Student Scores (Reverse Order) ---")
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]}: {scores[i]}")

def main():
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones",
        "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"
    ]
    exam_scores = [88, 92, 76, 85, 95, 79, 91, 84, 73, 89]
    
    display_parallel(last_names, exam_scores)
    display_parallel_reverse(last_names, exam_scores)

main()
