import pygatt
import time
from random import *
import logging
from binascii import hexlify
adapter = pygatt.GATTToolBackend()



def SW_bloodPressure():
    
    adapter.start()
    def noti(handle, value):
        
        global systolic
        global diastolic
        global con_status  
        """
        handle -- integer, characteristic read handle the data was received on
        value -- bytearray, the data returned in the notification
        """
        reading=hexlify(value)
        length_of_reading=len(reading)
        print("read value: "+str(reading)+"String length: "+str(length_of_reading))
        if length_of_reading==40:
            systolic = int(hexlify(value)[36:38],16)
            diastolic = int(hexlify(value)[34:36],16)
            heart_rate=int(hexlify(value)[36:38],16)
            Oxigen_Level=int(hexlify(value)[32:34],16)
            print("Heart Rate: "+str(heart_rate)+ " BPM")
            print("Oxigen Level: "+str(Oxigen_Level)+" Spo2")
            print("Blood Pressure:"+str(systolic)+"/"+str(diastolic)+"mmHg")
       
    while True:  
        try:
            device = adapter.connect('BA:03:8C:75:64:22', timeout=2, )
            device.subscribe('6e400003-b5a3-f393-e0a9-e50e24dcca9d', callback=noti)
            break
        except pygatt.exceptions.NotConnectedError:
            print('Waiting...')


    adapter.sendline('char-write-req 0x0020 cd0006120118000101')

    time.sleep(16)

    adapter.stop()
    print('Done')
    print ("Print to check",systolic, diastolic)
    return systolic, diastolic
#dia,sys=SW_bloodPressure()
