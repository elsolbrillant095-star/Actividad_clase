import tkinter as tk
from tkinter import messagebox
import json, os

ARCHIVO = "habitos.json"
habitos = []

def guardar():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(habitos, f, ensure_ascii=False, indent=2)

def cargar():
    global habitos
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            habitos = json.load(f)
    actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for h in habitos:
        estado = "✔" if h["hecho"] else "✖"
        lista.insert(tk.END, f"{estado} {h['nombre']} - {h['minutos']} min")

def agregar():
    nombre = ent_nombre.get().strip()
    minutos = ent_min.get().strip()
    if not nombre or not minutos:
        messagebox.showwarning("Error","Completa todos los campos")
        return
    try:
        minutos = int(minutos)
    except ValueError:
        messagebox.showwarning("Error","Los minutos deben ser un número")
        return
    habitos.append({"nombre":nombre,"minutos":minutos,"hecho":False})
    ent_nombre.delete(0,tk.END)
    ent_min.delete(0,tk.END)
    guardar()
    actualizar_lista()

def marcar(valor):
    try:
        i = lista.curselection()[0]
    except IndexError:
        messagebox.showwarning("Error","Selecciona un hábito")
        return
    habitos[i]["hecho"] = valor
    if not valor:
        habitos[i]["minutos"] += 5
    guardar()
    actualizar_lista()

def nuevo_dia():
    for h in habitos:
        if not h["hecho"]:
            h["minutos"] += 5
        h["hecho"] = False
    guardar()
    actualizar_lista()
    messagebox.showinfo("Nuevo día","¡Comienza un nuevo día!")

root=tk.Tk()
root.title("📚 Daily Habit Tracker")
root.geometry("560x620")
root.configure(bg="#eef6ff")

tk.Label(root,text="📚 Daily Habit Tracker",font=("Arial",20,"bold"),
         bg="#eef6ff",fg="#1e3a8a").pack(pady=15)

frm=tk.Frame(root,bg="#eef6ff")
frm.pack()

tk.Label(frm,text="Nombre del hábito",bg="#eef6ff").grid(row=0,column=0,sticky="w")
ent_nombre=tk.Entry(frm,width=35,font=("Arial",11))
ent_nombre.grid(row=1,column=0,pady=5)

tk.Label(frm,text="Minutos",bg="#eef6ff").grid(row=2,column=0,sticky="w")
ent_min=tk.Entry(frm,width=15,font=("Arial",11))
ent_min.grid(row=3,column=0,pady=5)

tk.Button(root,text="➕ Agregar hábito",bg="#2563eb",fg="white",width=25,
          command=agregar).pack(pady=10)

lista=tk.Listbox(root,width=55,height=14,font=("Arial",11),
                 bg="white",selectbackground="#93c5fd")
lista.pack(pady=10)

bot=tk.Frame(root,bg="#eef6ff")
bot.pack()

tk.Button(bot,text="✔ Hecho",bg="#16a34a",fg="white",width=18,
          command=lambda: marcar(True)).grid(row=0,column=0,padx=5,pady=5)
tk.Button(bot,text="✖ No hecho (+5 min)",bg="#dc2626",fg="white",width=18,
          command=lambda: marcar(False)).grid(row=0,column=1,padx=5,pady=5)
tk.Button(root,text="🔄 Nuevo día",bg="#f59e0b",fg="white",width=20,
          command=nuevo_dia).pack(pady=10)

cargar()
root.mainloop()
