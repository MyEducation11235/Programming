import unittest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class CalculatorTestCase(unittest.TestCase):
    def test_encrypt_vigenere_1(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
    def test_encrypt_vigenere_2(self):
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')
    def test_encrypt_vigenere_3(self):
        self.assertEqual(encrypt_vigenere("Python3.6", 'd'), 'Sbwkrq3.6')
    def test_encrypt_vigenere_4(self):
        self.assertEqual(encrypt_vigenere(""), "")
    def test_encrypt_vigenere_5(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", 'LEMON'), "LXFOPVEFRNHR")     

    def test_decrypt_vigenere_1(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
    def test_decrypt_vigenere_2(self):
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
    def test_decrypt_vigenere_3(self):
        self.assertEqual(decrypt_vigenere('Sbwkrq3.6', 'D'), "Python3.6")
    def test_decrypt_vigenere_4(self):
        self.assertEqual(decrypt_vigenere(""), "")
    def test_decrypt_vigenere_5(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")    

if __name__ == "__main__":
	unittest.main()
