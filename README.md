1.		INTRODUCTION

1.1	Background
With time, technology improves and advancement in medical equipment such as LASIK for example, commonly referred to as laser eye surgery which is able restore blurred vision. MRI machines are no exception. It helps doctors to diagnose the insides of the human body without the need to do surgery. However, despite having such equipment, there are still limitations to them, such as dry eyes and regression for patients undergoing LASIK [1], MRI users also face different problems like claustrophobia and anxiety due to the confined space and loud noises where approximately 15% of all patients who are taking the MRI scan suffer from claustrophobia and cannot be imaged due to unnecessary movements [2]. These problems may vary according to people, especially uncomforting for those who are first timers. Here at Temasek Polytechnic, we a group of engineering students are tasked to help reduce the variation of behaviours which would affect the MRI scan results between different patients by developing an MRI scan simulator to help the patients get used to the procedures before going in for the real scan. Our project uses the wireless sensors available on the market and our coding knowledge to create a network of sensors to monitor the vital sign status of patients whilst going through the simulation. This enables the hospital staff to diagnose what is causing the patient to have unnecessary movements prior to the actual scan.

1.2	Objectives
The aim of this project is to develop a simulation of the pre magnetic resonance imaging (MRI) scan to help patients get familiarised with the environment during the scan. This is to prevent unnecessary movements made by the patients during the scan due to panic or many other reasons. Those movements might affect the scan as it could cause improper imaging, causing the need to repeat the scan which would be a waste of time and resources. The project consists of a smartwatch and oximeter to retrieve vital sign values (heart rate, blood pressure, oxygen saturation), and a mattress with pressure sensors (for motion detection). The data obtained from the sensors and mattress will be sent to a web API for analysis and storage purposes. The data then can be accessed by a hospital staff to check if the patient is ready for the MRI scan.

The specific objectives of the project are to:

•	Program a diagnostic tool inside a Raspberry Pi 4B(8GB) to integrate the connection between various hardware and software.

•	Set up a wireless connection network between the Raspberry Pi to extract readings from the vital sign devices such as oximeters and smartwatches through Bluetooth Low Energy (BLE) technology.

•	Build a compact yet durable housing with aluminium and acrylic sheets, which hosts all the components.










2.		PROJECT DEVELOPMENT

2.1	Hardware
Before starting to work on the project, we had to think about what we had to consider as we had to capture vital parameters of the patient to analyse suitability for the MRI scan. Firstly, we researched on the different vital sign devices that could be used for retrieving blood pressure, heart rate and oxygen saturation. The device most suited for reading blood pressure and heart rate was an oximeter, while a smartwatch was most suited to read oxygen saturation. As the project required the eventual integration of all the devices wirelessly on a single Raspberry Pi, we have decided to use an ESP 32 to connect to the BLE oximeter via Bluetooth and connect the ESP 32 to the Raspberry Pi via micro-USB for the oximeter’s Bluetooth connection as the Raspberry Pi’s Bluetooth receiver will be used by the smartwatch.
                             Figure 1   Advantages and disadvantages of the different vital sign devices
We researched on the different types of oximeters and blood pressure measurement devices (see Figure 1). At first, we wanted to get the oximeter ring. However, the cost was too high, so we decided to use the oximeter finger device instead. We chose the smart watch instead of the blood pressure pump as it is not bulky, is wireless and its measurement is invasive.

2.2	Software
For the first 6 weeks, we developed a Windows desktop application using the MVP framework, a simple data UI to view the sensor data. It was to simulate and to test whether the sensors will be compatible so that we would not have troubles integrating to the other group which were working on the UI section. We had also developed a Web API using the MVC framework to POST sensor data and GET sensor data for the Windows desktop application.

After that, we started to develop a diagnostic tool in Python using Tkinter which would be based inside the Raspberry Pi. Since Tkinter’s framework was only single threaded, we had issues trying to figure out how to run another Python script in the background as if not, the entire UI would stop functioning until the script runs finish. We managed to found a solution using the multithreading function to optimise the usage of threads available in the Raspberry Pi to make the UI smoother.











