from Crypto.Random import get_random_bytes
import base64
aes_key=get_random_bytes(32)
encoded_key=base64.b64encode(aes_key).decode()
print("Generated aes-256 key",encoded_key)