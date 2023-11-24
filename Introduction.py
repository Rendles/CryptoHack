
############################################## ASCII TO STRING ######################################################
asciiToString = []

ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for _ in range(len(ascii)):
    asciiToString.extend(chr(ascii[_]))

print("ASCII TO STRING:")
print(asciiToString, "\n")
#####################################################################################################################


############################################### HEX TO BYTES ########################################################
hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
hexToBytes = bytes.fromhex(hex)

print("BYTES FROM HEX:")
print(hexToBytes, "\n")
#####################################################################################################################


################################## HEX TO BYTES TO BASE64 ###########################################################
import base64

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

hexToBytes = bytes.fromhex(hex)
bytesToBase64 = base64.b64encode(hexToBytes)

print("HEX TO BYTES TO BASE64:")
print(bytesToBase64, "\n")
#####################################################################################################################


################################# BASE TO MSG #######################################################################
from Crypto.Util.number import *

base10 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
longToBytes = long_to_bytes(base10)

print("BASE TO BYTES:")
print(longToBytes, "\n")
#####################################################################################################################


################################################### XOR #############################################################
from pwn import *
str1 = 'label'
str2 = "13"
new_string = ""
for _ in str1:
    new_string += chr(ord(_) ^ 13)

str1ToBytes = [ord(item) for item in str1]
str2ToBytes = [ord(item) for item in str2]

newStr = xor(str1ToBytes, str2ToBytes)
print(new_string + "123 ")
#####################################################################################################################


####################################### XOR PROPS ###################################################################
Key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
Key2Key1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
Key2Key3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FlagKey1Key3Key2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

hexToBytes = bytes.fromhex(Key1)
hexToBytes2 = bytes.fromhex(Key2Key1)
hexToBytes3 = bytes.fromhex(Key2Key3)
hexToBytes4 = bytes.fromhex(FlagKey1Key3Key2)

print(hexToBytes, '\n', hexToBytes2, '\n', hexToBytes3, '\n', hexToBytes4, '\n')

Key2 = xor(hexToBytes, hexToBytes2)
Key3 = xor(hexToBytes3, Key2)
Key123 = xor(hexToBytes, hexToBytes3)
Flag = xor(Key123, hexToBytes4)
print(Flag)
print('\n')
#####################################################################################################################


########################################### LOVELY BYTE #############################################################
Str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# for _ in range(100):
#     new_str = xor(Str, _)
#     print(new_str)

print('Загадка Жака Фреско')
print(Str, '\n')
#####################################################################################################################


################################ LAST ###############################################################################

Str = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# print(Str)
Str1 = b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]"
Str2 = b"\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e"
Str3 = b"\x07~&4Q\x15\x01\x04"
PartOfAnswer = 'crypto{'
b = []
key1 = 'myXORkey'

for _ in range(len(key1)):
    b.extend(long_to_bytes(ord(key1[_])))
    # b += long_to_bytes(ord(PartOfAnswer[_]))



# key = xor(Str1, b)
answer = xor(b, Str)
print("Answer: ", answer)

# print('\n')
# print(Str)
# for _ in range(256):A
#     new_str = xor(Str, _)




#####################################################################################################################