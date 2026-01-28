# Proyecto de Automatización de Entornos de Desarrollo
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
├── setup.py              # Script de automatización principal ⭐
├── requirements.txt      # Dependencias del proyecto
├── RESPUESTAS_FORO.md    # Respuestas del foro de discusión
├── GUIA_USO.md          # Guía de uso detallada
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
dev_env\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## 🏃‍♂️ Uso del Proyecto

### Activar el entorno virtual

```bash
# Linux/macOS
source dev_env/bin/activate

# Windows
dev_env\Scripts\activate
```

### Ejecutar la aplicación

```bash
python App/main.py
```

La aplicación estará disponible en: `http://localhost:5000`

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

## 🌐 Endpoints de la API

### Rutas Principales
- `GET /` - Información de la API
- `GET /health` - Estado del servidor
- `GET /docs` - Documentación de endpoints

### API de Usuarios
- `GET /api/users` - Listar todos los usuarios
- `POST /api/users` - Crear nuevo usuario
- `GET /api/users/:id` - Obtener usuario específico
- `PUT /api/users/:id` - Actualizar usuario
- `DELETE /api/users/:id` - Eliminar usuario
- `POST /api/users/:id/deactivate` - Desactivar usuario

## 🧪 Ejemplo de Uso de la API

```bash
# Crear un usuario
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "email": "john@example.com"}'

# Listar usuarios
curl http://localhost:5000/api/users

# Obtener usuario específico
curl http://localhost:5000/api/users/1
```

## 💡 Impacto de la Automatización

La automatización de este entorno de desarrollo:
- ⚡ Reduce el tiempo de configuración de horas a minutos (95% de reducción)
- 🎯 Elimina errores de configuración manual
- 🔄 Garantiza consistencia entre todos los desarrolladores
- 📈 Mejora la productividad del equipo
- 🛡️ Establece estándares de calidad desde el inicio

## 📚 Documentación Adicional

- [GUIA_USO.md](GUIA_USO.md) - Guía detallada de uso
- [RESPUESTAS_FORO.md](RESPUESTAS_FORO.md) - Respuestas del foro de discusión

## 🤝 Contribución

Este proyecto sigue las metodologías ágiles (Scrum/XP) y prácticas DevOps:

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📖 Referencias

- Pando, B. et al. (2024). Estudio terciario sobre adopción de DevOps. *Revista Ibérica de Sistemas e Tecnologias de Informação*, (53), 23-36.
- Patilla, H. J. et al. (2023). Scrumban/XP: Propuesta para mejorar la eficiencia de la gestión de proyectos ágiles en el desarrollo de software. *Revista Ibérica de Sistemas e Tecnologias de Informação*, 14-32.
- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de pytest](https://docs.pytest.org/)

## 📝 Licencia

Proyecto educativo - Plataformas de Desarrollo de Software

## ✍️ Autor

Desarrollado para el foro de discusión sobre automatización de entornos de desarrollo con Python.

---

**Empresa XYZ** - Transformando la eficiencia en el desarrollo de software
