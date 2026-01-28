# Guía de Uso del Proyecto

## 🚀 Inicio Rápido

### 1. Ejecutar el Script de Automatización

```bash
# Navegar a la carpeta del proyecto
cd /Users/leomos/PDSoftware/foro_automatizacion_python

# Ejecutar el script de configuración automatizada
python3 setup.py
```

Este script realizará automáticamente:
- ✅ Creación del entorno virtual `dev_env`
- ✅ Instalación de todas las dependencias
- ✅ Creación de la estructura de carpetas
- ✅ Generación de archivos de configuración

### 2. Activar el Entorno Virtual

```bash
# En macOS/Linux
source dev_env/bin/activate

# En Windows
dev_env\Scripts\activate
```

### 3. Ejecutar la Aplicación

```bash
# Iniciar el servidor Flask
python App/main.py
```

La aplicación estará disponible en: `http://localhost:5000`

### 4. Ejecutar las Pruebas

```bash
# Todas las pruebas
pytest

# Con reporte de cobertura
pytest --cov=App --cov-report=html

# Solo pruebas unitarias
pytest Tests/unit/

# Solo pruebas de integración
pytest Tests/integration/
```

### 5. Verificar Calidad de Código

```bash
# Formatear código automáticamente
black App/ Tests/

# Verificar estilo
flake8 App/ Tests/
```

---

## 📋 Endpoints Disponibles

### Rutas Principales

- **GET** `/` - Información de la API
- **GET** `/health` - Estado del servidor
- **GET** `/docs` - Documentación de endpoints

### API de Usuarios

- **GET** `/api/users` - Listar todos los usuarios
- **POST** `/api/users` - Crear nuevo usuario
- **GET** `/api/users/:id` - Obtener usuario específico
- **PUT** `/api/users/:id` - Actualizar usuario
- **DELETE** `/api/users/:id` - Eliminar usuario
- **POST** `/api/users/:id/deactivate` - Desactivar usuario

---

## 🧪 Ejemplos de Uso de la API

### Crear un Usuario

```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com"
  }'
```

### Listar Usuarios

```bash
curl http://localhost:5000/api/users
```

### Obtener Usuario por ID

```bash
curl http://localhost:5000/api/users/1
```

### Actualizar Usuario

```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newemail@example.com"
  }'
```

### Eliminar Usuario

```bash
curl -X DELETE http://localhost:5000/api/users/1
```

---

## 📁 Estructura del Proyecto

```
foro_automatizacion_python/
├── App/                        # Código fuente
│   ├── __init__.py            # Inicialización de Flask
│   ├── main.py                # Punto de entrada
│   ├── models/                # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   └── user.py           # Modelo User
│   ├── routes/                # Rutas Flask
│   │   ├── __init__.py
│   │   ├── main.py           # Rutas principales
│   │   └── users.py          # CRUD usuarios
│   └── utils/                 # Utilidades
│       ├── __init__.py
│       └── validators.py     # Validadores
├── Tests/                     # Pruebas
│   ├── conftest.py           # Configuración pytest
│   ├── unit/                 # Pruebas unitarias
│   │   ├── test_user_model.py
│   │   └── test_validators.py
│   └── integration/          # Pruebas integración
│       └── test_api.py
├── dev_env/                   # Entorno virtual (generado)
├── setup.py                   # Script de automatización ⭐
├── requirements.txt           # Dependencias
├── RESPUESTAS_FORO.md        # Respuestas del foro
├── GUIA_USO.md               # Este archivo
└── README.md                  # Documentación principal
```

---

## 🎓 Conceptos Demostrados

### 1. Automatización de Entornos
- Script `setup.py` que configura todo automáticamente
- Eliminación de configuración manual
- Reducción de errores humanos

### 2. Desarrollo Profesional
- **Factory Pattern**: Creación de la app Flask
- **Blueprints**: Organización modular de rutas
- **ORM**: SQLAlchemy para base de datos
- **Validación**: Validadores personalizados

### 3. Testing Automatizado
- **Pytest**: Framework de testing moderno
- **Fixtures**: Reutilización de código de testing
- **Coverage**: Medición de cobertura
- **Pruebas unitarias e integración**

### 4. Calidad de Código
- **Black**: Formateo automático
- **Flake8**: Linting
- **Type hints**: Mejor documentación del código

### 5. Mejores Prácticas
- **Separación de responsabilidades**
- **Configuración via variables de entorno**
- **Documentación completa**
- **Código limpio y mantenible**

---

## 🔧 Troubleshooting

### Error: "No module named 'flask'"

**Solución**: Asegúrate de que el entorno virtual esté activado
```bash
source dev_env/bin/activate  # macOS/Linux
dev_env\Scripts\activate     # Windows
```

### Error: "Database not found"

**Solución**: La base de datos se crea automáticamente al iniciar la app por primera vez
```bash
python App/main.py
```

### Error en las pruebas

**Solución**: Instala las dependencias de desarrollo
```bash
pip install -r requirements.txt
```

---

## 📝 Notas Importantes

1. **Entorno Virtual**: Siempre activa el entorno virtual antes de trabajar
2. **Base de Datos**: Se usa SQLite por defecto (archivo `dev.db`)
3. **Testing**: Usa base de datos en memoria para pruebas
4. **Producción**: Cambiar configuraciones en `.env` para producción

---

## 🎯 Próximos Pasos

Para extender este proyecto:

1. **Agregar autenticación**: Flask-Login o JWT
2. **Containerización**: Crear Dockerfile
3. **CI/CD**: GitHub Actions para automatizar testing
4. **Frontend**: React/Vue.js para interfaz
5. **Deployment**: Desplegar en Heroku/AWS/Azure

---

## 📚 Recursos Adicionales

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de pytest](https://docs.pytest.org/)
- [PEP 8 - Guía de estilo Python](https://pep8.org/)

---

*Guía creada para el proyecto de Automatización de Entornos - Empresa XYZ*
