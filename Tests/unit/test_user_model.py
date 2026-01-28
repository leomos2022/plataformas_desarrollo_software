"""
Pruebas unitarias para el modelo User
Demuestra el uso de pytest para testing automatizado
"""

import pytest
from datetime import datetime
from App.models.user import User
from App import db


class TestUserModel:
    """Suite de pruebas para el modelo User"""
    
    def test_create_user(self, app, init_database):
        """Test: Crear un nuevo usuario"""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            db.session.add(user)
            db.session.commit()
            
            assert user.id is not None
            assert user.username == 'testuser'
            assert user.email == 'test@example.com'
            assert user.is_active is True
            assert isinstance(user.created_at, datetime)
    
    def test_user_to_dict(self, app, init_database):
        """Test: Conversión de usuario a diccionario"""
        with app.app_context():
            user = User(username='dictuser', email='dict@example.com')
            db.session.add(user)
            db.session.commit()
            
            user_dict = user.to_dict()
            
            assert isinstance(user_dict, dict)
            assert user_dict['username'] == 'dictuser'
            assert user_dict['email'] == 'dict@example.com'
            assert 'id' in user_dict
            assert 'created_at' in user_dict
            assert 'is_active' in user_dict
    
    def test_user_repr(self, app, init_database):
        """Test: Representación string del usuario"""
        with app.app_context():
            user = User(username='repruser', email='repr@example.com')
            db.session.add(user)
            db.session.commit()
            
            assert repr(user) == '<User repruser>'
    
    def test_create_user_static_method(self, app, init_database):
        """Test: Método estático create_user"""
        with app.app_context():
            user = User.create_user('staticuser', 'static@example.com')
            
            assert user.id is not None
            assert user.username == 'staticuser'
            assert user.email == 'static@example.com'
    
    def test_update_user(self, app, init_database):
        """Test: Actualizar datos de usuario"""
        with app.app_context():
            user = User.create_user('updateuser', 'update@example.com')
            original_updated_at = user.updated_at
            
            user.update(email='newemail@example.com')
            
            assert user.email == 'newemail@example.com'
            assert user.updated_at > original_updated_at
    
    def test_deactivate_user(self, app, init_database):
        """Test: Desactivar usuario"""
        with app.app_context():
            user = User.create_user('deactiveuser', 'deactive@example.com')
            
            assert user.is_active is True
            
            user.deactivate()
            
            assert user.is_active is False
    
    def test_delete_user(self, app, init_database):
        """Test: Eliminar usuario"""
        with app.app_context():
            user = User.create_user('deleteuser', 'delete@example.com')
            user_id = user.id
            
            user.delete()
            
            deleted_user = User.query.get(user_id)
            assert deleted_user is None
    
    def test_unique_username(self, app, init_database):
        """Test: Username debe ser único"""
        with app.app_context():
            User.create_user('uniqueuser', 'unique1@example.com')
            
            # Intentar crear otro usuario con el mismo username
            user2 = User(username='uniqueuser', email='unique2@example.com')
            db.session.add(user2)
            
            with pytest.raises(Exception):
                db.session.commit()
    
    def test_unique_email(self, app, init_database):
        """Test: Email debe ser único"""
        with app.app_context():
            User.create_user('user1', 'same@example.com')
            
            # Intentar crear otro usuario con el mismo email
            user2 = User(username='user2', email='same@example.com')
            db.session.add(user2)
            
            with pytest.raises(Exception):
                db.session.commit()


class TestUserValidation:
    """Pruebas de validación de datos de usuario"""
    
    def test_username_not_null(self, app, init_database):
        """Test: Username no puede ser nulo"""
        with app.app_context():
            user = User(username=None, email='test@example.com')
            db.session.add(user)
            
            with pytest.raises(Exception):
                db.session.commit()
    
    def test_email_not_null(self, app, init_database):
        """Test: Email no puede ser nulo"""
        with app.app_context():
            user = User(username='testuser', email=None)
            db.session.add(user)
            
            with pytest.raises(Exception):
                db.session.commit()
