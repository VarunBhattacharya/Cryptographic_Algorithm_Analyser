from Crypto.Cipher import DES
from secrets import token_bytes



class desCipher:
    def __init__(self, message):
        self.message = message
        self.key = b'Helloqwe'
        self.nonce = b'-\xfb\x16$&\x04\xa9\x19\x91\xb6\xf5&b\xbf\x16' #Generate nonce -- random value each time we instantiate AES object
    
    def encryptMessage(self):
        cipher = DES.new(self.key, DES.MODE_EAX) #Create AES object
        encText = cipher.encrypt(self.message.encode()) #Encrypt message
        return encText
    
    def decryptMessage(self):
        deCipher = DES.new(self.key, DES.MODE_EAX, nonce = self.nonce) #Create AES object
        decText = deCipher.decrypt(self.message.encode()) #Decrypt message
        return str(decText)



# if __name__ == '__main__':
#     message = 'Test1'
#     obj = desCipher(message)
#     print(obj.encryptMessage())
#     print(obj.decryptMessage())


# key = b'Helloqwe'

# def encrypt(msg):
#     cipher = DES.new(key, DES.MODE_EAX)
#     nonce = cipher.nonce
#     ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
#     return nonce, ciphertext, tag

# def decrypt(nonce, ciphertext, tag):
#     cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext)
#     try:
#         cipher.verify(tag)
#         return plaintext.decode('ascii')
#     except:
#         return False

# nonce, ciphertext, tag = encrypt(input('Enter a message: '))
# plaintext = decrypt(nonce, ciphertext, tag)

# print(f'Cipher text: {ciphertext}')
# print(key)

# if not plaintext:
#     print('Message is corrupted!')
# else:
#     print(f'Plain text: {plaintext}')