"""
Rutas principales de la aplicación
Blueprint para endpoints generales
"""

from flask import Blueprint, jsonify
from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    Endpoint principal - Página de bienvenida
    
    Returns:
        JSON con información de la API
    """
    return jsonify({
        'message': 'API de Automatización de Entornos de Desarrollo',
        'version': '1.0.0',
        'description': 'Proyecto para el foro de Plataformas de Desarrollo de Software',
        'empresa': 'XYZ',
        'endpoints': {
            'health': '/health',
            'users': '/api/users',
            'documentation': '/docs'
        },
        'tecnologias': ['Flask', 'SQLAlchemy', 'pytest'],
        'timestamp': datetime.utcnow().isoformat()
    })


@main_bp.route('/health')
def health():
    """
    Health check endpoint - Verifica el estado del servidor
    
    Returns:
        JSON con el estado del servicio
    """
    return jsonify({
        'status': 'healthy',
        'service': 'dev-environment-api',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@main_bp.route('/docs')
def documentation():
    """
    Documentación de la API
    
    Returns:
        JSON con la documentación de endpoints
    """
    return jsonify({
        'api_documentation': {
            'name': 'API de Gestión de Usuarios',
            'version': '1.0.0',
            'endpoints': [
                {
                    'method': 'GET',
                    'path': '/',
                    'description': 'Información general de la API'
                },
                {
                    'method': 'GET',
                    'path': '/health',
                    'description': 'Verificar estado del servicio'
                },
                {
                    'method': 'GET',
                    'path': '/api/users',
                    'description': 'Listar todos los usuarios'
                },
                {
                    'method': 'POST',
                    'path': '/api/users',
                    'description': 'Crear un nuevo usuario',
                    'body': {
                        'username': 'string (requerido)',
                        'email': 'string (requerido)'
                    }
                },
                {
                    'method': 'GET',
                    'path': '/api/users/:id',
                    'description': 'Obtener un usuario específico'
                },
                {
                    'method': 'PUT',
                    'path': '/api/users/:id',
                    'description': 'Actualizar un usuario'
                },
                {
                    'method': 'DELETE',
                    'path': '/api/users/:id',
                    'description': 'Eliminar un usuario'
                }
            ]
        }
    })
