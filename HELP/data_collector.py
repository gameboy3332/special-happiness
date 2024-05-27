# data_collector.py
import requests
import pandas as pd
from config import CSV_PATH

def get_binance_data(symbol="BTCUSDT", interval="1m", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df.to_csv(f"{CSV_PATH}\\{symbol}_data.csv", index=False)
    return df

if __name__ == "__main__":
    get_binance_data()
