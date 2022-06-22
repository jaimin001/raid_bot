from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

def encrypt_file(file_name, encrypted_file_name, key_path):
    with open(file_name, 'rb') as file:
        original_data = file.read()
    with open(key_path, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original_data)
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


encrypt_file("file1.txt", "enc1.txt", "filekey.key")
encrypt_file("file2.txt", "enc2.txt", "filekey.key")
encrypt_file("file3.txt", "enc3.txt", "filekey.key")