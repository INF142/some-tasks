from socket import socket
from threading import Thread


def accept(sock):
  while True:
    conn, address = sock.accept() 
    print('accepted', conn, 'from', address)
    Thread(target=read, args=(conn,)).start()


def read(conn):
  while True:
    data = conn.recv(1024)  
    if data:
      sentence = data.decode()
      new_sentence = sentence.upper()
      conn.send(new_sentence.encode())
    else:
      print('closing', conn)
      conn.close()
      break


sock = socket()
sock.bind(("localhost", 5555))
sock.listen()
accept(sock)
