import streamlit as st
from transformers import pipeline

pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")

st.title("Sistema de Preguntas y Respuestas")
st.write("Interactúa con el modelo de preguntas y respuestas.")

context = st.text_area("Introduce el contexto:")

question = st.text_input("Introduce tu pregunta:")

if st.button("Obtener respuesta"):
    if context.strip() and question.strip():
        result = pipe(question=question, context=context)
        st.subheader("Respuesta:")
        st.write(result['answer'])
        st.subheader("Puntuación de la respuesta:")
        st.write(result['score'])
    else:
        st.warning("Por favor, proporciona tanto un contexto como una pregunta.")
