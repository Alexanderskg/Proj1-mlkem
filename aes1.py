from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import socket
import os

def generate_key():
    return os.urandom(32)  # 256-bit key

def generate_iv():
    return os.urandom(16)  # 128-bit IV

def encrypt(data, key, iv):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

data = b"Mensaje secreto"

key = generate_key()
iv = generate_iv()

encrypted_data = encrypt(data, key, iv)

print(data)
print(encrypted_data)

with socket.create_connection(('192.168.122.14', 65432)) as sock:  # IP de PC2
    sock.sendall(key + iv + encrypted_data)
    print("Datos enviados a PC2")