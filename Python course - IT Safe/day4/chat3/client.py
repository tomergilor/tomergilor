from socket import *
import threading


def reader(client):
    while True:
        data = client.recv(2048).decode()
        print ("Server: {0}".format(data))


client = socket(AF_INET, SOCK_STREAM)
client.connect(("10.100.102.13",3333))

t = threading.Thread(target=reader, args=(client,))
t.start()

while True:
    data = input("Client: ")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break