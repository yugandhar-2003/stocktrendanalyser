# stocktrendanalyser

# 📈 Stock Trend Analyzer

A simple and interactive Python-based stock trend analyzer built in **Google Colab**. This tool fetches historical stock data using `yfinance`, visualizes price trends and moving averages, and performs forecasting using both **Linear Regression** and **Facebook Prophet**.

---

## 🔧 Features

- ✅ Download historical stock data using Yahoo Finance API  
- 📊 Plot stock closing prices with 50-day and 200-day SMA (Simple Moving Averages)  
- 📈 Predict future price trends using Linear Regression  
- 🔮 Forecast next 90 days using Facebook Prophet  
- 📌 Summary of key stats like highest, lowest, and current price

---

## 🛠️ Requirements

This project runs in Google Colab. The following libraries are automatically installed in the notebook:

- `yfinance`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `prophet`

---

## 🚀 How to Use

1. Open the notebook in [Google Colab](https://colab.research.google.com)
2. Run the cells step by step
3. Modify the `ticker` symbol (default is `AAPL`) to analyze any other stock
4. Visualize trends, view statistics, and forecast prices

---

## 🧠 Example Ticker Symbols

| Company       | Ticker |
|---------------|--------|
| Apple         | AAPL   |
| Microsoft     | MSFT   |
| Tesla         | TSLA   |
| Amazon        | AMZN   |
| Google (Alphabet) | GOOG  |

---

## 📂 Files

- `stock_trend_analyzer.ipynb` – Main notebook for running the trend analyzer
- `README.md` – This file

---
