import unittest
from src.lab1.calculator import calculator


class TestCalculator(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calculator("4 + 7"), "4+7 = 11")
	def test_subtract(self):
		self.assertEqual(calculator("10-2"), "10+-2 = 8")
	def test_multiply(self):
		self.assertEqual(calculator("3*7"), "3*7 = 21")
	def test_divide(self):
		self.assertEqual(calculator("10/2"), "10/2 = 5")
	def test_divide_by_zero(self):
		self.assertEqual(calculator("10/0"), "10/0 Произошла ошибка во время рассчёта: Деление на ноль!")
	def test_abc(self):
		self.assertEqual(calculator("40abc"), "40hjo Произошла ошибка во время рассчёта: Посторонний символ 'a'!")


if __name__ == "__main__":
	unittest.main()