import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

st.title("📊 GOLD DASHBOARD")

# DATA
data = yf.download("GC=F", period="2y", interval="1d")
data = data[['Close']].dropna()

st.line_chart(data)
