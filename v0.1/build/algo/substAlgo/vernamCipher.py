#Import Libraries
from vernamcipher.cryptographic import Cryptographic

class vernamCipher:
    def __init__(self, message):
        self.message = message
        self.key = "SecretCodeSecretCodeSecretCode"
    
    def encryptMessage(self):
        return Cryptographic.exclusive_operations(self.message, self.key)
    
    def decryptMessage(self):
        return Cryptographic.exclusive_operations(self.message, self.key)

# if __name__ == "__main__":
#     message = "This is a test"
#     obj = vernamCipher(message)
#     print(obj.encryptMessage())
#     obj2 = vernamCipher(obj.encryptMessage())
#     print(obj2.decryptMessage())