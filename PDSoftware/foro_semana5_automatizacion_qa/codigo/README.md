# 💻 Código de Implementación - Foro Semana 5

## 📋 Descripción

Este directorio contiene la implementación práctica del **Anexo del Foro Semana 5** sobre Automatización en QA. El código demuestra:

- ✅ Automatización de pruebas con pytest y unittest
- ✅ Manejo robusto de excepciones
- ✅ Cobertura exhaustiva: casos válidos, inválidos y de borde
- ✅ Verificación explícita de manejo de errores
- ✅ Código profesional con logging y documentación

---

## 📁 Estructura de Archivos

```
codigo/
├── calculadora.py          # Módulo principal con funciones matemáticas
├── test_calculadora.py     # Suite de pruebas automatizadas (68 pruebas)
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

---

## 🚀 Instalación y Configuración

### 1. Clonar o Descargar el Repositorio

```bash
cd foro_semana5_automatizacion_qa/codigo
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecución de Pruebas

### Opción 1: Ejecutar con unittest

```bash
python -m unittest test_calculadora.py -v
```

**Salida esperada:**
```
test_dividir_casos_borde (__main__.TestCalculadoraUnitTest) ... ok
test_dividir_casos_validos (__main__.TestCalculadoraUnitTest) ... ok
test_dividir_excepcion_division_zero (__main__.TestCalculadoraUnitTest) ... ok
...
----------------------------------------------------------------------
Ran 40 tests in 0.123s

OK
```

### Opción 2: Ejecutar con pytest (Recomendado)

```bash
pytest test_calculadora.py -v
```

**Salida esperada:**
```
test_calculadora.py::TestCalculadoraUnitTest::test_dividir_casos_validos PASSED
test_calculadora.py::TestCalculadoraPytest::test_dividir_parametrizado[10-2-5.0] PASSED
...
================================ 68 passed in 0.45s =================================
```

### Opción 3: Ejecutar con Cobertura de Código

```bash
pytest test_calculadora.py -v --cov=calculadora --cov-report=html
```

**Esto genera:**
- Reporte en terminal
- Reporte HTML en `htmlcov/index.html`

```bash
# Abrir reporte en navegador
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Opción 4: Ejecutar Solo Pruebas Específicas

```bash
# Solo pruebas de división
pytest test_calculadora.py::TestCalculadoraPytest::test_dividir_parametrizado -v

# Solo pruebas marcadas como smoke
pytest -m smoke -v

# Solo pruebas que NO son lentas
pytest -m "not slow" -v
```

### Opción 5: Ejecución Paralela (Rápida)

```bash
pytest test_calculadora.py -n 4 -v
# -n 4 = usar 4 procesos en paralelo
```

---

## 📊 Cobertura de Pruebas Implementada

### Resumen de Casos

| Función | Casos Válidos | Casos Inválidos | Casos Borde | Total |
|---------|--------------|----------------|-------------|-------|
| `dividir()` | 8 | 5 | 4 | **17** |
| `raiz_cuadrada()` | 7 | 3 | 3 | **13** |
| `factorial()` | 5 | 4 | 2 | **11** |
| `es_palindromo()` | 10 | 3 | 4 | **17** |
| `promedio()` | 4 | 4 | 2 | **10** |
| **TOTAL** | **34** | **19** | **15** | **68** |

### Tipos de Excepciones Verificadas

- ✅ **TypeError**: Validación de tipos de entrada
- ✅ **ValueError**: Validación de dominio matemático
- ✅ **ValueError**: Validación de límites y recursos
- ✅ **ValueError**: Validación de estado (listas vacías, etc.)

---

## 🔍 Características del Código

### Módulo `calculadora.py`

**Funciones implementadas:**

1. **`dividir(a, b)`** - División con validación de tipos y división por cero
2. **`raiz_cuadrada(x)`** - Raíz cuadrada con validación de dominio
3. **`factorial(n)`** - Factorial con validación de límites
4. **`es_palindromo(cadena)`** - Verificación de palíndromos
5. **`promedio(numeros)`** - Cálculo de promedio con validación

**Características:**
- Excepción personalizada `CalculadoraError`
- Logging para trazabilidad
- Docstrings detallados con ejemplos
- Type hints para mejor IDE support
- Validación exhaustiva de entrada

### Módulo `test_calculadora.py`

**Frameworks utilizados:**
- `unittest` - Framework estándar de Python
- `pytest` - Framework moderno con más features

**Técnicas de testing:**
- Pruebas parametrizadas (`@pytest.mark.parametrize`)
- Marcadores personalizados (`@pytest.mark.smoke`, `@pytest.mark.regression`)
- Verificación de mensajes de excepción
- Setup/teardown methods
- Assertions descriptivas

---

## 📖 Ejemplos de Uso

### Uso Directo del Módulo

```python
from calculadora import Calculadora

calc = Calculadora()

# Operaciones válidas
resultado = calc.dividir(10, 2)  # 5.0
raiz = calc.raiz_cuadrada(16)    # 4.0
fact = calc.factorial(5)          # 120
palin = calc.es_palindromo("oso") # True
prom = calc.promedio([1,2,3,4,5]) # 3.0

# Manejo de excepciones
try:
    calc.dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: No es posible dividir por cero
```

### Ejecución de Demostración

```bash
python calculadora.py
```

---

## 🎯 Métricas de Calidad

### Cobertura de Código

```bash
pytest --cov=calculadora test_calculadora.py --cov-report=term

Name              Stmts   Miss  Cover
-------------------------------------
calculadora.py       95      0   100%
-------------------------------------
TOTAL                95      0   100%
```

**Resultado:** 100% de cobertura de código

### Tiempo de Ejecución

```bash
pytest test_calculadora.py --durations=0

68 passed in 0.45s
```

**Resultado:** Todas las pruebas ejecutan en menos de 0.5 segundos

---

## 🛠️ Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'pytest'"

**Solución:**
```bash
pip install -r requirements.txt
```

### Error: "No module named 'calculadora'"

**Solución:** Asegúrate de estar en el directorio correcto:
```bash
cd codigo/
python -m pytest test_calculadora.py
```

### Las pruebas fallan inesperadamente

**Solución:** Verifica la versión de Python:
```bash
python --version  # Debe ser Python 3.9+
```

---

## 📚 Referencias del Código

- **pytest Documentation**: https://docs.pytest.org/
- **unittest Documentation**: https://docs.python.org/3/library/unittest.html
- **Coverage.py**: https://coverage.readthedocs.io/

---

## ✅ Cumplimiento de Requisitos del Anexo

| Requisito | Estado | Evidencia |
|-----------|--------|-----------|
| Script en Python | ✅ | `calculadora.py`, `test_calculadora.py` |
| Cobertura completa (válidos, inválidos, borde) | ✅ | 68 pruebas clasificadas |
| Verificación de excepciones | ✅ | 19 pruebas de excepciones |
| Uso de assert | ✅ | Todo el archivo `test_calculadora.py` |
| Ejecución con pytest/unittest | ✅ | Ambos frameworks implementados |

---

## 👥 Elaborado Por

Equipo del Foro Semana 5 - Plataformas de Desarrollo de Software  
Fecha: Febrero 2026

---

## 📞 Soporte

Para preguntas sobre este código, consulte:
- Documentación del foro en `/participaciones_foro/`
- README principal en `/README.md`
- Docstrings en el código fuente
