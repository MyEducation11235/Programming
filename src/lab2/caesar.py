def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for el in plaintext:
        added_ch = ''
        if ord('a') <= ord(el) <= ord('z'):
            added_ch = chr(ord('a') + (ord(el) - ord('a') + shift) % 26)
        elif ord('A') <= ord(el) <= ord('Z'):
            added_ch = chr(ord('A') + (ord(el) - ord('A') + shift) % 26)
        else:
            added_ch = el
        ciphertext += added_ch
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for el in ciphertext:
        added_ch = ''
        if ord('a') <= ord(el) <= ord('z'):
            added_ch = chr(ord('a') + (ord(el) - ord('a') - shift + 26) % 26)
        elif ord('A') <= ord(el) <= ord('Z'):
            added_ch = chr(ord('A') + (ord(el) - ord('A') - shift + 26) % 26)
        else:
            added_ch = el
        plaintext += added_ch
    return plaintext

#print(encrypt_caesar('AbZ', 4))
