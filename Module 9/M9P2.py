def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.000
    return hits / at_bats

def main_problem2():
    player_count = 0
    keep_going = "yes"
    while keep_going.lower() in ["yes", "y"]:
        last_name = input("Enter player's last name: ")
        try:
            hits = int(input("Enter number of hits: "))
            at_bats = int(input("Enter number of at bats: "))
            avg = compute_batting_average(hits, at_bats)
            player_count += 1
            print(f"Player: {last_name} | Batting Average: {avg:.3f}\n")
        except ValueError:
            print("Invalid input. Please enter integers.")
            continue
        keep_going = input("Do you want to enter another player? (yes/no): ")
    print(f"\nTotal number of players entered: {player_count}")

if __name__ == "__main__":
    main_problem2()