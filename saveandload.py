from Crypto.Random import get_random_bytes

key=get_random_bytes(32)

with open("aes_key.bin","wb") as key_file:
    key_file.write(key)
with open("aes_key.bin","rb") as key_file:
    loaded_file=key_file.read()
print(key==loaded_file)