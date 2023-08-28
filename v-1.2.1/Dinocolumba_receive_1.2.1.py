# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:51:50 2023

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

def C_CUT(lakey, pisNB):
    def cut_characters(input_string, num_characters):
        if num_characters >= len(input_string):
            return input_string
        else:
            return input_string[:num_characters]
    
    result = cut_characters(lakey, pisNB)
    return result

def D_CUT(lakey, pisNB):
    
    def remove_characters(input_string, num_characters):
        if num_characters >= len(input_string):
            return ""
        else:
            return input_string[num_characters:]
    
    result = remove_characters(lakey, pisNB)
    return result

def handle_client(c, addr):
    pass

def decode(VTS):
    result = subprocess.check_output(["python", "Dinocolumba_decode_I.py", VTS])
    result = result.decode("utf-8")

    returned_values = ast.literal_eval(result)
    server_port, worda, l_worda, r_worda, chack = returned_values
    return server_port, worda, l_worda, r_worda, chack

server_ip = str(input("Please enter the recipient's IP address: \n\n:]: "))
CCd = input('\nPlease enter your Communication_code: \n\n:]: ')
server_port, worda, l_worda, r_worda, chack = decode(CCd)
server_port = int(server_port)
shift = server_port % 25

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

def decrypt_message(encrypted_message_str, fernet):
    encrypted_message_bytes = base64.b64decode(encrypted_message_str.encode())
    decrypted_message = fernet.decrypt(encrypted_message_bytes).decode("utf-8")
    return decrypted_message

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)
server_socket.bind(server_address)
server_socket.listen(1)
print("\n ⟳ Waiting for client connection...")

client_socket, client_address = server_socket.accept()
print("\n ☸ Established connection with client at ", client_address)

client_socket.send("first_verification_code".encode("utf-8"))
verification_response = client_socket.recv(1024).decode("utf-8")
dchack = C_CUT(verification_response, 9)
namew = D_CUT(verification_response, 9)

fernet = KEYMAKER(worda, namew)

if dchack == chack:
    
    keyw = KEYMAKER(worda, namew)
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        decoded_data = data.decode("utf-8")
        decrypted_message = decrypt_message(decoded_data, fernet)
        print("\nReceived data:", decrypted_message)

        if decrypted_message.strip() == "end":
            break

    print('\n ☸ Received termination message "end", closing connection with client at ', client_address)
    client_socket.close()
    time.sleep(3)
else:
    print("\n *_* Verification failed. Closing connection.")
    time.sleep(3)

server_socket.close()
sys.exit()