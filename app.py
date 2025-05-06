import streamlit as st
from docx import Document
import datetime

# Función para convertir el documento a formato GIFT
def convertir_a_gift(docx_file):
    doc = Document(docx_file)

    gift_lines = ["$CATEGORY: $system$/IEP/Chatbots/c1\n\n"]
    question = ""
    options = []
    correct = ""
    feedback = ""
    question_number = 1

    def agregar_pregunta():
        nonlocal question_number
        if question and options:
            gift_lines.append(f"::P{question_number:02d}_{datetime.datetime.now().strftime('%d%m%y')}::[html]<p>{question}</p>{{")
            for opt in options:
                letra = opt[0]
                texto = opt[3:].strip()
                simbolo = "=" if letra == correct else "~"
                gift_lines.append(f"{simbolo}<p>{texto}</p>#{'<p>' + feedback + '</p>'}")
            gift_lines.append("}\n")
            question_number += 1

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        if text[0].isdigit() and "." in text:
            agregar_pregunta()
            question = text[text.find('.') + 1:].strip()
            options = []

        elif text[0].lower() in ['a', 'b', 'c', 'd'] and text[1:3] == ') ':
            options.append(text)

        elif text.lower().startswith("respuesta correcta"):
            correct = text.split(":", 1)[1].strip()[0].lower()

        elif text.lower().startswith("feedback"):
            feedback = text.split(":", 1)[1].strip()

    agregar_pregunta()

    return "\n".join(gift_lines)

# Interfaz de usuario
st.set_page_config(page_title="Conversor GIFT", layout="centered")
st.title("📄 Conversor de Exámenes Word a Formato GIFT para Moodle")

st.write("Sube un archivo `.docx` con preguntas y respuestas. El sistema lo convertirá automáticamente al formato GIFT utilizado por Moodle.")

uploaded_file = st.file_uploader("📤 Sube tu archivo Word", type=["docx"])

if uploaded_file:
    gift_content = convertir_a_gift(uploaded_file)
    st.success("✅ Conversión exitosa. Descarga el archivo a continuación:")

    st.download_button(
        label="📥 Descargar archivo GIFT (.txt)",
        data=gift_content,
        file_name="examen_convertido.txt",
        mime="text/plain"
    )