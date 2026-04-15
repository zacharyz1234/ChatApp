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



client_username = input("Enter your username: ")


# Creates a client socket
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    # Connects the client socket to the server
    client_socket.connect((server_ip, server_port))
except KeyboardInterrupt:
    print("Could not connect to server. Ending session")
    exit

try:
    # Receives the server username first and sends
    # the client username so both ends have each
    # others' usernames
    server_username = client_socket.recv(2048).decode()
except KeyboardInterrupt:
    print("Connection lost. Ending Session...")
client_socket.send(client_username.encode())


print("Connection to server established. Send the first message: ")

while True:

    try:
        client_message = input(client_username + ": ")
    except KeyboardInterrupt:
        print("Connection lost. Ending session...")
        break


    if(client_message != 'end'):
        # Try/except loop to make sure the connection
        # hasn't been lost
        try:
            client_socket.send(client_message.encode())
        except KeyboardInterrupt:
            print("Connection lost. Ending session...")
            break

    else:

        try:
            client_socket.send(client_message.encode())
        except KeyboardInterrupt:
            print("Connection lost. Ending session...")
            # There's no need for a break in this block because it will
            # break anyways. This is just to let the user know
            # that the connection was lost
        break

    try:
        server_message = client_socket.recv(2048).decode()
    except KeyboardInterrupt:
        print("Connection lost. Ending session... ")
        break

    if(server_message == 'end'):
        print("Server ended session")
        break
    else:
        print(server_username + ': ' + server_message)

client_socket.close()

