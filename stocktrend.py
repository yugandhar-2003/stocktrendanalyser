!pip install yfinance matplotlib pandas seaborn scikit-learn prophet --quiet

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
from prophet import Prophet

# ----  Download stock data ----
ticker = "AAPL"  # You can change this to any stock symbol
df = yf.download(ticker, start="2019-01-01", end="2024-12-31")
df.reset_index(inplace=True)
df.columns = df.columns.str.strip()

# ---- Visualize closing price ----
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.title(f'{ticker} Stock Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.show()

# ----  Add Simple Moving Averages ----
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(14,6))
plt.plot(df['Date'], df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', color='green')
plt.plot(df['Date'], df['SMA_200'], label='200-Day SMA', color='red')
plt.title(f'{ticker} Trend with SMAs')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# ----  Linear Regression Forecast ----
df['Days'] = (df['Date'] - df['Date'].min()).dt.days
X = df[['Days']]
y = df['Close']
model = LinearRegression()
model.fit(X, y)
df['Predicted_Close'] = model.predict(X)

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Actual Close')
plt.plot(df['Date'], df['Predicted_Close'], label='Linear Trend', linestyle='--')
plt.title(f'{ticker} - Actual vs Trend (Linear Regression)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# ----  Prophet Forecast ----
# Prepare data
prophet_df = df[['Date', 'Close']].copy()
prophet_df.columns = ['ds', 'y']
prophet_df['ds'] = pd.to_datetime(prophet_df['ds'], errors='coerce')
prophet_df['y'] = pd.to_numeric(prophet_df['y'], errors='coerce')
prophet_df.dropna(subset=['ds', 'y'], inplace=True)

# Fit and predict
m = Prophet()
m.fit(prophet_df)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)

# Plot forecast
fig = m.plot(forecast)
plt.title(f"{ticker} - Prophet Forecast (Next 90 Days)")
plt.show()

# ----  Print Summary Stats ----
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df.dropna(subset=['Close'], inplace=True)

print(f"Highest Close: {df['Close'].max():.2f}")
print(f"Lowest Close: {df['Close'].min():.2f}")
print(f"Current Close: {df['Close'].iloc[-1]:.2f}")
