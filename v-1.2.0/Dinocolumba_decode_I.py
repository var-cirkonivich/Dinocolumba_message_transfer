# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:59:39 2023

@author: Pakhomav
"""

import subprocess
import sys

def DC(lakey1):
    
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
    
    def PUN(worda):
        OGTU = int(sum(ord(char) for char in worda))
        total_unicode = int(OGTU)
        while total_unicode > 25:
            total_unicode -= 25
        return OGTU, total_unicode
    
    worda = C_CUT(lakey1, 7)
    lakey2 = D_CUT(lakey1, 7)
    WS, shift = PUN(worda)
    WSD, Wshift = PUN(str(WS))
    D1pkp = decrypt(lakey2, Wshift)
    D2pkp = decrypt(D1pkp, shift)
    PRT = C_CUT(D2pkp, 5)
    key = D_CUT(D2pkp, 5)
    return PRT, key

lakey = sys.argv[1]
PRT, key = DC(lakey)
returned_values = (PRT, key)
print(returned_values)







