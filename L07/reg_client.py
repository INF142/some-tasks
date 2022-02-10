from getpass import getpass
from os import environ  # To be discussed in the group session
from socket import create_connection

server = environ.get("SERVER", "localhost")
sock = create_connection((server, 5550))

for _ in range(3):
    user = input("User: ")
    password = getpass()
    message = user+";"+password
    sock.sendall(message.encode())
    response = sock.recv(2048).decode()
    print(response)
    if response != "Invalid password":
        break
