import pygatt
import time
from random import *
import logging
from binascii import hexlify
adapter = pygatt.GATTToolBackend()


def SW_Connect():
    #adapter.stop()
    global device
    adapter.start()
    while True:  
        try:
            device = adapter.connect('BA:03:8C:75:64:22', timeout=2, )
            #device.subscribe('6e400003-b5a3-f393-e0a9-e50e24dcca9d', callback=SW_Read_BloodPressure)
            #device.subscribe('00002a19-0000-1000-8000-00805f9b34fb', callback=SW_Read_BatteryLevel)
            break
        except pygatt.exceptions.NotConnectedError:
            SW_ConnectStatus= "disconnected"
            print('Connecting...')
    print("Smart Watch connected!")
    SW_ConnectStatus= "connected"
    for x in range(1):
        Vibrate_watch()
        time.sleep(1.5)
       
    return SW_ConnectStatus
    #adapter.sendline('char-write-req 0x0020 cd0006120118000101')
    #adapter.sendline('char-read-hnd 1b')

    #time.sleep(30)
    #print ("Print to check",systolic, diastolic)
   
    #adapter.stop()
   
def SW_Read_BloodPressure():
    global systolic
    global diastolic
    systolic=None
    diastolic=None
    print('Start Read_BloodPressure')
    adapter.sendline('char-write-req 0x0020 cd0006120118000101')
    def Read_BloodPressure(handle, value):
        """
        handle -- integer, characteristic read handle the data was received on
        value -- bytearray, the data returned in the notification
        """
        reading=hexlify(value)
        length_of_reading=len(reading)
        print("___Raw BP value: "+str(reading)+"String length: "+str(length_of_reading))
        if length_of_reading==40:
            global systolic
            global diastolic
            systolic = int(hexlify(value)[36:38],16)
            diastolic = int(hexlify(value)[34:36],16)
            heart_rate=int(hexlify(value)[36:38],16)
            Oxigen_Level=int(hexlify(value)[32:34],16)
            print("Heart Rate: "+str(heart_rate)+ " BPM")
            print("Oxigen Level: "+str(Oxigen_Level)+" Spo2")
            print("Blood Pressure:"+str(systolic)+"/"+str(diastolic)+"mmHg")
    device.subscribe('6e400003-b5a3-f393-e0a9-e50e24dcca9d', callback=Read_BloodPressure)
    #time.sleep(16)
       
    while True:
        if (systolic!=None):
            print("data receive")
            break
        else:
            print("Measuring blood pressure, please waite...")
            time.sleep(2)
   
    print("systolic, diastolic",systolic, diastolic)
    print("Finish Reading Blood Pressure")
    return systolic, diastolic
       
def SW_Read_BatteryLevel():
    global battery_level
    battery_level=None
    print('Read_Read_BatteryLevel')
    adapter.sendline('char-write-req 0x001c 0100')
    def Read_BatteryLevel(handle, value):
        global battery_level
        reading=hexlify(value)
        length_of_reading=len(reading)
        print("___Raw battery value: "+str(reading)+"String length: "+str(length_of_reading))
        battery_level = int(hexlify(value)[0:2],16)
        #print("Battery Level:"+str(battery_level)+"%")
    device.subscribe('00002a19-0000-1000-8000-00805f9b34fb', callback=Read_BatteryLevel)
   
    while True:
        if (battery_level!=None):
            print("Battery level retrieved")
            break
        else:
            print("Retriving battery status...")
            time.sleep(1)
    print("Battery Level: "+str(battery_level)+"%")
    print("Finish reading battery status")
    return battery_level

def Vibrate_watch():
    print('<<<<Watch Vibrate>>>')
    adapter.sendline('char-write-req 0x0020 cd000612010b000101')
 
 

#SW_Connect()
#SW_Read_BloodPressure()
#SW_Read_BatteryLevel()
#adapter.stop()

