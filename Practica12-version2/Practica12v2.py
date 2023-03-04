from tkinter import *
from tkinter import messagebox
from Clases import *

#Creación de la ventana
ventana = Tk()
ventana.title("Login")
ventana.geometry("800x600")
ventana.config(bg="#c2d6d6")
ventana.resizable(width=False, height=False)

usuario = StringVar()
contra = StringVar()



# def Login(correo, password):
#     if  correo== ("jesus@123.com") and password == ("12345"):
#         messagebox.showinfo('Bienvenido', "Bienvenido de nuevo.")
#     else:
#         messagebox.showerror('Error', "Correo o Contraseña incorrectos. Intentelo de nuevo.")




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
#Creacion de los input's
correo = (Entry(seccion2, textvariable= usuario))
correo.pack()

password = (Entry(seccion2, textvariable= contra, show="*"))
password.pack()

#Definimos nuestras variables

#Definimos las funciones
def Login():
    us_1 = usuario.get()
    pss_1 = contra.get()
    user = Usuario(us_1, pss_1)
    user.validacion(us_1, pss_1)
    
#Creacion del boton
botonLogin = Button(seccion2, text="Login", bg="#85adad", fg="#ffffff", cursor="hand2", command=Login)
botonLogin.pack()

ventana.mainloop()
