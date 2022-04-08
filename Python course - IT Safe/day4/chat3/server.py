from socket import *
import threading


def worker(client):
    while True:
        data = client.recv(2048).decode()

        if data == "exit":
            client.close()
            clients.remove(client)
            break

        for item in clients:
            item.sendall(data.encode())


server = socket(AF_INET, SOCK_STREAM)
server.bind(("",3333))
server.listen(100)
clients = []

# we got a client
while True:
    client, addr = server.accept()
    clients.append(client)

    t = threading.Thread(target=worker,args=(client,))
    t.start()