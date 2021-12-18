import re

def valida_nombre(formulario):

    if len(formulario.nombre.get()) > 0:
            regex = r'[A-Za-z áéíóú]{2,255}'
            if not (re.fullmatch(regex, formulario.nombre.get())):
                return False
            return True
    return False

def valida_apellido(formulario):
    if len(formulario.apellido.get()) > 0:
            regex = r'[A-Za-z áéíóú]{2,255}'
            if not (re.fullmatch(regex, formulario.apellido.get())):
                return False
            return True
    return False

def valida_telefono(formulario):
    if len(formulario.telefono.get()) > 0:
            regex = r'[*+]?\d{3,15}'
            if not (re.fullmatch(regex, formulario.telefono.get())):
                return False
            return True
    return False

def valida_email(formulario):
    if len(formulario.email.get()) > 0:
        regex = r'\b[A-Za-z0-9\._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, formulario.email.get())):
            return False 
        return True   
    return True           
