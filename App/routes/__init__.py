"""
Rutas y Blueprints de la aplicación Flask
"""

from App.routes.main import main_bp
from App.routes.users import users_bp

__all__ = ['main_bp', 'users_bp']
