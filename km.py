from common import *


def get_random_str():

    l = random.choice(range(16, 32))
    return "".join([random.choice(string.ascii_letters) for x in range(l)])


def init_km():

    k1 = my_bytes(hashlib.md5(get_random_str().encode("ascii")).hexdigest())
    k2 = my_bytes(hashlib.md5(get_random_str().encode("ascii")).hexdigest())

    return k1, k2


print(*init_km())
