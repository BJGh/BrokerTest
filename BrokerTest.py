# Assuming the transactions are stored in a list of dictionaries
transactions = [
    {"symbol": "AAPL", "quantity": 10, "price": 100, "type": "buy"},
    {"symbol": "AAPL", "quantity": 10, "price": 150, "type": "sell"},
    {"symbol": "AAPL", "quantity": 5, "price": 200, "type": "buy"},
    {"symbol": "AAPL", "quantity": 5, "price": 250, "type": "buy"},
]

# Extracting a list of all symbols in the transactions
symbols = list(set(transaction["symbol"] for transaction in transactions))

# Calculating the current quantity of each symbol in the portfolio
portfolio = {}
for symbol in symbols:
    buys = sum(transaction["quantity"] for transaction in transactions
               if transaction["symbol"] == symbol and transaction["type"] == "buy")
    sells = sum(transaction["quantity"] for transaction in transactions
                if transaction["symbol"] == symbol and transaction["type"] == "sell")
    portfolio[symbol] = buys - sells

# Calculating the FIFO average cost price for each symbol in the portfolio
cost_prices = {}
for symbol in symbols:
    quantities = []
    prices = []
    for transaction in transactions:
        if transaction["symbol"] == symbol:
            if transaction["type"] == "buy":
                quantities.append(transaction["quantity"])
                prices.append(transaction["price"])
            elif transaction["type"] == "sell":
                quantity = transaction["quantity"]
                while quantity > 0:
                    if quantity >= quantities[0]:
                        quantity -= quantities.pop(0)
                        prices.pop(0)
                    else:
                        quantities[0] -= quantity
                        break
    cost_prices[symbol] = sum(qty * price for qty, price in zip(quantities, prices)) / sum(quantities)

# Printing the results
print("Portfolio:")
for symbol, quantity in portfolio.items():
    print(f"{symbol}: {quantity}")
print("Cost Prices:")
for symbol, cost_price in cost_prices.items():
    print(f"{symbol}: {cost_price}")
