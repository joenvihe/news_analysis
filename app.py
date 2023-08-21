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
