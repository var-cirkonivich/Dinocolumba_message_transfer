# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:51:50 2023

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
shift = server_port % 25

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode("utf-8")
    return decrypted_message

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("\n ⟳ Waiting for client connection...")

while True:
    client_socket, client_address = server_socket.accept()
    print("\n ☸ Established connection with client at ", client_address)
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        decoded_data = data.decode("utf-8")
        decrypted_message = decrypt_message(decoded_data, keyw)
        print("\nReceived data : ", decrypted_message)
        
        if decrypted_message.strip() == "end":
            break
    
    print('\n ☸ Received termination message "end", closing connection with client at ', client_address)
    client_socket.close()
    time.sleep(3)
    break
    
server_socket.close()
sys.exit()