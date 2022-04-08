from socket import *


class serverSocket(object):
    def __init__(self, address, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((address, port))
        self.server.listen(100)
        self.is_closed = False

    def accept(self):
        self.client, addr = self.server.accept()

    def __call__(self, *args, **kwargs):

        self.client.sendall("Welcome".encode())
        while True:
            data = self.client.recv(2048).decode()
            print (data)
            if data == "exit":
                self.client.close()
                self.server.close()
                self.is_closed = True
                break

            data = input("[+] Server: ")
            self.client.sendall(data.encode())

srv = serverSocket("", 1337)
srv.accept()
srv()

