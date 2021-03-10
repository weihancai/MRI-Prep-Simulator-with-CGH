import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys
import os
import threading
import time
import subprocess
import random
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
# from subprocess import call

from pressure_mat import *
from WK15_SMwatch import *
# from oximeter import oxy
from multiprocessing.pool import ThreadPool

window = tk.Tk()  # Initialise tkinter
window.title("Diagnostic Tool GUI")  # Set window title
window.geometry('1024x600')  # Set window dimensions

style = ttk.Style()
# style.configure("Custom.TNotebook.Tab", padding=[10,10])
theme = ThemedStyle(window)
theme.set_theme("plastik")
style.configure("Custom.TNotebook.Tab", padding=[10, 15])

# Create tab control for tabLayout
TAB_CONTROL = ttk.Notebook(window, style="Custom.TNotebook")
# Tab1 (Smartwatch & Oximeter)
TAB1 = tk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Oximeter & Smartwatch')
# Tab2 (Pressure mat)
TAB2 = tk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Pressure Mat')
TAB_CONTROL.pack(expand=1, fill="both")

frame = tk.Frame(TAB2, borderwidth=1, padx=10)
frame.grid(row=0, column=0)  # frame layout for tab2 (left)

frame2 = tk.Frame(TAB2, borderwidth=1, padx=10)
frame2.grid(row=0, column=1)  # frame layout for tab2 (right)

frame3 = tk.Frame(frame, borderwidth=1, padx=10)
frame3.grid(row=7, column=0)  # frame layout for movement location part

# style.use('seaborn')#Pressure Table Design Style

f = Figure(figsize=(7, 3.5), dpi=90)
a = f.add_subplot(111)
a.set_title("Pressure Over Time")
a.set_ylim([0, 1024])

canvas = FigureCanvasTkAgg(f, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, sticky=tk.W)  # Pressure table init settings

swTrigger = 0
oxiTrigger = 0
batteryTrigger = 0
pressureTrigger = 0
# Initialise variables for button presses

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
s12 = 0
s13 = 0
s14 = 0
s15 = 0
s16 = 0  # Have to initialise 1 by 1 if not TypeError
xList = list(range(0, 10))
yList1 = [0] * 10
yList2 = [0] * 10
yList3 = [0] * 10
yList4 = [0] * 10
yList5 = [0] * 10
yList6 = [0] * 10
yList7 = [0] * 10
yList8 = [0] * 10
yList9 = [0] * 10
yList10 = [0] * 10
yList11 = [0] * 10
yList12 = [0] * 10
yList13 = [0] * 10
yList14 = [0] * 10
yList15 = [0] * 10
yList16 = [0] * 10  # Have to initialise 1 by 1 if not TypeError
colourArray = ['#87CEEB', '#00FFFF', '#00FF7F', '#32CD32', '#FFD700', '#EEDD82', '#FFA500', '#FF8C00', '#FFC0CB',
               '#FF69B4', '#BA55D3', '#CD3278', '#F08080', '#CD4F39', '#8A8A8A', '#000000']


# skyblue, cyan, springgreen, limegreen, gold, lightgoldenrod, orange, darkorange, pink, hotpink, mediumorchid, violetred3, lightcoral,
# tomato3, grey54, black

# matplotlib variable initialising for plotting stuff

