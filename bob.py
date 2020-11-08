from common import *


def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port_B)
    print("Listening on port {}".format(port_B))
    sock.bind(server_address)
    sock.listen(1)

    while True:

        data = None

        print("Waiting for new connection")
        connection, client_address = sock.accept()
        print("Received connection from {}".format(client_address))
        method = connection.recv(3).decode("ascii")
        print("Received method {}".format(method))

        key = connection.recv(32).decode("ascii")
        print("Received key: {}.".format(key))
        key = my_bytes(key) ^ K3
        print("Decrypting key to {}".format(str(key)))

        print("Sending ACK to begin data transfer")
        connection.sendall("ACK".encode("ascii"))
        data_len = int(connection.recv(16).decode("ascii"))
        print("Got contenth length: {}".format(data_len))
        data = connection.recv(data_len)
        print("Received encrypted file.\n Closing connection!")

        connection.close()

        print("Decrypting file")
        if method == "cbc":
            content = decrypt_cbc(data, key, IV)
        else:
            content = decrypt_ofb(data, key, IV)

        print("Writing file to disk")
        with open("file.out", 'wb') as f:
            f.write(content)


if __name__ == "__main__":
    os.system("title BoB")
    main()
