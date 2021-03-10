import random
import matplotlib.pyplot as plt
import datetime
import time
import os
from time import strftime
from matplotlib.animation import FuncAnimation
import numpy as np
import requests, json
import spidev
import time

head="Head moved"
body="Body moved"
leg="Leg moved"


ch00 = 0;ch01 = 1; ch02 = 2; ch03 = 3; ch04 = 4; ch05 = 5;ch06= 6;  ch07 = 7
ch10 = 0; ch11 = 1; ch12 = 2; ch13 = 3; ch14 = 4; ch15 = 5; ch16= 6;  ch17 = 7

#Create SPI
spi = spidev.SpiDev()
#spi.open(0, 0)

def readadc1(adcnum1):
        # read SPI data from the MCP3008, 8 channels in total
        spi.open(0, 0)
        spi.max_speed_hz = 1000
        if adcnum1 > 7 or adcnum1 < 0:
                return -1
        r = spi.xfer2([1, 8 + adcnum1 << 4, 0])
       
        data1 = ((r[1] & 3) << 8) + r[2]
       
        spi.close()
        return data1
   
   

def readadc2(adcnum2):
        # read SPI data from the MCP3008, 8 channels in total
        spi.open(0, 1)
        spi.max_speed_hz = 1000
        if adcnum2 > 7 or adcnum2 < 0:
                return -1
        r = spi.xfer2([1, 8 + adcnum2 << 4, 0])
        data2 = ((r[1] & 3) << 8) + r[2]
       
        spi.close()
        return data2
   
   
def readPressure():
   
        pad_value1 = readadc1(ch00)
        pad_value2 = readadc1(ch01)
        pad_value3 = readadc1(ch02)
        pad_value4 = readadc1(ch03)
        pad_value5 = readadc1(ch04)
        pad_value6 = readadc1(ch05)
        pad_value7 = readadc1(ch06)
        pad_value8 = readadc1(ch07)
        pad2_value1 = readadc2(ch10)
        pad2_value2 = readadc2(ch11)
        pad2_value3 = readadc2(ch12)
        pad2_value4 = readadc2(ch13)
        pad2_value5 = readadc2(ch14)
        pad2_value6 = readadc2(ch15)
        pad2_value7 = readadc2(ch16)
        pad2_value8 = readadc2(ch17)
        return pad_value1, pad_value2, pad_value3, pad_value4, pad_value5, pad_value6, pad_value7, pad_value8, pad2_value1, pad2_value2, pad2_value3, pad2_value4, pad2_value5, pad2_value6, pad2_value7, pad2_value8
       
#         print("Pressure Pad Value: %d" %  pad_value1, pad_value2, pad_value3, pad_value4, pad_value5, pad_value6, pad_value7, pad_value8, pad2_value1, pad2_value2, pad2_value3, pad2_value4, pad2_value5, pad2_value6, pad2_value7, pad2_value8)