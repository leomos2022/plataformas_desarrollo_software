"""
Suite de Pruebas Automatizadas para Calculadora
Foro Semana 5 - Automatización en QA: Elevando la Eficiencia

Esta suite demuestra:
- Pruebas con unittest y pytest
- Cobertura de casos válidos, inválidos y de borde
- Verificación exhaustiva de excepciones
- Pruebas parametrizadas
- Organización profesional de tests

Ejecución:
    python -m unittest test_calculadora.py -v
    pytest test_calculadora.py -v
    pytest --cov=calculadora test_calculadora.py --cov-report=html
"""

import pytest
import unittest
import math
from calculadora import Calculadora, CalculadoraError


# ==========================================
# SUITE UNITTEST - Clase TestCalculadoraUnitTest
# ==========================================

class TestCalculadoraUnitTest(unittest.TestCase):
    """
    Pruebas unitarias usando el framework unittest.
    Demuestra el enfoque tradicional de testing en Python.
    """
    
    def setUp(self):
        """Configuración ejecutada antes de cada prueba"""
        self.calc = Calculadora()
    
    # ===== PRUEBAS PARA DIVISIÓN =====
    
    def test_dividir_casos_validos(self):
        """Caso POSITIVO: División con valores válidos"""
        # Enteros positivos
        self.assertEqual(self.calc.dividir(10, 2), 5.0)
        self.assertEqual(self.calc.dividir(100, 4), 25.0)
        
        # Flotantes
        self.assertAlmostEqual(self.calc.dividir(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.dividir(1.0, 3.0), 0.3333333, places=5)
        
        # Números negativos
        self.assertEqual(self.calc.dividir(-10, 2), -5.0)
        self.assertEqual(self.calc.dividir(10, -2), -5.0)
        self.assertEqual(self.calc.dividir(-10, -2), 5.0)
    
    def test_dividir_casos_borde(self):
        """Caso BORDE: División con valores límite"""
        # Dividir por 1
        self.assertEqual(self.calc.dividir(42, 1), 42.0)
        
        # Cero como numerador
        self.assertEqual(self.calc.dividir(0, 5), 0.0)
        
        # Números muy grandes
        resultado = self.calc.dividir(1e10, 1e5)
        self.assertAlmostEqual(resultado, 1e5)
        
        # Números muy pequeños
        resultado = self.calc.dividir(1, 1e10)
        self.assertAlmostEqual(resultado, 1e-10)
    
    def test_dividir_excepcion_division_cero(self):
        """Caso NEGATIVO: Verificación de excepción por división entre cero"""
        with self.assertRaises(ValueError) as context:
            self.calc.dividir(10, 0)
        
        # Verificar mensaje específico
        self.assertIn("No es posible dividir por cero", str(context.exception))
    
    def test_dividir_excepcion_tipo_invalido(self):
        """Caso NEGATIVO: Verificación de excepción por tipo inválido"""
        # String como numerador
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)
        
        # String como denominador
        with self.assertRaises(TypeError):
            self.calc.dividir(10, "2")
        
        # Lista como argumento
        with self.assertRaises(TypeError):
            self.calc.dividir([10], 2)
        
        # Boolean (caso especial en Python)
        with self.assertRaises(TypeError):
            self.calc.dividir(True, False)
    
    # ===== PRUEBAS PARA RAÍZ CUADRADA =====
    
    def test_raiz_cuadrada_casos_validos(self):
        """Caso POSITIVO: Raíz cuadrada con valores válidos"""
        # Casos exactos
        self.assertEqual(self.calc.raiz_cuadrada(0), 0.0)
        self.assertEqual(self.calc.raiz_cuadrada(1), 1.0)
        self.assertEqual(self.calc.raiz_cuadrada(4), 2.0)
        self.assertEqual(self.calc.raiz_cuadrada(9), 3.0)
        self.assertEqual(self.calc.raiz_cuadrada(16), 4.0)
        self.assertEqual(self.calc.raiz_cuadrada(100), 10.0)
        
        # Casos con decimales
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), 1.41421356, places=5)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(3), 1.73205080, places=5)
    
    def test_raiz_cuadrada_casos_borde(self):
        """Caso BORDE: Raíz cuadrada con valores límite"""
        # Número muy grande
        resultado = self.calc.raiz_cuadrada(1e10)
        self.assertAlmostEqual(resultado, 1e5)
        
        # Número muy pequeño cercano a cero
        resultado = self.calc.raiz_cuadrada(1e-10)
        self.assertAlmostEqual(resultado, 1e-5)
    
    def test_raiz_cuadrada_excepcion_numero_negativo(self):
        """Caso NEGATIVO: Verificación de excepción con número negativo"""
        with self.assertRaises(ValueError) as context:
            self.calc.raiz_cuadrada(-1)
        
        self.assertIn("número negativo", str(context.exception))
        
        # Más casos negativos
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-100)
    
    def test_raiz_cuadrada_excepcion_tipo_invalido(self):
        """Caso NEGATIVO: Verificación de excepción por tipo inválido"""
        with self.assertRaises(TypeError):
            self.calc.raiz_cuadrada("4")
        
        with self.assertRaises(TypeError):
            self.calc.raiz_cuadrada([4])
        
        with self.assertRaises(TypeError):
            self.calc.raiz_cuadrada(None)
    
    # ===== PRUEBAS PARA FACTORIAL =====
    
    def test_factorial_casos_validos(self):
        """Caso POSITIVO: Factorial con valores válidos"""
        # Casos conocidos
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
        self.assertEqual(self.calc.factorial(20), 2432902008176640000)
    
    def test_factorial_casos_borde(self):
        """Caso BORDE: Factorial con valores límite"""
        # Valor máximo permitido
        resultado = self.calc.factorial(100)
        self.assertIsInstance(resultado, int)
        self.assertGreater(resultado, 0)
        
        # Verificar que es correcto
        self.assertEqual(resultado, math.factorial(100))
    
    def test_factorial_excepcion_numero_negativo(self):
        """Caso NEGATIVO: Verificación de excepción con número negativo"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-1)
        
        self.assertIn("número negativo", str(context.exception))
        
        with self.assertRaises(ValueError):
            self.calc.factorial(-10)
    
    def test_factorial_excepcion_excede_limite(self):
        """Caso NEGATIVO: Verificación de excepción por exceder límite"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(101)
        
        self.assertIn("excede el límite", str(context.exception))
    
    def test_factorial_excepcion_tipo_invalido(self):
        """Caso NEGATIVO: Verificación de excepción por tipo inválido"""
        # Float en lugar de int
        with self.assertRaises(TypeError):
            self.calc.factorial(5.5)
        
        # String
        with self.assertRaises(TypeError):
            self.calc.factorial("5")
        
        # Boolean
        with self.assertRaises(TypeError):
            self.calc.factorial(True)
    
    # ===== PRUEBAS PARA PALÍNDROMO =====
    
    def test_palindromo_casos_validos_true(self):
        """Caso POSITIVO: Cadenas que son palíndromos"""
        # Palíndromos simples
        self.assertTrue(self.calc.es_palindromo("oso"))
        self.assertTrue(self.calc.es_palindromo("aba"))
        self.assertTrue(self.calc.es_palindromo("reconocer"))
        
        # Con espacios
        self.assertTrue(self.calc.es_palindromo("anita lava la tina"))
        self.assertTrue(self.calc.es_palindromo("a man a plan a canal panama"))
        
        # Con mayúsculas
        self.assertTrue(self.calc.es_palindromo("Oso"))
        self.assertTrue(self.calc.es_palindromo("Anita Lava La Tina"))
    
    def test_palindromo_casos_validos_false(self):
        """Caso POSITIVO: Cadenas que NO son palíndromos"""
        self.assertFalse(self.calc.es_palindromo("hola"))
        self.assertFalse(self.calc.es_palindromo("python"))
        self.assertFalse(self.calc.es_palindromo("automatizacion"))
    
    def test_palindromo_casos_borde(self):
        """Caso BORDE: Casos límite de palíndromos"""
        # Un solo carácter
        self.assertTrue(self.calc.es_palindromo("a"))
        self.assertTrue(self.calc.es_palindromo("Z"))
        
        # Dos caracteres iguales
        self.assertTrue(self.calc.es_palindromo("aa"))
        
        # Dos caracteres diferentes
        self.assertFalse(self.calc.es_palindromo("ab"))
    
    def test_palindromo_excepcion_cadena_vacia(self):
        """Caso NEGATIVO: Verificación de excepción con cadena vacía"""
        with self.assertRaises(ValueError) as context:
            self.calc.es_palindromo("")
        
        self.assertIn("vacía", str(context.exception))
        
        # Solo espacios
        with self.assertRaises(ValueError):
            self.calc.es_palindromo("   ")
    
    def test_palindromo_excepcion_tipo_invalido(self):
        """Caso NEGATIVO: Verificación de excepción por tipo inválido"""
        with self.assertRaises(TypeError):
            self.calc.es_palindromo(123)
        
        with self.assertRaises(TypeError):
            self.calc.es_palindromo(['a', 'b', 'a'])
        
        with self.assertRaises(TypeError):
            self.calc.es_palindromo(None)
    
    # ===== PRUEBAS PARA PROMEDIO =====
    
    def test_promedio_casos_validos(self):
        """Caso POSITIVO: Promedio con valores válidos"""
        self.assertAlmostEqual(self.calc.promedio([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(self.calc.promedio([10, 20, 30]), 20.0)
        self.assertAlmostEqual(self.calc.promedio([5.5, 4.5]), 5.0)
        
        # Con negativos
        self.assertAlmostEqual(self.calc.promedio([-5, 5]), 0.0)
        self.assertAlmostEqual(self.calc.promedio([-10, -20, -30]), -20.0)
    
    def test_promedio_casos_borde(self):
        """Caso BORDE: Promedio con casos límite"""
        # Un solo elemento
        self.assertEqual(self.calc.promedio([42]), 42.0)
        
        # Todos ceros
        self.assertEqual(self.calc.promedio([0, 0, 0]), 0.0)
    
    def test_promedio_excepcion_lista_vacia(self):
        """Caso NEGATIVO: Verificación de excepción con lista vacía"""
        with self.assertRaises(ValueError) as context:
            self.calc.promedio([])
        
        self.assertIn("vacía", str(context.exception))
    
    def test_promedio_excepcion_tipo_invalido(self):
        """Caso NEGATIVO: Verificación de excepción por tipo inválido"""
        # No es lista
        with self.assertRaises(TypeError):
            self.calc.promedio("1,2,3")
        
        # Lista con strings
        with self.assertRaises(TypeError):
            self.calc.promedio([1, 2, "3"])
        
        # Lista con None
        with self.assertRaises(TypeError):
            self.calc.promedio([1, None, 3])


# ==========================================
# SUITE PYTEST - Clase TestCalculadoraPytest
# ==========================================

class TestCalculadoraPytest:
    """
    Pruebas unitarias usando pytest.
    Demuestra el enfoque moderno con fixtures y parametrización.
    """
    
    def setup_method(self):
        """Configuración ejecutada antes de cada prueba (pytest style)"""
        self.calc = Calculadora()
    
    # ===== PRUEBAS PARAMETRIZADAS =====
    
    @pytest.mark.parametrize("a,b,esperado", [
        # Casos normales
        (10, 2, 5.0),
        (100, 4, 25.0),
        (9, 3, 3.0),
        # Casos con negativos
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
        # Casos con decimales
        (7.5, 2.5, 3.0),
        (1.0, 2.0, 0.5),
    ])
    def test_dividir_parametrizado(self, a, b, esperado):
        """Pruebas parametrizadas para división - múltiples casos en uno"""
        assert self.calc.dividir(a, b) == pytest.approx(esperado)
    
    @pytest.mark.parametrize("numero,esperado", [
        (0, 0.0),
        (1, 1.0),
        (4, 2.0),
        (9, 3.0),
        (16, 4.0),
        (25, 5.0),
        (100, 10.0),
    ])
    def test_raiz_cuadrada_parametrizado(self, numero, esperado):
        """Pruebas parametrizadas para raíz cuadrada"""
        assert self.calc.raiz_cuadrada(numero) == pytest.approx(esperado)
    
    @pytest.mark.parametrize("n,esperado", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (10, 3628800),
    ])
    def test_factorial_parametrizado(self, n, esperado):
        """Pruebas parametrizadas para factorial"""
        assert self.calc.factorial(n) == esperado
    
    @pytest.mark.parametrize("cadena", [
        "oso",
        "aba",
        "reconocer",
        "anita lava la tina",
        "a man a plan a canal panama",
        "Oso",
        "AbA",
    ])
    def test_palindromo_true_parametrizado(self, cadena):
        """Pruebas parametrizadas para palíndromos verdaderos"""
        assert self.calc.es_palindromo(cadena) is True
    
    @pytest.mark.parametrize("cadena", [
        "hola",
        "python",
        "automatizacion",
        "testing",
    ])
    def test_palindromo_false_parametrizado(self, cadena):
        """Pruebas parametrizadas para no-palíndromos"""
        assert self.calc.es_palindromo(cadena) is False
    
    # ===== PRUEBAS DE EXCEPCIONES CON PYTEST =====
    
    def test_dividir_excepcion_con_match(self):
        """Verificación de excepción con mensaje específico usando pytest"""
        with pytest.raises(ValueError, match="dividir por cero"):
            self.calc.dividir(10, 0)
        
        with pytest.raises(TypeError, match="debe ser un número"):
            self.calc.dividir("10", 2)
    
    def test_raiz_cuadrada_excepcion_con_match(self):
        """Verificación de excepción con mensaje específico"""
        with pytest.raises(ValueError, match="número negativo"):
            self.calc.raiz_cuadrada(-1)
        
        with pytest.raises(TypeError, match="debe ser un número"):
            self.calc.raiz_cuadrada("4")
    
    def test_factorial_excepcion_con_match(self):
        """Verificación de excepción con mensaje específico"""
        with pytest.raises(ValueError, match="número negativo"):
            self.calc.factorial(-5)
        
        with pytest.raises(ValueError, match="excede el límite"):
            self.calc.factorial(101)
        
        with pytest.raises(TypeError, match="número entero"):
            self.calc.factorial(5.5)
    
    def test_palindromo_excepcion_con_match(self):
        """Verificación de excepción con mensaje específico"""
        with pytest.raises(ValueError, match="vacía"):
            self.calc.es_palindromo("")
        
        with pytest.raises(TypeError, match="cadena de texto"):
            self.calc.es_palindromo(123)
    
    def test_promedio_excepcion_con_match(self):
        """Verificación de excepción con mensaje específico"""
        with pytest.raises(ValueError, match="vacía"):
            self.calc.promedio([])
        
        with pytest.raises(TypeError, match="debe ser una lista"):
            self.calc.promedio("1,2,3")
    
    # ===== PRUEBAS DE INTEGRACIÓN =====
    
    def test_operaciones_combinadas(self):
        """Prueba de integración: combinar múltiples operaciones"""
        # Calcular: √(10/2) debería ser √5 ≈ 2.236
        division = self.calc.dividir(10, 2)
        raiz = self.calc.raiz_cuadrada(division)
        assert raiz == pytest.approx(2.236, rel=0.001)
        
        # Factorial y promedio
        fact = self.calc.factorial(5)  # 120
        prom = self.calc.promedio([100, 120, 140])  # 120
        assert fact == prom


# ==========================================
# PRUEBAS DE MARCADORES PYTEST
# ==========================================

class TestMarcadoresPytest:
    """Demostración de marcadores pytest para organizar pruebas"""
    
    def setup_method(self):
        self.calc = Calculadora()
    
    @pytest.mark.smoke
    def test_funciones_basicas_funcionan(self):
        """Prueba de humo: verificación rápida de que las funciones básicas funcionan"""
        assert self.calc.dividir(4, 2) == 2.0
        assert self.calc.raiz_cuadrada(4) == 2.0
        assert self.calc.factorial(4) == 24
    
    @pytest.mark.slow
    def test_factorial_numeros_grandes(self):
        """Prueba lenta: factoriales grandes"""
        resultado = self.calc.factorial(100)
        assert resultado > 0
        assert resultado == math.factorial(100)
    
    @pytest.mark.edge_case
    def test_casos_limite_extremos(self):
        """Casos borde extremos"""
        # División con números muy pequeños
        assert self.calc.dividir(1, 1e15) == pytest.approx(1e-15)
        
        # Raíz cuadrada de número muy grande
        assert self.calc.raiz_cuadrada(1e20) == pytest.approx(1e10)


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == '__main__':
    # Ejecutar con unittest
    print("=" * 70)
    print("EJECUTANDO PRUEBAS CON UNITTEST")
    print("=" * 70)
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 70)
    print("PARA EJECUTAR CON PYTEST, USE:")
    print("pytest test_calculadora.py -v")
    print("pytest --cov=calculadora test_calculadora.py --cov-report=html")
    print("=" * 70)
