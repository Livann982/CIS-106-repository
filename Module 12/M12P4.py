def display_players(names, averages):
    print("--- Player Batting Averages ---")
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]:.3f}")
    print()

def search_player(names, averages, target):
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            print(f"Found: {names[i]} - Batting Average: {averages[i]:.3f}")
            break

def main():
    player_names = []
    batting_avgs = []
    
    with open("players.txt", "r") as file:
        line = file.readline().strip()
        while line != "":
            player_names.append(line)
            avg = float(file.readline().strip())
            batting_avgs.append(avg)
            line = file.readline().strip()
            
    display_players(player_names, batting_avgs)
    
    search_name = input("Enter a last name to search (or 'quit' to exit): ")
    while search_name.lower() != "quit":
        search_player(player_names, batting_avgs, search_name)
        search_name = input("\nEnter a last name to search (or 'quit' to exit): ")

main()
