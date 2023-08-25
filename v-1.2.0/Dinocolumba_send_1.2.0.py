# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:58:30 2023

@author: Pakhomav
"""

from cryptography.fernet import Fernet
import subprocess
import socket
import time
import ast
import sys

def decode(VTS):
    result = subprocess.check_output(["python", "Dinocolumba_decode_I.py", VTS])
    result = result.decode("utf-8")

    returned_values = ast.literal_eval(result)
    PRT, key= returned_values
    return PRT, key

server_ip = str(input("Please enter the recipient's IP address: \n\n:]: "))
CCd = input('\nPlease enter your Communication_code: \n\n:]: ')
server_port, keyw = decode(CCd)
server_port = int(server_port)
shift = str(server_port % 25)

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    message = input('\nPlease input the content to be transmitted (Enter "end" to finish) : \n\n:]: ')
    encrypted_message = encrypt_message(message, keyw)
    en_message = str(encrypted_message)
    client_socket.send(encrypted_message)
    
    if message == "end":
        break

client_socket.close()
print("\n *_* Connection has been closed. ")
time.sleep(3)
sys.exit()