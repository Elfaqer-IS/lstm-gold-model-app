import streamlit as st
import yfinance as yf

st.title("Gold Data")

data = yf.download("GC=F", period="1y", interval="1d")

st.line_chart(data['Close'])
