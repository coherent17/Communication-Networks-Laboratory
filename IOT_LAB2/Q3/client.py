import bluetooth

bd_addr="DC:A6:32:11:A3:66"

port = 2

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("client_0811562 & server 109700035")

sock.close()