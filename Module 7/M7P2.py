try:
    start = int(input("Enter the start value: "))
    stop = int(input("Enter the stop value: "))
    increment = int(input("Enter the increment value: "))

    print(f"\n{'Sequence':<15}")

    current = start
    if increment > 0:
        while current <= stop:
            print(f"{current:<15}")
            current += increment
    elif increment < 0:
        while current >= stop:
            print(f"{current:<15}")
            current += increment
    else:
        print("Increment cannot be zero (infinite loop hazard).")

except ValueError:
    print("Please enter valid integers for start, stop, and increment values.")