import socket
server = socket.socket()
host = socket.gethostname()
port = 8080
server.bind(host,port))
server.listen(5)
while true:
  conn,addr = server.accept()
  print("connection successful from:",addr)
  conn.send(bytes("hii",'utf-8'))
  conn.close
