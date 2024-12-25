# Thư viện
import streamlit as st
import pandas as pd
import numpy as np
import joblib as jb
import yfinance as yf
from datetime import datetime, timedelta

# Tên web app
st.title("Stock Price Prediction App")

# Tên cổ phiếu
stock_options = {
    "FPT Corporation (FPT)": "FPT.VN",
    "Vinamilk (VNM)": "VNM.VN",
    "Hoa Phat Group (HPG)": "HPG.VN",
    "The Gioi Di Dong (MWG)": "MWG.VN",
    "Vietcombank (VCB)": "VCB.VN",
}
stock_name = st.selectbox("Chọn cổ phiếu:", options=list(stock_options.keys()))
stock_ticker = stock_options[stock_name]
stock = {
    "FPT.VN": 'FPT',
    "VNM.VN": 'VNM',
    "HPG.VN": 'HPG',
    "MWG.VN": 'MWG',
    "VCB.VN": 'VCB'
}
# Số ngày muốn dự đoán
n_days = st.number_input("Chọn số ngày muốn dự đoán (tối đa 60 ngày, mặc định 7 ngày):", min_value=1, value=7, step=1)
# Tải những model và scaler đã được train và fit
model = jb.load('Linear model trained.pkl')
scaler = jb.load('Scaler fitted.pkl')
def generate_features(stock_ticker):
    start_date = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Tải dữ liệu từ sàn Yahoo Finance
    stock = yf.download(stock_ticker, start=start_date, end=end_date).reset_index()
    # Xử lý MultiIndex
    stock.columns = stock.columns.get_level_values(0)
    # Tạo chuỗi ngày liên tục 60 ngày
    full_date_range = pd.date_range(start=start_date, end=end_date)
    
    # Xử lý dữ liệu khuyết thiếu
    missing_dates = full_date_range.difference(stock['Date'])
    missing_dates = pd.DataFrame({'Date': missing_dates})
    stock = pd.concat([stock, missing_dates], ignore_index=True)
    stock['Date'] = pd.to_datetime(stock['Date'])
    stock = stock.sort_values(by='Date', ascending=False).reset_index(drop=True)
    stock = stock.set_index('Date')
    stock = stock.fillna(stock.mean())

    # Lấy dữ liệu giá đóng cửa
    price = stock['Close']
    features = {}
    # Những ngày trong quá khứ dùng để dự đoán
    days_list = list(range(0, 60, 7)) + list(range(6, 60, 7)) + list(range(5, 60, 7))
    for i in days_list:
        features[f'Price past {i+1} days'] = price.iloc[i]
    df = pd.DataFrame(features, index=[0])
    return [df,price]
def predict(x):
    x_scaled = scaler[stock[stock_ticker]].transform(x)
    # Dự đoán
    y = model[stock[stock_ticker]].predict(x_scaled)
    return round(y[0],2)
if st.button("Dự đoán"):
    try:
            # Chuẩn bị dữ liệu
            price = generate_features(stock_ticker)
            X = price[0]
            # Dự đoán
            future_prices = []
            cummulative_profit = 0
            for i in range(1,n_days+1):
                future_price = predict(X)
                cummulative_profit = cummulative_profit + (future_price - X['Price past 1 days'].values[0])
                future_prices.append(future_price)
                # Thêm giá đã dự đoán vào dataframe để dự đoán tiếp
                new_index = datetime.now() + timedelta(days=i)
                x = price[1]
                x.loc[new_index] = future_price 
                x = x.sort_index(ascending=False)
                days_list = list(range(0, 60, 7)) + list(range(6, 60, 7)) + list(range(5, 60, 7))
                features = {}
                for i in days_list:
                    features[f'Price past {i+1} days'] = x.iloc[i]
                    X = pd.DataFrame(features, index=[0])
            if cummulative_profit >= 0:
                decision = "Mua"
            else:
                decision = "Bán"
            # Hiển thị dự đoán
            future_dates = [datetime.now() + timedelta(days=i) for i in range(1, n_days + 1)]
            predictions = pd.DataFrame({"Date": future_dates, "Predicted Price": future_prices})
            st.subheader("Predicted Prices")
            st.write(predictions)
            st.line_chart(predictions.set_index("Date"))
            # Hiển thị lợi nhuận tích lũy và quyết định
            st.metric("Lợi nhuận tích lũy: ", round(cummulative_profit,2)) 
            st.metric("Lời khuyên", decision)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")