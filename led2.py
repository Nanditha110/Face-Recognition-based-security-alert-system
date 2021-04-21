#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:53:15 2019

@author: nanditha
"""
import serial                                 # add Serial library for Serial communication

Arduino_Serial = serial.Serial('//dev/tty.usbmodem1421',9600)  #Create Serial port object called arduinoSerialData
Arduino_Serial.readline()               #read the serial data and print it as line
print("Enter 1 to ON LED and 0 to OFF LED")

while 1:                                      #infinite loop
    input_data =(input())                 #waits until user enters data
    print ("you entered", input_data)           #prints the data for confirmation
    
    if (input_data == '1'):                   #if the entered data is 1 
        Arduino_Serial.write(b'1')             #send 1 to arduino
        print ("LED ON")
       
    
    if (input_data == '0'):                   #if the entered data is 0
        Arduino_Serial.write(b'0')             #send 0 to arduino 
        print ("LED OFF")
print("h")