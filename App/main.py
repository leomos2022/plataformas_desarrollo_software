#!/usr/bin/env python3
"""
Punto de entrada principal de la aplicación
Demuestra la integración de Flask + SQLAlchemy + Testing automatizado
"""

from App import create_app
import os


def main():
    """Función principal que inicia la aplicación"""
    # Crear la aplicación usando el patrón Factory
    app = create_app()
    
    # Configuración del servidor
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    print("\n" + "="*70)
    print("  APLICACIÓN FLASK - ENTORNO AUTOMATIZADO")
    print("="*70)
    print(f"\n✓ Servidor iniciado en: http://{host}:{port}")
    print(f"✓ Modo: {'Desarrollo' if debug else 'Producción'}")
    print(f"✓ Base de datos: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("\nEndpoints disponibles:")
    print("  - GET  /              -> Página principal")
    print("  - GET  /health        -> Estado del servidor")
    print("  - GET  /api/users     -> Listar usuarios")
    print("  - POST /api/users     -> Crear usuario")
    print("  - GET  /api/users/:id -> Obtener usuario específico")
    print("\nPresiona CTRL+C para detener el servidor\n")
    print("="*70 + "\n")
    
    # Iniciar el servidor
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
