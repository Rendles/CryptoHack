from pwn import *

# From ECB
ciphertext = "36c14793851b60a98fe7acf515d5b6dd7312830e60634534576f274119a93943c25d51547b77a8153ca20a983f89e051"

# FROM CBC
plaintext = "60b6a12f09098700966fd689628d697755b33ee3f1741b9aec85f3c060b6dde82c26f53e51071a05603006603888183e"

block_size = 16

ct_blocks = re.findall('.{%s}' % (block_size * 2), ciphertext)
pt_blocks = re.findall('.{%s}' % (block_size * 2), plaintext)
b = [[], [], []]

b[0] = xor(bytes.fromhex(ct_blocks[0]), bytes.fromhex(pt_blocks[1]))
b[1] = xor(bytes.fromhex(ct_blocks[1]), bytes.fromhex(pt_blocks[2]))
a1 = bytes.hex(b[0])
a2 = bytes.hex(b[1])
print(a1, a2)
