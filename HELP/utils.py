# utils.py
import pandas as pd

def calculate_indicators(df):
    df['MA5'] = df['close'].rolling(window=5).mean()
    df['MA10'] = df['close'].rolling(window=10).mean()
    return df

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\柳柳柳柳柳\\PycharmProjects\\b\\BMI計算機\\.venv\\HELP\\aaa\\BTCUSDT_data.csv")
    df = calculate_indicators(df)
    df.to_csv("C:\\Users\\柳柳柳柳柳\\PycharmProjects\\b\\BMI計算機\\.venv\\HELP\\aaa\\BTCUSDT_data_with_indicators.csv", index=False)
