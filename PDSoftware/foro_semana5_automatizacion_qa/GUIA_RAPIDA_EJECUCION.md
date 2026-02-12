# ⚡ Guía Rápida de Ejecución - 5 Minutos

Esta guía te permitirá ejecutar las pruebas automatizadas en menos de 5 minutos.

---

## 📋 Prerrequisitos

- ✅ Python 3.9 o superior instalado
- ✅ pip (gestor de paquetes de Python)
- ✅ Terminal/Consola

**Verificar Python:**
```bash
python --version  # o python3 --version
# Debe mostrar: Python 3.9.x o superior
```

---

## 🚀 Pasos de Ejecución

### 1️⃣ Navegar al Directorio de Código

```bash
cd foro_semana5_automatizacion_qa/codigo
```

### 2️⃣ Instalar Dependencias (Solo Primera Vez)

```bash
pip install -r requirements.txt
```

**Tiempo estimado:** 30 segundos

**Dependencias instaladas:**
- pytest 7.4.0
- pytest-cov 5.0.0
- pytest-xdist 3.5.0
- coverage 7.2.7

### 3️⃣ Ejecutar Pruebas

#### Opción A: Ejecución Básica con pytest ⭐ (Recomendado)

```bash
pytest test_calculadora.py -v
```

**Salida esperada:**
```
================================= test session starts ==================================
collected 68 items

test_calculadora.py::TestCalculadoraUnitTest::test_dividir_casos_validos PASSED  [ 1%]
test_calculadora.py::TestCalculadoraUnitTest::test_dividir_casos_borde PASSED    [ 2%]
...
================================= 68 passed in 0.45s ===================================
```

#### Opción B: Ejecución con unittest

```bash
python -m unittest test_calculadora.py -v
```

#### Opción C: Ejecución con Reporte de Cobertura 📊

```bash
pytest test_calculadora.py -v --cov=calculadora --cov-report=html
```

**Ver reporte en navegador:**
```bash
# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov/index.html
```

#### Opción D: Ejecución Paralela (Más Rápida) 🚀

```bash
pytest test_calculadora.py -n 4
# -n 4 = usa 4 procesos en paralelo
```

---

## 📊 Resultados Esperados

### ✅ Todas las Pruebas Pasan

```
================================= 68 passed in 0.45s ===================================
```

**Métricas:**
- ✅ 68 pruebas ejecutadas
- ✅ 100% de pruebas exitosas
- ✅ Tiempo de ejecución: < 0.5 segundos
- ✅ Cobertura de código: 100%

### 📈 Reporte de Cobertura

```
Name              Stmts   Miss  Cover
-------------------------------------
calculadora.py       95      0   100%
-------------------------------------
TOTAL                95      0   100%
```

---

## 🧪 Probar Funcionalidad Manualmente

### Ejecutar Demo Interactiva

```bash
python calculadora.py
```

**Salida esperada:**
```
=== Demostración de Calculadora ===

División: 10 / 2 = 5.0
Raíz cuadrada: √16 = 4.0
Factorial: 5! = 120
Palíndromo: 'anita lava la tina' = True
Promedio: [1,2,3,4,5] = 3.0

=== Demostración de Manejo de Excepciones ===

✓ Excepción capturada: No es posible dividir por cero
✓ Excepción capturada: No es posible calcular raíz cuadrada de un número negativo
✓ Excepción capturada: No es posible calcular factorial de un número negativo
```

### Usar en Python Interactivo

```bash
python
```

```python
>>> from calculadora import Calculadora
>>> calc = Calculadora()

>>> calc.dividir(10, 2)
5.0

>>> calc.raiz_cuadrada(16)
4.0

>>> calc.factorial(5)
120

>>> calc.es_palindromo("anita lava la tina")
True

>>> calc.promedio([1, 2, 3, 4, 5])
3.0

# Probar excepción
>>> calc.dividir(10, 0)
ValueError: No es posible dividir por cero
```

---

## 🔍 Comandos Útiles Adicionales

### Ejecutar Solo Pruebas Específicas

```bash
# Solo pruebas de división
pytest test_calculadora.py::TestCalculadoraPytest::test_dividir_parametrizado

# Solo pruebas marcadas como 'smoke'
pytest -m smoke

# Excluir pruebas lentas
pytest -m "not slow"
```

### Ver Detalles de Pruebas que Fallan

```bash
pytest test_calculadora.py -v --tb=short
```

### Ejecutar con Salida Detallada

```bash
pytest test_calculadora.py -vv
```

### Generar Reporte JSON

```bash
pytest test_calculadora.py --json-report --json-report-file=reporte.json
```

---

## ⚠️ Solución de Problemas Comunes

### Problema: "ModuleNotFoundError: No module named 'pytest'"

**Solución:**
```bash
pip install -r requirements.txt
```

### Problema: "No module named 'calculadora'"

**Solución:** Asegúrate de estar en el directorio correcto:
```bash
pwd  # Debe terminar en /codigo
cd foro_semana5_automatizacion_qa/codigo
```

### Problema: Python no reconocido

**Solución:** Intenta con `python3` en lugar de `python`:
```bash
python3 --version
python3 -m pytest test_calculadora.py
```

### Problema: Permisos denegados (Windows)

**Solución:** Ejecuta la terminal como Administrador

---

## 📚 Siguiente Paso

Una vez ejecutadas las pruebas exitosamente, puedes:

1. **Revisar el código fuente**: `calculadora.py` y `test_calculadora.py`
2. **Leer la documentación técnica**: `codigo/README.md`
3. **Explorar participaciones del foro**: `participaciones_foro/`
4. **Ver el README principal**: `README.md`

---

## ⏱️ Resumen Temporal

| Actividad | Tiempo |
|-----------|--------|
| Navegar al directorio | 10 seg |
| Instalar dependencias | 30 seg |
| Ejecutar pruebas | 5 seg |
| **TOTAL** | **< 1 minuto** |

**Revisar reporte de cobertura:** +1 minuto  
**Probar manualmente:** +2 minutos

---

## ✅ Checklist de Éxito

- [ ] Python 3.9+ instalado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Pruebas ejecutadas (`pytest test_calculadora.py -v`)
- [ ] Todas las 68 pruebas pasaron ✅
- [ ] Reporte de cobertura generado (opcional)
- [ ] Demo manual probada (opcional)

---

## 🎯 Lo Aprendido en 5 Minutos

En solo 5 minutos, has:

✅ Ejecutado 68 pruebas automatizadas  
✅ Verificado 100% de cobertura de código  
✅ Validado casos válidos, inválidos y de borde  
✅ Comprobado manejo robusto de excepciones  
✅ Observado pruebas con pytest y unittest  

**¡Esto es el poder de la automatización en QA!** 🚀

---

*Elaborado para el Foro Semana 5 - Febrero 2026*
