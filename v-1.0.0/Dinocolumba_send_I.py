# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:45:07 2023

@author: Pakhomav
"""

import socket

def send_message(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())

IP = str(input("Please enter the recipient's IP address : \n\n:]: "))
PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
MTS = input("\nPlease input the content to be transmitted : \n\n:]: ")

send_message(IP, PRT, MTS)

