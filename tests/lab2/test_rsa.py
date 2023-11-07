import unittest

from src.lab2.rsa import *

class CalculatorTestCase(unittest.TestCase):
    def test_is_prime(self):
         self.assertEqual(is_prime(2), True)
         self.assertEqual(is_prime(11), True)
         self.assertEqual(is_prime(8), False)   
    def test_gcd(self):
         self.assertEqual(gcd(12, 15), 3)
         self.assertEqual(gcd(3, 7), 1)
    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
    def test_general(self):
        p = 17
        q = 19
        public, private = generate_keypair(p, q)
        message = "Hellow word!"
        encrypted_msg = encrypt(private, message)
        self.assertEqual(decrypt(public, encrypted_msg), message)

         
if __name__ == "__main__":
	unittest.main()
