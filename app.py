import streamlit as st

# Crear una función para mostrar el contenido según la opción seleccionada
def show_content(option):
    if option == "Inicio":
        st.write("Contenido de Inicio: ¡Hola!")
    elif option == "Fin":
        st.write("Contenido de Fin: ¡Adiós!")

# Crear una barra de menú en la barra lateral
st.sidebar.title("Menú")
menu_option = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Fin"])

# Mostrar el contenido según la opción seleccionada
show_content(menu_option)
