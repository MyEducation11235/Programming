import unittest
import random
import string

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class MyTestCase(unittest.TestCase):
    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))



if __name__ == '__main__':
    unittest.main()
