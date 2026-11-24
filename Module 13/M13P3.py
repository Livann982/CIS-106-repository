def load_players(filename):
    players_dict = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, avg = line.split(",")
                players_dict[name.strip()] = float(avg.strip())
    return players_dict

def print_players(players_dict):
    print(f"{'Player Name':<15} {'Batting Avg':>12}")
    print("-" * 28)
    for name, avg in players_dict.items():
        print(f"{name:<15} {avg:>12.3f}")

def main():
    filename = "players.txt"
    batting_averages = load_players(filename)
    print_players(batting_averages)

if __name__ == "__main__":
    main()
