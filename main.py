import cryptocompare

def main():
    while True:
        try:
            crypto_ticker = input("Please enter crypto ticker: ")
            crypto_amount = float(input(f"Please enter {crypto_ticker} quantity to convert to usd: "))

            crypto_price = get_crypto_price(crypto_ticker, "usd")

            print(f"{crypto_amount} {crypto_ticker} is: {crypto_price*crypto_amount} USD")     
        except:
            print(f"{crypto_ticker} is not valid")



def get_crypto_price(crypto_ticker: str, currency: str):
    prices_dict = cryptocompare.get_price(crypto_ticker, currency=currency)
    return prices_dict[crypto_ticker.upper()][currency.upper()]


if __name__ == '__main__':
    main()