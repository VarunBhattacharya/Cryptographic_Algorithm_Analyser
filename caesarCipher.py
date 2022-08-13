class caesarCipher:
    def __init__(self, message):
        self.message = message
    key = 4

    def encrypt_char(self,c):
            return chr(ord('A') + (ord(c) - ord('A') + self.key)%26)
    
    def encrypt_message(self):
        self.message = self.message.upper()
        cipher_message = ''
        for c in self.message:
            if ((ord(c)>=65 and ord(c)<=90)):
                cipher_message += self.encrypt_char(c)
            else:
                cipher_message += c
        return cipher_message
    
    def decrypt_char(self,c):
            return chr(ord('A') + (ord(c) - ord('A') + 26 - self.key) % 26)
        
    def decrypt_message(self):
        self.message = self.message.upper()
        plain_text = ''
        for c in self.cipher:
            if ((ord(c)>=65 and ord(c)<=90)):
                plain_text += self.decrypt_char(c)
            else:
                plain_text += c
        return plain_text
