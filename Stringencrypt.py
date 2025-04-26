from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES 

key=get_random_bytes(32)
cipher=AES.new(key,AES.MODE_GCM)

message=b"Hwllobhsfhvfs"
ciphertext,tag=cipher.encrypt_and_digest(message)
print(ciphertext.hex())