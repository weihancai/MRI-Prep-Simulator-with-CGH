'''
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
name =get_ip_address()
print(name)
'''


import requests
import json


#def json_formater():

def post_request(Sensor_Data,API):
    
    #jsonData = '{ "name":"John", "age":30, "city":"New York"}'
    '''
    jsonData = '{ "sensor_type":"BloodPressure", "systolic":121, "diastolic":"71"}'
    jsonData = '{ "sensor_type":"Oximeter", "heart_rate":66, "blood_oxigen":"98"}'
    jsonData = '{ "sensor_type":"Pressure_mat", "age":30, "city":"New York"}'
    '''
    print(f'/n /n Received Sensor Data: {Sensor_Data}')
    print(f'API Set: {API}')
    
    IP_address="192.168.0.20"
    
    URL="http://"+IP_address+"/MRIData"+API
    print(f'Current URL:{URL}')
    systolic=100
    jsonData = json.loads(Sensor_Data)
    response = requests.post(URL, systolic)
    print(response.text)
    print (f"Printing API Response:{response}")
    print (f"Done...Printing API Response:{response.ok}/n")
    #print (response.content)
 

x='{"systolic":113,"diastolic":75}'
API="/api/BloodPressures"
post_request(x,API)


