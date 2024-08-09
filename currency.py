def currency_converter():
    amount = float(input("Enter the amount in USD: "))
    exchange_rate = float(input("Enter the exchange rate from USD to INR: "))
    converted_amount = amount * exchange_rate
    print("The amount in INR is:", converted_amount)
currency_converter()
