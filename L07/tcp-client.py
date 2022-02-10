from socket import socket


sock = socket()
server_address = ("localhost", 5555)
sock.connect(server_address)
sentence = input("Input lowercase sentence: ")
sock.send(sentence.encode())
new_sentence = sock.recv(1024).decode()
print(f"From Server: {new_sentence}")
sock.close()
