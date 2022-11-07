#Import necessary modules
from Crypto.Cipher import AES

class aesCipher:
    def __init__(self, message):
        self.message = message
        self.key = b'SecretCodeSECcoD'
        self.nonce = b'-\xfb\x16$&\x04\xa9\x19\x91\xb6\xf5&b\xbf\x16' #Generate nonce -- random value each time we instantiate AES object
    
    def encryptMessage(self):
        cipher = AES.new(self.key, AES.MODE_EAX) #Create AES object
        encText = cipher.encrypt(self.message.encode()) #Encrypt message
        return encText
    
    def decryptMessage(self):
        deCipher = AES.new(self.key, AES.MODE_EAX, nonce = self.nonce) #Create AES object
        decText = deCipher.decrypt(self.message.encode()) #Decrypt message
        return str(decText)


# if __name__ == '__main__':
#     message = 'VarunBhattachary'
#     obj = aesCipher(message)
#     print(obj.encryptMessage())
#     print(obj.decryptMessage())
