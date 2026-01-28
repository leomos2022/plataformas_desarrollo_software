"""
Blueprint para gestión de usuarios
CRUD completo de usuarios usando Flask + SQLAlchemy
"""

from flask import Blueprint, request, jsonify
from App import db
from App.models.user import User
from App.utils.validators import validate_user_data, validate_email

users_bp = Blueprint('users', __name__)


@users_bp.route('', methods=['GET'])
def get_users():
    """
    Obtiene lista de todos los usuarios
    
    Query params:
        active: (optional) Filtrar por usuarios activos (true/false)
        limit: (optional) Limitar cantidad de resultados
    
    Returns:
        JSON con lista de usuarios
    """
    try:
        # Obtener parámetros de query
        active_only = request.args.get('active', 'true').lower() == 'true'
        limit = request.args.get('limit', type=int)
        
        # Construir query
        query = User.query
        
        if active_only:
            query = query.filter_by(is_active=True)
        
        if limit:
            query = query.limit(limit)
        
        users = query.all()
        
        return jsonify({
            'success': True,
            'count': len(users),
            'users': [user.to_dict() for user in users]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@users_bp.route('', methods=['POST'])
def create_user():
    """
    Crea un nuevo usuario
    
    Body (JSON):
        username: Nombre de usuario (requerido)
        email: Correo electrónico (requerido)
    
    Returns:
        JSON con el usuario creado
    """
    try:
        data = request.get_json()
        
        # Validar datos
        is_valid, error_message = validate_user_data(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'error': error_message
            }), 400
        
        username = data.get('username')
        email = data.get('email')
        
        # Verificar si el usuario ya existe
        if User.query.filter_by(username=username).first():
            return jsonify({
                'success': False,
                'error': f'El usuario "{username}" ya existe'
            }), 409
        
        if User.query.filter_by(email=email).first():
            return jsonify({
                'success': False,
                'error': f'El email "{email}" ya está registrado'
            }), 409
        
        # Crear usuario
        user = User.create_user(username=username, email=email)
        
        return jsonify({
            'success': True,
            'message': 'Usuario creado exitosamente',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Obtiene un usuario específico por ID
    
    Args:
        user_id: ID del usuario
    
    Returns:
        JSON con los datos del usuario
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({
                'success': False,
                'error': f'Usuario con ID {user_id} no encontrado'
            }), 404
        
        return jsonify({
            'success': True,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Actualiza un usuario existente
    
    Args:
        user_id: ID del usuario
    
    Body (JSON):
        username: (optional) Nuevo nombre de usuario
        email: (optional) Nuevo email
    
    Returns:
        JSON con el usuario actualizado
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({
                'success': False,
                'error': f'Usuario con ID {user_id} no encontrado'
            }), 404
        
        data = request.get_json()
        
        # Validar email si se proporciona
        if 'email' in data and not validate_email(data['email']):
            return jsonify({
                'success': False,
                'error': 'Email inválido'
            }), 400
        
        # Actualizar usuario
        user.update(**data)
        
        return jsonify({
            'success': True,
            'message': 'Usuario actualizado exitosamente',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Elimina un usuario
    
    Args:
        user_id: ID del usuario
    
    Returns:
        JSON confirmando la eliminación
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({
                'success': False,
                'error': f'Usuario con ID {user_id} no encontrado'
            }), 404
        
        username = user.username
        user.delete()
        
        return jsonify({
            'success': True,
            'message': f'Usuario "{username}" eliminado exitosamente'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@users_bp.route('/<int:user_id>/deactivate', methods=['POST'])
def deactivate_user(user_id):
    """
    Desactiva un usuario (soft delete)
    
    Args:
        user_id: ID del usuario
    
    Returns:
        JSON confirmando la desactivación
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({
                'success': False,
                'error': f'Usuario con ID {user_id} no encontrado'
            }), 404
        
        user.deactivate()
        
        return jsonify({
            'success': True,
            'message': f'Usuario "{user.username}" desactivado exitosamente',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
