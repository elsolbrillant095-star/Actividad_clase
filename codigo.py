import tkinter as tk
 
screen = tk.Tk()
screen.title("Estado de ánimo")
screen.geometry("600x500")
 
titulo = tk.Label(
    screen,
    text="ESTADO DE ÁNIMO",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)
 
tk.Label(screen, text="¿Cómo te llamas?").pack()
 
entry_nombre = tk.Entry(screen)
entry_nombre.pack()
 
tk.Label(screen, text="¿Cómo te sientes el día de hoy?").pack()

entry_animo = tk.Entry(screen)
entry_animo.pack()

resultado = tk.Label(screen, text="")
resultado.pack(pady=20)
 
def estados_animos():
    nombre=entry_nombre.get().lower()
    tu_estado = entry_animo.get().lower()
 
    if tu_estado == "feliz":
        mensaje = f"{nombre}, nunca dejes de creer en ti y en la capacidad que tienes de lograr todo eso que quieres."
    elif tu_estado == "triste":
        mensaje = f"{nombre},Todo es temporal, incluso los días malos."
    elif tu_estado == "enojado":
        mensaje = f"{nombre},A veces las cosas no salen como queremos, pero era necesario vivirlas para crecer."
    elif tu_estado == "cansado":
        mensaje = f"{nombre},Lo único imposible es aquello que no intentas."
    else:
        mensaje = "No reconozco ese estado de ánimo."
 
    resultado.config(text=mensaje)
 
tk.Button(
    screen,
    text="Mostrar mensaje",
    command=estados_animos
).pack(pady=10)
 
screen.mainloop()
 