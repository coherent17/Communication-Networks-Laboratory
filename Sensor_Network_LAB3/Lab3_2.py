# -*- coding: utf-8 -*-
from flask import Flask, request, Response, jsonify, make_response

from flask_restful import Api
from flask_restful import Resource

import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

class MyApp(Resource):
    def get(self):
        return Response(
            '''
            Welcome to my humidity&temperature RESTful API.
            Please make a HTTP POST request to this app, and you can
            decide to get the humidity or temperature data.
            The json embedded in the request woudl be:

            {
                "user" : "0811562",
                "data" : "H"
            }

            or

            {
                "user" : "0811562",
                "data" : "T"
            }
            '''
        )
    
    def post(self):
        json = request.get_json()

        if len(json) == 0:
            # 若使用者傳入的 Json 為空白的話，需回傳 HTTP Status Code = 400 的網頁內容
            # 此處會用到的 functions
            #    1. jsonify(message = ....)
            #    2. make_response(...., 400)

            ''' start of you code '''
            message = jsonify(message = 'Json empty!')
            response = make_response(message, 400)
            return response
            
            ''' end of you code '''
        
        ID = str(json['user'])
        data_type = json['data']


        # 從溫濕度模組取的數值
        # 此處會用到的 function
        #    1.  Adafruit_DHT.read_retry(...., ....)
 
        ''' start of you code '''
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        humidity = str(humidity)
        temperature = str(temperature)

        ''' end of you code '''
   
        # 從 json field "data" 中判斷使用者想要的是溫度還是濕度，還有例外判斷(else 的部分)
        # 此處會用到的 functions
        #    1. jsonify(message = ....)
        #    2. make_response(...., 200) or make_response(...., 400) (else 部分) 
        #
        
        if data_type == 'T':
            ''' start of you code '''
            response = jsonify(message ="Hi, 0811562 the current temperature is " + temperature + " °C")
            return response
            
            ''' end of you code '''
        
        elif data_type == 'H':
            ''' start of you code '''
            response = jsonify(message ="Hi, 0811562 the current humidity is " + humidity + " %")
            return response
            
            ''' end of you code '''
        
        else:
            ''' start of you code '''
            response = make_response(jsonify(message= 'Error'), 400)
            return response
            
            ''' end of you code '''

app = Flask(__name__)      
api = Api(app)

api.add_resource(MyApp, '/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9808, debug = True)