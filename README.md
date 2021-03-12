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

