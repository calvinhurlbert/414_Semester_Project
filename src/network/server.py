import socket

# Socket IP and port global variables
server_host = "127.0.0.1"
server_port = 414

# Setting up socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_host, server_port))
server.listen(1)
print ("Socket created\n")

# Function to authenticate the password
def authenticate(password):
	valid_passwords = ["testpass", "password123"]
	return True if password in valid_passwords else False

connection_limit = 10
current_connections = 0

# Server loop
while True:
	if current_connections >= connection_limit:
		continue

	# Waiting for client connection
	print("Waiting for client ...")
	client, addr = server.accept()
	print("Client connected from: ", addr)
	current_connections += 1

	# Receiving password
	password = client.recv(64).decode()
	print("Password received: ", password)

	# Authenticating password
	verified = authenticate(password)
	response = "Password verified" if verified else "Password not valid"

	# Sending output back to client
	client.send(response.encode())
	print("Response sent\n")

	# Closing connection to client
	client.close()
	current_connections -= 1
