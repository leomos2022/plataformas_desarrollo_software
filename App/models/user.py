"""
Modelo de Usuario - SQLAlchemy ORM
Demuestra el uso de SQLAlchemy para modelado de datos
"""

from datetime import datetime
from App import db


class User(db.Model):
    """
    Modelo de Usuario que representa la tabla 'users' en la base de datos
    
    Atributos:
        id: Identificador único del usuario
        username: Nombre de usuario único
        email: Correo electrónico único
        created_at: Fecha de creación del registro
        updated_at: Fecha de última actualización
        is_active: Estado del usuario (activo/inactivo)
    """
    
    __tablename__ = 'users'
    
    # Campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    def __repr__(self):
        """Representación en string del objeto User"""
        return f'<User {self.username}>'
    
    def to_dict(self):
        """
        Convierte el objeto User a un diccionario
        Útil para serialización JSON
        
        Returns:
            dict: Representación del usuario en formato diccionario
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active
        }
    
    @staticmethod
    def create_user(username, email):
        """
        Método estático para crear un nuevo usuario
        
        Args:
            username: Nombre de usuario
            email: Correo electrónico
            
        Returns:
            User: Nueva instancia de usuario
        """
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, **kwargs):
        """
        Actualiza los campos del usuario
        
        Args:
            **kwargs: Campos a actualizar
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        """Elimina el usuario de la base de datos"""
        db.session.delete(self)
        db.session.commit()
    
    def deactivate(self):
        """Desactiva el usuario (soft delete)"""
        self.is_active = False
        self.updated_at = datetime.utcnow()
        db.session.commit()
