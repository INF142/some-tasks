from socket import socket
from task2 import numerals, response


if __name__ == "__main__":
    # Instantiate a socket sock and listen on localhost port 12000
    while True:
      conn, _ = sock.accept()
      while True:
        request_message = conn.recv(1024)
        if not request_message:
          conn.close()
          break
        conn.sendall(response(request_message.decode()).encode())
