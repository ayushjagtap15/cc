import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Step 1: Generate AES key
key = get_random_bytes(32)

# Step 2: Encrypt the file
filename = "aes_key.bin"

# Create the file first (your part)
with open(filename, "wb") as f:
    f.write(key)

# Now encrypt the file contents
with open(filename, "rb") as f:
    data = f.read()

cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted_" + filename, "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(ciphertext)


with open(filename, "ba+", buffering=0) as f:
    length = f.tell()
    f.seek(0)
    f.write(b'\x00' * length)
    f.flush()
    os.fsync(f.fileno())

os.remove(filename)
