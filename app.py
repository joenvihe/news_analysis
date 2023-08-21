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
        <a class="menu-item" href="#" onclick="selectOption('Inicio')">Inicio</a>
        <a class="menu-item" href="#" onclick="selectOption('Opción 1')">Opción 1</a>
        <a class="menu-item" href="#" onclick="selectOption('Opción 2')">Opción 2</a>
    </div>
    <script>
    function selectOption(option) {
        Streamlit.setSessionState({ selected_option: option });
    }
    </script>
    """,
    unsafe_allow_html=True,
)

# Contenido de la página
st.title("Contenido de la Página")

# Detectar la opción seleccionada en el menú
if "selected_option" not in st.session_state:
    st.session_state.selected_option = "Inicio"

# Mostrar el contenido correspondiente a la opción seleccionada
if st.session_state.selected_option == "Opción 1":
    st.write("Hola")
elif st.session_state.selected_option == "Opción 2":
    st.write("Adiós")
