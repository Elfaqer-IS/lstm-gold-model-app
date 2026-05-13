import os

if os.path.exists("predictions.csv"):
    df = pd.read_csv("predictions.csv")
else:
    st.warning("predictions.csv introuvable")
    df = None
