import os
import sys 
import random
import Crypto
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from constants import TextColors
from decimal import Decimal
from RSA.rsa_math import RSAmath

class _RSA():
    def __init__(self, m, key_size=1024):
        self.key_size = key_size
        self.rsa_math = RSAmath()
        self.keys_generator(m)
        self.step_bytes = self.key_size // 8 - 1

    def keys_generator(self, m):
        self.public_key = []
        n = 0
        while m > n:
            p, q = self.rsa_math.generate_pq(self.key_size)
            n = p * q

        phi = (p - 1) * (q - 1)
        for e in range(2, phi):
            if self.rsa_math.greatest_common_divisor(e, phi) == 1:
                break

        self.public_key.append(e)
        self.public_key.append(n)
        d = self.rsa_math.modular_inverse(e, phi)
        self.private_key = int(d)

    def encryption_ecb(self, data_to_encrypt):
        encrypted_data = []

        for i in range(0, len(data_to_encrypt), self.step_bytes):
            raw_bytes = bytearray(data_to_encrypt[i:i+self.step_bytes])

            encrypted_int = pow(int.from_bytes(raw_bytes, 'big'), self.public_key[0], self.public_key[1])
            encrypted_bytes = encrypted_int.to_bytes(self.step_bytes+1, 'big')
                
            for j in range(0, len(raw_bytes)):
                if j < len(raw_bytes)-1:
                    encrypted_data.append(encrypted_bytes[j])
                else:
                    encrypted_data.append(int.from_bytes(encrypted_bytes[j:], 'big'))

        return encrypted_data

    def decryption_ecb(self, encrypted_data):
        decrypted_data = []

        for i in range(0, len(encrypted_data), self.step_bytes):
            if i % 12700 == 0:
                os.system('clear')
                print(TextColors.OKGREEN + "Decrypting...".ljust(i//25000, '#') + TextColors.ENDC)

            encrypted_hex = encrypted_data[i:i+self.step_bytes]
            encrypted_bytes = b''

            for j in range(0, len(encrypted_hex)):
                if j < len(encrypted_hex)-1:
                    encrypted_bytes += encrypted_hex[j].to_bytes(1, 'big')
                else:
                    encrypted_bytes += encrypted_hex[j].to_bytes(self.step_bytes-len(encrypted_hex)+2, 'big')
            
            int_from_bytes = int.from_bytes(encrypted_bytes, 'big')
            decrypted_int = pow(int_from_bytes, self.private_key, self.public_key[1])
            decrypted_bytes = decrypted_int.to_bytes(len(encrypted_hex), 'big')
            
            for byte in decrypted_bytes:
                decrypted_data.append(byte)
        
        return decrypted_data

    def encryption_cbc(self, data_to_encrypt):
        encrypted_data = []

        self.cbc_vector = random.getrandbits(self.key_size)
        prev_xor = self.cbc_vector

        for i in range(0, len(data_to_encrypt), self.step_bytes):
            raw_bytes = bytearray(data_to_encrypt[i:i+self.step_bytes])

            prev_xor = prev_xor.to_bytes(self.step_bytes+1, 'big')
            prev_xor = int.from_bytes(prev_xor[:len(raw_bytes)], 'big')
            xored_int = int.from_bytes(raw_bytes, 'big') ^ prev_xor

            encrypted_int = pow(xored_int, self.public_key[0], self.public_key[1])
            prev_xor = encrypted_int
            encrypted_bytes = encrypted_int.to_bytes(self.step_bytes+1, 'big')

            for j in range(0, len(raw_bytes)):
                if j < len(raw_bytes)-1:
                    encrypted_data.append(encrypted_bytes[j])
                else:
                    encrypted_data.append(int.from_bytes(encrypted_bytes[j:], 'big'))

        return encrypted_data
   
    def decryption_cbc(self, encrypted_data):
        decrypted_data = []
        prev_xor = self.cbc_vector

        for i in range(0, len(encrypted_data), self.step_bytes):
            if i % 12700 == 0:
                os.system('clear')
                print(TextColors.OKGREEN + "Decrypting...".ljust(i//25000, '#') + TextColors.ENDC)

            encrypted_hex = encrypted_data[i:i+self.step_bytes]
            encrypted_bytes = b''

            for j in range(0, len(encrypted_hex)):
                if j < len(encrypted_hex)-1:
                    encrypted_bytes += encrypted_hex[j].to_bytes(1, 'big')
                else:
                    encrypted_bytes += encrypted_hex[j].to_bytes(self.step_bytes-len(encrypted_hex)+2, 'big')

            decrypted_int = pow(int.from_bytes(encrypted_bytes, 'big'), self.private_key, self.public_key[1])
            
            prev_xor = prev_xor.to_bytes(self.step_bytes+1, 'big')
            prev_xor = int.from_bytes(prev_xor[:len(encrypted_hex)], 'big')
            xored_int = prev_xor ^ decrypted_int

            decrypted_bytes = xored_int.to_bytes(len(encrypted_hex), 'big')
            prev_xor = int.from_bytes(encrypted_bytes, 'big')

            for byte in decrypted_bytes:
                decrypted_data.append(byte)

        return decrypted_data

    def encryption_library(self, data_to_encrypt):
        encrypted_data = []
        key = RSA.construct((self.public_key[1] , self.public_key[0]))
        cipher = PKCS1_OAEP.new(key)  

        for i in range(0, len(data_to_encrypt), 63):
            if i % 6300 == 0:
                os.system('clear')
                print(TextColors.OKGREEN + "Encrypting...".ljust(i//25000, '#') + TextColors.ENDC)
            
            raw_bytes = bytearray(data_to_encrypt[i:i+63])
            encrypted_bytes = cipher.encrypt(raw_bytes)
                
            for j in range(0, len(raw_bytes)):
                if j < len(raw_bytes)-1:
                    encrypted_data.append(encrypted_bytes[j])
                else:
                    encrypted_data.append(int.from_bytes(encrypted_bytes[j:], 'big'))

        return encrypted_data
        