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

# Crear el menú en el header
st.markdown(
    """
    <div class="header">
        <a class="menu-item" href="#inicio">Inicio</a>
        <a class="menu-item" href="#opcion1">Opción 1</a>
        <a class="menu-item" href="#opcion2">Opción 2</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Agregar espaciado para separar el menú del contenido
st.write("")

# Agregar secciones para cada opción del menú
if st.button("Inicio"):
    st.write("¡Hola! Bienvenido a la sección de Inicio.")

if st.button("Opción 1"):
    st.write("Esta es la sección de la Opción 1. ¡Contenido interesante!")

if st.button("Opción 2"):
    st.write("Aquí está la sección de la Opción 2. ¡Descubre más contenido!")

# Agregar espaciado al final
st.write("")

