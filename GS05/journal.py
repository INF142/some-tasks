from selectors import EVENT_READ, DefaultSelector
from socket import create_server, socket
from typing import Callable

# Masks for labeling sockets registered in a selector.
# They stand for accept journalist, serve journalist,
# accept reader and serve reader, respectively.
ACC_JOUR, SER_JOUR, ACC_READ, SER_READ = range(4)

# Note that the server does not need to store the
# decoded news. Hence, in order to optimize the app
# the news are stored in bytes. An analogous reasoning
# follows for the forthcoming functions
# write_on_journal and read_journal.

# List containing the news
journal: list[bytes] = []

# Selector object
sel = DefaultSelector()


def write_on_journal(data: bytes) -> bytes:
    """Add raw data to the journal.
    Return b'OK'."""
    pass  # Task 2


def read_journal(name: bytes) -> bytes:
    """Return a message in bytes, which
    greets the readers and gather the news
    in the journal."""
    pass  # Task 3


def serve(conn: socket, response: Callable[[bytes], bytes]) -> None:
    """Handle a registered socket using
    the response function."""
    if data := conn.recv(256):
        pass  # Task 4. Send response(data).
    else:
        pass  # Task 4. Unregister the socket and close it. Why is this necessary?


def accept(welcome_sock: socket, mask: int) -> None:
    """Accept an incoming connection through a
    welcoming socket and register it in sel passing
    mask as data."""
    pass  # Task 5
    # conn, _ =
    # conn.setblocking(...)
    # sel.register(...)


def add_server(address: tuple[str, int], mask: int) -> None:
    """Create a welcoming socket listening on address and
    register it in sel passing mask as data."""
    pass  # Task 6
    # sock =
    # sock.setblocking(...)
    # Listen
    # sel.register(...)


# Add a welcoming socket for journalists
add_server(("localhost", 5550), ACC_JOUR)

# Add a welcoming socket for readers
add_server(("localhost", 5552), ACC_READ)

# Dictionary that maps masks to the corresponding
# method. Each method takes a socket as an argument.
mask_to_method = {
    ACC_JOUR: lambda sock: accept(sock, SER_JOUR),
    ACC_READ: lambda sock: accept(sock, SER_READ),
    SER_JOUR: lambda sock: serve(sock, write_on_journal),
    SER_READ: lambda sock: serve(sock, read_journal)
}

while True:
    # Select the events corresponding to sockets
    # that are ready to be read.
    events = sel.select(10)

    for key, _ in events:
        # Call the method corresponding to the mask,
        # given in key.data, with the corresponding
        # socket, which is identified by key.fileobj.
        mask_to_method[key.data](key.fileobj)
