import numpy as np
import yfinance as yf
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import os

# Suppress TensorFlow logs to prevent crashes
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class PricePredictor:
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None

    def fetch_data(self, ticker):
        """Fetches last 2 years of stock data silently."""
        # progress=False prevents yfinance from printing to console
        data = yf.download(ticker, period="2y", interval="1d", progress=False)
        if data.empty:
            raise ValueError(f"No data found for {ticker}")
        return data['Close'].values.reshape(-1, 1)

    def train_model(self, ticker):
        """Trains an LSTM model on the fly."""
        # 1. Prepare Data
        data = self.fetch_data(ticker)
        scaled_data = self.scaler.fit_transform(data)

        X_train, y_train = [], []
        prediction_days = 60

        if len(scaled_data) <= prediction_days:
             return "Not enough data."

        for x in range(prediction_days, len(scaled_data)):
            X_train.append(scaled_data[x-prediction_days:x, 0])
            y_train.append(scaled_data[x, 0])

        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

        # 2. Build LSTM
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
        self.model.add(LSTM(units=50, return_sequences=False))
        self.model.add(Dense(units=25))
        self.model.add(Dense(units=1))

        self.model.compile(optimizer='adam', loss='mean_squared_error')
        # verbose=0 ensures SILENCE during training
        self.model.fit(X_train, y_train, batch_size=32, epochs=5, verbose=0)

        return "Model Trained."

    def predict_next_price(self, ticker):
        """Uses the trained model to predict tomorrow's price."""
        if self.model is None:
            self.train_model(ticker)
        
        data = self.fetch_data(ticker)
        scaled_data = self.scaler.transform(data)
        
        prediction_days = 60
        last_60_days = scaled_data[-prediction_days:]
        X_test = []
        X_test.append(last_60_days)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # verbose=0 ensures SILENCE during prediction
        pred_price = self.model.predict(X_test, verbose=0)
        pred_price = self.scaler.inverse_transform(pred_price)
        
        current_price = data[-1][0]
        predicted = pred_price[0][0]
        
        trend = "UP 🟢" if predicted > current_price else "DOWN 🔴"
        
        return {
            "current_price": float(current_price),
            "predicted_next_close": float(predicted),
            "trend": trend
        }