import streamlit as st


# Titulo de la Aplicacion.
st.title('Hola desde Streamlit Cloud')

# Boton para mostrar el mensaje.
if st.button('Mostrar mensaje'):
    st.write('Vos sos amigo de Karina y de Pupo!')