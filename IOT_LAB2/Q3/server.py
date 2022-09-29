import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=2
server_sock.bind(("DC:A6:32:22:2C:B3", port))
server_sock.listen(1)
client_sock,address=server_sock.accept()
print "Accepted connection from ", address

data = client_sock.recv(1024)
print "receiverd [%s]" % data

client_sock.close()
server_sock.close()