3.		PROJECT DESCRIPTION
3.1	Hardware
3.1.1	Selection of Vital Sign Equipment
We selected the vital sign equipment with the objective of monitoring the patients and detecting any sign of claustrophobia and anxiety.

3.1.2	Physical Observation of different Symptoms

Sensors currently can detect physical changes easily but are usually not practical when it comes to detecting feelings or a state of mind. According to research papers, claustrophobia [3] and anxiety [4] [5] have these symptoms:
Symptoms of claustrophobia:
•	Rapid Heartbeat
•	Trembling 
•	Shortness of breath
•	Feeling intense fear or pain
Symptoms of anxiety
•	Rapid heart rate
•	Increase in blood pressure
•	Rapid breading/hyperventilation
•	Muscle twitching
•	Difficulty focusing
•	Heavy sweating








3.1.3	Selection of Sensors
To detect these symptoms, we will be selecting the Oximeter, to detect abnormal heart rate which can be tied to a rapid heart rate for both claustrophobia and anxiety feelings and oxygen level. We also use a smartwatch to measure blood pressure to detect any increase of blood pressure when patients feel anxiety. After weeks of research, we have decided on two hardware devices that meets all the following requirements:
•	Decent battery level to reduce the constant need to plug in to recharge
•	Bluetooth Low Energy (BLE) connection for wireless connection
•	Able to extract readings from the devices (able to access encrypted data)
•	Devices should be easy to use and comfortable to wear
Figure 2   Rossmax SB210 Oximeter                                   Figure 3   DayBand SW-TLWB6A-TLD

For the Oximeter, we have chosen the SB210 from Rossmax (see Figure 2) and for the smartwatch, we chose the SW-TLWB6A-TLD from DayBand (see Figure 3).

3.1.4	Selection of Microcontroller
We had chosen the Raspberry Pi 4 as our microcontroller as it has the following features:
•	Low cost
•	Huge processing power in a compact board
•	Many interfaces consisting of HDMI, multiple USB, Ethernet, onboard Wi-Fi and Bluetooth, many GPIOs, and more which our project requires
•	Supports Linux, Python (making it easy to build applications)
•	Readily available examples with community support

In addition to that, we will also be using an ESP 32 device to support a second Bluetooth communication. Similarly, there are also a lot of public library resources available online as well to aid with the communication protocols.

3.2	Casing
3.2.1	Objective of Casing
The following points are what we envisioned the casing to provide:
•	House all the electronic components in a safe, enclosed environment
•	Screen holder to steadily place the touchscreen display

3.2.2	Inspiration for Casing
The design of the case is inspired by the natural mass of hexagonal prismatic wax cells built by honeybees in their nests, the honeycomb. The honeycomb inspired design will give us large storage capacity, a rigid structure and aesthetically pleasing looks. A drawer will also be added to store the smart watch, oximeter, or any other important stuff (see Figure 4 and 5).                        
               Figure 4   Side of case with drawer                                            Figure 5   Inside of case







3.2.3	Material and Manufacturing
In Temasek Polytechnic, there are various tools available to use freely for students like us to produce the casing:
•	3D printer to manufacture the drawer
•	Laser cutter to cut out acrylic holes and basic shapes
•	Plasma laser cutter to cut out aluminium support
•	Drill to make holes for screws
•	Files to smooth out the surfaces

3.2.4	Wiring Diagram
                                                   Figure 6   Simplified wiring diagram
The wiring of the project consists of a 7-inch touchscreen display (HDMI), ESP32 (Micro USB) for oximeter Bluetooth connection, ADC (GPIO) to connect the 16 pressure sensors and Raspberry Pi smartwatch Bluetooth connection. A fully detailed wiring diagram is provided in Appendix A.
3.2.5	Material List
Casing

Description	Dimension (mm)	Pieces	Prices ($)
Acrylic panel Transparent	600*300*5	2	-
Aluminium Plate	600*400*2	2	-
M3 Screw 17mm	3*17	12	-
M3 Screw 10mm	3*10	16	-
M3 Nuts	3*2	28	-
Neodymium magnet	5*3	8	5.00
Acrylic Glue	50ml	1	12.00

