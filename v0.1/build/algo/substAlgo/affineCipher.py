class affineCipher:
    def __init__(self):
        pass

    def encryptChar(self, char):
        return chr((7 * ord(char) + 26) % 128)

    def encryptMessage(self, message):
        return ''.join(map(self.encryptChar, message))
    
    def decryptChar(self, char):
        return chr(15 * (ord(char) - 26) % 128)

    def decryptMessage(self, message):
        return ''.join(map(self.decryptChar, message))


if __name__ == "__main__":
    obj = affineCipher()
    print(obj.encryptMessage("Varun"))
    print(obj.decryptMessage('tA8M∟'))