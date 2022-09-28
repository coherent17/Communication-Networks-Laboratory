import bluetooth

bd_addr="DC:A6:32:22:2C:B3"

port = 2

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()