import os
import sys
import unittest

# Make the Lab1 folder importable so `from src import calculator` works from any cwd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(-1, -1), -2)
        self.assertAlmostEqual(calculator.fun1(0.1, 0.2), 0.3)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3), 10)
        self.assertEqual(calculator.fun4(5, 5), 35)
        self.assertEqual(calculator.fun4(-2, 4), -12)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(6, 3), 2)
        self.assertAlmostEqual(calculator.fun5(1, 3), 0.3333333, places=6)
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(1, 0)

    def test_invalid_inputs(self):
        for func in (calculator.fun1, calculator.fun2, calculator.fun3,
                     calculator.fun4, calculator.fun5):
            for bad in ("2", None, True):
                with self.subTest(func=func.__name__, bad=bad):
                    with self.assertRaises(ValueError):
                        func(bad, 1)


if __name__ == "__main__":
    unittest.main()
