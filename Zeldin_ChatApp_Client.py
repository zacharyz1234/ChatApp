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

#Creates a client socket
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

#Connects the client socket to the server
client_socket.connect((server_ip, server_port))
server_username = client_socket.recv(2048).decode()
client_socket.send(client_username.encode())
print("Connection accepted. Send the first message: ")

while True:

    client_message = input()

    if(client_message != 'end'):
        client_message = client_username + ': ' + client_message
        print(client_message)
        client_socket.send(client_message.encode())
    else:
        print(client_message)


    server_message = client_socket.recv(2048).decode()
    print(server_message)

