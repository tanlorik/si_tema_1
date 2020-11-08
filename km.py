from common import *


def get_random_str():

    l = random.choice(range(16, 32))
    return "".join([random.choice(string.ascii_letters) for x in range(l)])


def init_km():

    k1 = my_bytes(hashlib.md5(get_random_str().encode("ascii")).hexdigest())
    k2 = my_bytes(hashlib.md5(get_random_str().encode("ascii")).hexdigest())

    return k1, k2


def main():

    K1, K2 = init_km()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_KM)
    print("Listening on port {}".format(port_KM))
    sock.bind(server_address)
    sock.listen(1)

    while True:

        data = None

        print("Waiting for new connection")
        connection, client_address = sock.accept()
        print("Received connection from {}".format(client_address))
        method = connection.recv(3).decode("ascii")
        print("Received method {}".format(method))
        if method == 'cbc':
            data = (K1 ^ K3).data.hex()
        elif method == 'ofb':
            data = (K1 ^ K3).data.hex()
        else:
            data = "ERROR" * 6 + "!!"

        connection.sendall(data.encode("ascii"))
        print("Sending encrypted key {} for {}.\nClosing connection.".format(
            data, method))
        connection.close()


if __name__ == "__main__":
    os.system("title Key Master")
    main()
