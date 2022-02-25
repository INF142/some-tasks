from os import environ
from selectors import EVENT_READ, DefaultSelector
from socket import create_server


class ChatServerSel:

    def __init__(self, host, port, buffer_size = 2048):
        self._passwords = {}
        self._connections = {}
        self._messages = []
        self._buffer_size = buffer_size
        self._selector = DefaultSelector()
        self._welcome_sock = create_server((host, port))
        self._welcome_sock.setblocking(False)
        self._selector.register(self._welcome_sock, EVENT_READ)
        self._run()

    def _run(self):
        while True:
            sel = self._selector.select()
            for key, _ in sel:
                if sock_handler := key.data:
                    sock_handler(key.fileobj)
                else:
                    self._accept()
            self._send_messages()

    def _accept(self):
        conn, _ = self._welcome_sock.accept()
        conn.setblocking(False)
        self._selector.register(conn, EVENT_READ, self._welcome)

    def _welcome(self, conn):
        if data := conn.recv(self._buffer_size):
            user, password = data.decode().split(";")
            if self._register_or_log_in(conn, user, password):
                self._connections[user] = conn
                self._selector.modify(
                    conn,
                    EVENT_READ,
                    lambda conn: self._handle_user(conn, user)
                )
        else:
            self._selector.unregister(conn)
            conn.close()

    def _register_or_log_in(self, conn, user, password):
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
        if message := conn.recv(self._buffer_size):
            self._messages.append((user, message))
        else:
            del self._connections[user]
            self._selector.unregister(conn)
            conn.close()

    def _send_messages(self):
        for user, message in self._messages:
            for key in self._connections:
                if key != user:
                    conn = self._connections[key]
                    try:
                        conn.sendall(user.encode() + b"| " + message)
                    except:
                        del self._connections[key]
                        self._selector.unregister(conn)
                        conn.close()
        self._messages = []


if __name__ == "__main__":
    host = environ.get("HOST", "localhost")
    server = ChatServerSel(host, 5550)
    server.turn_on()
