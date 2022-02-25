from getpass import getpass
from os import environ  # To be discussed in the group session
from queue import Queue
from socket import create_connection, timeout
from threading import Thread


class ChatClient:

    def __init__(self, server: str, buffer_size: int = 2048) -> None:
        self._server = server
        self._buffer_size = buffer_size
        self._messages = Queue()

    def start(self):
        if self._register():
            self._chatting = True
            Thread(target=self._recv).start()
            self._chat()

    def _chat(self):
        while (message := input("> ")).lower() != ".exit":
            if message:
                self._sock.sendall(message.encode())
            while not self._messages.empty():
                print(self._messages.get())
        self._chatting = False
        self._sock.close()

    def _register(self) -> bool:
        print("Registering...")
        while user := input("User: "):
            password = getpass()
            message = user+";"+password
            self._sock = create_connection((self._server, 5550), timeout=5)
            self._sock.sendall(message.encode())
            response = self._sock.recv(self._buffer_size).decode()
            print(response)
            if response != "Invalid password":
                return True
        return False

    def _recv(self):
        while self._chatting:
            try:
                data = self._sock.recv(2048)
            except timeout:
                pass
            except:
                break
            else:
                if data:
                    self._messages.put(data.decode())
                else:
                    break


if __name__ == "__main__":
    server = environ.get("SERVER", "localhost")
    client = ChatClient(server)
    client.start()
