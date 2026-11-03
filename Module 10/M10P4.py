def compute_ticket_price(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles <= 29:
        return 10
    elif 10 <= miles <= 19:
        return 8
    else:
        return 5

def main():
    total_ticket_sum = 0
    while True:
        run_program = input("Do you want to purchase a ticket? (Yes or No): ").strip().lower()
        if run_program != "yes":
            break
        last_name = input("Enter last name: ").strip()
        miles = float(input("Enter miles from downtown Chicago: "))
        ticket_price = compute_ticket_price(miles)
        total_ticket_sum += ticket_price
        print(f"Ticket Price for {last_name}: ${ticket_price:.2f}\n")
    print(f"\n--- Cumulative Summary ---")
    print(f"Sum price of all tickets: ${total_ticket_sum:,.2f}")

if __name__ == "__main__":
    main()
