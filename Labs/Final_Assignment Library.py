import yfinance as yf
import json
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")
with open('D:\\Saurabh Pandey\\Softwares\\Python\\Python\\Analyzing-Historical-Stock-Revenue-Data-and-Building-a-Dashboard\\Files\\apple.json') as json_file:
    apple_info = json.load(json_file)
print(apple_info['country'])

apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

print(apple.dividends)
