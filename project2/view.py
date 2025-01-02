import streamlit as st
from models import ModelHandler

handler = ModelHandler()

st.title("Traduce y resume con IA")
st.write("Introduce un texto para generar el contenido")

user_input = st.text_area("Introduce el texto:")

if st.button("Generar"):
    if user_input.strip():
        st.subheader("Traducción:")
        translation = handler.translate_text(user_input, source_lang="English", target_lang="German")
        st.write(translation)

        st.subheader("Resumen:")
        summary = handler.summarize_text(user_input, max_length=50, min_length=10)
        st.write(summary)

    else:
        st.warning("Por favor, introduce un texto.")