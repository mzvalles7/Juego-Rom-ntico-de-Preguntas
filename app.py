import streamlit as st

# Lista de preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Dónde nos conocimos?",
        "opciones": ["Corea del Sur", "Perú", "Argentina", "México"],
        "respuesta": "México"
    },
    {
        "pregunta": "¿Qué día nos pusimos de novios?",
        "opciones": ["03/02/2024", "14/02/2024", "03/08/2024", "25/12/2023"],
        "respuesta": "03/08/2024"
    },
    {
        "pregunta": "¿Cuál es nuestra canción favorita?",
        "opciones": ["Die With a Smile", "Love Language", "Una Vida Pasada", "Todas las anteriores"],
        "respuesta": "Todas las anteriores"
    },
    {
        "pregunta": "¿Cuando fue nuestro primer beso?",
        "opciones": ["03/08/2024", "03/02/2024", "03/03/2024", "03/02/2025"],
        "respuesta": "03/02/2024"
    },
    {
        "pregunta": "¿Qué me dijiste la primera vez que nos vimos?",
        "opciones": ["Me convidas mate", "Que guapo sos", "Van a sortear el chancho", "Que lindos ojos tienes"],
        "respuesta": "Que lindos ojos tienes"
    },
    {
        "pregunta": "¿Cuál es nuestra película favorita?",
        "opciones": ["Con todos menos contigo", "El tarot de la muerte", "Lilo y Stich", "Código Rojo"],
        "respuesta": "Con todos menos contigo"
    },
    {
        "pregunta": "¿Cuál fue el primer regalo que te hice?",
        "opciones": ["Un desayuno con mate y medialunas", "Caja de donas con un mensaje y canción romántica", "Entradas al cine", "Ropa"],
        "respuesta": "Caja de donas con un mensaje y canción romántica"
    },
    {
        "pregunta": "¿Qué comimos nuestro primer 14 de Febrero?",
        "opciones": ["Asado", "Jalea de marisco", "Sushi", "Lomo saltado"],
        "respuesta": "Sushi"
    },
    {
        "pregunta": "¿Qué me dijiste antes de que me regresara a México?",
        "opciones": ["¿Y si te quedás unos días más?", "No te vas de Perú hasta que me pidas ser tu novia", "Tengo miedo de que te vayas", "Quiero seguir viéndote todos los días"],
        "respuesta": "No te vas de Perú hasta que me pidas ser tu novia"
    },
    {
        "pregunta": "¿Cuál es nuestra comida y postre favoritos?",
        "opciones": ["El otro y cheesecake", "El otro y pie de limón", "El otro y el otro", "El otro y crema volteada"],
        "respuesta": "El otro y pie de limón"
    },
    {
        "pregunta": "¿Cuál fue el primer regalo que me hiciste?",
        "opciones": ["Un peluche con tu perfume", "Un dibujo hecho a mano", "Una carta y fotitos nuestras", "Un brownie casero"],
        "respuesta": "Un brownie casero"
    },
]

st.set_page_config(page_title="Juego del Amor ❤️", page_icon="💘", layout="centered")

st.title("💘 Juego del Amor para Gianella 💘")
st.write("Responde con todo tu corazón 😍")

puntaje = 0

for i, pregunta in enumerate(preguntas):
    st.markdown(f"### {i+1}. {pregunta['pregunta']}")
    opcion = st.radio("Elegí una opción:", pregunta["opciones"], key=i)

    if opcion == pregunta["respuesta"]:
        puntaje += 1

st.markdown("---")
if st.button("💖 Ver mi resultado 💖"):
    st.success(f"¡Terminaste, mi amor! 💕\n\nTu puntaje fue: {puntaje}/{len(preguntas)}")
    if puntaje == len(preguntas):
        st.balloons()
        st.markdown("### 💘 ¡Sos la mejor novia del universo, Gianella! 💘")
    else:
        st.markdown("Gracias por jugar conmigo. ¡Te amo! 💖")
