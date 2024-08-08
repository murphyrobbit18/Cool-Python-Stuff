import subprocess

def process():
    subprocess.call("start C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell", shell=True) 
    # Here, I would like to write this in the new opened powershell : python ./hello_world.py (then press ENTER)

process()
input("end")