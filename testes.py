import unittest
from Ac_01 import exercicio01, exercicio02, exercicio03, exercicio04

class ac_exerecicio_01(unittest.TestCase):
    def test_exercicio01_01(self):
        self.assertEqual(exercicio01(6.25, 160, 1.3), 987.00)
    
    def test_exercicio01_02(self):
        self.assertEqual(exercicio01(20.5, 240, 1.7), 4836.36)

    def test_exercicio01_03(self):
        self.assertEqual(exercicio01(13.9, 200, 6.48), 2599.86)


class ac_exerecicio_02(unittest.TestCase):
    def test_exercicio02_01(self):
        self.assertEqual(exercicio02(100), [91.00, 9.00])
    
    def test_exercicio02_02(self):
        self.assertEqual(exercicio02(1500), [1365.00, 135.00])

    def test_exercicio02_03(self):
        self.assertEqual(exercicio02(60000), [54600.00, 5400.00])


class ac_exerecicio_03(unittest.TestCase):
    def test_exercicio03_01(self):
        self.assertEqual(exercicio03(500.00, 50.00), 450.00)
    
    def test_exercicio03_02(self):
        self.assertEqual(exercicio03(10500.00, 500.00), 10000.00)

    def test_exercicio03_03(self):
        self.assertEqual(exercicio03(90.00, 0.80), 89.20)


class ac_exerecicio_04(unittest.TestCase):
    def test_exercicio04_01(self):
        self.assertEqual(exercicio04(75.00), [82.50, 7.5])
    
    def test_exercicio04_02(self):
        self.assertEqual(exercicio04(125), [137.50, 12.5])

    def test_exercicio04_03(self):
        self.assertEqual(exercicio04(350.87), [385.96, 35.09])


if __name__ == '__main__':
    unittest.main