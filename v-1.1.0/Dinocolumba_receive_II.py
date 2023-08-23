# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:33:27 2023

@author: Pakhomav
"""

import socket
from cryptography.fernet import Fernet, InvalidToken
import time
import sys

def decrypt_massage(key, enrypted_message):
    try:
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(enrypted_message)
        return decrypted_message
    except InvalidToken:
        print("Invalid token or decryption key.")
        return None

def receive_message(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            received_message = data.decode()
            return received_message
def main():
    IP = str(input("Please enter the recipient's IP address : \n\n:]: "))
    PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
    start_time = time.time()
    key = receive_message(IP, PRT)
    received_message = receive_message(IP, PRT)
    FRM = decrypt_massage(key, received_message)
    print("Received message : \n\n   ", FRM)
    time.sleep(10)
    try:
        while time.time() - start_time <= 1000:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n*_* Program interrupted.")
        sys.exit()
    print("\n*_* Over time, program interrupted.")
    time.sleep(2)
    sys.exit()

main()

           