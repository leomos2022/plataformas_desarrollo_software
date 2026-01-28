"""
Configuración para pytest
"""

import pytest
from App import create_app, db


@pytest.fixture(scope='session')
def app():
    """
    Crea una instancia de la aplicación para testing
    
    Yields:
        Flask app configurada para testing
    """
    test_app = create_app('testing')
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    yield test_app


@pytest.fixture(scope='function')
def client(app):
    """
    Crea un cliente de prueba para realizar peticiones HTTP
    
    Args:
        app: Fixture de la aplicación
    
    Yields:
        Flask test client
    """
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def init_database(app):
    """
    Inicializa la base de datos para cada test
    
    Args:
        app: Fixture de la aplicación
    """
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()
