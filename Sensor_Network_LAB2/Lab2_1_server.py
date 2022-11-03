# -*- coding: utf-8 -*-
import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7788")

print('Worker %s is running ...' % os.getpid())
worker=os.getpid()
while True:
    # Receive [a, b] from the client
    data = socket.recv_multipart()
    print("compute " + data[0] + " + " + data[1]+" and send response")
    result = str(int(data[0])+int(data[1]))
    result = result +" (from worker " +str(worker)+ " )"

    # Return the result back to the client
    socket.send_string(result)