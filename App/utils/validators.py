"""
Validadores de datos
Funciones para validar entradas de usuario
"""

import re


def validate_email(email):
    """
    Valida formato de email usando expresión regular
    
    Args:
        email: String con el email a validar
    
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    if not email:
        return False
    
    # Expresión regular para validar email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None


def validate_username(username):
    """
    Valida formato de nombre de usuario
    
    Reglas:
    - Mínimo 3 caracteres
    - Máximo 80 caracteres
    - Solo letras, números, guiones y guiones bajos
    
    Args:
        username: String con el nombre de usuario
    
    Returns:
        bool: True si el username es válido
    """
    if not username:
        return False
    
    if len(username) < 3 or len(username) > 80:
        return False
    
    # Solo permite letras, números, guiones y guiones bajos
    username_pattern = r'^[a-zA-Z0-9_-]+$'
    return re.match(username_pattern, username) is not None


def validate_user_data(data):
    """
    Valida los datos completos de un usuario
    
    Args:
        data: Diccionario con los datos del usuario
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not data:
        return False, "No se proporcionaron datos"
    
    # Validar username
    username = data.get('username')
    if not username:
        return False, "El campo 'username' es requerido"
    
    if not validate_username(username):
        return False, "Username inválido. Debe tener entre 3-80 caracteres y solo letras, números, - y _"
    
    # Validar email
    email = data.get('email')
    if not email:
        return False, "El campo 'email' es requerido"
    
    if not validate_email(email):
        return False, "Formato de email inválido"
    
    return True, None
