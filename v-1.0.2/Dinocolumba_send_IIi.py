# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:45:07 2023

@author: Pakhomav
"""

import socket
from cryptography.fernet import Fernet
import sys

def send_massage(IP, PRT, MTS):
    
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    def send_message(host, port, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data.encode())
    
    def b_code(text):
        return text.encode('utf-8')
    
    def encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += char
        return encrypted_text
    
    binary_key = key
    b_MTS = b_code(MTS)
    e_MTS = cipher_suite.encrypt(b_MTS)
    
    shift = PRT % 25
    S_e_MTS = encrypt(e_MTS.decode(), shift)
    
    try:
        send_message(IP, PRT, binary_key.decode())
        send_message(IP, PRT, S_e_MTS)
    except ConnectionResetError as e:
        print("\n*_* Connection reset error:", e)

IP = str(input("Please enter the recipient's IP address: \n\n:]: "))
PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties: \n\n:]: "))
MTS = input("\nPlease input the content to be transmitted: \n\n:]: ")
send_massage(IP, PRT, MTS)

while True:
    sss = input('\nIf you need to stop the program, please enter "end". \n\n:]: ')
    if sss == "end":
        break
    else:
        MTS = input("\nPlease input the content to be transmitted: \n\n:]: ")
        send_massage(IP, PRT, MTS)
sys.exit()


