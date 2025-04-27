from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Step 3.1: Generate a Key
def generate_key():
    key = get_random_bytes(32)  # Generate a random 32-byte key
    with open("key.bin", "wb") as key_file:
        key_file.write(key)
    print("Key saved to 'key.bin'")

# Step 3.2: Load an Existing Key
def load_key():
    with open("key.bin", "rb") as key_file:
        return key_file.read()

# Step 4: Encrypt a File
def encrypt_file(file_path, key):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read file data
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Pad data to make it a multiple of AES block size (16 bytes)
    padding_length = 16 - len(file_data) % 16
    padded_data = file_data + bytes([padding_length] * padding_length)

    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)

    # Save encrypted data and IV
    with open(file_path + ".enc", "wb") as enc_file:
        enc_file.write(iv + encrypted_data)
    print(f"File '{file_path}' encrypted as '{file_path}.enc'")

# Step 5: Decrypt a File
def decrypt_file(encrypted_path, key):
    with open(encrypted_path, "rb") as enc_file:
        # Read IV (first 16 bytes)
        iv = enc_file.read(16)
        encrypted_data = enc_file.read()

    # Create the cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt and remove padding
    decrypted_data = cipher.decrypt(encrypted_data)
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Save decrypted data
    original_path = encrypted_path.replace(".enc", "_decrypted")
    with open(original_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    print(f"File '{encrypted_path}' decrypted as '{original_path}'")

# Step 6: Main Function to Combine Everything
if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    choice = int(input("Choose an option: "))

    if choice == 1:
        generate_key()
    elif choice == 2:
        key = load_key()
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
    elif choice == 3:
        key = load_key()
        encrypted_path = input("Enter the path of the encrypted file: ")
        decrypt_file(encrypted_path, key)
    else:
        print("Invalid choice")