import socket

# Socket IP and port global variables
server_host = "127.0.0.1"
server_port = 443

# Authentication loop
while True:
    password = input("Input password: ")

    # Creating socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to auth server
    server.connect((server_host, server_port))
    print("Connecting to server ...")
        
    # Receiving and printing response from server
    server.send(password.encode())
    response = server.recv(64).decode()
    print(response, "\n")
        
    server.close()
