# trader.py
from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def execute_trade(symbol="BTCUSDT", side="BUY", quantity=0.001, price=None):
    order = client.order_limit(
        symbol=symbol,
        side=side,
        quantity=quantity,
        price=price
    )
    return order

if __name__ == "__main__":
    side = "BUY"  # or "SELL" based on prediction
    order = execute_trade(side=side)
    print(order)
