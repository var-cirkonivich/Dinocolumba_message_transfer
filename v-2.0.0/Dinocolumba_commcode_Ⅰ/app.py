from flask import Flask
import webbrowser
import subprocess
import time

app = Flask(__name__, template_folder="templates")
app = Flask(__name__, static_folder="static")

app_process = subprocess.Popen(["python", "Dinocolumba_commcode.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

time.sleep(3)

webbrowser.open_new_tab("http://127.0.0.1:5000")