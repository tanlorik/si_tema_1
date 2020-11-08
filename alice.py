from common import *


def get_method():

    while True:
        x = input("Please choose an encryption method:\n1.CBC\n2.OFB\n>").lower()
        if x in ["1", "cbc"]:
            method = "cbc"
            return method
        elif x in ["2", "ofb"]:
            method = "ofb"
            return method
        else:
            print("Wrong, input, try again")
            continue


def get_key(method):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_KM)
    sock.connect(server_address)
    print("Connected to KM server")
    sock.sendall(method.encode("ascii"))
    print("Sending encryption method {}".format(method))
    enc_key = sock.recv(32).decode("ascii")
    if "ERROR" in enc_key:
        raise RuntimeError("Server did not recognize encryption method")
    print("Received key: {}.\nClosing connection.".format(enc_key))
    sock.close()
    key = my_bytes(enc_key) ^ K3
    print("Decrypting key to {}".format(str(key)))

    return enc_key, key


def call_bob():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_B)
    sock.connect(server_address)
    print("Connected to B")

    return sock


def main():

    method = get_method()
    enc_key, key = get_key(method)

    sock = call_bob()

    sock.sendall(method.encode("ascii"))
    print("Sending encryption method {}".format(method))
    sock.sendall(enc_key.encode("ascii"))
    print("Sending encrypted key")
    resp = sock.recv(3).decode("ascii")
    if resp == "ACK":
        print("B is ready for data transfer")

    content = open("file.in", "rb").read()

    if method == "cbc":
        data = ecrypt_cbc(content, key, IV)
    else:
        data = ecrypt_ofb(content, key, IV)

    data_len = "%016d" % len(data)

    print("Sending data length: {}".format(data_len))
    sock.sendall(data_len.encode("ascii"))
    print("Sending data file")
    sock.sendall(data)
    print("Closing connection!")
    sock.close()


if __name__ == "__main__":
    main()