Electronics

Description	Dimension (mm)	Pieces	Prices ($)
Raspberry Pi 4B(8GB)	85.6*56.5	1	166.42
7-inch Touchscreen	170*125*20	1	98.98
Oximeter (Rossmax Oximeter)	50*40*30	1	143.90
ESP32	50*30*5	1	12.20
M5 smart watch	Unknown	1	4.78
SD Card 64GB	Unknown	1	9.8
Type-c cable	Unknown	1	7.71
Micro-USB cable	Unknown	1	7.34
Raspberry Pi cooling fan	30*30*7	3	5.10
Raspberry Pi heat sink	70*55*30	1	8.90
WS2812B RGB LED ring	36mm Diameter	1	2.02

3.3	Software
3.3.1	Diagnostic Tool
We developed a diagnostic tool software using Python’s Tkinter framework inside of the Raspberry Pi which integrates all the codes for the smart watch, oximeter, and pressure sensors to view and check if there are any issues with the components. It can retrieve Bluetooth data from the various sensors, view the status of the various sensors, select, and run individual sensors if needed and able to send data through an API which is made by a separate group to store values. The initial flowchart for the diagnostic tool is provided in Appendix B.










3.3.2	Structure Diagram
 
Figure 7   Structural diagram of the project scope

3.3.3	Codes
The partial codes with explanation to execute Tkinter interface of the diagnostic tool is provided in Appendix C. The partial codes with explanation to execute smartwatch controls is provided in Appendix D. The partial codes with explanation to execute oximeter controls is provided in Appendix E. The program to communicate with ESP32 and oximeter via Bluetooth is provided in Appendix F.




4.		RESULTS
                                      Figure 8   Oximeter and Smartwatch tab of the Diagnostic Tool
                     Figure 9   Waiting for connection                                    Figure 10   Connection Successful
                                                       Figure 11   Check if device is worn correctly
To retrieve the values of the patient’s heart rate and oxygen saturation level, press the “oximeter” button on the diagnostic tool. The Raspberry Pi will then retrieve data from an ESP32 which is connected to the BLE oximeter via Bluetooth. The data displayed includes the BPM levels, SP02 levels as well as connection status.
To retrieve the values of the patient's blood pressure, press the “Smart Watch” button on the diagnostic tool. The Raspberry Pi will then call the smartwatch to measure and send back all the data it has retrieved. Systolic, diastolic, battery level, connectivity status will be sent from the watch peripherally. (see Figure 8, 9, 10, 11)
                                              Figure 12   Pressure mat tab of the diagnostic tool
To retrieve the values of the change in pressure levels of the patient, press the “Pressure Levels” button on the diagnostic tool. The Raspberry Pi will then retrieve the 16 different pressure sensor values from the analog-to-digital converter (ADC) and display it on the graph and labels. The “Head”, “Body” and “Leg” labels will light up as red if movement is detected and green if no movement is detected. (see Figure 12)












5.		CONCULSION
Our project group has successfully implemented the retrieval of vital signs data via Bluetooth from the oximeter and smartwatch with the capability of having a diagnostic tool to view and retrieve data, and to check the status of those devices and the status of the pressure sensors to detect movement from the pressure mattress group.
As the diagnostic tool was developed using Tkinter, it lacked customisation and thus the GUI might look a bit too basic. Another area of limitation is that the oximeter is unable to diagnose accurately as there is no function to check if the Bluetooth connection is connected or disconnected.

For the Bluetooth connection issues, the only two ways to fix it is to reverse engineer the built in Bluetooth chip sets which will take a very long time as it is very advanced. The other way will be contacting the manufacturer where they most likely will not aid us in for security reasons.

Acknowledgements
The group would like to thank Mr Kumbar Shankarappa for his patience and help with his advice and suggestions, and always being supportive.







