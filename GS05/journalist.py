# Instantiate a TCP socket called sock and connect it to
# localhost on port 5550.

name = input("Name: ")
while command := input("> ").lower():
    if command == "write":
        text = name + "| " + input(">> ")
        sock.sendall(text.encode())
        print("Status: ", sock.recv(128).decode())
    elif command == "change name":
        name = input("Name: ")
    else:
        print("Invalid command")
