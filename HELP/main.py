import time
from data_collector import get_binance_data
from predictor import get_latest_data, predict_price
from trader import execute_trade
from gui import TradingApp
import tkinter as tk


def main():
    # 初始化GUI
    root = tk.Tk()
    app = TradingApp(root)

    while True:
        # 数据收集
        get_binance_data()

        # 获取最新数据
        latest_data = get_latest_data()

        # 价格预测
        prediction = predict_price(latest_data)

        # 根据预测结果决定交易方向
        if float(prediction) > float(latest_data['close']):
            side = "BUY"
        else:
            side = "SELL"

        # 执行交易
        execute_trade(side=side)

        # 更新GUI状态
        app.update_status()

        # 每分钟执行一次
        time.sleep(60)


if __name__ == "__main__":
    main()
