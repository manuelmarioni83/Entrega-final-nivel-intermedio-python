import tkinter
from botonera import Botonera
from formulario import Formulario
import lista_contactos


class Agenda_view():
    """
    Esta clase es la vista de la aplicación
    """
    def __init__(self,modelo,controlador):
        """
        El método __init__ es el constructor de la clase Agenda_view
        1) crea la ventana principal de mi aplicación
        2) carga el treeview con la lista de contactos
        """
        self.modelo = modelo
        self.controlador = controlador
        self.crear_window()
        self.actualizar_lista()
        

    def crear_window(self):
        """
        El método crear_window crea la ventana y los widgets contenidos en la misma
    
        """
        self.window = tkinter.Tk()
        self.window.geometry("640x700")
        self.window.resizable(0,0)
        
        frame_formulario = tkinter.Frame(self.window)
        self.formulario = Formulario(frame_formulario)
        frame_formulario.place(x = 100, y = 40)
           
        self.botonera = Botonera(self.window,self.controlador)
     
        frame_lista = tkinter.Frame(self.window)
        self.lista = lista_contactos.Lista_contactos(frame_lista,self.controlador)
        frame_lista.place(x = 20, y = 310)
        
    def actualizar_lista(self):
        """
        El método actualizar_lista carga la lista de contactos en el treeview
    
        """
        contactos = self.modelo.obtener_contactos()
        self.lista.actualizar(contactos)
        
