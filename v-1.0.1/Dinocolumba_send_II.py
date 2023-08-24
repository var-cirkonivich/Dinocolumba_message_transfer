# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:45:07 2023

@author: Pakhomav
"""

import socket
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def send_message(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)

def b_code(text):
    return text.encode('utf-8')

IP = str(input("Please enter the recipient's IP address : \n\n:]: "))
PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
MTS = input("\nPlease input the content to be transmitted : \n\n:]: ")

b_MTS = b_code(MTS)
e_MTS = cipher_suite.encrypt(b_MTS)
binary_key = key

try:
    send_message(IP, PRT, binary_key)
    send_message(IP, PRT, e_MTS)
except ConnectionResetError as e:
    print("Connection reset error:", e)