References
[1] Mayo Clinic Staff. (2019). LASIK eye surgery. [Online] Available: https://www.mayoclinic.org/tests-procedures/lasik-eye-surgery/about/pac-20384774
[2] BMC Med Imaging. (2011). Reduction of claustrophobia during magnetic resonance imaging. [Online] Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3045881/#:~:text=Thus%2C%20claustrophobia%20preventing%20MR%20imaging,to%202.5%25)%20%5B3%5D.
[3] J.L. Timothy. (2017). Everything You Should Know About Claustrophobia. [Online] Available: https://www.healthline.com/health/claustrophobia
[4] J.L. Timothy. (2018). Everything You Should Know About Anxiety. [Online] Available: https://www.healthline.com/health/anxiety-symptoms#symptoms
[5] A. Biggers. (2019). What is the link between anxiety and high blood pressure? [Online] Available: https://www.medicalnewstoday.com/articles/327212#anxiety-causing-high-blood-pressure

Other Sources
Rossmax. Data and Descriptions for Rossmax Devices. [Online] Available: https://www.rossmax.com/nb/products/monitoring/pulse-oximeters/sb210-fingertip-pulse-oximeter.html
Shopee. Data and Descriptions for SW-TLWB6A-TLD Smartwatch. [Online] Available: https://shopee.sg/Ready-Stock%F0%9F%92%96Bluetooth-Smartwatch-Waterproof-Heart-Rate-Blood-Pressure-Temperature-Monitoring-Smart-Bracelet-Watch-i.200891487.5839058546

Appendices
Appendix A: Detailed Wiring Diagram
Appendix B: Initial Diagnostic Tool Flowchart
Appendix C: Partial Tkinter Codes
Appendix D: Partial Smartwatch control codes
Appendix E: Partial Oximeter control codes
Appendix F: Partial ESP32 and Oximeter BLE codes
Appendix A – Detailed Wiring Diagram
 








Appendix B – Initial Diagnostic Tool Flowchart
 









Appendix C – Partial Tkinter Codes
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
Imports that are required for the GUI. Matplotlib has to be imported in embedded form to be able to be placed in the Tkinter layout.
window = tk.Tk()  # Initialise tkinter
window.title("Diagnostic Tool GUI")  # Set window title
window.attributes('-fullscreen', True)  # Set window dimensions
style = ttk.Style()
# style.configure("Custom.TNotebook.Tab", padding=[10,10])
theme = ThemedStyle(window)
theme.set_theme("plastik")
Basic Tkinter window and theme initialisation.
# Create tab control for tabLayout
TAB_CONTROL = ttk.Notebook(window, style="Custom.TNotebook")
# Tab1 (Smartwatch & Oximeter)
TAB1 = tk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Oximeter & Smartwatch')
# Tab2 (Pressure mat)
TAB2 = tk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Pressure Mat')
TAB_CONTROL.pack(expand=1, fill="both")
Initialisation of the Notebook component (tab layout)
frame = tk.Frame(TAB2, borderwidth=1, padx=10)
frame.grid(row=0, column=0)  # frame layout for tab2 (left)

frame2 = tk.Frame(TAB2, borderwidth=1, padx=10)
frame2.grid(row=0, column=1)  # frame layout for tab2 (right)

frame3 = tk.Frame(frame, borderwidth=1, padx=10)
frame3.grid(row=7, column=0)  # frame layout for movement location part
Initialisation of the different frames used to organise the oximeter, smartwatch and pressure parts of the UI.
f = Figure(figsize=(7, 3.5), dpi=90)
a = f.add_subplot(111)
a.set_title("Pressure Over Time")
a.set_ylim([0, 1024])

canvas = FigureCanvasTkAgg(f, master=frame)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, sticky=tk.W)  # Pressure table init settings
Pressure table initialisation settings
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

Appendix D – Partial Smartwatch control codes
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
When smart watch button is clicked, toggle swTrigger, start thread for retrieve_smartwatch_values function if swTrigger is set to 1 and change button colour according to whether it is ON (swTrigger = 1) or OFF (swTrigger = 0).
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
Establish connection to the smartwatch from another script (SW_ReadBloodPressure( )). If successful, show connection success status. Else, show disconnected status. Label colour will follow accordingly (red = disconnect, green = success). Start a new thread for battery level. Repeatedly get sensor values until swTrigger = 0 where adapter.stop( ) will end the connection.
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
Retrieve battery level of smartwatch function from another script (SW_Read_BatteryLevel ( ))








