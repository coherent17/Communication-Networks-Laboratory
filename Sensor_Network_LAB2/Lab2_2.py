# -*- coding: utf-8 -*-
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.0.114:5556")


# Subscribe to two topics, humidity and temp
topicfilter1 = "humidity"
topicfilter2 = "temp"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter1)
socket.setsockopt(zmq.SUBSCRIBE, topicfilter2)

print("Start!!\n")

temp_sum = 0
humid_sum = 0

for i in range(10):
    # get temperature data
    mes = socket.recv()
    print(mes)
    splitted_str = mes.split()
    temp_sum += int(splitted_str[2])

    #get humid data
    mes = socket.recv()
    print(mes)
    splitted_str = mes.split()
    humid_sum += int(splitted_str[2])

# Compute average value
print("avg temperature: {}".format(temp_sum / 10.0))
print("avg humidity: {}".format(humid_sum / 10.0))