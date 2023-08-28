# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:59:39 2023

@author: Pakhomav
"""

import subprocess
import sys

def RCAP(input_text, position1, position2):
    
    char_list = list(input_text)
    char_list[position1], char_list[position2] = char_list[position2], char_list[position1]
    
    replaced_text = ''.join(char_list)
    return replaced_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            elif char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        elif char.isdigit():
            decrypted_char = chr(((ord(char) - ord('0') - key) % 10) + ord('0'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def C_CUT(lakey, pisNB):
    def cut_characters(input_string, num_characters):
        if num_characters >= len(input_string):
            return input_string
        else:
            return input_string[:num_characters]
    
    result = cut_characters(lakey, pisNB)
    return result

def M_CUT(lakey, pisNB):
    def cut_characters(input_string, num_characters):
        if num_characters >= len(input_string):
            return input_string
        else:
            return input_string[-num_characters:]
    
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

def PUN(worda):
    OGTU = int(sum(ord(char) for char in worda))
    total_unicode = int(OGTU)
    while total_unicode > 25:
        total_unicode -= 25
    return OGTU, total_unicode

def SCS(input_string):
    swapped_string = ""
    
    for char in input_string:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char
    
    return swapped_string

def DC(lakeywe):
    
    lakeyw = SCS(lakeywe)
    
    l_worda = C_CUT(lakeyw, 7)
    l_chack = M_CUT(lakeyw, 3)
    
    lakey = decrypt(lakeyw, 23)
    
    lakey3 = RCAP(lakey, 5, 8)
    lakey2 = RCAP(lakey3, 3, 11)
    
    r_worda = C_CUT(lakey2, 7)
    r_chack = M_CUT(lakey2, 3)

    worda = C_CUT(lakey2, 7)
    lakey3 = D_CUT(lakey2, 7)
    
    WS, shift = PUN(worda)
    WSD, Wshift = PUN(str(WS))
    
    lakey4 = decrypt(lakey3, Wshift)
    lakey5 = decrypt(lakey4, shift)
    
    PRT = C_CUT(lakey5, 5)
    chack = D_CUT(lakey5, 5)
    
    A_chack = chack + l_chack + r_chack
    
    return PRT, worda, l_worda, r_worda, A_chack

lakey = sys.argv[1]
PRT, worda, l_worda, r_worda, A_chack = DC(lakey)
returned_values = (PRT, worda, l_worda, r_worda, A_chack)
print(returned_values)







