import streamlit as st
import pandas as pd
import numpy as np

# Import data
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

# Create sidebar
st.sidebar.title("COVID-19 Data")

# Select country
country = st.sidebar.selectbox("Country", df["location"].unique())

# Display data
st.write(df[df["location"] == country])

# Ejecutar la aplicación
if __name__ == "__main__":
    st.run()