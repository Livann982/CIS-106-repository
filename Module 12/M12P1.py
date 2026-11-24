def display_names(names):
    print("--- Last Names ---")
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    print("\n--- Last Names (Reverse Order) ---")
    # Start at the last index (len - 1), stop before -1, step by -1
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

def main():
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones",
        "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"
    ]
    
    display_names(last_names)
    display_reverse(last_names)

main()
