def compute_bowling_averages(g1, g2, g3, handicap):
    avg_score = (g1 + g2 + g3) / 3
    avg_with_handicap = avg_score + handicap
    return avg_score, avg_with_handicap

def main():
    last_name = input("Enter bowler's last name: ")
    g1 = float(input("Enter game 1 score: "))
    g2 = float(input("Enter game 2 score: "))
    g3 = float(input("Enter game 3 score: "))
    handicap = float(input("Enter handicap: "))

    avg_score, avg_with_handicap = compute_bowling_averages(g1, g2, g3, handicap)

    print(f"\nBowler Last Name: {last_name}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Average Score with Handicap: {avg_with_handicap:.2f}")

if __name__ == "__main__":
    main()
