#Ini baru belajar bikin script:v
#oke

import json
import sys
import os
import time


def main():
        os.system('clear')
        os.system('figlet Zendot-H')
        print '''

       [+]Author : Zendot-H
       [+]Judul  : Belajar buat script
       '''
main()

x = "zendot"
y = "123"

def login():

    time.sleep(1)

    user = raw_input("Username: ")
    pasw = raw_input("Password: ")
    if user ==x and pasw ==y:
        print "Berhasil..."
        time.sleep(2)
    else:
        print"Ini salah. Coba masukkin yg bener!"
        time.sleep(2)

if __name__ == "__main__":
        login()