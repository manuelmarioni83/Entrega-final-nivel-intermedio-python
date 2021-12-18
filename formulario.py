import tkinter
import validaciones
import excepciones


class Formulario():
    """
    Esta es la clase Formulario

    """
    def __init__(self, frame):

        """
        El método __init__ es el constructor de la clase Formulario, inicializa el formulario de mi aplicación.

        """

    
        l1 = tkinter.Label(frame, text = "Id")
        l2 = tkinter.Label(frame, text = "Nombre *")
        l3 = tkinter.Label(frame, text = "Apellido *")
        l4 = tkinter.Label(frame, text = "Dirección")
        l5 = tkinter.Label(frame, text = "Teléfono *")
        l6 = tkinter.Label(frame, text = "Email")

        l1.grid(row = 0, column = 0, sticky = tkinter.W,padx=5,pady=5)
        l2.grid(row = 1, column = 0, sticky = tkinter.W,padx=5,pady=5)
        l3.grid(row = 2, column = 0, sticky = tkinter.W,padx=5,pady=5)
        l4.grid(row = 3, column = 0, sticky = tkinter.W,padx=5,pady=5)
        l5.grid(row = 4, column = 0, sticky = tkinter.W,padx=5,pady=5)
        l6.grid(row = 5, column = 0, sticky = tkinter.W,padx=5,pady=5)
            
        self.id = tkinter.Entry(frame,width=30)
        self.nombre = tkinter.Entry(frame,width=30)
        self.apellido = tkinter.Entry(frame,width=30)
        self.direccion = tkinter.Entry(frame,width=30)
        self.telefono = tkinter.Entry(frame,width=30)
        self.email = tkinter.Entry(frame,width=30)

        self.id.grid(row = 0, column = 1,padx=5,pady=5)
        self.nombre.grid(row = 1, column = 1,padx=5,pady=5)
        self.apellido.grid(row = 2, column = 1,padx=5,pady=5)
        self.direccion.grid(row = 3, column = 1,padx=5,pady=5)
        self.telefono.grid(row = 4, column = 1,padx=5,pady=5)
        self.email.grid(row = 5, column = 1,padx=5,pady=5)

    def limpia_campos(self):
        """
        El método limpia_campos borra los datos de los campos de mi formulario

        """
        self.id.delete(0,tkinter.END)
        self.nombre.delete(0,tkinter.END)
        self.apellido.delete(0,tkinter.END)
        self.direccion.delete(0,tkinter.END)
        self.telefono.delete(0,tkinter.END)
        self.email.delete(0,tkinter.END)

    def llenar_campos(self,contacto):
        """
        El método llenar_campos completa los campos del formulario con las variables de una instancia de contacto

        """
        self.id.insert(0,contacto.id)
        self.nombre.insert(0,contacto.nombre)
        self.apellido.insert(0,contacto.apellido)
        self.direccion.insert(0,contacto.direccion)
        self.telefono.insert(0,contacto.telefono)
        self.email.insert(0,contacto.email)

    def validar_campos(self):
        """
        El método validar_campos valida que los datos ingresados por el usuario tengan el formato correcto y que se ingresen los
        datos de carácter obligatorio (nombre, apellido, teléfono)

        """
        try:

            if not validaciones.valida_nombre(self):
                raise excepciones.Nombre_incorrecto

            if not validaciones.valida_apellido(self):
                raise excepciones.Apellido_incorrecto

            if not validaciones.valida_telefono(self):
                raise excepciones.Telefono_incorrecto

            if not validaciones.valida_email(self):
                raise excepciones.Mail_incorrecto
            

        except excepciones.Formulario_excepcion as e1:
            tkinter.messagebox.showerror(message=e1.mensaje_error, title="Error")
            return False
        else:
            return True


    


        