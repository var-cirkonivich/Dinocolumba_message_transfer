import random
import string
import nltk
from nltk.corpus import words
from flask import Flask, request, jsonify, render_template
import webbrowser

app = Flask(__name__)

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif char.isdigit():
            encrypted_char = chr(((ord(char) - ord('0') + key) % 10) + ord('0'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
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

def RDL():
    letters = string.ascii_letters
    random_letters = random.choices(letters, k=3)
    random_string = ''.join(random_letters)
    return random_string

def RCAP(input_text, position1, position2):
    
    char_list = list(input_text)
    char_list[position1], char_list[position2] = char_list[position2], char_list[position1]
    
    replaced_text = ''.join(char_list)
    return replaced_text

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

def sum_unicode(string):
    total = 0
    for char in string:
        total += ord(char)
    while True:
        if total <= 9:
            break
        total -= 9
    return total

def mnm(initial_c):
    initial_code = sum_unicode(initial_c)
    if initial_code>=10 or initial_code<=-1:
        mnm()
    else:
        random_numbers = random.sample(range(1024, 65400), 10)
        PRT = random_numbers[initial_code]
        if PRT <= 10000:
            PRT_str = '0' + str(PRT)
        else:
            PRT_str = str(PRT)
        passker = RDL()
        passkey = SLW()
        PKP = PRT_str + passker
        WS, shift = PUN(passkey)
        WSD, Wshift = PUN(str(WS))
        E1pkp = encrypt(PKP, shift)
        E2pkp = encrypt(E1pkp, Wshift)
        CMCDD = passkey + E2pkp
        CMCDD2 = RCAP(CMCDD, 8, 5)
        CMCDDr = RCAP(CMCDD2, 11, 3)
        CMCDD3 = encrypt(CMCDDr, 23)
        CF = SCS(CMCDD3)
        return CF

@app.route("/")
def index():
    return render_template("DC_commcode.html")

@app.route("/show-result")
def show_result():
    result_data = request.args.get("result")
    return render_template("CMD_print_page2.html", result=result_data)

def generate_CF(input_text):
    
    CF = mnm(input_text)

    return CF

@app.route("/send-data", methods=["POST"])
def receive_data_from_frontend():
    data = request.json
    input_text = data.get("input")
    
    CF = generate_CF(input_text)
    
    return jsonify({"CF": CF})

if __name__ == "__main__":
    app.run(debug=True)