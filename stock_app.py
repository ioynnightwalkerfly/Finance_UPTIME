import yfinance as yf
import streamlit as st

# ส่วนอินพุต
st.title("Stock Price Viewer")
symbol = st.text_input("Enter stock symbol (e.g., NVDA):", "NVDA")
start_date = st.date_input("Start date", value=None)
end_date = st.date_input("End date", value=None)

# ดึงข้อมูลหุ้น
if st.button("Get Stock Data"):
    if start_date and end_date:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        st.line_chart(stock_data['Close'])
        st.write(stock_data)
    else:
        st.error("Please select a valid date range.")
