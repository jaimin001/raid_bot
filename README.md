# Raid Bot
Microsoft Cyber-Security Engage '22

The main objective of this bot is to detect False Data Injection Attack (FDIA) and also
By-pass Logic Attack and many other attacks where adversaries try to change or read data.
## How it Works 

* `file1.txt / file2.txt / file3.txt` : These are the original files which consists of random number and signifies data that critical infrastructure use.

* `raid_encrypt.py` :
    * contains the functions that are needed to encrypt a file.
    * It encrypts the file as `enc1.txt /enc2.txt / enc3.txt`.
    * Also it saves the encryption and decryption key as filekey.key in byte format.
    * As soon as we get the encrypted files, we should delete original files to make the system unbrechable.
    * If the database is needed in plain text, then raid_bot should be killed and decrypted using the key.

* `raid_bot.py` :
    * This is the main file which constantly check if the databases are not tampered.
    * Once it starts, it locks the filekey.key by changing its permissions to "000", whichmakes it inaccessible to read or write.
    * If any file is changed or tampered, "The System has been Breached !!" signal alerts the officials to take further actions which makes our system foolproof.
    * In the below example, enc2.txt was tampered to make this result possible.
        > ![breached](images/breached.jpg)

* `filekey.key` : This file right now contains encryption and decryption key, but once raid_bot starts running, this file would become unacessible.
    > ![not_accessible](images/not_accessible.jpg)