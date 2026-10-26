def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0.0
    return miles / gallons

def main_problem3():
    trip_count = 0
    keep_going = "yes"
    while keep_going.lower() in ["yes", "y"]:
        destination = input("Enter destination city: ")
        try:
            miles = float(input("Enter miles travelled: "))
            gallons = float(input("Enter gallons used: "))
            mpg = compute_mpg(miles, gallons)
            trip_count += 1
            print(f"Destination: {destination} | Miles: {miles:.1f} | MPG: {mpg:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        keep_going = input("Do you want to enter another trip? (yes/no): ")
    print(f"\nTotal number of entries made (trips): {trip_count}")

if __name__ == "__main__":
    main_problem3()
