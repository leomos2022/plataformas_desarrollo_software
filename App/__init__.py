"""
Paquete principal de la aplicación
Inicializa Flask y extensiones
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar extensiones
db = SQLAlchemy()


def create_app(config_name='development'):
    """
    Factory pattern para crear la aplicación Flask
    
    Args:
        config_name: Nombre de la configuración a usar (development, testing, production)
    
    Returns:
        Flask app configurada
    """
    app = Flask(__name__)
    
    # Configuración básica
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones con la app
    db.init_app(app)
    CORS(app)
    
    # Registrar blueprints
    from App.routes import main_bp, users_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix='/api/users')
    
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
    
    return app
