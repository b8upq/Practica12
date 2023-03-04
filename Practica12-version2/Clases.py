from tkinter import messagebox

#Declarar clases
class Usuario:
    def __init__(self, correo, password):
        self.correo = correo
        self.password = password
        
    def validacion(self, correo, password):
        
        self.correo = "email.com"
        self.password = "1234"
                
        if  correo == self.correo and password == self.password:
            print("Exito")
            messagebox.showinfo('Bienvenido', "Bienvenido de nuevo.")

        else:
            print("Error.")
            messagebox.showerror('Error', "Correo o Contraseña incorrectos. Intentelo de nuevo.")




 

        
        
    

# class Password:
#     def __init__(self, password):
#         self.password = password
        

# Cla              




    
    