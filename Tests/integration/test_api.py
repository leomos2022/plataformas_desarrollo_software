"""
Pruebas de integración para la API de usuarios
Pruebas end-to-end de los endpoints REST
"""

import pytest
import json


class TestUserAPI:
    """Suite de pruebas de integración para la API de usuarios"""
    
    def test_get_empty_users_list(self, client, init_database):
        """Test: Obtener lista vacía de usuarios"""
        response = client.get('/api/users')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['count'] == 0
        assert len(data['users']) == 0
    
    def test_create_user_success(self, client, init_database):
        """Test: Crear usuario exitosamente"""
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com'
        }
        
        response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        data = json.loads(response.data)
        
        assert response.status_code == 201
        assert data['success'] is True
        assert data['user']['username'] == 'newuser'
        assert data['user']['email'] == 'newuser@example.com'
        assert 'id' in data['user']
    
    def test_create_user_invalid_data(self, client, init_database):
        """Test: Crear usuario con datos inválidos"""
        invalid_data = {
            'username': 'ab',  # Muy corto
            'email': 'invalid-email'
        }
        
        response = client.post(
            '/api/users',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['success'] is False
    
    def test_create_duplicate_username(self, client, init_database):
        """Test: Intentar crear usuario con username duplicado"""
        user_data = {
            'username': 'duplicate',
            'email': 'first@example.com'
        }
        
        # Crear primer usuario
        client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        
        # Intentar crear segundo usuario con mismo username
        duplicate_data = {
            'username': 'duplicate',
            'email': 'second@example.com'
        }
        
        response = client.post(
            '/api/users',
            data=json.dumps(duplicate_data),
            content_type='application/json'
        )
        data = json.loads(response.data)
        
        assert response.status_code == 409
        assert data['success'] is False
    
    def test_get_user_by_id(self, client, init_database):
        """Test: Obtener usuario por ID"""
        # Crear usuario
        user_data = {'username': 'getuser', 'email': 'get@example.com'}
        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        user_id = json.loads(create_response.data)['user']['id']
        
        # Obtener usuario por ID
        response = client.get(f'/api/users/{user_id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['user']['id'] == user_id
        assert data['user']['username'] == 'getuser'
    
    def test_get_nonexistent_user(self, client, init_database):
        """Test: Intentar obtener usuario que no existe"""
        response = client.get('/api/users/9999')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert data['success'] is False
    
    def test_update_user(self, client, init_database):
        """Test: Actualizar usuario"""
        # Crear usuario
        user_data = {'username': 'updateuser', 'email': 'update@example.com'}
        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        user_id = json.loads(create_response.data)['user']['id']
        
        # Actualizar usuario
        update_data = {'email': 'newemail@example.com'}
        response = client.put(
            f'/api/users/{user_id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['user']['email'] == 'newemail@example.com'
    
    def test_delete_user(self, client, init_database):
        """Test: Eliminar usuario"""
        # Crear usuario
        user_data = {'username': 'deleteuser', 'email': 'delete@example.com'}
        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        user_id = json.loads(create_response.data)['user']['id']
        
        # Eliminar usuario
        response = client.delete(f'/api/users/{user_id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        
        # Verificar que el usuario fue eliminado
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 404
    
    def test_deactivate_user(self, client, init_database):
        """Test: Desactivar usuario"""
        # Crear usuario
        user_data = {'username': 'deactiveuser', 'email': 'deactive@example.com'}
        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        user_id = json.loads(create_response.data)['user']['id']
        
        # Desactivar usuario
        response = client.post(f'/api/users/{user_id}/deactivate')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['user']['is_active'] is False
    
    def test_get_users_with_filters(self, client, init_database):
        """Test: Obtener usuarios con filtros"""
        # Crear varios usuarios
        users = [
            {'username': 'user1', 'email': 'user1@example.com'},
            {'username': 'user2', 'email': 'user2@example.com'},
            {'username': 'user3', 'email': 'user3@example.com'}
        ]
        
        for user_data in users:
            client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        
        # Obtener con límite
        response = client.get('/api/users?limit=2')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['count'] == 2


class TestMainRoutes:
    """Pruebas para las rutas principales"""
    
    def test_index_route(self, client):
        """Test: Ruta principal"""
        response = client.get('/')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert 'message' in data
        assert 'version' in data
        assert 'endpoints' in data
    
    def test_health_check(self, client):
        """Test: Health check"""
        response = client.get('/health')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['status'] == 'healthy'
    
    def test_documentation_route(self, client):
        """Test: Ruta de documentación"""
        response = client.get('/docs')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert 'api_documentation' in data
        assert 'endpoints' in data['api_documentation']
