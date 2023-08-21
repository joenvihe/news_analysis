import streamlit as st

# Estilos CSS personalizados para la barra de menú
custom_styles = """
<style>
.navbar {
    display: flex;
    background-color: #333;
    padding: 10px 0;
    color: white;
}

.nav-link {
    text-decoration: none;
    color: white;
    padding: 5px 10px;
}

.nav-link:hover {
    background-color: #555;
}
</style>
"""

# Barra de menú personalizada
st.markdown(custom_styles, unsafe_allow_html=True)
menu_option = st.selectbox("", ["Inicio", "Fin"], key="menu")

# Sección de contenido
st.title("Contenido")

# Agrega aquí tu lógica para mostrar el contenido correspondiente a la opción seleccionada
if menu_option == "Inicio":
    st.write("Hola, bienvenido.")
elif menu_option == "Fin":
    st.write("Adiós, hasta luego.")


"""
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
st.set_page_config(layout="wide")
# Esconder el mensaje de "Rerunning"



# Estilos CSS para el menú de navegación
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: space-around;
    background-color: #333;
    padding: 10px 0;
}

div[data-testid="stToolbar"] {
  display: none;
}

.nav-link {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# Estilos CSS personalizados para la barra de menú
custom_styles = """
<style>
.navbar {
    display: flex;
    background-color: #333;
    padding: 10px 0;
    color: white;
}

.nav-link {
    text-decoration: none;
    color: white;
    padding: 5px 10px;
}

.nav-link:hover {
    background-color: #555;
}
</style>
"""

# Barra de menú personalizada
st.markdown(custom_styles, unsafe_allow_html=True)
menu_option = st.selectbox("", ["Inicio", "Opción 1", "Opción 2", "Opción 3"], key="menu")

# Sección de contenido
st.title("Contenido Principal")


# Menú de navegación
##st.markdown('<div class="navbar"><a class="nav-link" href="#inicio">Inicio</a><a class="nav-link" href="#opcion1">Opción 1</a><a class="nav-link" href="#opcion2">Opción 2</a><a class="nav-link" href="#opcion3">Opción 3</a></div>', unsafe_allow_html=True)
##menu_option = st.selectbox("Selecciona una opción del menú", ["Inicio", "Opción 1", "Opción 2"])

# Sección Inicio
#st.markdown('<h2 id="inicio">Inicio</h2>', unsafe_allow_html=True)
#st.title("Dashboard de Análisis de Datos")

# Opciones del menú

if menu_option == "Inicio":
    # Sección 1: Introducción
    st.markdown("## Sección 1: Introducción")
    st.write("Bienvenido al manual de usuario de la aplicación. Aquí encontrarás información sobre cómo utilizar la aplicación y sus características principales.")

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

elif menu_option == "Opción 1":
    # Sección 2: Uso básico
    st.markdown('<h2 id="opcion1">Opción 1</h2>', unsafe_allow_html=True)
    st.write("En esta sección, te explicaremos cómo usar las funciones básicas de la aplicación. Por ejemplo, cómo seleccionar un país y visualizar sus datos.")
elif menu_option == "Opción 2":
    st.write("Aquí encontrarás información sobre la Opción 3.")
else:
    st.write("Selecciona una opción del menú para ver la información relacionada.")


# Información de contacto
#st.sidebar.title("Contacto")
#st.sidebar.write("Correo electrónico: ejemplo@example.com")
#st.sidebar.write("Teléfono: +123-456-7890")

"""
