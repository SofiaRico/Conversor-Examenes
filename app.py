import streamlit as st
from docx import Document
import datetime
import re

def convertir_a_gift(docx_file):
    doc = Document(docx_file)

    gift_lines = ["$CATEGORY: $system$/IEP/Chatbots/c1\n\n"]
    current_question = {"enunciado": "", "respuestas": [], "correcta": "", "feedback": ""}
    question_number = 0
    fecha_actual = datetime.datetime.now().strftime("%d%m%y")

    def agregar_pregunta(qnum, q):
        if not q["enunciado"] or not q["respuestas"]:
            return
        gift_lines.append(f"::P{qnum}_{fecha_actual}::[html]<p>{q['enunciado']}</p>{{")
        # Separamos cada posible respuesta en caso estén juntas en un solo string
        for opt in q["respuestas"]:
            opciones = re.split(r'(?=[abcdABCD]\))', opt)
            for opcion in opciones:
                if opcion.strip() == '':
                    continue
                letra = opcion[0].lower()
                texto = re.sub(r"^[abcdABCD]\)\s*", "", opcion).strip()
                simbolo = "=" if letra == q["correcta"] else "~"
                gift_lines.append(f"{simbolo}<p>{texto}</p>#<p>{q['feedback']}</p>")
        gift_lines.append("}\n")

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        if re.match(r"^\d+\.", text):
            if current_question["enunciado"]:
                question_number += 1
                agregar_pregunta(question_number, current_question)
                current_question = {"enunciado": "", "respuestas": [], "correcta": "", "feedback": ""}
            current_question["enunciado"] = text.split('.', 1)[1].strip()
        elif re.match(r"^[abcdABCD]\)", text):
            current_question["respuestas"].append(text)
        elif text.lower().startswith("respuesta correcta:"):
            current_question["correcta"] = text.split(":", 1)[1].strip()[0].lower()
        elif text.lower().startswith("feedback:"):
            current_question["feedback"] = text.split(":", 1)[1].strip()

    if current_question["enunciado"]:
        question_number += 1
        agregar_pregunta(question_number, current_question)

    return "\n".join(gift_lines)

# Streamlit UI
st.set_page_config(page_title="Conversor GIFT", layout="centered")
st.title("📄 Conversor de Exámenes Word a Formato GIFT para Moodle")

st.write("Sube un archivo `.docx` con preguntas y respuestas. El sistema lo convertirá al formato GIFT con HTML correctamente estructurado.")

uploaded_file = st.file_uploader("📤 Sube tu archivo Word", type=["docx"])

if uploaded_file:
    gift_content = convertir_a_gift(uploaded_file)
    st.success("✅ Conversión exitosa. Descarga el archivo a continuación:")

    st.download_button(
        label="📥 Descargar archivo GIFT (.txt)",
        data=gift_content,
        file_name="examen_moodle_gift.txt",
        mime="text/plain"
    )