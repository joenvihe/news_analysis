import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta


# Cargar los datos de ejemplo (puedes reemplazarlo con tus propios datos)
data = pd.DataFrame({
    'Fecha': pd.date_range('2023-01-01', '2023-08-31', freq='D'),
    'Ventas': np.random.randint(100, 1000, size=243),
    'Gastos': np.random.randint(50, 500, size=243),
    'Utilidad': np.random.randint(10, 300, size=243)
})

# Estilo CSS para el menú en el header

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
query_params = st.experimental_get_query_params()
if "page" in query_params:
    option = query_params["page"][0]
else:
    option = "inicio"
print(option)

# Mostrar sección de Inicio
if option == "inicio":
    # Create a date slider
    #start_date = st.slider("Start date", date=datetime.date(2023, 1, 1))
    #end_date = st.slider("End date", date=datetime.date(2023, 12, 31))

    
    st.title("Portada")
    st.write("Bienvenido al manual de usuario de la aplicación. Aquí encontrarás información sobre cómo utilizar la aplicación y sus características principales.")

    # Agregar estilo CSS para alinear las columnas verticalmente
    st.markdown(
        """
        <style>
        .stButton>button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Create two columns layout
    col1, col2, col3 = st.columns(3)

    # Column 1: Display country data
    with col1:
        # Gráfico de líneas para Ventas y Gastos
        #st.subheader("Gráfico de Ventas y Gastos")
        #plt.figure(figsize=(10, 6))
        #sns.lineplot(data=data, x='Fecha', y='Ventas', label='Ventas')
        #sns.lineplot(data=data, x='Fecha', y='Gastos', label='Gastos')
        #plt.xlabel("Fecha")
        #plt.ylabel("Monto")
        #plt.legend()
        #st.pyplot(plt)

        st.subheader("Lo positivo") 
        sns.set_theme(style="whitegrid")
        # Initialize the matplotlib figure
        f, ax = plt.subplots(figsize=(10, 6))
        # Load the example car crash dataset
        crashes = pd.DataFrame([
            {"noticia":"n1","total":15,"positivo":6},
            {"noticia":"n2","total":11,"positivo":7},
            {"noticia":"n3","total":13,"positivo":3},
            {"noticia":"n4","total":16,"positivo":9},
            {"noticia":"n5","total":19,"positivo":5}
        ]) 
        # Plot the total crashes
        sns.set_color_codes("pastel")
        sns.barplot(x="total", y="noticia", data=crashes,
                    label="Total", color="b")
        # Plot the crashes where alcohol was involved
        sns.set_color_codes("muted")
        sns.barplot(x="positivo", y="noticia", data=crashes,
                    label="Lo-positivo", color="b")
        # Add a legend and informative axis label
        ax.legend(ncol=2, loc="lower right", frameon=True)
        ax.set(xlim=(0, 24), ylabel="",
            xlabel="lo positivo por el total de noticias")
        sns.despine(left=True, bottom=True)
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
        # Gráfico de dispersión para Ventas vs. Utilidad
        st.subheader("Gráfico de Ventas vs. Utilidad")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x='Ventas', y='Utilidad')
        plt.xlabel("Ventas")
        plt.ylabel("Utilidad")
        st.pyplot(plt)

    col21, col22 = st.columns(2)

    # Column 1: Display country data
    with col21:
        # Gráfico de dispersión para Ventas vs. Utilidad
        st.subheader("Gráfico de Ventas vs. Utilidad")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x='Ventas', y='Utilidad')
        plt.xlabel("Ventas")
        plt.ylabel("Utilidad")
        st.pyplot(plt)

    # Column 2: Display charts
    with col22:
        # Gráfico de barras para Utilidad
        st.subheader("Gráfico de Utilidad")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x='Fecha', y='Utilidad')
        plt.xlabel("Fecha")
        plt.ylabel("Utilidad")
        plt.xticks(rotation=45)
        st.pyplot(plt)


    # Gráfico de dispersión para Ventas vs. Utilidad
    st.subheader("Gráfico de Ventas vs. Utilidad")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Ventas', y='Utilidad')
    plt.xlabel("Ventas")
    plt.ylabel("Utilidad")
    st.pyplot(plt)

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
