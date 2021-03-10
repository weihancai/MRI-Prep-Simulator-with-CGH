import pygatt
import time
from random import *
import logging
from binascii import hexlify
adapter = pygatt.GATTToolBackend()

#This function have to be called first to connect the watch
def SW_Connect():
    #adapter.stop()
    global device
    adapter.start()
    while True:  
        try:
            device = adapter.connect('78:02:B7:40:7C:FD', timeout=2 )
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


#This funciton calls and get the Blood Pressur value
def SW_Read_BloodPressure():
    global systolic
    global diastolic
    global BP_status
    BP_status =""
    systolic=0
    diastolic=0
    print('Start Read_BloodPressure')
    adapter.sendline('char-write-req 0x001d c711')
    def Read_BloodPressure(handle, value):
        """
        handle -- integer, characteristic read handle the data was received on
        value -- bytearray, the data returned in the notification
        """
        global reading
        reading=hexlify(value)
        length_of_reading=len(reading)
        print("___Raw BP value: "+str(reading)+"String length: "+str(length_of_reading))
        if length_of_reading==10:
            global systolic
            global diastolic
            global BP_status
            BP_status = int(hexlify(value)[4:6],16)
            systolic = int(hexlify(value)[6:8],16)
            diastolic = int(hexlify(value)[8:10],16)
            print("Blood Pressure:"+str(systolic)+"/"+str(diastolic)+"mmHg")
    device.subscribe('000033f2-0000-1000-8000-00805f9b34fb', callback=Read_BloodPressure)
    #time.sleep(16)
   
    while True:
        if (systolic!=0):
            print("data receive")
            BP_status="Blood Pressure Data Received Successfully"
            break
        elif (BP_status==255):
            print("Watch not worn Properly")
            BP_status="Watch not worn Properly"
            break
        
        else:
            print("Measuring blood pressure, please waite...")
            time.sleep(2)
   
    print("systolic, diastolic",systolic, diastolic)
    print("Finish Reading Blood Pressure")
    return BP_status, systolic, diastolic

#This funcitons call and gets the watch battery level
def SW_Read_BatteryLevel():
    global battery_level
    battery_level=None
    print('Read_Read_BatteryLevel')

    
    def Read_BatteryLevel(handle, value):
        global battery_level
        reading=hexlify(value)
        length_of_reading=len(reading)
        print("___Raw battery value: "+str(reading)+"String length: "+str(length_of_reading))
        Battery_Signal_Check = int(hexlify(value)[0:2],16)
        if(Battery_Signal_Check==162):
            battery_level = int(hexlify(value)[2:4],16)

    device.subscribe('000033f2-0000-1000-8000-00805f9b34fb', callback=Read_BatteryLevel)
    adapter.sendline('char-write-req 0x001d a242')

   
    while True:
        if (battery_level!=None):
            print("Battery level retrieved")
            break
        else:
            print("Retriving battery status...")
            time.sleep(5)
    print("Battery Level: "+str(battery_level)+"%")
    print("Finish reading battery status")
    return battery_level

#This functions vibrate the watch
def Vibrate_watch():
    print('<<<<Watch Vibrate>>>')
    adapter.sendline('char-write-req 0x001d ab00000001020701')

