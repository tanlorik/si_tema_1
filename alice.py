from common import *

_DEBUG_ = True

if _DEBUG_:

    K1 = my_bytes(hashlib.md5("test1".encode("ascii")).hexdigest())
    K2 = my_bytes(hashlib.md5("test2".encode("ascii")).hexdigest())
    content = bytes(
        "The slow brown fox jumps over the lazy dog!".encode("ascii"))

enc = ecrypt_cbc(content, K1, IV)
dec = decrypt_cbc(enc, K1, IV)
print(dec)
print(decrypt_ofb(ecrypt_ofb(content, K2, IV), K2, IV))
