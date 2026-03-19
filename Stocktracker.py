
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

print("📊 Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))
    price = stock_prices[stock]

    investment = price * quantity
    total_investment += investment

    print(f"{stock} Investment = {investment}")

print("\n💰 Total Investment =", total_investment)

# Save result in file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total_investment}")

print("✅ Data saved to portfolio.txt")