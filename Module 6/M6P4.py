tickets = int(input("Enter the number of concert tickets: "))
if tickets >= 25:
    price_per_ticket = 50
elif tickets >= 10:
    price_per_ticket = 60
elif tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 75
    total_cost = tickets * price_per_ticket
    print(f"\nNumber of Tickets: {tickets}")
print(f"{'Description':<18}{'Amount':>12}")
print("-" * 30)
print(f"{'Price Per Ticket:':<18}${price_per_ticket:>11,.2f}")
print(f"{'Total Cost:':<18}${total_cost:>11,.2f}")