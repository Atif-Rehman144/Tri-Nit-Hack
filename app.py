import requests
import json
import random
#import serial              
from time import sleep
# import webbrowser           
# import sys
# import smbus	
# import RPi.GPIO as GPIO
#--------------------------------------------------------------------------------------------------------#
# def GPS_Info():
#     global NMEA_buff
#     global lat_in_degrees
#     global long_in_degrees
#     nmea_time = []
#     nmea_latitude = []
#     nmea_longitude = []
#     nmea_time = NMEA_buff[0]                    
#     nmea_latitude = NMEA_buff[1]                
#     nmea_longitude = NMEA_buff[3]               
    
#     print("NMEA Time: ", nmea_time,'\n')
#     print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
    
#     lat = float(nmea_latitude)                  
#     longi = float(nmea_longitude)               
    
#     lat_in_degrees = convert_to_degrees(lat)    
#     long_in_degrees = convert_to_degrees(longi) 
    

# def convert_to_degrees(raw_value):
#     decimal_value = raw_value/100.00
#     degrees = int(decimal_value)
#     mm_mmmm = (decimal_value - int(decimal_value))/0.6
#     position = degrees + mm_mmmm
#     position = "%.4f" %(position)
#     return position
# #------------------------------------------------------------------------------------------------------------------#
# def MPU_Init():
# 	
# 	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
# 	
# 	
# 	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
# 	

# 	bus.write_byte_data(Device_Address, CONFIG, 0)
# 	
# 	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
# 	

# 	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

# def read_raw_data(addr):
# 	
#         high = bus.read_byte_data(Device_Address, addr)
#         low = bus.read_byte_data(Device_Address, addr+1)
    
        
#         value = ((high << 8) | low)
        
      
#         if(value > 32768):
#                 value = value - 65536
#         return value
# #-----------------------------------------------------------------------------------------------------------------------#

def send_data_to_thingspeak(api_key, field1, field2, field3,field4):
    url = "https://api.thingspeak.com/update?api_key={}".format(api_key)
    payload = "field1={}&field2={}&field3={}&field4={}".format(field1, field2, field3,field4)
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Data sent successfully to Thingspeak")
    else:
        print("Failed to send data to Thingspeak")
# #------------------------------------------------------------------------------------------------------------------------#
# gpgga_info = "$GPGGA,"
# ser = serial.Serial ("/dev/ttyS0")              
# GPGGA_buffer = 0
# NMEA_buff = 0
# lat_in_degrees = 0
# long_in_degrees = 0
# sensor = 16
# buzzer = 18

# GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
# trig_pin=11
# echo_pin=12
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(sensor,GPIO.IN)
# GPIO.setup(buzzer,GPIO.OUT)

# GPIO.output(buzzer,False)

# GPIO.setup(trig_pin,GPIO.OUT)
# GPIO.setup(echo_pin,GPIO.IN)
# GPIO.OUTPUT(trig_pin,GPIO.LOW)
# time.sleep(2)
# GPIO.output(trig_pin,GPIO.HIGH)
# tme.sleep(0.00001)
# GPIO.output(trig_pin,LOW)

# PWR_MGMT_1   = 0x6B
# SMPLRT_DIV   = 0x19
# CONFIG       = 0x1A
# GYRO_CONFIG  = 0x1B
# INT_ENABLE   = 0x38
# ACCEL_XOUT_H = 0x3B
# ACCEL_YOUT_H = 0x3D
# ACCEL_ZOUT_H = 0x3F
# GYRO_XOUT_H  = 0x43
# GYRO_YOUT_H  = 0x45
# GYRO_ZOUT_H  = 0x47

# bus = smbus.SMBus(1) 	
# Device_Address = 0x68  

# MPU_Init()

# print (" Reading Data of Gyroscope and Accelerometer")

# while True:
    

#     try:
#         while True:
#             received_data = (str)(ser.readline())                   
#             GPGGA_data_available = received_data.find(gpgga_info)                   
#             if (GPGGA_data_available>0):
#                 GPGGA_buffer = received_data.split("$GPGGA,",1)[1]   
#                 NMEA_buff = (GPGGA_buffer.split(','))               
#                 GPS_Info()                                          
     
#                 print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
#                 map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees    
#                 print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")               
#                 print("------------------------------------------------------------\n")
                            
#     except KeyboardInterrupt:
#         webbrowser.open(map_link)        
#         sys.exit(0)
#     while GPIO.input(echo_pin)==0:
#         pulse_send=time.time()
    
#     while GPIO.input(trig_pin)==1:
#         pulse_recieved=time.time()
#     pulse_duration=pulse_received-pulse_send
#     pulse_duration=round(pulse_duration/2.2)
#     distance=34000*pulse_duration
#     print(distance)
#     acc_x = read_raw_data(ACCEL_XOUT_H)
# 	acc_y = read_raw_data(ACCEL_YOUT_H)
# 	acc_z = read_raw_data(ACCEL_ZOUT_H)
# 	
# 	
# 	gyro_x = read_raw_data(GYRO_XOUT_H)
# 	gyro_y = read_raw_data(GYRO_YOUT_H)
# 	gyro_z = read_raw_data(GYRO_ZOUT_H)
# 	
# 	
# 	Ax = acc_x/16384.0
# 	Ay = acc_y/16384.0
# 	Az = acc_z/16384.0
# 	
# 	Gx = gyro_x/131.0
# 	Gy = gyro_y/131.0
# 	Gz = gyro_z/131.0
# 	

# 	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
# 	sleep(1)
# try: 
#    while True:
#         while GPIO.input(sensor)==0:
#             pulse_send=time.time()

#         while GPIO.input(sensor)==1:
#            pulse_recieved=time.time()
#         pulse_duration=pulse_received-pulse_send
#         pulse_duration=round(pulse_duration/2.2)
#         distance=34000*pulse_duration


# except KeyboardInterrupt:
#     GPIO.cleanup()

        

api_key = "TN7Y5MB3ZGLQ38ZA"
for i in range(0,15):
    field1=acc=round(random.uniform(0,2),2) #acc
    field2=speed=round(random.uniform(0,120), 2) # speed
    field3=RPM=round(random.uniform(0,4000), 2) # RPM
    field4=ultra_distance=round(random.uniform(0,400), 2)# ultrasound
    send_data_to_thingspeak(api_key,field1,field2,field3,field4)
    if acc>1.4705:
          print("Reduce your Acceleration !!")
    else:
        print("")
        
    if speed>90:
        print(" SPEED LIMIT CROSSED !!")
    else:
        print("")
    if (speed==0 and RPM!=0):
          count=count+1
          if count>=30:
              print("TURN OFF VEHICLE !!")
    else:
        count=0
    if ultra_distance<50:
          print(" OBSTACLE AHEAD !!!")