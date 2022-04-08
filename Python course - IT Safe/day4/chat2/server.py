from socket import *
import threading


def worker(client):
    while True:
        data = client.recv(2048).decode()

        if data == "exit":
            client.close()
            break

        print("Client: {0}".format(data))
        data = input("Client: ")
        client.sendall(data.encode())


server = socket(AF_INET, SOCK_STREAM)
server.bind(("",3333))
server.listen(100)

# we got a client
while True:
    client, addr = server.accept()
    t = threading.Thread(target=worker,args=(client,))
    t.start()