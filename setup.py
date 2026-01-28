#!/usr/bin/env python3
"""
Script de automatización para configuración de entorno de desarrollo
Empresa XYZ - Plataformas de Desarrollo de Software

Este script automatiza:
- Creación de entorno virtual 'dev_env'
- Instalación de dependencias (flask, SQLAlchemy, pytest)
- Creación de estructura de carpetas (App/, Tests/)
- Generación de archivos de configuración (README.md, requirements.txt)
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


class EnvironmentSetup:
    """Clase para automatizar la configuración del entorno de desarrollo"""
    
    def __init__(self, project_name="dev_env"):
        self.project_name = project_name
        self.base_dir = Path.cwd()
        self.venv_dir = self.base_dir / project_name
        self.is_windows = platform.system() == "Windows"
        
    def print_step(self, message):
        """Imprime un mensaje formateado para cada paso"""
        print(f"\n{'='*70}")
        print(f"▶ {message}")
        print(f"{'='*70}\n")
    
    def create_virtual_environment(self):
        """Crea el entorno virtual dev_env"""
        self.print_step("Paso 1: Creando entorno virtual 'dev_env'")
        
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(self.venv_dir)],
                check=True
            )
            print(f"✓ Entorno virtual '{self.project_name}' creado exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error al crear entorno virtual: {e}")
            sys.exit(1)
    
    def get_pip_executable(self):
        """Obtiene la ruta del ejecutable pip del entorno virtual"""
        if self.is_windows:
            return self.venv_dir / "Scripts" / "pip.exe"
        return self.venv_dir / "bin" / "pip"
    
    def get_python_executable(self):
        """Obtiene la ruta del ejecutable python del entorno virtual"""
        if self.is_windows:
            return self.venv_dir / "Scripts" / "python.exe"
        return self.venv_dir / "bin" / "python"
    
    def install_dependencies(self):
        """Instala las dependencias requeridas"""
        self.print_step("Paso 2: Instalando dependencias (flask, SQLAlchemy, pytest)")
        
        pip_executable = self.get_pip_executable()
        dependencies = [
            "flask>=3.0.0",
            "SQLAlchemy>=2.0.0",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",  # Para cobertura de código
            "python-dotenv>=1.0.0",  # Para variables de entorno
            "black>=23.0.0",  # Formateador de código
            "flake8>=6.0.0",  # Linter
        ]
        
        try:
            # Actualizar pip primero
            subprocess.run(
                [str(pip_executable), "install", "--upgrade", "pip"],
                check=True
            )
            
            # Instalar dependencias
            subprocess.run(
                [str(pip_executable), "install"] + dependencies,
                check=True
            )
            print("✓ Dependencias instaladas exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error al instalar dependencias: {e}")
            sys.exit(1)
    
    def create_project_structure(self):
        """Crea la estructura de carpetas del proyecto"""
        self.print_step("Paso 3: Creando estructura de carpetas")
        
        directories = [
            "App",
            "App/models",
            "App/routes",
            "App/utils",
            "Tests",
            "Tests/unit",
            "Tests/integration",
            "config",
            "docs",
        ]
        
        for directory in directories:
            dir_path = self.base_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            
            # Crear __init__.py para paquetes Python
            if directory.startswith("App") or directory.startswith("Tests"):
                (dir_path / "__init__.py").touch()
            
            print(f"✓ Creado: {directory}/")
        
        print("\n✓ Estructura de carpetas creada exitosamente")
    
    def create_requirements_file(self):
        """Crea el archivo requirements.txt"""
        self.print_step("Paso 4: Creando archivo requirements.txt")
        
        requirements_content = """# Dependencias principales del proyecto
# Framework web
flask>=3.0.0
Flask-CORS>=4.0.0

# ORM y Base de datos
SQLAlchemy>=2.0.0
Flask-SQLAlchemy>=3.1.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-flask>=1.3.0

# Desarrollo
python-dotenv>=1.0.0
black>=23.0.0
flake8>=6.0.0
pylint>=3.0.0

# Utilidades
requests>=2.31.0
python-dateutil>=2.8.2
"""
        
        requirements_path = self.base_dir / "requirements.txt"
        requirements_path.write_text(requirements_content)
        print(f"✓ Archivo requirements.txt creado")
    
    def create_readme(self):
        """Crea el archivo README.md con instrucciones"""
        self.print_step("Paso 5: Creando archivo README.md")
        
        readme_content = """# Proyecto de Automatización de Entornos de Desarrollo
## Empresa XYZ - Plataformas de Desarrollo de Software

Este proyecto demuestra la automatización de la configuración de entornos de desarrollo utilizando Python, implementando mejores prácticas de DevOps y desarrollo ágil.

---

## 📋 Descripción

Proyecto desarrollado para el foro de discusión sobre el **impacto de la automatización en entornos de desarrollo con Python**. Incluye un script automatizado que configura todo el entorno de desarrollo necesario para comenzar a trabajar inmediatamente.

## 🚀 Características

- ✅ Creación automática de entorno virtual
- ✅ Instalación automática de dependencias
- ✅ Estructura de proyecto organizada
- ✅ Configuración de testing con pytest
- ✅ Herramientas de calidad de código (black, flake8)
- ✅ Ejemplos de código funcional
- ✅ Documentación completa

## 📁 Estructura del Proyecto

