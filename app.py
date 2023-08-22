import streamlit as st

# Estilo CSS para el menú en el header
st.markdown(
    """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        background-color: #f2f2f2;
        padding: 10px 20px;
        align-items: center;
    }
    
    .menu-item {
        margin-right: 20px;
        color: #333;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

urlpath = ' http://157.230.88.234:8888'


# Crear el menú en el header
st.markdown(
    """
    <div class="header">
        <a class="menu-item" href="{urlpath}?page=inicio">Inicio</a>
        <a class="menu-item" href="{urlpath}?page=hola">Hola</a>
        <a class="menu-item" href="{urlpath}?page=fin">Fin</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Agregar título a la portada
st.title("Portada")
query_params = st.experimental_get_query_params()
print(query_params)
option = "inicio"

# Mostrar sección de Inicio
if option == "inicio":
    st.header("Sección de Inicio")
    st.write("¡Bienvenido a la sección de Inicio! Aquí encontrarás información de la portada.")

# Mostrar mensaje "Hola"
if option == "hola":
    st.header("¡Hola!")
    st.write("¡Hola! Este es un mensaje de saludo.")

# Mostrar mensaje "Fin"
if option == "fin":
    st.header("Fin")
    st.write("¡Gracias por visitar la sección de Fin!")

# Agregar espaciado al final
st.write("")
