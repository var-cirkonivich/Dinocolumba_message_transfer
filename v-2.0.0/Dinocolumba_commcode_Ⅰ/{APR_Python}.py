import time
import subprocess

subprocess.Popen(["python", "Dinocolumba_commcode.py"])

time.sleep(3)

subprocess.Popen(["python", "app.py"])
