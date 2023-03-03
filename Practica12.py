#Importación de librerias
from tkinter import *

#Creación de la ventana
ventana = Tk()
ventana.title("Login")
ventana.geometry("800x600")
ventana.config(bg="#c2d6d6")

#Creación de secciones
seccion1 = Frame(ventana, bg='#c2d6d6')
seccion1.pack(expand=True, fill= 'both')

seccion2 = Frame(ventana, bg='#c2d6d6', )
seccion2.pack(expand=True, fill='both')


#Creatividad artistica
label0 = Label(seccion1, text="",font=40, fg="black", bg='#a3c2c2')
label0.pack(fill="x")
label1 = Label(seccion1, text="BIENVENIDO",font=40, fg="black", bg='#a3c2c2')
label1.pack(fill="x")
label2 = Label(seccion1, text="",font=40, fg="black", bg='#a3c2c2')
label2.pack(fill="x")




correo = Entry(seccion2)
correo.pack()

password = Entry(seccion2)
password.pack()


#Creacion del boton
botonLogin = Button(seccion2, text="Login", bg="#85adad", fg="#ffffff")
botonLogin.pack()






ventana.mainloop()