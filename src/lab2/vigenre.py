def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    keyword = keyword.lower()
    ciphertext = ""
    for i, el in enumerate(plaintext):
        added_ch = ''
        if ord('a') <= ord(el) <= ord('z'):
            added_ch = chr(ord('a') + (ord(el) - ord('a') + ord(keyword[i % len(keyword)]) - ord('a')) % 26)
        elif ord('A') <= ord(el) <= ord('Z'):
            added_ch = chr(ord('A') + (ord(el) - ord('A') + ord(keyword[i % len(keyword)]) - ord('a')) % 26)
        else:
            added_ch = el
        ciphertext += added_ch
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    keyword = keyword.lower()
    plaintext = ""
    for i, el in enumerate(ciphertext):
        added_ch = ''
        if ord('a') <= ord(el) <= ord('z'):
            added_ch = chr(ord('a') + (ord(el) - ord('a') - (ord(keyword[i % len(keyword)]) - ord('a')) + 26) % 26)
        elif ord('A') <= ord(el) <= ord('Z'):
            added_ch = chr(ord('A') + (ord(el) - ord('A') - (ord(keyword[i % len(keyword)]) - ord('a')) + 26) % 26)
        else:
            added_ch = el
        plaintext += added_ch
    return plaintext


#print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))