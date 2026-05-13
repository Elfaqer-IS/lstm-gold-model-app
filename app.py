import streamlit as st
import numpy as np
import pandas as pd
import os
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

st.title("📈 Gold Price Prediction (LSTM)")

# ---------------------------
# LOAD MODEL (sécurisé)
# ---------------------------
@st.cache_resource
def load_lstm_model():
    if os.path.exists("gold_model.h5"):
        return load_model("gold_model.h5")
    else:
        st.error("❌ Modèle gold_model.h5 introuvable")
        return None

model = load_lstm_model()

# ---------------------------
# LOAD DATA (sécurisé)
# ---------------------------
if os.path.exists("predictions.csv"):
    df = pd.read_csv("predictions.csv")
else:
    st.warning("⚠️ predictions.csv introuvable")
    df = pd.DataFrame()

# ---------------------------
# YFINANCE (avec cache pour éviter rate limit)
# ---------------------------
@st.cache_data(ttl=3600)
def get_gold_data():
    data = yf.download("GC=F", period="1y")
    return data

st.subheader("📊 Données Or")
gold_data = get_gold_data()
st.dataframe(gold_data.tail())

# ---------------------------
# PREDICTION (sécurisée)
# ---------------------------
if model is not None and not df.empty:
    st.subheader("🔮 Résultats prédictions")
    st.dataframe(df)