Appendix E – Partial Oximeter control codes
 def oximeter_button_event():
    global oxiTrigger
    if oxiTrigger == 0:
        oxiTrigger = 1
        btnOximeter['style'] = "Green.TButton"
    elif oxiTrigger == 1:
        oxiTrigger = 0
        btnOximeter['style'] = "Red.TButton"
    oxy_thread=threading.Thread(target=retrieve_oxymeter_values)
    oxy_thread.start()
Oximeter button trigger event. Starts a new thread to retrieve oximeter values. oxiTrigger = 1 is ON while oxiTrigger = 0 is OFF.
 def retrieve_oxymeter_values():
    print("OXYMETER")
    lblOxyStatus['text'] = "Connecting to device to retrieve values\n(if nothing happens for about 20 seconds, try restarting the application and/or the smartwatch)"
    lblOxyStatus['bg'] = "yellow"
    global oxiTrigger
    while True:
        if oxiTrigger == 1:
            ox,bp=oxy()
            if(ox != 0 and bp != 0):
                print("Sp02:"+str(ox)+"BPM:"+str(bp))
                lblSpO2Title['text'] = "Oxygen Saturation SpO2 (%): " + str(ox)
                lblBPMTitle['text'] = "Beats per Minute (BPM): " + str(bp)
                lblOxyStatus['text'] = "Successfully connected to oximeter"
                lblOxyStatus['bg'] = "lightgreen"
            else:
                lblOxyStatus['text'] = "Currently receiving values of 0. Please check if user is wearing the oximeter.\nIf nothing happens, please restart the oximeter."
                lblOxyStatus['bg'] = "lightcoral"
        elif oxiTrigger == 0:
            lblOxyStatus['text'] = "Press button to diagnose"
            lblOxyStatus['bg'] = "yellow"
            break
Function to continuously retrieve oximeter values while oxiTrigger = 1. Updates UI accordingly to statuses. Unlike the smartwatch, the oximeter part has no genuine way of knowing whether the device is connected or disconnected.



Appendix F – ESP32 and Oximeter BLE codes
#include "BLEDevice.h"

// The remote service we wish to connect to.
static BLEUUID serviceUUID("6e40f680-b5a3-f393-e0a9-e50e24dcca9e");
// The characteristic of the remote service we are interested in.
static BLEUUID    charUUID("6e40f682-b5a3-f393-e0a9-e50e24dcca9e");

static boolean doConnect = false;
static boolean connected = false;
static boolean doScan = false;
static BLERemoteCharacteristic* pRemoteCharacteristic;
static BLEAdvertisedDevice* myDevice;
int bpm;
int spo2;

static void notifyCallback(/*Serial.print("Notify callback for characteristic ");*/
  BLERemoteCharacteristic* pBLERemoteCharacteristic,//Serial.print(pBLERemoteCharacteristic->getUUID().toString().c_str());
  uint8_t* pData,
  size_t length, 
  bool isNotify) {
  for (int i = 1; i < 3; i++) { //Serial.print(" of data length ");
    if(i==1){
    Serial.print("SPO2:");
    Serial.print(pData[i]);
    Serial.print(",");
    }
    if(i==2){
    Serial.print("BPM:");
    Serial.print(pData[i]);
    Serial.println();//Serial.println(length);
  }
  }
  //Serial.println();//Serial.println(length);
  
 // if (pData[0] == 0x81) {
 //   bpm = pData[1];
 //  spo2 = pData[2];
 //  }
 //  if (pData[1] > 100){
 //    Serial.print("spo2 is too high "); 
 //   }
 //   else if(pData[1] < 90){
 //    Serial.print("spo2 is too low ");
 //   }
//    else{
//      Serial.print("spo2 is normal ");
 //  }
}

class MyClientCallback : public BLEClientCallbacks {
  void onConnect(BLEClient* pclient) {
    Serial.println("onConnect");
  }

