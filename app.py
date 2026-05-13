import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# ⚠️ TensorFlow seulement ici (local load model OK)

model = load_model("gold_model.h5")

st.title("📊 GOLD LSTM PREDICTION")

# DATA
data = yf.download("GC=F", period="2y", interval="1d")
data = data[['Close']].dropna()

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

window = 60

x_input = scaled[-window:]
x_input = np.array([x_input])
x_input = np.reshape(x_input, (1, window, 1))

pred = model.predict(x_input, verbose=0)

# inverse scaling
dummy = np.zeros((1,1))
dummy[0,0] = pred[0,0]

pred_price = scaler.inverse_transform(dummy)[0][0]

current_price = data['Close'].values[-1]

signal = "BUY 📈" if pred_price > current_price else "SELL 📉"

st.metric("Current Price", round(current_price, 2))
st.metric("Predicted Price", round(pred_price, 2))

st.subheader("Signal")
st.write(signal)
