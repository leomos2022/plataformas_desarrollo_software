"""
Pruebas unitarias para los validadores
"""

import pytest
from App.utils.validators import validate_email, validate_username, validate_user_data


class TestEmailValidator:
    """Pruebas para el validador de email"""
    
    def test_valid_email(self):
        """Test: Emails válidos"""
        valid_emails = [
            'test@example.com',
            'user.name@example.com',
            'user+tag@example.co.uk',
            'test123@test-domain.com'
        ]
        
        for email in valid_emails:
            assert validate_email(email) is True, f"Email {email} debería ser válido"
    
    def test_invalid_email(self):
        """Test: Emails inválidos"""
        invalid_emails = [
            'invalid',
            '@example.com',
            'user@',
            'user @example.com',
            'user@example',
            '',
            None
        ]
        
        for email in invalid_emails:
            assert validate_email(email) is False, f"Email {email} debería ser inválido"


class TestUsernameValidator:
    """Pruebas para el validador de username"""
    
    def test_valid_username(self):
        """Test: Usernames válidos"""
        valid_usernames = [
            'user123',
            'test_user',
            'test-user',
            'User_Name-123'
        ]
        
        for username in valid_usernames:
            assert validate_username(username) is True, f"Username {username} debería ser válido"
    
    def test_invalid_username_length(self):
        """Test: Username con longitud inválida"""
        assert validate_username('ab') is False  # Muy corto
        assert validate_username('a' * 81) is False  # Muy largo
    
    def test_invalid_username_characters(self):
        """Test: Username con caracteres inválidos"""
        invalid_usernames = [
            'user name',  # Espacios
            'user@name',  # Caracteres especiales
            'user.name',  # Punto
            'user#123',   # Hash
        ]
        
        for username in invalid_usernames:
            assert validate_username(username) is False, f"Username {username} debería ser inválido"
    
    def test_empty_username(self):
        """Test: Username vacío o None"""
        assert validate_username('') is False
        assert validate_username(None) is False


class TestUserDataValidator:
    """Pruebas para el validador completo de datos de usuario"""
    
    def test_valid_user_data(self):
        """Test: Datos de usuario válidos"""
        data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        is_valid, error = validate_user_data(data)
        assert is_valid is True
        assert error is None
    
    def test_missing_username(self):
        """Test: Falta el username"""
        data = {
            'email': 'test@example.com'
        }
        
        is_valid, error = validate_user_data(data)
        assert is_valid is False
        assert 'username' in error.lower()
    
    def test_missing_email(self):
        """Test: Falta el email"""
        data = {
            'username': 'testuser'
        }
        
        is_valid, error = validate_user_data(data)
        assert is_valid is False
        assert 'email' in error.lower()
    
    def test_invalid_username_format(self):
        """Test: Formato de username inválido"""
        data = {
            'username': 'ab',  # Muy corto
            'email': 'test@example.com'
        }
        
        is_valid, error = validate_user_data(data)
        assert is_valid is False
        assert 'username' in error.lower()
    
    def test_invalid_email_format(self):
        """Test: Formato de email inválido"""
        data = {
            'username': 'testuser',
            'email': 'invalid-email'
        }
        
        is_valid, error = validate_user_data(data)
        assert is_valid is False
        assert 'email' in error.lower()
    
    def test_empty_data(self):
        """Test: Datos vacíos"""
        is_valid, error = validate_user_data({})
        assert is_valid is False
        
        is_valid, error = validate_user_data(None)
        assert is_valid is False
