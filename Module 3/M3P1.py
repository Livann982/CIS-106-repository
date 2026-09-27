ticker = input("Enter the stock ticker symbol: ").upper()
shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))
amount_invested = shares * cost_per_share
print(f"\nStock Ticker: {ticker}")
print(f"Amount Invested: ${amount_invested:,.2f}")
