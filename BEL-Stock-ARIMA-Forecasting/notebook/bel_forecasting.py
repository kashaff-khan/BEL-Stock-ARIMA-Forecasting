import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

# Load your dataset
df = pd.read_csv("data/BEL.csv")

# Rename columns properly
df = df.rename(columns={
    'DateTime': 'Date',
    'BELEQN': 'Close'
})

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Set index
df.set_index('Date', inplace=True)

# Keep only Close column
df = df[['Close']]
df = pd.read_csv("data/BEL.csv")

df = df.rename(columns={
    'DateTime': 'Date',
    'BELEQN': 'Close'
})

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df = df[['Close']]

# CLEAN DATA (IMPORTANT FIX)
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df = df.replace([float('inf'), -float('inf')], pd.NA)
df = df.dropna()
# Convert to numeric (important)
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Remove NaN and infinite values
df = df.replace([float('inf'), -float('inf')], pd.NA)
df = df.dropna()

# Handle missing values
df = df.ffill()

# 📈 Plot Trend
plt.figure(figsize=(10,5))
plt.plot(df['Close'])
plt.title("BEL Stock Price Trend")
plt.savefig("output/trend.png")
plt.show()

# 📊 ADF Test
result = adfuller(df['Close'])
print("ADF Statistic:", result[0])
print("p-value:", result[1])

# Differencing
df_diff = df['Close'].diff().dropna()

# 📉 ACF
plot_acf(df_diff)
plt.savefig("output/acf.png")
plt.show()

# 📉 PACF
plot_pacf(df_diff)
plt.savefig("output/pacf.png")
plt.show()

# 🤖 ARIMA Model
model = ARIMA(df['Close'], order=(1,1,1))
model_fit = model.fit()

# 🔮 Forecast
forecast = model_fit.forecast(steps=30)

plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='Historical')
plt.plot(forecast, label='Forecast', color='red')
plt.legend()
plt.title("BEL Forecast")
plt.savefig("output/forecast.png")
plt.show()
