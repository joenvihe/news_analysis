import streamlit as st

# Agregar CSS personalizado para la barra de menú
st.markdown(
    """
    <style>
    .menu-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #333;
        color: white;
    }
    
    .menu-option {
        margin-right: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Crear la barra de menú en la cabecera
st.markdown(
    """
    <div class="menu-bar">
        <div class="menu-option" id="inicio">Inicio</div>
        <div class="menu-option" id="hola">Hola</div>
        <div class="menu-option" id="fin">Fin</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Obtener el valor de la opción seleccionada
option = st.session_state.selected_option
if option:
    print("hol")
else:
    option = "inicio"

# Mostrar contenido según la opción seleccionada
if option == "inicio":
    st.title("Página de Inicio")
    st.write("Bienvenido a la página de inicio.")
elif option == "hola":
    st.title("Página de Hola")
    st.write("¡Hola! Esta es la página de saludo.")
elif option == "fin":
    st.title("Página de Fin")
    st.write("Esta es la página de fin.")
