def compute_wall_area(length, width, height):
    return (2 * length * height) + (2 * width * height)

def compute_ceiling_floor_area(length, width):
    return length * width

def main():
    while True:
        run_program = input("Do you want to run the room painting program? (Yes or No): ").strip().lower()
        if run_program != "yes":
            break
        length = float(input("Enter room length (feet): "))
        width = float(input("Enter room width (feet): "))
        height = float(input("Enter room height (feet): "))
        wall_sq_ft = compute_wall_area(length, width, height)
        wall_gallons = wall_sq_ft / 50.0  
        ceiling_sq_ft = compute_ceiling_floor_area(length, width)
        ceiling_gallons = ceiling_sq_ft / 400.0  
        print(f"\n--- Room Results ---")
        print(f"Wall Area: {wall_sq_ft:.2f} sq. ft.")
        print(f"Gallons needed for walls: {wall_gallons:.2f} gallons")
        print(f"Ceiling/Floor Area: {ceiling_sq_ft:.2f} sq. ft.")
        print(f"Gallons needed for ceiling/floor: {ceiling_gallons:.2f} gallons\n")

if __name__ == "__main__":
    main()
