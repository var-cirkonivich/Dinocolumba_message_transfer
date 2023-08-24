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

def receive_message(conn):
    data = conn.recv(1024)
    received_message = data.decode('utf-8')
    return received_message

def connect_socket(IP, PRT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PRT))
    s.listen()
    conn, addr = s.accept()
    return s, conn

IP = str(input("Please enter the sender's IP address : \n\n:]: "))

while True:
    PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
    try:
        s, conn = connect_socket(IP, PRT)

        received_messages = []
        while len(received_messages) < 2:
            received_message = receive_message(conn)
            received_message_S = decrypt(received_message, PRT % 25)
            received_messages.append(received_message_S)

        key = receive_message(conn)
        FRM = decrypt_message(key, received_messages[0])
        if FRM:
            print("\nReceived message : \n\n   ", FRM.decode('utf-8'))

        conn.close()  # 斷開連線
    except KeyboardInterrupt:
        print("\n*_* Program interrupted.")
        sys.exit()







