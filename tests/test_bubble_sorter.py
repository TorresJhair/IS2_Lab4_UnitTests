"""Casos de prueba xUnit (unittest) para BubbleSorter."""
import unittest

from src.bubble_sorter import BubbleSorter


class BubbleSorterTest(unittest.TestCase):

    def setUp(self):
        self.sorter = BubbleSorter()       # Inicializar el SUT

    def tearDown(self):
        self.sorter = None                 # Liberar recursos

    def test_cp1_vector_sin_iteraciones(self):
        """CP1 - Camino 1-2-8-9: el bucle externo no se ejecuta."""
        # Arrange
        vet = [7]
        esperado = [7]
        # Act
        resultado = self.sorter.bubble_sort(vet)
        # Assert
        self.assertEqual(esperado, resultado)

    def test_cp3_vector_ya_ordenado(self):
        """CP3 - Camino 1-2-3-4-6-3-7-2-8-9: el if es falso."""
        # Arrange
        vet = [1, 2, 3]
        esperado = [1, 2, 3]
        # Act
        resultado = self.sorter.bubble_sort(vet)
        # Assert
        self.assertEqual(esperado, resultado)

    def test_cp4_vector_desordenado(self):
        """CP4 - Camino 1-2-3-4-5-6-3-7-2-8-9: el if es verdadero."""
        # Arrange
        
        vet = [2, 3, 1]
        esperado = [1, 2, 3]
        # Act
        resultado = self.sorter.bubble_sort(vet)
        # Assert
        self.assertEqual(esperado, resultado)


if __name__ == "__main__":
    unittest.main()
