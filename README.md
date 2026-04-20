BEL Stock Price Forecasting using ARIMA

 Overview:
This project analyzes and forecasts Bharat Electronics Limited (BEL) stock prices using the ARIMA time series model. It focuses on historical trend analysis and short-term prediction.

Objective:
Clean and preprocess stock data
Perform time series analysis
Build ARIMA model for forecasting
Predict future stock trends

Dataset:

Columns used:
DateTime → converted to Date
BELEQN → treated as Close price

Only cleaned Close price is used for modeling.

Tools Used:
Python
Pandas
Matplotlib
Statsmodels (ARIMA)

Data Processing:
Renamed columns
Converted date format
Removed missing/infinite values
Applied forward cleaning

Model Used:
ARIMA (1,1,1)
ADF test for stationarity
ACF & PACF plots for analysis

Output:
Generated visualizations:
Trend plot (trend.png)
ACF plot (acf.png)
PACF plot (pacf.png)
Forecast plot (forecast.png)

Project Structure:

BEL-Stock-ARIMA-Forecasting/
├── data/
├── notebook/
├── output/
├── requirements.txt
└── README.md

Note:
This model is for educational purposes only and not for financial decision-making.

Result:
The ARIMA model captures stock trend behavior and provides short-term forecasting insights.

Student Details: 
Kashaf Khan 
Uin - 231A055 , roll no. - 30 
