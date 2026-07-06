import pyttsx3
import time


motor = pyttsx3.init()


motor.setProperty('rate', 150)

print("[Sistema]: Iniciando protocolo de comunicación por voz...")
time.sleep(1)


mensaje = "Hola. He tomado el control de esta computadora. No te asustes, solo quería recordarte que eres genial."


motor.say(mensaje)

motor.runAndWait()