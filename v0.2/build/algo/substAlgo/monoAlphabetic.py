from operator import invert


class monoAlphabetic:
    def __init__(self,message):
        self.message = message        
            
    monoAlphabeticKey = {
            'A': 'N',
            'B': 'M',
            'C': 'B',
            'D': 'V',
            'E': 'C',
            'F': 'X',
            'G': 'Z',
            'H': 'A',
            'I': 'S',
            'J': 'F',
            'K': 'D',
            'L': 'G',
            'M': 'H',
            'N': 'K',
            'O': 'J',
            'P': 'L',
            'Q': 'P',
            'R': 'O',
            'S': 'I',
            'T': 'Y',
            'U': 'U',
            'V': 'T',
            'W': 'R',
            'X': 'W',
            'Y': 'E',
            'Z': 'Q',
        }
    
    def encryptWithMonoalphabetic(self):
        self.message = self.message.upper()
        encryptedMessage = []
        for letter in self.message:
            encryptedMessage.append(self.monoAlphabeticKey.get(letter, letter))
        print("Reached here")
        return ''.join(encryptedMessage)
    
    def inverseMonoalphaKey(monoAlphabeticKey):
        inverseKey = {}
        for key, value in monoAlphabeticKey.items():
            inverseKey[value] = key
        return inverseKey
    
    decryptionKey = inverseMonoalphaKey(monoAlphabeticKey)
            
    def decryptWithMonoalphabetic(self):
        self.message = self.message.upper()
        decryptedMessage = []
        for letter in self.message:
            decryptedMessage.append(self.decryptionKey.get(letter, letter))
        return ''.join(decryptedMessage)

