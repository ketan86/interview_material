"""Bitwise XOR operator is one of the magical operators in c. It has a
special property that if C = A ^ B, one can get A by XORing C with B
and B by XORing B with C.
"""
SECRET = 1990


def encrypt(text):
    encrypted_string = ''
    for char in text:
        encrypted_string += chr(ord(char) ^ SECRET)
    return encrypted_string


def decrypt(text):
    decrypted_string = ''
    for char in text:
        decrypted_string += chr(ord(char) ^ SECRET)
    return decrypted_string


encrypted = encrypt('I love leetcode')
print(encrypted)
decrypted = decrypt(encrypted)
print(decrypted)
