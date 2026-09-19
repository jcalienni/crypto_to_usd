import requests

class BinanceTickerClient:
    def __init__(self):
        # Binance public ticker endpoint (no authentication needed)
        url = "https://api.binance.com/api/v3/ticker/price"
        response = requests.get(url)
        response.raise_for_status()
        tickers_list = response.json()
        
        # Map lowercase base assets to their full USDT trading pair (e.g., 'btc' -> 'BTCUSDT')
        # This handles symbols like BTC, ETH, SOL, XRP natively against USDT.
        self.ticker_to_symbol = {
            item['symbol'].replace('USDT', '').lower(): item['symbol'] 
            for item in tickers_list if item['symbol'].endswith('USDT')
        }

    def get_price_by_ticker(self, ticker, vs_currency="usdt"):
        # Convert ticker to lowercase to match the mapping
        ticker_lower = ticker.lower()
        
        if ticker_lower not in self.ticker_to_symbol:
            raise ValueError(f"Ticker '{ticker}' not found on Binance USDT markets.")
            
        symbol = self.ticker_to_symbol[ticker_lower]
        
        # Fetch the live price directly from Binance public API
        price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        price_response = requests.get(price_url)
        price_response.raise_for_status()
        
        data = price_response.json()
        return float(data['price'])

def main():
    client = BinanceTickerClient()
    while True:
        try:
            crypto_ticker = input("Please enter crypto ticker: ")
            crypto_amount = float(input(f"Please enter {crypto_ticker} quantity to convert to usd: "))

            crypto_price = client.get_price_by_ticker(crypto_ticker)

            print(f"{crypto_amount} {crypto_ticker} is: {crypto_price * crypto_amount} USD")    
        except Exception:
            print(f"{crypto_ticker} is not valid")

if __name__ == '__main__':
    main()