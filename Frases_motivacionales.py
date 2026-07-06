import tkinter as tk
import random

frases = [
    ("El único modo de hacer un gran trabajo es amar lo que haces.", "Steve Jobs"),
    ("No cuentes los días, haz que los días cuenten.", "Muhammad Ali"),
    ("El éxito es la suma de pequeños esfuerzos repetidos.", "Robert Collier"),
    ("Cree que puedes y ya estás a medio camino.", "Theodore Roosevelt"),
    ("La mejor forma de predecir el futuro es creándolo.", "Peter Drucker"),
    ("Cae siete veces, levántate ocho.", "Proverbio japonés"),
]

temas = {
    "atardecer": ("#ff7e5f", "#ffffff"),
    "oceano":    ("#2b5876", "#e0f7fa"),
    "bosque":    ("#134e13", "#e8f5e9"),
    "lavanda":   ("#6a5acd", "#f3e5f5"),
    "medianoche": ("#1a1a2e", "#eaeaea"),
}

ventana = tk.Tk()
ventana.title("Frases Motivacionales")
ventana.geometry("480x300")
ventana.resizable(False, False)

label_frase = tk.Label(
    ventana, text="", wraplength=420, font=("Georgia", 16, "italic"),
    justify="center"
)
label_frase.pack(expand=True, padx=20)

label_autor = tk.Label(ventana, text="", font=("Georgia", 12, "bold"))
label_autor.pack(pady=(0, 20))

def nueva_frase():
    frase, autor = random.choice(frases)
    nombre_tema, (fondo, texto) = random.choice(list(temas.items()))

    ventana.configure(bg=fondo)
    label_frase.configure(text=f"“{frase}”", bg=fondo, fg=texto)
    label_autor.configure(text=f"— {autor}   ·   tema: {nombre_tema}", bg=fondo, fg=texto)
    boton.configure(bg=texto, fg=fondo)

boton = tk.Button(
    ventana, text="Nueva frase", font=("Georgia", 12, "bold"),
    relief="flat", padx=15, pady=8, command=nueva_frase
)
boton.pack(pady=10)

nueva_frase()  
ventana.mainloop()