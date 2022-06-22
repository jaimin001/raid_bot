from cryptography.fernet import Fernet
import oschmod
import signal
import os, sys

def decrypt_file(encrypted_file_name):
    try:
        with open(encrypted_file_name, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data)
    except:
        return

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n : ")
    if res.lower() == 'y':
        oschmod.set_mode("filekey.key", "444")
        sys.stdout = open(os.devnull, 'w')
        exit(0)

def raid_bot():
    while True:
        decrypt_file1 = decrypt_file("enc1.txt")
        decrypt_file2 = decrypt_file("enc2.txt")
        decrypt_file3 = decrypt_file("enc3.txt")

        if decrypt_file1 == decrypt_file2 and decrypt_file1 == decrypt_file3:
                pass
        else:
            print("The System has been Breached !!")
            return

with open("filekey.key", 'rb') as filekey:
    key = filekey.read()
key = key.decode('utf-8')
oschmod.set_mode("filekey.key", "000")
signal.signal(signal.SIGINT, handler)

raid_bot()
