import hashlib
import requests
import asyncio
from Crypto.Cipher import AES

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
url = 'https://aes.cryptohack.org/passwords_as_keys/decrypt'
url1 = 'https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/'

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]


async def ddos(words, url, ciphertext):
    for _ in range(len(words)):
        KEY = hashlib.md5(words[_].encode()).digest().hex()
        r = requests.get(f'{url}/{ciphertext}/{KEY}/')
        data = r.json()
        plaintext = data["plaintext"]
        try:
            print(bytearray.fromhex(plaintext).decode())
        except:
            print("Error")
            # pass


asyncio.run(ddos(words, url, ciphertext))