  void onDisconnect(BLEClient* pclient) {
    connected = false;
    Serial.println("onDisconnect");
  }
};

bool connectToServer() {
    Serial.print("Forming a connection to ");
    Serial.println(myDevice->getAddress().toString().c_str());
    BLEClient*  pClient  = BLEDevice::createClient();
    Serial.println(" - Created client");

    pClient->setClientCallbacks(new MyClientCallback());
    // Connect to the remove BLE Server.
    pClient->connect(myDevice);  // if you pass BLEAdvertisedDevice instead of address, it will be recognized type of peer device address (public or private)
    Serial.println(" - Connected to server");
    // Obtain a reference to the service we are after in the remote BLE server.
    BLERemoteService* pRemoteService = pClient->getService(serviceUUID);
    if (pRemoteService == nullptr) {
      Serial.print("Failed to find our service UUID: ");
      Serial.println(serviceUUID.toString().c_str());
      pClient->disconnect();
      return false;
    }
    Serial.println(" - Found our service");
    // Obtain a reference to the characteristic in the service of the remote BLE server.
    pRemoteCharacteristic = pRemoteService->getCharacteristic(charUUID);
    if (pRemoteCharacteristic == nullptr) {
      Serial.print("Failed to find our characteristic UUID: ");
      Serial.println(charUUID.toString().c_str());
      pClient->disconnect();
      return false;
    }
    Serial.println(" - Found our characteristic");
    // Read the value of the characteristic.
    if(pRemoteCharacteristic->canRead()) {
      std::string value = pRemoteCharacteristic->readValue();
      Serial.print("The characteristic value was: ");
      Serial.println(value.c_str());
    }
    connected = true;
    return true;
}
/**
 * Scan for BLE servers and find the first one that advertises the service we are looking for.
 */
class MyAdvertisedDeviceCallbacks: public BLEAdvertisedDeviceCallbacks {
 /**
   * Called for each advertising BLE server.
   */
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    Serial.print("BLE Advertised Device found: ");
    Serial.println(advertisedDevice.toString().c_str());

    // We have found a device, let us now see if it contains the service we are looking for.
    if (advertisedDevice.haveServiceUUID() && advertisedDevice.isAdvertisingService(serviceUUID)) {

      BLEDevice::getScan()->stop();
      myDevice = new BLEAdvertisedDevice(advertisedDevice);
      doConnect = true;
      doScan = true;

    } // Found our server
  } // onResult
}; // MyAdvertisedDeviceCallbacks

void setup() {
  Serial.begin(115200);
  Serial.println(" i am iside setup.");
  Serial.println("Starting Arduino BLE Client application...");
  BLEDevice::init("");
  BLEScan* pBLEScan = BLEDevice::getScan();// Retrieve a Scanner 
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());// set the callback we want to use to be informed when we have detected a new device.
  pBLEScan->setInterval(1349);
  pBLEScan->setWindow(449);
  pBLEScan->setActiveScan(true);// Specify that we want active scanning
  pBLEScan->start(5, false);//start the scan to run for 5 seconds.
} // End of setup.

// This is the Arduino main loop function.
void loop() {
  if (doConnect == true) { // If the flag "doConnect" is true then we have scanned for and found the desired BLE Server with which we wish to connect.
    if (connectToServer()) { // Now we connect to it.
      Serial.println("We are now connected to the BLE Server."); // Once we are connected we set the connected flag to be true. 
    } else {
      Serial.println("We have failed to connect to the server; there is nothin more we will do.");
    }
    doConnect = false;
  } 
   Connection();
  delay(1000); // Delay a second between loops.  
} // End of loop

void Connection(){  
 if(connected){  // If we are connected to a peer BLE Server,
    String newValue = "Time since boot: " + String(millis()/1000); //update the characteristic each time we are reached with the current time since boot
    //Serial.println("Setting new characteristic value to \"" + newValue + "\"");
    if(pRemoteCharacteristic->canNotify())
      pRemoteCharacteristic->registerForNotify(notifyCallback);
  }
  else{
     loop();
 }
}


