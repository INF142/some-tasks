from os import environ  # To be discussed in the group session
from socket import create_server, timeout
from threading import Lock, Thread


class RegistrationServer:

    def __init__(self, host, port):
        self._welcome_sock = create_server((host, port))
        self._welcome_sock.settimeout(5)
        self._passwords = {}
        self._connections = {}
        self._passwords_lock = Lock()
        self._connections_lock = Lock()
        self._BUFFER_SIZE = 2048

    def turn_on(self):
        self._serving = True
        Thread(target=self._accept).start()

    def shut_down(self):
        self._serving = False

    @property
    def connected_users(self):
        with self._connections_lock:
            return list(self._connections)

    @property
    def registered_users(self):
        with self._passwords_lock:
            return list(self._passwords)

    def _accept(self):
        while self._serving:
            try:
                conn, _ = self._welcome_sock.accept()
            except timeout:
                pass
            else:
                print("Accepting connection")
                Thread(target=self._welcome, args=(conn,)).start()

    def _welcome(self, conn):
        for _ in range(3):
            data = conn.recv(self._BUFFER_SIZE)
            user, password = data.decode().split(";")
            if self._register_or_log_in(conn, user, password):
                with self._connections_lock:
                    self._connections[user] = conn
                break
        else:
            conn.close()

    def _register_or_log_in(self, conn, user, password):
        with self._passwords_lock:
            if user in self._passwords and self._passwords[user] == password:
                print(f"User {user} is logged in.")
                conn.sendall("Logged in".encode())
                return True
            if user not in self._passwords:
                self._passwords[user] = password
                print(f"User {user} has signed in.")
                conn.sendall("Signed in".encode())
                return True
            else:
                conn.sendall("Invalid password".encode())
                return False


if __name__=="__main__":
    host = environ.get("HOST", "localhost")
    server = RegistrationServer(host, 5550)
    server.turn_on()
