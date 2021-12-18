class Formulario_excepcion(Exception):
    """
    Esta clase permite capturar todos los errores de formulario en un solo bloque try exception

    """
    pass

class Apellido_incorrecto(Formulario_excepcion):
    def __init__(self):
        self.mensaje_error = "Por favor, ingrese un apellido válido"

class Nombre_incorrecto(Formulario_excepcion):
    def __init__(self):
        self.mensaje_error = "Por favor, ingrese un nombre válido"

class Telefono_incorrecto(Formulario_excepcion):
    def __init__(self):
        self.mensaje_error = "Por favor, ingrese un teléfono válido"

class Mail_incorrecto(Formulario_excepcion):
    def __init__(self):
        self.mensaje_error = "Por favor, ingrese un email válido"
