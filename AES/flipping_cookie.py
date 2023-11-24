import re
from pwn import *
import numpy as np
from datetime import datetime, timedelta
from Crypto.Util.number import *



cookie = "e86e4558be7f7a73bc62860ef00a772d430ee4b916bb5d3c4b6422520d2c549008aec70b303a64f1aa302b97d6eb070f"
block_size = 16
# ct_blocks = re.findall('.{%s}' % (block_size * 2), cookie)
iv = [0xff]*block_size
plaintext = xor(iv, cookie)


def flip(cookie, plain):
    start = plain.find(b'admin=False')
    cookie = bytes.fromhex(cookie)
    iv = [0xff]*block_size
    cipher_fake = list(cookie)
    fake = b';admin=True;'
    for i in range(len(fake)):
        cipher_fake[block_size+i] = plain[block_size+i] ^ cookie[block_size+i] ^ fake[i]
        iv[start+i] = plain[start+i] ^ cookie[start+i] ^ fake[i]

    cipher_fake = bytes(cipher_fake).hex()
    iv = bytes(iv).hex()
    return cipher_fake, iv


expires_at = (datetime.today() + timedelta(days=1))
plain = f"admin=False;expiry={expires_at}".encode()
cookie, iv = flip(cookie, plain)
