# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:33:27 2023

@author: Pakhomav
"""

import socket
import time
import sys

def receive_message(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            received_message = data.decode()
            print("Received message : \n\n   ", received_message)
            return received_message
def main():
    IP = str(input("Please enter the recipient's IP address : \n\n:]: "))
    PRT = int(input("\nPlease enter the dynamic port numbers for both communicating parties : \n\n:]: "))
    start_time = time.time()
    received_message = receive_message(IP, PRT)
    try:
        while time.time() - start_time <= 66:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n*_* Program interrupted.")
        sys.exit()
    print("\n*_* Over time, program interrupted.")
    time.sleep(2)
    sys.exit()

main()

