import os
import sys
import random
import hashlib
import string
import socket


port_B = 54321
port_KM = 54322


class my_bytes:

    def __init__(self, hex):

        self.data = bytes.fromhex(hex)

    def __xor__(self, ba2):

        return my_bytes("".join(["%02X" % (_a ^ _b) for _a, _b in zip(self.data, ba2.data)]))

    def __str__(self):

        return self.data.hex()


def hex_fill(data, l=16):

    return data.hex() + "00" * (l - len(data))


def block_encrypt(data, key):

    return data ^ key


def ecrypt_cbc(data, key, iv):

    rez = bytes([])

    for i in range(0, len(data), 16):

        plaintext = my_bytes(hex_fill(data[i:i+16]))
        tmp = plaintext ^ iv
        iv = block_encrypt(tmp, key)

        rez += iv.data

    return rez


def decrypt_cbc(data, key, iv):

    rez = bytes([])

    for i in range(0, len(data), 16):

        cyphertext = my_bytes(hex_fill(data[i:i+16]))
        tmp1 = block_encrypt(cyphertext, key)
        tmp1 = tmp1 ^ iv
        iv = cyphertext

        rez += tmp1.data

    i = 0

    while rez[i-1] == 0:
        i -= 1

    if i < 0:
        return rez[:i]
    return rez


def ecrypt_ofb(data, key, iv):

    rez = bytes([])

    for i in range(0, len(data), 16):

        plaintext = my_bytes(hex_fill(data[i:i+16]))
        iv = block_encrypt(iv, key)
        tmp = plaintext ^ iv

        rez += tmp.data

    return rez


def decrypt_ofb(data, key, iv):

    rez = bytes([])

    for i in range(0, len(data), 16):

        plaintext = my_bytes(hex_fill(data[i:i+16]))
        iv = block_encrypt(iv, key)
        tmp = plaintext ^ iv

        rez += tmp.data

    i = 0

    while rez[i-1] == 0:
        i -= 1

    if i < 0:
        return rez[:i]

    return rez


K3 = my_bytes(hashlib.md5("cheia_mea".encode("ascii")).hexdigest())
IV = my_bytes(hashlib.md5(
    "vector_de_initializare".encode("ascii")).hexdigest())


def main():

    pass


if __name__ == "__main__":
    main()
