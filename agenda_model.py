import sqlite3
from sqlite3 import Error
from agenda_config import db_ubicacion
from contacto import Contacto
import tkinter


class Agenda_model():

    """
    Esta clase es el modelo de la aplicación, contiene la interacción con la BBDD
    """

    def __init__(self):

        """
        El método __init__ es el constructor de la clase, crea la conexión con sqlite3
        """
        
        try:
            self.conn = sqlite3.connect(db_ubicacion)
        except Error as e:
            print(e)

        self.crea_tabla()
    
    def crea_tabla(self):
        """
        El método crea_tabla crea la tabla agenda
        """
        cursor = self.conn.cursor()
        try:
            sql = 'create table if not exists agenda (id integer primary key autoincrement,nombre text, apellido text, direccion text, telefono text, email text)'
            cursor.execute(sql)
            self.conn.commit()
        except Error as e:
            print(e)

    def inserta_contacto(self,contacto):
        """
        El método inserta_contacto inserta un contacto en la tabla agenda

        """
        cursor = self.conn.cursor()
        sql = 'insert into agenda (nombre,apellido,direccion,telefono,email) values (?,?,?,?,?)'
        try:
            cursor.execute(sql,[contacto.nombre,contacto.apellido,contacto.direccion,contacto.telefono,contacto.email])
            self.conn.commit()
        except Error as e:
            print(e)
            tkinter.messagebox.showerror(message="No se ha podido agregar el contacto", title="Error")

    def elimina_contacto(self,id):
        """
        El método elimina_contacto elimina un contacto en la tabla agenda por ID

        """
        cursor = self.conn.cursor()
        sql = 'delete from agenda where id = ?'
        cantidad = 0
        try:
            cursor.execute(sql, (id,))
            cantidad = cursor.rowcount
            self.conn.commit()
        except Error as e:
            print(e)
            tkinter.messagebox.showerror(message="No se ha podido eliminar el contacto", title="Error")
        finally:
            return cantidad

    def actualiza_contacto(self,contacto):
        """
        El método actualiza_contacto actualiza un contacto en la tabla agenda por ID

        """
        cursor = self.conn.cursor()
        sql = 'update agenda set  nombre = ?, apellido = ?, direccion = ? , telefono = ?, email = ? where id = ?'
        cantidad = 0
        try:
            cursor.execute(sql,[contacto.nombre,contacto.apellido,contacto.direccion,contacto.telefono,contacto.email,contacto.id])
            cantidad = cursor.rowcount
            self.conn.commit()
        except Error as e:
            print(e)
            tkinter.messagebox.showerror(message="No se ha podido actualizar el contacto", title="Error")
        finally:
            return cantidad


    def buscar_contacto(self,id):
        """
        El método buscar_contacto busca un contacto en la tabla agenda por ID

        """
        cursor = self.conn.cursor()
        sql = "select * from agenda where id = ?"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row is None:
            tkinter.messagebox.showerror(message="Id de contacto inexistente", title="Error")
        else:
            contacto = Contacto(row[0],row[1],row[2],row[3],row[4],row[5])
            return contacto

    def obtener_contactos(self):
        """
        El método obtener_contactos devuelve la lista de contactos existentes en la tabla agenda

        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM agenda")

        rows = cursor.fetchall()
        lista = []
        for row in rows:
            contacto = Contacto(row[0],row[1],row[2],row[3],row[4],row[5])
            lista.append(contacto)
        return lista




""" agenda_modelo = Agenda_model()
contacto = Contacto(None,'Noelia','Beret','Concepcion Arenal 2739','1136524342','noeliaberet@yahoo.com')
agenda_modelo.inserta_contacto(contacto)
contactos = agenda_modelo.lista_contactos()  """



