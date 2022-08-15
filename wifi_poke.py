import subprocess
import os
import sys

#new file
pass_file = open('passwords.txt', "a")
pass_file.write("Passwords below:\n\n")

#lists
wifi_files = []
wifi_names = []
wifi_passwords = []
#python for windows cmd
command = subprocess.run(["netsh","wlan","export","profile","key=clear"], capture_output = True).stdout.decode()

#current directory
path = os.getcwd()

#go
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_names.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = stripped[:-14]
                        wifi_passwords.append(back)
                        for x, y in zip(wifi_names, wifi_passwords):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep ='\n')
                            sys.stdout.Close()
