# -*- coding: utf-8 -*-
import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.bind("tcp://*:7788")

# wait for all workers connected
time.sleep(1)

for i in range(9):
    a = str(random.randint(0, 100))
    b = str(random.randint(0, 100))
    
    # Send integer list = [a, b] to servers
    socket.send_multipart([a, b])

    # receive results from servers
    result=socket.recv()
    print("compute " + a + " + " + b +"\n = " + result)