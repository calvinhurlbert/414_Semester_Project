import socket

# Socket IP and port global variables
server_host = "127.0.0.1"
server_port = 443

# Setting up socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(1)
print ("Socket created\n")

# Function to authenticate the password
def authenticate(password):
	valid_passwords = ["testpass", "password123"]
	return True if password in valid_passwords else False

# Server loop
while True:
	# Waiting for client connection
	print("Waiting for client ...")
	client, addr = server.accept()
	print("Client connected from: ", addr)

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
