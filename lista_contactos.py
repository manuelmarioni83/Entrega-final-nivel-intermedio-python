from tkinter import ttk

class Lista_contactos(ttk.Treeview):
    """
    La clase Lista_contactos extiende de la clase ttk.Treeview. 
    Muestra en pantalla los datos de los contactos dados de alta en la base de datos
    """
    def __init__(self,frame,controlador):
        """
        El método __init__ es el constructor de la clase Lista_contactos
        """
        super(Lista_contactos,self).__init__(frame,columns=(1, 2, 3, 4, 5, 6), show ='headings', height=16, selectmode="browse")
        self.pack(fill='x', side='left')

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.yview)
        vsb.pack(side='right', fill='y')
        self.configure(yscrollcommand=vsb.set)

        self.heading(1, text="Id")
        self.heading(2, text="Nombre")
        self.heading(3, text="Apellido")
        self.heading(4, text="Dirección")
        self.heading(5, text="Teléfono")
        self.heading(6, text="Email")
        self.column("1", width = 30, anchor ='c')
        self.column("2", width = 90, anchor ='c')
        self.column("3", width = 90, anchor ='c')
        self.column("4", width = 150, anchor ='c')
        self.column("5", width = 90, anchor ='c')
        self.column("6", width = 140, anchor ='c')
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.bind("<<TreeviewSelect>>", lambda e: controlador.seleccionar_contacto())

    def actualizar(self, contactos):
        """
        El método actualizar actualiza el treeview
        """
        records = self.get_children()
        for element in records:
	        self.delete(element)

        for contacto in contactos:
            self.insert('',"end", values = (contacto.id,contacto.nombre,contacto.apellido,contacto.direccion,contacto.telefono,contacto.email))
