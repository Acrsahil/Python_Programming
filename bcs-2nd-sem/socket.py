import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('', )
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for incoming connections...")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    
    try:
        print("Connection established with:", client_address)
        
        # Send data to the client
        message = "Hello, client! Welcome to the server."
        client_socket.sendall(message.encode())
        
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print("Received data from client:", data)
        
    finally:
        # Clean up the connection
        client_socket.close()
