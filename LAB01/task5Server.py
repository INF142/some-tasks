from selectors import DefaultSelector, EVENT_READ
from socket import socket

from task2 import numerals, response


def accept(sock):
    conn, address = sock.accept()  # Should be ready
    print('accepted', conn, 'from', address)
    conn.setblocking(False)
    sel.register(conn, EVENT_READ)


def read(conn):
    # Fill in here


sel = DefaultSelector()
sock = socket()
sock.bind(("localhost", 12000))
sock.listen()
sock.setblocking(False)
sel.register(sock, EVENT_READ, True)

while True:
    events = sel.select()
    for key, _ in events:
        if key.data:
            accept(key.fileobj)
        else:
            read(key.fileobj)
