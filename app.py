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

# Estilo CSS para el menú en el header

#


st.markdown(
    """
    <style>
    .header {
        display: flex;
        top: 0;
        justify-content: space-between;
        width: 100%;
        background-color: #f2f2f2;
        padding: 10px 20px;
        align-items: center;
        z-index: 100;        
    }

    .menu-item {
        margin-right: 20px;
        color: #333;
        text-decoration: none;
        font-weight: bold;
    }

    header[data-testid='stHeader'] {
        height:0%;
    }
    
    div[data-testid='block-container']{
        max-width:90%;
        padding-top:0%; 
    }

    div[data-testid='stToolbar'] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Crear el menú en el header
st.markdown(
    """
    <div class="header">
        <a class="menu-item" href="?page=inicio" target="_self">Inicio</a>
        <a class="menu-item" href="?page=hola" target="_self">Hola</a>
        <a class="menu-item" href="?page=fin" target="_self">Fin</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Agregar título a la portada
st.title("Portada")
query_params = st.experimental_get_query_params()
if "page" in query_params:
    option = query_params["page"][0]
else:
    option = "inicio"
print(option)

# Mostrar sección de Inicio
if option == "inicio":
    st.write("Bienvenido al manual de usuario de la aplicación. Aquí encontrarás información sobre cómo utilizar la aplicación y sus características principales.")
    # Create two columns layout
    col1, col2, col3 = st.columns(3)

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

    # Column 3: Display charts
    with col3:
        # Tabla de datos
        st.subheader("Tabla de Datos")
        st.dataframe(data)

        # Resumen estadístico
        st.subheader("Resumen Estadístico")
        st.write(data.describe())

# Mostrar mensaje "Hola"
if option == "hola":
    st.session_state.option = "hola"
    st.header("¡Hola!")
    st.write("¡Hola! Este es un mensaje de saludo.")

# Mostrar mensaje "Fin"
if option == "fin":
    st.session_state.option = "fin"
    st.header("Fin")
    st.write("¡Gracias por visitar la sección de Fin!")