```
.
├── App/                    # Código fuente de la aplicación
│   ├── models/            # Modelos de base de datos (SQLAlchemy)
│   ├── routes/            # Rutas y endpoints (Flask)
│   └── utils/             # Utilidades y helpers
├── Tests/                 # Pruebas unitarias e integración
│   ├── unit/              # Pruebas unitarias
│   └── integration/       # Pruebas de integración
├── config/                # Archivos de configuración
├── docs/                  # Documentación adicional
├── dev_env/              # Entorno virtual (generado automáticamente)
├── setup.py              # Script de automatización principal
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo

```

## 🛠️ Instalación y Configuración

### Opción 1: Instalación Automatizada (Recomendada)

Ejecuta el script de automatización que configurará todo el entorno:

```bash
# En Linux/macOS
python3 setup.py

# En Windows
python setup.py
```

El script realizará automáticamente:
1. Creación del entorno virtual 'dev_env'
2. Instalación de todas las dependencias
3. Creación de la estructura de carpetas
4. Generación de archivos de configuración

### Opción 2: Instalación Manual

Si prefieres configurar manualmente:

```bash
# 1. Crear entorno virtual
python3 -m venv dev_env

# 2. Activar entorno virtual
# En Linux/macOS:
source dev_env/bin/activate
# En Windows:
dev_env\\Scripts\\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## 🏃‍♂️ Uso del Proyecto

### Activar el entorno virtual

```bash
# Linux/macOS
source dev_env/bin/activate

# Windows
dev_env\\Scripts\\activate
```

### Ejecutar la aplicación

```bash
python App/main.py
```

### Ejecutar pruebas

```bash
# Todas las pruebas
pytest

# Con cobertura de código
pytest --cov=App --cov-report=html

# Pruebas específicas
pytest Tests/unit/
```

### Formatear código

```bash
# Formatear con black
black App/ Tests/

# Verificar estilo con flake8
flake8 App/ Tests/
```

## 📦 Dependencias Principales

- **Flask** (3.0.0+): Framework web ligero y flexible
- **SQLAlchemy** (2.0.0+): ORM para manejo de bases de datos
- **pytest** (7.4.0+): Framework de testing moderno
- **python-dotenv**: Manejo de variables de entorno
- **black**: Formateador automático de código
- **flake8**: Linter para verificar estilo de código

## 🧪 Ejemplos de Uso

### Crear un modelo de base de datos

```python
from App.models.user import User
from App.database import db

# Crear nuevo usuario
user = User(username="john_doe", email="john@example.com")
db.session.add(user)
db.session.commit()
```

### Crear una ruta en Flask

```python
from flask import Blueprint

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    return {"message": "Lista de usuarios"}
```

## 🤝 Contribución

Este proyecto sigue las metodologías ágiles (Scrum/XP) y prácticas DevOps:

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📚 Recursos y Referencias

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de pytest](https://docs.pytest.org/)
- Pando, B. et al. (2024). Estudio terciario sobre adopción de DevOps
- Patilla, H. J. et al. (2023). Scrumban/XP: Propuesta para mejorar la eficiencia

## 💡 Impacto de la Automatización

La automatización de este entorno de desarrollo:
- ⚡ Reduce el tiempo de configuración de horas a minutos
- 🎯 Elimina errores de configuración manual
- 🔄 Garantiza consistencia entre todos los desarrolladores
- 📈 Mejora la productividad del equipo
- 🛡️ Establece estándares de calidad desde el inicio

## 📝 Licencia

Proyecto educativo - Plataformas de Desarrollo de Software

## ✍️ Autor

Desarrollado para el foro de discusión sobre automatización de entornos de desarrollo con Python.

---

**Nota**: Este README fue generado automáticamente por el script de configuración.
"""
        
        readme_path = self.base_dir / "README.md"
        readme_path.write_text(readme_content)
        print(f"✓ Archivo README.md creado")
    
    def create_example_files(self):
        """Crea archivos de ejemplo para demostrar funcionalidad"""
        self.print_step("Paso 6: Creando archivos de ejemplo")
        
        # Crear .env.example
        env_example = """# Variables de entorno del proyecto
FLASK_APP=App.main
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///dev.db
"""
        (self.base_dir / ".env.example").write_text(env_example)
        
        # Crear .gitignore
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
dev_env/
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
htmlcov/
.coverage
*.cover

# Environment
.env
.env.local

# Database
*.db
*.sqlite3

# Logs
*.log
"""
        (self.base_dir / ".gitignore").write_text(gitignore_content)
        
        print("✓ Archivos de configuración creados (.env.example, .gitignore)")
    
    def run(self):
        """Ejecuta todos los pasos de configuración"""
        print("\n" + "="*70)
        print("  AUTOMATIZACIÓN DE ENTORNO DE DESARROLLO - EMPRESA XYZ")
        print("  Plataformas de Desarrollo de Software")
        print("="*70)
        
        self.create_virtual_environment()
        self.install_dependencies()
        self.create_project_structure()
        self.create_requirements_file()
        self.create_readme()
        self.create_example_files()
        
        # Mensaje final
        self.print_step("✓ CONFIGURACIÓN COMPLETADA EXITOSAMENTE")
        
        activation_cmd = (
            f"dev_env\\Scripts\\activate" if self.is_windows 
            else "source dev_env/bin/activate"
        )
        
        print(f"""
El entorno de desarrollo ha sido configurado correctamente.

Para comenzar a trabajar:

1. Activa el entorno virtual:
   {activation_cmd}

2. Verifica la instalación:
   pip list

3. Ejecuta los ejemplos de código:
   python App/main.py

4. Ejecuta las pruebas:
   pytest

¡El entorno está listo para desarrollo!
        """)


if __name__ == "__main__":
    setup = EnvironmentSetup()
    setup.run()
