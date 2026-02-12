# 🚀 Guía para Compartir en GitHub

Esta guía te ayudará a subir el proyecto completo a GitHub para compartirlo con profesores y estudiantes.

---

## 📋 Pasos para Crear el Repositorio en GitHub

### 1️⃣ Crear Repositorio en GitHub.com

1. Ve a [github.com](https://github.com) e inicia sesión
2. Clic en el botón **"+"** → **"New repository"**
3. Completa los datos:
   - **Repository name**: `foro_semana5_automatizacion_qa`
   - **Description**: `Foro Semana 5: Automatización en QA - Elevando la Eficiencia. Suite de 68 pruebas automatizadas con Python, pytest y unittest.`
   - **Visibility**: Public ✅ (para compartir fácilmente)
   - **Initialize repository**: NO marcar ninguna opción (ya tenemos archivos)
4. Clic en **"Create repository"**

---

### 2️⃣ Preparar el Repositorio Local

Abre la terminal en la carpeta del proyecto:

```bash
cd /Users/leomos/PDSoftware/foro_semana5_automatizacion_qa
```

#### Inicializar Git (si no está inicializado)

```bash
git init
```

#### Agregar Todos los Archivos

```bash
git add .
```

#### Crear el Primer Commit

```bash
git commit -m "Initial commit: Foro Semana 5 - Automatización en QA

- 68 pruebas automatizadas con pytest y unittest
- 100% cobertura de código
- Manejo robusto de excepciones
- 4 participaciones académicas completas
- Documentación exhaustiva"
```

---

### 3️⃣ Conectar con GitHub y Subir

Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub:

```bash
# Agregar repositorio remoto
git remote add origin https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa.git

# Cambiar nombre de rama a 'main' (si es necesario)
git branch -M main

# Subir código a GitHub
git push -u origin main
```

---

## ✅ Verificación

### Confirmar que todo se subió correctamente:

1. Ve a: `https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa`
2. Deberías ver:
   - ✅ README.md renderizado en la página principal
   - ✅ Carpetas: `codigo/`, `participaciones_foro/`, `docs/`
   - ✅ Archivos: `.gitignore`, `GUIA_RAPIDA_EJECUCION.md`
   - ✅ Badge verde indicando el proyecto

---

## 🎨 Mejorar la Presentación del Repositorio

### Agregar Topics (Etiquetas)

En la página principal del repositorio en GitHub:
1. Clic en **"⚙️ Settings"** (engranaje junto a "About")
2. En "Topics" agregar:
   - `python`
   - `pytest`
   - `testing`
   - `qa`
   - `automation`
   - `unittest`
   - `devops`
   - `iso-29110`

### Configurar el About

En el repositorio, clic en **"⚙️"** junto a "About" y agregar:
- **Description**: `Foro académico sobre automatización en QA: 68 pruebas, 100% cobertura, pytest/unittest`
- **Website**: (opcional, si tienes un sitio)
- ✅ Marcar "Issues" y "Projects" si quieres colaboración

---

## 📤 Compartir con Profesores y Estudiantes

### Opción 1: Compartir el Link Directo

Copia y comparte este link:
```
https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa
```

### Opción 2: Compartir Secciones Específicas

**Para el código:**
```
https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa/tree/main/codigo
```

**Para las participaciones del foro:**
```
https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa/tree/main/participaciones_foro
```

**Para la guía rápida:**
```
https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa/blob/main/GUIA_RAPIDA_EJECUCION.md
```

### Opción 3: Crear un Release

Para versión "oficial":

1. En GitHub, ve a **"Releases"** → **"Create a new release"**
2. **Tag version**: `v1.0.0`
3. **Release title**: `Foro Semana 5 - Entrega Final`
4. **Description**:
```markdown
# Foro Semana 5: Automatización en QA

## 🎯 Entrega Completa

Este release contiene:
- ✅ 68 pruebas automatizadas
- ✅ 100% cobertura de código
- ✅ 4 participaciones académicas
- ✅ Documentación completa

## 📊 Métricas
- Pruebas: 68 (34 válidas, 19 inválidas, 15 borde)
- Tiempo ejecución: < 0.5s
- ROI calculado: 515% primer mes

## 🚀 Inicio Rápido
```bash
git clone https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa.git
cd foro_semana5_automatizacion_qa/codigo
pip install -r requirements.txt
pytest test_calculadora.py -v
```

Ver [GUIA_RAPIDA_EJECUCION.md](GUIA_RAPIDA_EJECUCION.md) para más detalles.
```
5. Clic en **"Publish release"**

---

## 📧 Plantilla de Email para Compartir

```
Asunto: Foro Semana 5 - Automatización en QA - Entrega

Estimado/a Profesor/a [Nombre],

Comparto el repositorio de GitHub con el desarrollo completo del Foro Semana 5:

🔗 Link: https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa

📊 Resumen de la entrega:
- 68 pruebas automatizadas (pytest + unittest)
- 100% cobertura de código
- 4 participaciones académicas fundamentadas
- Documentación exhaustiva

🚀 Para ejecutar las pruebas (< 5 minutos):
1. Clonar repositorio
2. cd codigo && pip install -r requirements.txt
3. pytest test_calculadora.py -v

📖 Contenido principal:
- /codigo: Implementación técnica del anexo
- /participaciones_foro: Respuestas académicas (4 documentos)
- GUIA_RAPIDA_EJECUCION.md: Instrucciones de 5 minutos
- README.md: Documentación completa

Saludos cordiales,
[Tu nombre]
```

---

## 🔄 Actualizaciones Futuras

Si necesitas hacer cambios después de subir:

```bash
# 1. Hacer cambios en los archivos
# 2. Agregar cambios
git add .

# 3. Commit con mensaje descriptivo
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub
git push origin main
```

---

## 🌟 Consejos para Máxima Visibilidad

### 1. README atractivo ✅
Ya tienes un README completo con:
- Badges
- Estructura clara
- Enlaces directos
- Emojis para mejor lectura

### 2. Agregar GitHub Actions Badge (Opcional)

Si implementas CI/CD, puedes añadir al README:

```markdown
![Tests](https://github.com/TU_USUARIO/foro_semana5_automatizacion_qa/actions/workflows/tests.yml/badge.svg)
```

### 3. Code Quality Badges (Opcional)

Integrar con servicios:
- **Codecov**: Cobertura de código
- **CodeFactor**: Calidad de código
- **Codacy**: Análisis estático

---

## 📱 Compartir en Plataformas Académicas

### Canvas/Moodle
1. Copia el link del repositorio
2. Pégalo en la tarea/foro correspondiente
3. Agrega nota: "Ver README.md para documentación completa"

### Microsoft Teams
1. Publica en el canal del equipo
2. Usa la vista previa del link (se expande automáticamente)
3. Menciona a los miembros del equipo

### Email
Usa la plantilla de email arriba 👆

---

## 🔒 Opciones de Privacidad

### Si prefieres repositorio privado:

1. En GitHub, ve a **Settings** del repositorio
2. Scroll hasta **"Danger Zone"**
3. Clic en **"Change visibility"** → **"Make private"**
4. Para compartir con personas específicas:
   - **Settings** → **"Collaborators"** → **"Add people"**
   - Agregar emails de profesores/estudiantes

---

## 📊 Mostrar Estadísticas del Repositorio

GitHub genera automáticamente:
- **Insights**: Actividad de commits
- **Contributors**: Quién contribuyó
- **Traffic**: Cuántas visitas recibió

Útil para demostrar trabajo colaborativo.

---

## ✅ Checklist Final Antes de Compartir

- [ ] README.md completo y claro
- [ ] GUIA_RAPIDA_EJECUCION.md funcional
- [ ] requirements.txt actualizado
- [ ] .gitignore configurado (no subir __pycache__, venv)
- [ ] Todas las pruebas pasan localmente
- [ ] Participaciones del foro subidas
- [ ] Documentación en /docs completa
- [ ] Repository description configurada
- [ ] Topics/tags agregados
- [ ] README renderiza correctamente en GitHub
- [ ] Links en README funcionan

---

## 🎓 Ventajas de Usar GitHub para el Foro

1. **Profesionalismo**: Demuestra uso de herramientas de la industria
2. **Portafolio**: Se puede incluir en CV/LinkedIn
3. **Colaboración**: Fácil para trabajo en equipo
4. **Versionamiento**: Historial completo de cambios
5. **Accesibilidad**: Acceso desde cualquier lugar
6. **Presentación**: README bien formateado impresiona

---

## 💡 Tip Extra: Agregar a tu Perfil de GitHub

En tu perfil de GitHub, puedes "pin" este repositorio:
1. Ve a tu perfil: `github.com/TU_USUARIO`
2. Clic en **"Customize your pins"**
3. Selecciona este repositorio
4. Ahora aparecerá destacado en tu perfil

**Útil para**: Reclutadores, profesores, otros estudiantes

---

## 🆘 Soporte

Si tienes problemas al subir:

1. **Error de autenticación**:
   - Usa personal access token en lugar de password
   - GitHub Settings → Developer settings → Personal access tokens

2. **Archivos muy grandes**:
   - Verifica .gitignore
   - No deberías subir venv/, __pycache__

3. **Conflictos**:
   ```bash
   git pull origin main --rebase
   git push origin main
   ```

---

## 📚 Recursos Adicionales

- **GitHub Docs**: https://docs.github.com/
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf
- **Markdown Guide**: https://www.markdownguide.org/

---

*Guía elaborada para facilitar el compartir del Foro Semana 5*  
*Febrero 2026*
