from agenda_model import Agenda_model
from agenda_view import Agenda_view
from contacto import Contacto
from tkinter import messagebox

class Agenda_controller():
    """
    Esta clase es el controlador de la aplicación
    """
    def __init__(self):
        """
        El método __init__ es el constructor de la clase Agenda_controller
        """
        self.modelo = Agenda_model()
        self.vista = Agenda_view(self.modelo,self)

    def generar_alta(self):
        """
        El método generar_alta realiza todas las acciones necesarias para dar de alta un nuevo contacto:
        1) Valida que los datos ingresados en los campos de texto sean correctos. Si son incorrectos, muestra al usuario lo que debe cambiar
        2) Crea una instancia de la clase Contacto con los datos ingresados por el usuario en los campos de texto
        3) Inserta el contacto en la BBDD
        4) Actualiza la lista de contactos del treeview
        5) Limpia los campos del formulario
        6) Muestra mensaje de confirmación

        """
        if self.vista.formulario.validar_campos():
            contacto = Contacto(None,self.vista.formulario.nombre.get(),self.vista.formulario.apellido.get(),self.vista.formulario.direccion.get(),self.vista.formulario.telefono.get(), self.vista.formulario.email.get())
            self.modelo.inserta_contacto(contacto)
            self.vista.actualizar_lista()
            self.vista.formulario.limpia_campos()
            messagebox.showinfo(message="Contacto agregado exitosamente", title="Alta")

    def limpia_formulario(self):
        """
        El método limpia_formulario limpia los campos del formulario:
        
        """
        self.vista.formulario.limpia_campos()
    
    def generar_baja(self):
        """
        El método generar_baja realiza todas las acciones necesarias para dar de baja un contacto:
        1) Pide confirmación al usuario de que desea eliminar el contacto
        2) Si el usuario confirma que quiere eliminar el contacto:
            a) Elimina el contacto de la BBDD
            b) Si como resultado de la eliminación, devuelve que la cantidad de registros eliminados es 0, indica al usuario que el ID ingresado no existe
            c) Si como resultado de la eliminación, devuelve que la cantidad de registros eliminados es mayor a 0, actualiza la lista de contactos, 
            limpia los campos del formulario y muestra un mensaje indicando que el contacto se ha eliminado de forma exitosa

        """
        elimina_contacto = messagebox.askyesno(message="¿Está seguro de que desea eliminar este contacto?", title="Eliminación de Contacto")
        if elimina_contacto:
            cantidad = self.modelo.elimina_contacto(self.vista.formulario.id.get())
            if cantidad > 0:
                self.vista.actualizar_lista()
                self.vista.formulario.limpia_campos()
                messagebox.showinfo(message="Contacto eliminado exitosamente", title="Baja")
            else:
                messagebox.showerror(message="El ID solicitado no existe", title="Error")

    def generar_busqueda(self):
        """
        El método generar_busqueda realiza una búsqueda por ID de contacto en la base de datos:
        1) Verifica que el usuario haya ingresado el ID que desea bucar
        2) Busca el contacto en la BBDD
        3) Limpia los campos del formulario
        4) Completa el formulario con los datos del contacto cuyo ID se ha seleccionado
            
        """
        id = self.vista.formulario.id.get()
        if len(id) > 0:
            contacto = self.modelo.buscar_contacto(id)
            self.vista.formulario.limpia_campos()
            if contacto is not None:
                self.vista.formulario.llenar_campos(contacto)

    def seleccionar_contacto(self):

        """
        El método seleccionar_contacto completa los datos del formulario con los datos del registro que se ha seleccionado en 
        el treeview
            
        """
        
        selected = self.vista.lista.focus()
        contacto_selecc = self.vista.lista.item(selected, 'values')
        if len(contacto_selecc) > 0:
            self.vista.formulario.limpia_campos()
            contacto = Contacto(contacto_selecc[0],contacto_selecc[1],contacto_selecc[2],contacto_selecc[3],contacto_selecc[4],contacto_selecc[5])
            self.vista.formulario.llenar_campos(contacto)

    def generar_actualizacion(self):

        """
        El método generar_actualizacion realiza todas las acciones necesarias para actualizar un contacto:
        1) Valida el formato de los datos ingresados en el formulario
        2) Crea una instancia de contacto con los datos que el usuario ha cargado en el formulario
        3) Actualiza el contacto en la BBDD
            a) Si como resultado de la actualización, devuelve que la cantidad de registros actualizados es 0, indica al usuario que el ID ingresado no existe
            c) Si como resultado de la actualización, devuelve que la cantidad de registros actualizados es mayor a 0, actualiza la lista de contactos, 
            limpia los campos del formulario y muestra un mensaje indicando que el contacto se ha actualizado de forma exitosa

        """
        if self.vista.formulario.validar_campos():
            contacto = Contacto(self.vista.formulario.id.get(),self.vista.formulario.nombre.get(),self.vista.formulario.apellido.get(),self.vista.formulario.direccion.get(),self.vista.formulario.telefono.get(), self.vista.formulario.email.get())
            cantidad = self.modelo.actualiza_contacto(contacto)
            if cantidad > 0:
                self.vista.actualizar_lista()
                self.vista.formulario.limpia_campos()
                messagebox.showinfo(message="Contacto actualizado exitosamente", title="Actualización")
            else:
                messagebox.showerror(message="El ID solicitado no existe", title="Error")


        