def animate(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16):
    a.clear()
    a.set_title("Pressure Over Time")
    a.set_ylim([0, 1024])
    yList1.pop(0)
    yList1.append(s1)
    yList2.pop(0)
    yList2.append(s2)
    yList3.pop(0)
    yList3.append(s3)
    yList4.pop(0)
    yList4.append(s4)
    yList5.pop(0)
    yList5.append(s5)
    yList6.pop(0)
    yList6.append(s6)
    yList7.pop(0)
    yList7.append(s7)
    yList8.pop(0)
    yList8.append(s8)
    yList9.pop(0)
    yList9.append(s9)
    yList10.pop(0)
    yList10.append(s10)
    yList11.pop(0)
    yList11.append(s11)
    yList12.pop(0)
    yList12.append(s12)
    yList13.pop(0)
    yList13.append(s13)
    yList14.pop(0)
    yList14.append(s14)
    yList15.pop(0)
    yList15.append(s15)
    yList16.pop(0)
    yList16.append(s16)  # Have to initialise 1 by 1 if not TypeError
    a.plot(xList, yList1, colourArray[0])
    a.plot(xList, yList2, colourArray[1])
    a.plot(xList, yList3, colourArray[2])
    a.plot(xList, yList4, colourArray[3])
    a.plot(xList, yList5, colourArray[4])
    a.plot(xList, yList6, colourArray[5])
    a.plot(xList, yList7, colourArray[6])
    a.plot(xList, yList8, colourArray[7])
    a.plot(xList, yList9, colourArray[8])
    a.plot(xList, yList10, colourArray[9])
    a.plot(xList, yList11, colourArray[10])
    a.plot(xList, yList12, colourArray[11])
    a.plot(xList, yList13, colourArray[12])
    a.plot(xList, yList14, colourArray[13])
    a.plot(xList, yList15, colourArray[14])
    a.plot(xList, yList16, colourArray[15])


def close_program():
    global swTrigger
    if swTrigger > 0:
        adapter.stop()
    close = tk.messagebox.askokcancel("Close", "Would you like to close the program?")
    if close:
        window.destroy()


window.protocol("WM_DELETE_WINDOW", close_program)  # Set close button event to window (Tkinter)


def restart_program():
    """Restarts the current program"""
    global swTrigger
    if swTrigger > 0:
        adapter.stop()
    restart_program = tk.messagebox.askokcancel("Restart", "Would you like to restart the program?")
    if restart_program:
        python = sys.executable
        os.execl(python, python, *sys.argv)


def restart_device():
    global swTrigger
    if swTrigger > 0:
        adapter.stop()
    restart_device = tk.messagebox.askokcancel("Restart", "Would you like to restart the device?")
    if restart_device:
        os.system('sudo shutdown -r now')


# def thread_second():
# call(["python3", "Wk8_Read_From_SMwatch.py"], shell=True)

# def oxymeter_clock():
# oxi_tred=threading.Thread(target=retrieve_oxymeter_values)
# oxi_tred.start()
# window.after(1000, oxymeter_clock)

# def retrieve_oxymeter_values():
#    print("OXYMETER")
#    lblOxyStatus['text'] = "Connecting to device to retrieve values\n(if nothing happens for about 20 seconds, try restarting the application and/or the smartwatch)"
#    lblOxyStatus['bg'] = "yellow"
#    global oxiTrigger
#    while True:
#        if oxiTrigger == 1:
#            ox,bp=oxy()
#            if(ox != 0 and bp != 0):
#                print("Sp02:"+str(ox)+"BPM:"+str(bp))
#                lblSpO2Title['text'] = "Oxygen Saturation SpO2 (%): " + str(ox)
#                lblBPMTitle['text'] = "Beats per Minute (BPM): " + str(bp)
#                lblOxyStatus['text'] = "Successfully connected to oximeter"
#                lblOxyStatus['bg'] = "lightgreen"
#            else:
#                lblOxyStatus['text'] = "Currently receiving values of 0. Please check if user is wearing the oximeter.\nIf nothing happens, please restart the oximeter."
#                lblOxyStatus['bg'] = "lightcoral"
#        elif oxiTrigger == 0:
#            lblOxyStatus['text'] = "Press button to diagnose"
#            lblOxyStatus['bg'] = "yellow"
#            break

