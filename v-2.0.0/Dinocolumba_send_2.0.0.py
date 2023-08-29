# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:58:30 2023

@author: Pakhomav
"""

from cryptography.fernet import Fernet
import subprocess
import hashlib
import base64
import socket
import time
import ast
import sys

def decode(VTS):
    result = subprocess.check_output(["python", "Dinocolumba_decode_II.py", VTS])
    result = result.decode("utf-8")

    returned_values = ast.literal_eval(result)
    server_port, worda, l_worda, r_worda, chack = returned_values
    return server_port, worda, l_worda, r_worda, chack

server_ip = str(input("Please enter the recipient's IP address: \n\n:]: "))
CCd = input('\nPlease enter your Communication_code: \n\n:]: ')
namew = input('\nPlease enter your usee_name: \n\n:]: ')
server_port, worda, l_worda, r_worda, chack = decode(CCd)
server_port = int(server_port)
shift = str(server_port % 25)

def KEYMAKER(title_name, user_name):
    
    def generate_fernet_key(password, salt):
        key = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
        key = key[:32]
        return base64.urlsafe_b64encode(key)
    
    password = title_name.encode()
    
    def generate_salt_from_string(input_string):
        salt = hashlib.sha256(input_string.encode()).digest()
        return salt
    input_string = user_name
    salt = generate_salt_from_string(input_string)
    
    fernet_key = generate_fernet_key(password, salt)
    fernet = Fernet(fernet_key)
    return fernet

fernet = KEYMAKER(worda, namew)

def EAEM(message, fernet):
    encrypted_message = fernet.encrypt(message.encode())
    encoded_message = base64.b64encode(encrypted_message).decode()
    return encoded_message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

chack_bytes = chack.encode()
namew_bytes = namew.encode()
client_socket.send(chack_bytes)
client_socket.send(namew_bytes)

while True:
    message = input('\nPlease input the content to be transmitted (Enter "end" to finish):\n\n:]: ')
    
    encrypted_message = EAEM(message, fernet)
    client_socket.send(encrypted_message.encode())
    
    if message == "end":
        break

print("\n *_* Connection has been closed. ")
client_socket.close()
time.sleep(3)
sys.exit()