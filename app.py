import streamlit as st
import pandas as pd

st.title("📊 GOLD LSTM DASHBOARD (STABLE)")

# load predictions generated from Colab
df = pd.read_csv("predictions.csv")

st.line_chart(df)

st.write("Dernières valeurs :")
st.dataframe(df.tail())
