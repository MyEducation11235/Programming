import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CalculatorTestCase(unittest.TestCase):
    def test_encrypt_caesar_1(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
    def test_encrypt_caesar_2(self):
        self.assertEqual(encrypt_caesar("python"), 'sbwkrq')
    def test_encrypt_caesar_3(self):
        self.assertEqual(encrypt_caesar("Python3.6"), 'Sbwkrq3.6')
    def test_encrypt_caesar_4(self):
        self.assertEqual(encrypt_caesar(""), "")
    def test_encrypt_caesar_5(self):
        self.assertEqual(encrypt_caesar("AbZ", 4), "EfD")    

    def test_decrypt_caesar_1(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
    def test_decrypt_caesar_2(self):
        self.assertEqual(decrypt_caesar('sbwkrq'), "python")
    def test_decrypt_caesar_3(self):
        self.assertEqual(decrypt_caesar('Sbwkrq3.6'), "Python3.6")
    def test_decrypt_caesar_4(self):
        self.assertEqual(decrypt_caesar(""), "")
    def test_decrypt_caesar_5(self):
        self.assertEqual(decrypt_caesar("EfD", 4), "AbZ")    

if __name__ == "__main__":
	unittest.main()
