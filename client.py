import socket
client = socket.socket()
host = socket.gethostname()
port = 8080
client.connect((host,port))
print (client.recov(1024).decode())
client.close()
