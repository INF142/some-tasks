from os import environ
from socket import create_server, timeout
from threading import Lock, Thread


class ChatServer:

    def __init__(self, host: str, port: int, buffer_size: int = 2048):
        self._host = host
        self._port = port
        self._buffer_size = buffer_size
        self._passwords = {}
        self._connections = {}
        self._passwords_lock = Lock()
        self._connections_lock = Lock()

    def turn_on(self):
        self._welcome_sock = create_server(
            (self._host, self._port),
            reuse_port=True
        )
        self._welcome_sock.settimeout(5)
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
                Thread(target=self._welcome, args=(conn,)).start()

    def _welcome(self, conn):
        if data := conn.recv(self._buffer_size):
            user, password = data.decode().split(";")
            if self._register_or_log_in(conn, user, password):
                with self._connections_lock:
                    self._connections[user] = conn
                self._handle_user(conn, user)
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
                conn.sendall("Signed up".encode())
                return True
            conn.sendall("Invalid password".encode())
            return False

    def _handle_user(self, conn, user):
        while self._serving:
            if message := conn.recv(self._buffer_size):
                self._send_from_user(user, message)
            else:
                break
        del self._connections[user]

    def _send_from_user(self, user, message):
        with self._connections_lock:
            for key in self._connections:
                if key != user:
                    try:
                        self._connections[key].sendall(
                            user.encode() + b"| " + message
                        )
                    except:
                        del self._connections[key]


if __name__ == "__main__":
    host = environ.get("HOST", "localhost")
    server = ChatServer(host, 5550)
    server.turn_on()
