data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for amount, from_currency, to_currency, rate in data:
    print(f"{amount} {from_currency} to {to_currency} at rate {rate} is {int(rate*amount)}" )