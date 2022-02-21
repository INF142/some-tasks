# Instantiate a TCP socket called sock and connect it to
# localhost on port 5552.

name = input("Name: ")
while command := input("> ").lower():
    if command == "read":
        sock.sendall(name.encode())
        print(sock.recv(4096).decode())
    elif command == "change name":
        name = input("Name: ")
    else:
        print("Invalid command")
