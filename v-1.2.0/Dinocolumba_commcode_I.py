# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:22:25 2023

@author: Pakhomav
"""

import random
from cryptography.fernet import Fernet
import nltk
from nltk.corpus import words

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

def SLW():
    nltk.download('words')
    english_words = words.words()
    seven_letter_words = [word.lower() for word in english_words if len(word) == 7]
    random_words = random.sample(seven_letter_words, 23)
    random_word = random.choice(random_words)
    return random_word
        
def PUN(worda):
    OGTU = int(sum(ord(char) for char in worda))
    total_unicode = int(OGTU)
    while total_unicode > 25:
        total_unicode -= 25
    return OGTU, total_unicode

def mnm():
    initial_code = int(input("Please enter the initial_code (0 ≦ initial_code ≦ 9, initial_code ∈ ℕ₀) \n\n:]: "))
    if initial_code>=10 or initial_code<=-1:
        print("\n\n *_* initial_code creation ERROR. Please enter a positive integer between 0 and 9 (including 0 and 9) ! \n\n")
        mnm()
    else:
        random_numbers = random.sample(range(1024, 65400), 10)
        PRT = random_numbers[initial_code]
        if PRT <= 10000:
            PRT_str = '0' + str(PRT)
        else:
            PRT_str = str(PRT)
        key = Fernet.generate_key()
        key_dc =  key.decode()
        print('\n ☸ Kindly await, your "Communication code" is nearly ready for generation... ')
        PKP = PRT_str + key_dc
        passkey = SLW()
        WS, shift = PUN(passkey)
        WSD, Wshift = PUN(str(WS))
        E1pkp = encrypt(PKP, shift)
        E2pkp = encrypt(E1pkp, Wshift)
        CMCD = passkey + E2pkp
        print("\nCommunication code : \n")
        return CMCD

print(mnm())
print("\n\n")

