import unittest

from src.main import bmi_category, calculate_bmi


class TestBmiCalculator(unittest.TestCase):
	def test_calculate_bmi(self):
		self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.8571428571)

	def test_bmi_category(self):
		self.assertEqual(bmi_category(17.9), "Underweight")
		self.assertEqual(bmi_category(22.0), "Normal weight")
		self.assertEqual(bmi_category(27.0), "Overweight")
		self.assertEqual(bmi_category(31.0), "Obesity")


if __name__ == "__main__":
	unittest.main()
