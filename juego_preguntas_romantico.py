import tkinter as tk
from tkinter import messagebox

# Lista de preguntas iniciales
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

# Variables de juego
pregunta_actual = 0
puntaje = 0

# Función para mostrar la siguiente pregunta
def mostrar_pregunta():
    global pregunta_actual

    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]
        lbl_pregunta.config(text=pregunta["pregunta"])
        
        for i in range(4):
            botones_opciones[i].config(text=pregunta["opciones"][i], state="normal")
    else:
        mostrar_resultado()

# Función cuando se selecciona una respuesta
def responder(opcion):
    global puntaje, pregunta_actual

    respuesta_correcta = preguntas[pregunta_actual]["respuesta"]
    if opcion == respuesta_correcta:
        puntaje += 1

    pregunta_actual += 1
    mostrar_pregunta()

# Función para mostrar resultado final
def mostrar_resultado():
    mensaje = f"🎉 ¡Terminaste el juego, mi amor!\n\nTu puntaje: {puntaje}/{len(preguntas)}"
    if puntaje == len(preguntas):
        mensaje += "\n\n💘 ¡Sos la mejor novia del universo amor! 💘"
    else:
        mensaje += "\n\nGracias por jugar conmigo. ¡Te amo! 💖"
    messagebox.showinfo("Resultado", mensaje)
    ventana.destroy()

# Ventana principal
ventana = tk.Tk()
ventana.title("Juego del amor ❤️")
ventana.geometry("500x400")
ventana.configure(bg="lightpink")

lbl_pregunta = tk.Label(ventana, text="", font=("Helvetica", 16), bg="lightpink", wraplength=450, justify="center")
lbl_pregunta.pack(pady=40)

botones_opciones = []
for i in range(4):
    btn = tk.Button(ventana, text="", font=("Helvetica", 12), width=40,
                    command=lambda i=i: responder(botones_opciones[i]["text"]))
    btn.pack(pady=5)
    botones_opciones.append(btn)

mostrar_pregunta()
ventana.mainloop()
