# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:33:27 2023

@author: Pakhomav
"""

import socket
from cryptography.fernet import Fernet, InvalidToken
import time
import sys

def decrypt_message(key, encrypted_message):
    try:
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(encrypted_message)
        return decrypted_message
    except InvalidToken:
        print("\n*_* Invalid token or decryption key.")
        return None

def receive_message(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            received_message = data.decode('utf-8')
            return received_message

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    IP = str(input("Please enter the sender's IP address : \n\n:]: "))
    PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
    shift = PRT % 25
    start_time = time.time()
    key = receive_message(IP, PRT)
    received_message = receive_message(IP, PRT)
    received_message_S = decrypt(received_message, shift)
    FRM = decrypt_message(key, received_message_S)
    if FRM:
        print("Received message : \n\n   ", FRM.decode('utf-8'))
    time.sleep(10)
    try:
        while time.time() - start_time <= 360:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n*_* Program interrupted.")
        sys.exit()
    print("\n*_* Over time, program interrupted.")
    time.sleep(2)
    sys.exit()

main()


           