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
    st.session_state.option = "inicio"
    st.header("Sección de Inicio")
    st.write("¡Bienvenido a la sección de Inicio! Aquí encontrarás información de la portada.")

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