def retrieve_pressure_mat_values():
    print("PRESSURE MAT")
    global pressureTrigger
    while True:
        if pressureTrigger == 1:
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16 = readPressure()
            print("pressure mat value", s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
            lblSensor1['text'] = "Sensor 1: " + str(s1)
            lblSensor2['text'] = "Sensor 2: " + str(s2)
            lblSensor3['text'] = "Sensor 3: " + str(s3)
            lblSensor4['text'] = "Sensor 4: " + str(s4)
            lblSensor5['text'] = "Sensor 5: " + str(s5)
            lblSensor6['text'] = "Sensor 6: " + str(s6)
            lblSensor7['text'] = "Sensor 7: " + str(s7)
            lblSensor8['text'] = "Sensor 8: " + str(s8)
            lblSensor9['text'] = "Sensor 9: " + str(s9)
            lblSensor10['text'] = "Sensor 10: " + str(s10)
            lblSensor11['text'] = "Sensor 11: " + str(s11)
            lblSensor12['text'] = "Sensor 12: " + str(s12)
            lblSensor13['text'] = "Sensor 13: " + str(s13)
            lblSensor14['text'] = "Sensor 14: " + str(s14)
            lblSensor15['text'] = "Sensor 15: " + str(s15)
            lblSensor16['text'] = "Sensor 16: " + str(s16)
            animate(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
            if s1 >= 100 or s2 >= 100 or s3 >= 100 or s4 >= 100 or s5 >= 100 or s6 >= 100 or s7 >= 100 or s8 >= 100 or s9 >= 100 or s10 >= 100 or s11 >= 100 or s12 >= 100 or s13 >= 100 or s14 >= 100 or s15 >= 100 or s16 >= 100:
                lblPressureStatus['text'] = "Movement detected!"
                lblPressureStatus['bg'] = "lightcoral"
                if s1 >= 100 or s2 >= 100 or s3 >= 100 or s4 >= 100:
                    # leg
                    lblLegs['bg'] = "lightcoral"
                if s16 >= 100 or s5 >= 100 or s6 >= 100 or s7 >= 100 or s8 >= 100 or s13 >= 100 or s9 >= 100 or s10 >= 100 or s11 >= 100:
                    # body
                    lblBody['bg'] = "lightcoral"
                if s12 >= 100 or s15 >= 100 or s14 >= 100:
                    # head
                    lblHead['bg'] = "lightcoral"
            else:
                # no movement
                lblPressureStatus['text'] = "No movement detected!"
                lblPressureStatus['bg'] = "lightgreen"
                lblHead['bg'] = "lightgreen"
                lblBody['bg'] = "lightgreen"
                lblLegs['bg'] = "lightgreen"
            canvas.draw_idle()
        elif pressureTrigger == 0:
            lblPressureStatus['text'] = "Press button to diagnose"
            lblPressureStatus['bg'] = "yellow"
            lblHead['bg'] = "yellow"
            lblBody['bg'] = "yellow"
            lblLegs['bg'] = "yellow"
            lblSensor1['text'] = "Sensor 1: [variable]"
            lblSensor2['text'] = "Sensor 2: [variable]"
            lblSensor3['text'] = "Sensor 3: [variable]"
            lblSensor4['text'] = "Sensor 4: [variable]"
            lblSensor5['text'] = "Sensor 5: [variable]"
            lblSensor6['text'] = "Sensor 6: [variable]"
            lblSensor7['text'] = "Sensor 7: [variable]"
            lblSensor8['text'] = "Sensor 8: [variable]"
            lblSensor9['text'] = "Sensor 9: [variable]"
            lblSensor10['text'] = "Sensor 10: [variable]"
            lblSensor11['text'] = "Sensor 11: [variable]"
            lblSensor12['text'] = "Sensor 12: [variable]"
            lblSensor13['text'] = "Sensor 13: [variable]"
            lblSensor14['text'] = "Sensor 14: [variable]"
            lblSensor15['text'] = "Sensor 15: [variable]"
            lblSensor16['text'] = "Sensor 16: [variable]"
            break


def retrieve_battery_level():
    while True:
        battery_level = SW_Read_BatteryLevel()
        if (battery_level <= 25):
            lblBatteryLife['bg'] = "lightcoral"
        elif (battery_level <= 50):
            lblBatteryLife['bg'] = "yellow"
        elif (battery_level > 50):
            lblBatteryLife['bg'] = "lightgreen"
        lblBatteryLife['text'] = str(battery_level) + "%"


def retrieve_smartwatch_values():
    print("SMARTWATCH")
    lblBPStatus[
        'text'] = "Connecting to device to retrieve values\n(if nothing happens for about 20 seconds,\nplease restart the smartwatch and the device)"
    lblBPStatus['bg'] = "yellow"
    global swTrigger
    btnSmartWatch.configure(state=tk.DISABLED)
    connect_status = SW_Connect()
    if (connect_status == "connected"):
        btnSmartWatch.configure(state=tk.NORMAL)
        lblBPStatus['text'] = "Successfully connected to smartwatch."
        lblBPStatus['bg'] = "lightgreen"
        if (batteryTrigger == 1):
            battery_thread = threading.Thread(target=retrieve_battery_level)
            battery_thread.start()
        while True:
            if swTrigger == 1:
                BP_status, sys, dia = SW_Read_BloodPressure()
                lblSystolic['text'] = "Systolic (mm Hg): " + str(sys)
                lblDiastolic['text'] = "Diastolic (mm Hg): " + str(dia)
                if (dia & sys != 0):
                    lblBPStatus['bg'] = "lightgreen"
                else:
                    lblBPStatus['bg'] = "orangered"
                lblBPStatus['text'] = str(BP_status)
                dia = 0
                sys = 0

            if swTrigger == 0:
                lblBPStatus['text'] = "Press button to diagnose"
                lblBPStatus['bg'] = "yellow"
                lblSystolic['text'] = "Systolic (mm Hg): [variable]"
                lblDiastolic['text'] = "Diastolic (mm Hg): [variable]"
                lblBatteryLife['text'] = "Battery [%]"
                defaultbg = window.cget('bg')
                lblBatteryLife['bg'] = defaultbg
                connect_status = ""
                # battery_process.terminate()
                adapter.stop()
                break
    elif (connect_status == "disconnected"):
        lblBPStatus['text'] = "Disconnected from smartwatch. Trying to reconnect."
        lblBPStatus['bg'] = "lightcoral"


def smart_watch_button_event():
    global swTrigger
    global batteryTrigger
    sw_thread = threading.Thread(target=retrieve_smartwatch_values)
    if swTrigger == 0:
        swTrigger = 1
        batteryTrigger = batteryTrigger + 1
        sw_thread.start()
        # btnSmartWatch['bg'] = "lightgreen"
        btnSmartWatch['style'] = "Green.TButton"
    elif swTrigger == 1:
        swTrigger = 0
        # btnSmartWatch['bg'] = "lightcoral"
        btnSmartWatch['style'] = "Red.TButton"


# def oximeter_button_event():
#    global oxiTrigger
#    if oxiTrigger == 0:
#        oxiTrigger = 1
#        btnOximeter['style'] = "Green.TButton"
#    elif oxiTrigger == 1:
#        oxiTrigger = 0
#        btnOximeter['style'] = "Red.TButton"
#    oxy_thread=threading.Thread(target=retrieve_oxymeter_values)
#    oxy_thread.start()


# def test():
# ani = animation.FuncAnimation(f, animate, interval=100)

def pressure_mat_button_event():
    global pressureTrigger
    pressure_thread = threading.Thread(target=retrieve_pressure_mat_values)
    # graph_thread = threading.Thread(target=test)
    if pressureTrigger == 0:
        pressureTrigger = 1
        # graph_thread.start()
        pressure_thread.start()
        btnPressureTitle['style'] = "Green.TButton"
    elif pressureTrigger == 1:
        pressureTrigger = 0
        btnPressureTitle['style'] = "Red.TButton"


style.configure('Red.TButton', font=("arial", 28, 'bold'), foreground="red")
style.configure('Green.TButton', font=("arial", 28, 'bold'), foreground="green")
style.configure('Reboot.TButton', font=("arial", 14, 'bold'), foreground="orangered")
style.configure('Restart.TButton', font=("arial", 14, 'bold'), foreground="tomato")
style.configure('Default.TButton', font=("arial", 14, 'bold'))
# ttkthemes Button styling configuration

# TAB1
btnOximeter = ttk.Button(TAB1, text="Oximeter",
                         style='Red.TButton')  # font=(None, 28, 'bold'), bg="lightcoral")#, command=oximeter_button_event)
btnOximeter.grid(row=0, column=0, sticky=tk.W, ipadx=10, ipady=7)

lblOxygenLevel = tk.Label(TAB1, text="Oxygen Level", font=("arial", 12, 'bold'))
lblOxygenLevel.grid(row=1, column=0, sticky=tk.W)

lblSpO2Title = tk.Label(TAB1, text="Oxygen Saturation SpO2 (%): [variable]")
lblSpO2Title.grid(row=2, column=0, sticky=tk.W)

lblHeartRate = tk.Label(TAB1, text="Heart Rate", font=("arial", 12, 'bold'))
lblHeartRate.grid(row=3, column=0, sticky=tk.W)

lblBPMTitle = tk.Label(TAB1, text="Beats per Minute (BPM): [variable]")
lblBPMTitle.grid(row=4, column=0, sticky=tk.W)

lblLine = tk.Label(TAB1,
                   text="........................................................................................................................   ")
lblLine.grid(row=5, column=0, sticky=tk.W)

lblOxyStatusTitle = tk.Label(TAB1, text="Connection Status", font=("arial", 12, 'bold'))
lblOxyStatusTitle.grid(row=6, column=0, sticky=tk.W)

lblOxyStatus = tk.Label(TAB1, text="Press button to diagnose", bg="yellow")
lblOxyStatus.grid(row=7, column=0, sticky=tk.W)

lblLine2 = tk.Label(TAB1,
                    text="........................................................................................................................   ")
lblLine2.grid(row=8, column=0, sticky=tk.W)

lblSpace = tk.Label(TAB1, text=" ")
lblSpace.grid(row=9, column=0, sticky=tk.W)

btnRestartD = ttk.Button(TAB1, text="RESTART DEVICE", style='Reboot.TButton',
                         command=restart_device)  # font=(None, 14, 'bold'), bg="red", command=restart_device, height=2, width=15)
btnRestartD.grid(row=10, column=0, sticky=tk.W, ipadx=10.5, ipady=10)

lblLine8 = tk.Label(TAB1, text=" ")
lblLine8.grid(row=11, column=0, sticky=tk.W)

btnRestart = ttk.Button(TAB1, text="RESTART APP", style='Restart.TButton',
                        command=restart_program)  # font=(None, 14, 'bold'), bg="yellow", command=restart_program, height=2, width=15)
btnRestart.grid(row=12, column=0, sticky=tk.W, ipadx=25.5, ipady=10)

lblLine9 = tk.Label(TAB1, text=" ")
lblLine9.grid(row=13, column=0, sticky=tk.W)

btnClose = ttk.Button(TAB1, text="CLOSE", style='Default.TButton',
                      command=close_program)  # font=(None, 14, 'bold'), command=close_program, height=2, width=15)
btnClose.grid(row=14, column=0, sticky=tk.W, ipadx=42, ipady=10)

btnSmartWatch = ttk.Button(TAB1, text="Smart Watch", style='Red.TButton',
                           command=smart_watch_button_event)  # font=(None, 28, 'bold'), bg="lightcoral", command=smart_watch_button_event)
btnSmartWatch.grid(row=0, column=1, sticky=tk.W, ipadx=20, ipady=9)

lblBatteryLifeTitle = tk.Label(TAB1, text="Battery Life", font=("arial", 12, 'bold'))
lblBatteryLifeTitle.grid(row=1, column=1, sticky=tk.W)

lblBatteryLife = tk.Label(TAB1, text="[Battery %]")
lblBatteryLife.grid(row=2, column=1, sticky=tk.W)

lblBloodPressure = tk.Label(TAB1, text="Blood Pressure", font=("arial", 12, 'bold'))
lblBloodPressure.grid(row=3, column=1, sticky=tk.W)

lblSystolic = tk.Label(TAB1, text="Systolic (mm Hg): [variable]")
lblSystolic.grid(row=4, column=1, sticky=tk.W)

lblDiastolic = tk.Label(TAB1, text="Diastolic (mm Hg): [variable]")
lblDiastolic.grid(row=5, column=1, sticky=tk.W)

lblLine3 = tk.Label(TAB1,
                    text="...........................................................................................................................")
lblLine3.grid(row=6, column=1, sticky=tk.W)

lblBPStatusTitle = tk.Label(TAB1, text="Connection Status", font=("arial", 12, 'bold'))
lblBPStatusTitle.grid(row=7, column=1, sticky=tk.W)

lblBPStatus = tk.Label(TAB1, text="Press button to diagnose", bg="yellow")
lblBPStatus.grid(row=8, column=1, sticky=tk.W)

lblLine4 = tk.Label(TAB1,
                    text="...........................................................................................................................")
lblLine4.grid(row=9, column=1, sticky=tk.W)

lblGap3 = tk.Label(TAB1, text=" ", font=("arial", 24, 'bold'))
lblGap3.grid(row=10, column=1, sticky=tk.W)

img = ImageTk.PhotoImage(Image.open("tpxcgh.png"))
panel1 = tk.Label(TAB1, image=img)
panel1.grid(row=15, column=1, sticky=tk.E)

# btnRestart = tk.Button(TAB1, text="RESTART", font=(None, 14, 'bold'), bg="red", command=restart_program)
# btnRestart.grid(row=11, column=1, sticky=tk.W)

# btnClose = tk.Button(TAB1, text="CLOSE", font=(None, 14, 'bold'), command=close_program)
# btnClose.grid(row=12, column=1, sticky=tk.W)
# /TAB1

# TAB2
# Frame2
lblSensor1Color = tk.Label(frame2, text="   ", bg='skyblue')
lblSensor1Color.grid(row=0, column=1, sticky=tk.W)

lblSensor2Color = tk.Label(frame2, text="   ", bg='cyan')
lblSensor2Color.grid(row=1, column=1, sticky=tk.W)

lblSensor3Color = tk.Label(frame2, text="   ", bg='springgreen')
lblSensor3Color.grid(row=2, column=1, sticky=tk.W)

lblSensor4Color = tk.Label(frame2, text="   ", bg='limegreen')
lblSensor4Color.grid(row=3, column=1, sticky=tk.W)

lblSensor5Color = tk.Label(frame2, text="   ", bg='gold')
lblSensor5Color.grid(row=4, column=1, sticky=tk.W)

lblSensor6Color = tk.Label(frame2, text="   ", bg='lightgoldenrod')
lblSensor6Color.grid(row=5, column=1, sticky=tk.W)

lblSensor7Color = tk.Label(frame2, text="   ", bg='orange')
lblSensor7Color.grid(row=6, column=1, sticky=tk.W)

lblSensor8Color = tk.Label(frame2, text="   ", bg='darkorange')
lblSensor8Color.grid(row=7, column=1, sticky=tk.W)

lblSensor9Color = tk.Label(frame2, text="   ", bg='pink')
lblSensor9Color.grid(row=8, column=1, sticky=tk.W)

lblSensor10Color = tk.Label(frame2, text="   ", bg='hotpink')
lblSensor10Color.grid(row=9, column=1, sticky=tk.W)

lblSensor11Color = tk.Label(frame2, text="   ", bg='mediumorchid')
lblSensor11Color.grid(row=10, column=1, sticky=tk.W)

lblSensor12Color = tk.Label(frame2, text="   ", bg='violetred3')
lblSensor12Color.grid(row=11, column=1, sticky=tk.W)

lblSensor13Color = tk.Label(frame2, text="   ", bg='lightcoral')
lblSensor13Color.grid(row=12, column=1, sticky=tk.W)

lblSensor14Color = tk.Label(frame2, text="   ", bg='tomato3')
lblSensor14Color.grid(row=13, column=1, sticky=tk.W)

lblSensor15Color = tk.Label(frame2, text="   ", bg='gray54')
lblSensor15Color.grid(row=14, column=1, sticky=tk.W)

lblSensor16Color = tk.Label(frame2, text="   ", bg='black')
lblSensor16Color.grid(row=15, column=1, sticky=tk.W)

btnPressureTitle = ttk.Button(frame, text="Pressure Levels", style='Red.TButton',
                              command=pressure_mat_button_event)  # font=(None, 28, 'bold'), bg='lightcoral', command=pressure_mat_button_event)
btnPressureTitle.grid(row=0, column=0, sticky=tk.W, ipadx=15, ipady=7)

lblSensor1 = tk.Label(frame2, text="Sensor 1: [variable]")  # , bg='skyblue')
lblSensor1.grid(row=0, column=2, sticky=tk.W)

lblSensor2 = tk.Label(frame2, text="Sensor 2: [variable]")  # , bg='cyan')
lblSensor2.grid(row=1, column=2, sticky=tk.W)

lblSensor3 = tk.Label(frame2, text="Sensor 3: [variable]")  # , bg='springgreen')
lblSensor3.grid(row=2, column=2, sticky=tk.W)

lblSensor4 = tk.Label(frame2, text="Sensor 4: [variable]")  # , bg='limegreen')
lblSensor4.grid(row=3, column=2, sticky=tk.W)

lblSensor5 = tk.Label(frame2, text="Sensor 5: [variable]")  # , bg='gold')
lblSensor5.grid(row=4, column=2, sticky=tk.W)

lblSensor6 = tk.Label(frame2, text="Sensor 6: [variable]")  # , bg='lightgoldenrod')
lblSensor6.grid(row=5, column=2, sticky=tk.W)

lblSensor7 = tk.Label(frame2, text="Sensor 7: [variable]")  # , bg='orange')
lblSensor7.grid(row=6, column=2, sticky=tk.W)

lblSensor8 = tk.Label(frame2, text="Sensor 8: [variable]")  # , bg='darkorange')
lblSensor8.grid(row=7, column=2, sticky=tk.W)

lblSensor9 = tk.Label(frame2, text="Sensor 9: [variable]")  # , bg='pink')
lblSensor9.grid(row=8, column=2, sticky=tk.W)

lblSensor10 = tk.Label(frame2, text="Sensor 10: [variable]")  # , bg='hotpink')
lblSensor10.grid(row=9, column=2, sticky=tk.W)

lblSensor11 = tk.Label(frame2, text="Sensor 11: [variable]")  # , bg='mediumorchid')
lblSensor11.grid(row=10, column=2, sticky=tk.W)

lblSensor12 = tk.Label(frame2, text="Sensor 12: [variable]")  # , bg='violetred3')
lblSensor12.grid(row=11, column=2, sticky=tk.W)

lblSensor13 = tk.Label(frame2, text="Sensor 13: [variable]")  # , bg='lightcoral')
lblSensor13.grid(row=12, column=2, sticky=tk.W)

lblSensor14 = tk.Label(frame2, text="Sensor 14: [variable]")  # , bg='tomato3')
lblSensor14.grid(row=13, column=2, sticky=tk.W)

lblSensor15 = tk.Label(frame2, text="Sensor 15: [variable]")  # , bg='seashell3')
lblSensor15.grid(row=14, column=2, sticky=tk.W)

lblSensor16 = tk.Label(frame2, text="Sensor 16: [variable]")  # , bg='gray54')
lblSensor16.grid(row=15, column=2, sticky=tk.W)

lblLine6 = tk.Label(frame2, text="...........................................................................")
lblLine6.grid(row=16, column=2, sticky=tk.W)

lblPressureStatusTitle = tk.Label(frame2, text="Sensor Status", font=("arial", 12, 'bold'))
lblPressureStatusTitle.grid(row=17, column=2, sticky=tk.W)

lblPressureStatus = tk.Label(frame2, text="Press button to diagnose", bg="yellow")
lblPressureStatus.grid(row=18, column=2, sticky=tk.W)

lblLine7 = tk.Label(frame2, text="...........................................................................\n")
lblLine7.grid(row=19, column=2, sticky=tk.W)

panel2 = tk.Label(frame2, image=img)
panel2.grid(row=20, column=2, sticky=tk.E)
# /Frame2
# Frame3
lblMovementTitle = tk.Label(frame3, text="Movement Location:  ", font=("arial", 16, 'bold'))
lblMovementTitle.grid(row=0, column=0, sticky=tk.W)

lblHead = tk.Label(frame3, text=" Head ", bg="yellow", font=("arial", 20))
lblHead.grid(row=0, column=1, sticky=tk.W)

lblGap1 = tk.Label(frame3, text="     ")
lblGap1.grid(row=0, column=2, sticky=tk.W)

lblBody = tk.Label(frame3, text=" Body ", bg="yellow", font=("arial", 20))
lblBody.grid(row=0, column=3, sticky=tk.W)

lblGap2 = tk.Label(frame3, text="     ")
lblGap2.grid(row=0, column=4, sticky=tk.W)

lblLegs = tk.Label(frame3, text=" Leg ", bg="yellow", font=("arial", 20))
lblLegs.grid(row=0, column=5, sticky=tk.W)
# /Frame3
# /TAB2
window.mainloop()