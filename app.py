import streamlit as st

# Agregar el estilo CSS personalizado para el menú en el header
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
        <a class="menu-item" href="#">Inicio</a>
        <a class="menu-item" href="#">Opción 1</a>
        <a class="menu-item" href="#">Opción 2</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Contenido de la página
st.title("Contenido de la Página")

# Detectar la opción seleccionada en el menú
menu_option = st.session_state.selected_option

# Mostrar el contenido correspondiente a la opción seleccionada
if menu_option == "Opción 1":
    st.write("Hola")
elif menu_option == "Opción 2":
    st.write("Adiós")
