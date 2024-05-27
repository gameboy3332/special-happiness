import openai
import pandas as pd
from config import OPENAI_API_KEY, CSV_PATH

openai.api_key = OPENAI_API_KEY

def get_latest_data(symbol="BTCUSDT"):
    df = pd.read_csv(f"{CSV_PATH}\\{symbol}_data.csv")
    latest_data = df.tail(1).to_dict('records')[0]
    return latest_data

def predict_price(data):
    prompt = f"Based on the following data, predict the next minute's Bitcoin price: {data}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用新的模型名称
        messages=[
            {"role": "system", "content": "You are a financial expert predicting cryptocurrency prices."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50
    )
    prediction = response.choices[0].message['content'].strip()
    return prediction

if __name__ == "__main__":
    latest_data = get_latest_data()
    prediction = predict_price(latest_data)
    print(f"Predicted price: {prediction}")
