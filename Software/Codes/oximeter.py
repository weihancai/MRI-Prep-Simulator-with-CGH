import serial
import time
#Age = float(input("Input your Age: "))

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.flush()
def oxy():
    global SP02
    global BPM
    SP02 = 0
    BPM = 0
    if ser.in_waiting > 0:
        print("ser.in_waiting",ser.in_waiting)
        line = ser.readline().decode('latin-1').rstrip()
        line1 = line.find("SPO2:")
        #print(line1)
        if line1 != -1:
            #if line1 == "SPO2:":
            X, Y = line.split(",")
            Z, SP02 = X.split(":")
            #print(SP02)
            A, BPM = Y.split(":")
            #print(BPM)
            #print("RETURN " + SP02 + " " + BPM + "---------")
            
    return SP02, BPM
    
#while True:
    #oxy()
    
    #ox,bp=oxy()
    #if(ox != 0 or bp != 0):
       # print(ox,bp)
