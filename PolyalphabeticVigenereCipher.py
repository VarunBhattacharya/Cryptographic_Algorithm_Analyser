from operator import invert


class PolyalphabeticVigenereCipher:
    def __init__(self,message):
        self.message = message        

    
    key = 'heyitssecretkey'

 
    
    
    def encryptWithVigenere(self):
        self.message = self.message.lower()
        while(len(self.message) > len(self.key)):
            self.key+=self.key

        cipherText=""
        j =0
        for i in range(len(self.message)):
            if self.message[i].isalpha(): 
                k1=ord(self.message[i])-97
                k2=ord(self.key[j])-97
                s=chr((k1+k2)%26+97)
                cipherText+=s
                j=j+1
            else:
                cipherText+= self.message[i]
                
        return cipherText
    

    

            
    def decryptWithVigenere(self):
        self.message = self.message.lower()
        while(len(self.message) > len(self.key)):
            self.key+=self.key
            
        planeText=""
        j=0
        for i in range(len(self.message)):
            if self.message[i].isalpha(): 
                k1=ord(self.message[i])-97
                k2=ord(self.key[j])-97
                s=chr((((k1-k2)+26)%26)+97)
                planeText+=s
                j=j+1
            else:
                planeText+= self.message[i]

        return planeText
        





