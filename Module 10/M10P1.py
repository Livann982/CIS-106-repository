def compute_forecast(month, sales):
    month_clean = month.strip().lower()[:3]
    if month_clean in ["jan", "feb", "mar"]:
        forecast_percent = 0.10
    elif month_clean in ["apr", "may", "jun"]:
        forecast_percent = 0.15
    elif month_clean in ["jul", "aug", "sep"]:
        forecast_percent = 0.20
    elif month_clean in ["oct", "nov", "dec"]:
        forecast_percent = 0.25
    else:
        forecast_percent = 0.00
        print("Warning: Unknown month. Applying 0% forecast increase.")
    return sales * (1 + forecast_percent)

def main():
    while True:
        run_program = input("Do you want to run the sales forecast program? (Yes or No): ").strip().lower()
        if run_program != "yes":
            break
        last_name = input("Enter last name: ").strip()
        month = input("Enter current month (e.g., Jan, Feb, March): ").strip()
        sales = float(input("Enter current month's sales amount: $"))
        predicted_sales = compute_forecast(month, sales)
        print(f"\n--- Forecast Results for {last_name} ---")
        print(f"Current Month: {month.capitalize()}")
        print(f"Next Month's Projected Forecast: ${predicted_sales:,.2f}\n")

if __name__ == "__main__":
    main()
