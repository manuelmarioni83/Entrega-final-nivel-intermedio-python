import tkinter

class Botonera():
    """
    Esta clase es la botonera de la aplicación
    """
    def __init__(self, frame, controlador):
        """
        El método __init__ es el constructor de la clase Botonera. Instancia los botones de mi aplicación.
        """
        boton_alta = tkinter.Button(frame,text="Alta",command = controlador.generar_alta,width=12,padx=2,pady=2)
        boton_baja = tkinter.Button(frame,text="Baja",command = controlador.generar_baja,width=12,padx=2,pady=2)
        boton_modificacion = tkinter.Button(frame,text="Modificación",command = controlador.generar_actualizacion,width=12,padx=2,pady=2)
        boton_busqueda = tkinter.Button(frame,text="Búsqueda",command = controlador.generar_busqueda,width=12,padx=2,pady=2)
        boton_limpiar = tkinter.Button(frame,text="Limpiar",command = controlador.limpia_formulario ,width=12,padx=2,pady=2)
        boton_alta.place( x = 40, y = 260)
        boton_baja.place( x = 140, y = 260)
        boton_modificacion.place( x = 240, y = 260)
        boton_busqueda.place( x = 340, y = 260)
        boton_limpiar.place( x = 440, y = 260)
