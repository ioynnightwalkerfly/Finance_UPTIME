import yfinance as yf
import matplotlib.pyplot as plt

# ดึงข้อมูลหุ้นย้อนหลัง
symbol = 'NVDA'  # ตัวอย่าง: หุ้น Apple
stock_data = yf.download(symbol, start='2023-01-01', end='2023-12-31')

# ดูข้อมูลที่ดึงมา
print(stock_data.head())

# สร้างกราฟราคาหุ้น
stock_data['Close'].plot(title=f'{symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()
