from socket import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 4444))
server.listen(10)
print ("Server started")


client, addr = server.accept()
while True:
    data = client.recv(2048).decode()
    print("Client: {0}".format(data))

    if data == "exit":
        client.close()
        break

    data = input("Server: ")
    client.sendall(data.encode())

server.close()
