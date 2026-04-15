import socket as s

server_ip = input("Enter an IP Address (Hit enter for localhost): ")
if(len(server_ip) == 0):
    server_ip = 'localhost'

# Infinite while loop that cycles until a valid server port is accepted
while True:
    try:
        server_port = input("Please enter a valid port number: ")
        if(server_port == ''):
            server_port = 8080
            break
        # Port is input as a string so code has to typecast to check if the
        # number is valid. Also checks to make sure the port number is between
        # all valid port numbers
        elif(int(server_port) > 0 and int(server_port) < 65535):
            # Convert server port number to an int since it is entered
            # as a string
            server_port = int(server_port)
            break
    except ValueError:
        print("That is not a valid port number.")



server_username = input("Enter your username: ")

#create server socket
server_socket = s.socket(s.AF_INET, s.SOCK_STREAM) #STREAM FOR TCP

#Bind server socket to IP and port
try:
    server_socket.bind((server_ip, server_port))
except OSError:
    print("Server binding failed. Ending program...")
    exit()

#Server is listening for incoming connections
server_socket.listen(1)

# Accepts the incoming client connection request
connection_socket, client_address = server_socket.accept()

# Send the server's username
try:
    connection_socket.send(server_username.encode())
except OSError:
    print("Connection lost. Ending session...")

try:
    client_username = connection_socket.recv(2048).decode()
except OSError:
    print("Connection lost. Ending session...")

print("Connection accepted. Awaiting message...\n")

while True:
    try:
        client_message = connection_socket.recv(2048).decode()
    except OSError:
        print("Connection lost. Ending session...")
        break

    if(client_message == 'end'):
        print("Client ended session.")
        break
    else:
        print(client_username + ': ' + client_message)

    server_message = input(server_username + ": ")
    # Client will have a similar if statement to
    # concatenate their username to the message
    # if it isn't the end statement
    if(server_message != 'end'):
        try:
            connection_socket.send(server_message.encode())
        except OSError:
            print("Connection lost. Ending session...")
    else:
        try:
            connection_socket.send(server_message.encode())
        except OSError:
            print("Connection lost. Ending session...")
        break

# Once the loop is broken the connection ends
connection_socket.close()
