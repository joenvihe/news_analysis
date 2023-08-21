import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos de ejemplo (puedes reemplazarlo con tus propios datos)
data = pd.DataFrame({
    'Fecha': pd.date_range('2023-01-01', '2023-08-31', freq='D'),
    'Ventas': np.random.randint(100, 1000, size=243),
    'Gastos': np.random.randint(50, 500, size=243),
    'Utilidad': np.random.randint(10, 300, size=243)
})

# Título de la página
st.title("Dashboard de Análisis de Datos")

# Create two columns layout
col1, col2 = st.columns(2)

# Column 1: Display country data
with col1:
    # Gráfico de líneas para Ventas y Gastos
    st.subheader("Gráfico de Ventas y Gastos")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Fecha', y='Ventas', label='Ventas')
    sns.lineplot(data=data, x='Fecha', y='Gastos', label='Gastos')
    plt.xlabel("Fecha")
    plt.ylabel("Monto")
    plt.legend()
    st.pyplot(plt)


    # Gráfico de dispersión para Ventas vs. Utilidad
    st.subheader("Gráfico de Ventas vs. Utilidad")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Ventas', y='Utilidad')
    plt.xlabel("Ventas")
    plt.ylabel("Utilidad")
    st.pyplot(plt)

# Column 2: Display charts
with col2:
    # Gráfico de barras para Utilidad
    st.subheader("Gráfico de Utilidad")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x='Fecha', y='Utilidad')
    plt.xlabel("Fecha")
    plt.ylabel("Utilidad")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Tabla de datos
    st.subheader("Tabla de Datos")
    st.dataframe(data)

    # Resumen estadístico
    st.subheader("Resumen Estadístico")
    st.write(data.describe())

# Información de contacto
st.sidebar.title("Contacto")
st.sidebar.write("Correo electrónico: ejemplo@example.com")
st.sidebar.write("Teléfono: +123-456-7890")