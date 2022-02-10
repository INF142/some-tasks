from socket import socket


def request_to_server(sock: socket, message: str) -> str:
    # Fill in here


def numeral(sock):
    # Fill in here


def language(sock):
    # Fill in here


if __name__ == "__main__":
    # Instantiate a socket sock and connect it to localhost on port 12000

    print("Available commands are:\n language\n numeral")
    print("Press Enter to exit")
    while (command := input("command> ").lower()):
        if command == "numeral":
            numeral(sock)
        elif command == "language":
            language(sock)
        else:
            print("Invalid command")
