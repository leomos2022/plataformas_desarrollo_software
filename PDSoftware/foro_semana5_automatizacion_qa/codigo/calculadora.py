"""
Módulo de Calculadora con manejo robusto de excepciones
Foro Semana 5 - Automatización en QA: Elevando la Eficiencia

Este módulo demuestra prácticas profesionales de:
- Validación exhaustiva de entradas
- Manejo específico de excepciones
- Logging para trazabilidad
- Documentación con docstrings
"""

import math
import logging
from typing import Union, List

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class CalculadoraError(Exception):
    """Excepción base personalizada para errores de calculadora"""
    pass


class Calculadora:
    """
    Clase calculadora con operaciones matemáticas y manejo de excepciones.
    
    Esta implementación demuestra cómo validar entradas, manejar errores
    y proporcionar mensajes descriptivos para facilitar el debugging.
    """
    
    @staticmethod
    def dividir(a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide dos números con validación exhaustiva.
        
        Args:
            a: Numerador (int o float)
            b: Denominador (int o float)
            
        Returns:
            float: Resultado de la división a/b
            
        Raises:
            TypeError: Si los argumentos no son números
            ValueError: Si b es cero
            CalculadoraError: Para otros errores de cálculo
            
        Examples:
            >>> calc = Calculadora()
            >>> calc.dividir(10, 2)
            5.0
            >>> calc.dividir(10, 0)
            ValueError: No es posible dividir por cero
        """
        try:
            # Validación de tipos
            if not isinstance(a, (int, float)) or isinstance(a, bool):
                raise TypeError(
                    f"El numerador debe ser un número, se recibió {type(a).__name__}"
                )
            
            if not isinstance(b, (int, float)) or isinstance(b, bool):
                raise TypeError(
                    f"El denominador debe ser un número, se recibió {type(b).__name__}"
                )
            
            # Validación de división por cero
            if b == 0:
                raise ValueError("No es posible dividir por cero")
            
            # Realizar operación
            resultado = a / b
            logger.info(f"División exitosa: {a} / {b} = {resultado}")
            return resultado
            
        except ZeroDivisionError:
            # Captura adicional por si acaso
            logger.error(f"ZeroDivisionError capturado en división: {a}/{b}")
            raise ValueError("No es posible dividir por cero")
        except (TypeError, ValueError) as e:
            logger.error(f"Error en división: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado en división: {str(e)}")
            raise CalculadoraError(f"Error calculando {a}/{b}: {str(e)}")
    
    @staticmethod
    def raiz_cuadrada(x: Union[int, float]) -> float:
        """
        Calcula la raíz cuadrada con validación de dominio.
        
        Args:
            x: Número para calcular raíz cuadrada (debe ser >= 0)
            
        Returns:
            float: Raíz cuadrada de x
            
        Raises:
            TypeError: Si x no es número
            ValueError: Si x es negativo
            
        Examples:
            >>> calc = Calculadora()
            >>> calc.raiz_cuadrada(4)
            2.0
            >>> calc.raiz_cuadrada(-1)
            ValueError: No es posible calcular raíz cuadrada de número negativo
        """
        try:
            # Validación de tipo
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise TypeError(
                    f"El argumento debe ser un número, se recibió {type(x).__name__}"
                )
            
            # Validación de dominio matemático
            if x < 0:
                raise ValueError(
                    "No es posible calcular raíz cuadrada de un número negativo"
                )
            
            # Realizar cálculo
            resultado = math.sqrt(x)
            logger.info(f"Raíz cuadrada exitosa: √{x} = {resultado}")
            return resultado
            
        except (TypeError, ValueError) as e:
            logger.error(f"Error en raíz cuadrada: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado en raíz cuadrada: {str(e)}")
            raise CalculadoraError(f"Error calculando √{x}: {str(e)}")
    
    @staticmethod
    def factorial(n: int) -> int:
        """
        Calcula el factorial de un número entero no negativo.
        
        Args:
            n: Número entero >= 0
            
        Returns:
            int: Factorial de n (n!)
            
        Raises:
            TypeError: Si n no es entero
            ValueError: Si n es negativo o excede límites
            
        Examples:
            >>> calc = Calculadora()
            >>> calc.factorial(5)
            120
            >>> calc.factorial(-1)
            ValueError: No es posible calcular factorial de número negativo
        """
        try:
            # Validación estricta de tipo entero
            if not isinstance(n, int) or isinstance(n, bool):
                raise TypeError(
                    f"El argumento debe ser un número entero, se recibió {type(n).__name__}"
                )
            
            # Validación de rango
            if n < 0:
                raise ValueError(
                    "No es posible calcular factorial de un número negativo"
                )
            
            # Validación de límite para evitar overflow/tiempo excesivo
            if n > 100:
                raise ValueError(
                    "El factorial excede el límite de procesamiento (máximo 100)"
                )
            
            # Calcular factorial
            resultado = math.factorial(n)
            logger.info(f"Factorial exitoso: {n}! = {resultado}")
            return resultado
            
        except (TypeError, ValueError) as e:
            logger.error(f"Error en factorial: {str(e)}")
            raise
        except OverflowError:
            logger.error(f"OverflowError en factorial de {n}")
            raise ValueError("El factorial es demasiado grande para calcularlo")
        except Exception as e:
            logger.error(f"Error inesperado en factorial: {str(e)}")
            raise CalculadoraError(f"Error calculando {n}!: {str(e)}")
    
    @staticmethod
    def es_palindromo(cadena: str) -> bool:
        """
        Verifica si una cadena de texto es un palíndromo.
        
        Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda,
        ignorando espacios y mayúsculas.
        
        Args:
            cadena: Texto a evaluar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
            
        Raises:
            TypeError: Si la entrada no es string
            ValueError: Si la cadena está vacía
            
        Examples:
            >>> calc = Calculadora()
            >>> calc.es_palindromo("anita lava la tina")
            True
            >>> calc.es_palindromo("hola")
            False
        """
        try:
            # Validación de tipo
            if not isinstance(cadena, str):
                raise TypeError(
                    f"La entrada debe ser una cadena de texto, se recibió {type(cadena).__name__}"
                )
            
            # Validación de contenido
            if not cadena.strip():
                raise ValueError("La cadena no puede estar vacía o contener solo espacios")
            
            # Normalizar: eliminar espacios y convertir a minúsculas
            cadena_limpia = ''.join(cadena.lower().split())
            
            # Verificar palíndromo
            resultado = cadena_limpia == cadena_limpia[::-1]
            
            logger.info(
                f"Verificación de palíndromo: '{cadena}' "
                f"(normalizado: '{cadena_limpia}') = {resultado}"
            )
            return resultado
            
        except (TypeError, ValueError) as e:
            logger.error(f"Error en verificación de palíndromo: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado en palíndromo: {str(e)}")
            raise CalculadoraError(f"Error verificando palíndromo '{cadena}': {str(e)}")
    
    @staticmethod
    def promedio(numeros: List[Union[int, float]]) -> float:
        """
        Calcula el promedio de una lista de números.
        
        Args:
            numeros: Lista de números
            
        Returns:
            float: Promedio de los números
            
        Raises:
            TypeError: Si no es lista o contiene no-números
            ValueError: Si la lista está vacía
            
        Examples:
            >>> calc = Calculadora()
            >>> calc.promedio([1, 2, 3, 4, 5])
            3.0
        """
        try:
            # Validación de tipo lista
            if not isinstance(numeros, list):
                raise TypeError(
                    f"El argumento debe ser una lista, se recibió {type(numeros).__name__}"
                )
            
            # Validación de lista vacía
            if len(numeros) == 0:
                raise ValueError("La lista no puede estar vacía")
            
            # Validación de contenido
            for i, num in enumerate(numeros):
                if not isinstance(num, (int, float)) or isinstance(num, bool):
                    raise TypeError(
                        f"Elemento en posición {i} no es un número: {type(num).__name__}"
                    )
            
            # Calcular promedio
            resultado = sum(numeros) / len(numeros)
            logger.info(f"Promedio de {len(numeros)} números: {resultado}")
            return resultado
            
        except (TypeError, ValueError) as e:
            logger.error(f"Error en cálculo de promedio: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error inesperado en promedio: {str(e)}")
            raise CalculadoraError(f"Error calculando promedio: {str(e)}")


if __name__ == "__main__":
    # Demostración de uso
    calc = Calculadora()
    
    print("=== Demostración de Calculadora ===\n")
    
    # Casos exitosos
    print(f"División: 10 / 2 = {calc.dividir(10, 2)}")
    print(f"Raíz cuadrada: √16 = {calc.raiz_cuadrada(16)}")
    print(f"Factorial: 5! = {calc.factorial(5)}")
    print(f"Palíndromo: 'anita lava la tina' = {calc.es_palindromo('anita lava la tina')}")
    print(f"Promedio: [1,2,3,4,5] = {calc.promedio([1,2,3,4,5])}")
    
    print("\n=== Demostración de Manejo de Excepciones ===\n")
    
    # Casos de error
    try:
        calc.dividir(10, 0)
    except ValueError as e:
        print(f"✓ Excepción capturada: {e}")
    
    try:
        calc.raiz_cuadrada(-4)
    except ValueError as e:
        print(f"✓ Excepción capturada: {e}")
    
    try:
        calc.factorial(-5)
    except ValueError as e:
        print(f"✓ Excepción capturada: {e}")
