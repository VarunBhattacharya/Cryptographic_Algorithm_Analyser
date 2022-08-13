import string
class playfairCipher:
    def __init__(self, message,key,cipher_text):
        self.message = message
        self.key = key
        self.cipher_text=cipher_text

    def encryption_key_generation(self):
        str=string.ascii_lowercase.replace('j','.')
        self.key=self.key.lower()
        key_matrix=['' for i in range(5)]
        i=0;j=0
        for c in self.key:
            if c in str:
                key_matrix[i]+=c
                str=str.replace(c,'.')
                j+=1
                if(j>4):
                    i+=1
                    j=0
        for c in str:
            if c!='.':
                key_matrix[i]+=c

                j+=1
                if j>4:
                    i+=1
                    j=0
                    
        return(key_matrix)


    def playfairEncrypt(self):
        message_pairs=[]
        cipher_text_pairs=[]
        self.message=self.message.replace(" ","")
        self.message=self.message.lower()
        i=0
        while i<len(self.message):
            a=self.message[i]
            b=''

            if((i+1)==len(self.message)):
                b='x'
            else:
                b=self.message[i+1]

            if(a!=b):
                message_pairs.append(a+b)
                i+=2
            else:
                message_pairs.append(a+'x')
                i+=1
                
        for pair in message_pairs:
            flag=False
            for row in key_matrix:
                if(pair[0] in row and pair[1] in row):
                    j0=row.find(pair[0])
                    j1=row.find(pair[1])
                    cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
                    cipher_text_pairs.append(cipher_text_pair)
                    flag=True
            if flag:
                continue
                    
            for j in range(5):
                col="".join([key_matrix[i][j] for i in range(5)])
                if(pair[0] in col and pair[1] in col):
                    i0=col.find(pair[0])
                    i1=col.find(pair[1])
                    cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                    cipher_text_pairs.append(cipher_text_pair)
                    flag=True
            if flag:
                continue

            i0=0
            i1=0
            j0=0
            j1=0

            for i in range(5):
                row=key_matrix[i]
                if(pair[0] in row):
                    i0=i
                    j0=row.find(pair[0])
                if(pair[1] in row):
                    i1=i
                    j1=row.find(pair[1])
            cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
            cipher_text_pairs.append(cipher_text_pair)
        return ("".join(cipher_text_pairs)).upper()    
        
        
    def decryption_key_generation(self):
        str=string.ascii_lowercase.replace('j','.')
        self.key=self.key.lower()
        
        key_matrix=['' for i in range(5)]
        i=0;j=0
        for c in self.key:
            if c in str:
                key_matrix[i]+=c
                str=str.replace(c,'.')
                j+=1
                if(j>4):
                    i+=1
                    j=0
        for c in str:
            if c!='.':
                key_matrix[i]+=c

                j+=1
                if j>4:
                    i+=1
                    j=0
                    
        return(key_matrix)

    def playfairDecrypt(self):
        plain_text_pairs=[]
        cipher_text_pairs=[]
        self.cipher_text=self.cipher_text.lower()
        i=0
        while i<len(self.cipher_text):
            a=self.cipher_text[i]
            b=self.cipher_text[i+1]

            cipher_text_pairs.append(a+b)
            i+=2


        for pair in cipher_text_pairs:
            flag=False
            for row in key_matrix:
                if(pair[0] in row and pair[1] in row):
                    j0=row.find(pair[0])
                    j1=row.find(pair[1])
                    plain_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
                    plain_text_pairs.append(plain_text_pair)
                    flag=True
            if flag:
                continue
                    
            for j in range(5):
                col="".join([key_matrix[i][j] for i in range(5)])
                if(pair[0] in col and pair[1] in col):
                    i0=col.find(pair[0])
                    i1=col.find(pair[1])
                    plain_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
                    plain_text_pairs.append(plain_text_pair)
                    flag=True
            if flag:
                continue

            i0=0
            i1=0
            j0=0
            j1=0

            for i in range(5):
                row=key_matrix[i]
                if(pair[0] in row):
                    i0=i
                    j0=row.find(pair[0])
                if(pair[1] in row):
                    i1=i
                    j1=row.find(pair[1])
            plain_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
            plain_text_pairs.append(plain_text_pair)
        return ("".join(plain_text_pairs)).upper()

if __name__ == "__main__":
    key=input("Enter the key: ")
    message=input("Enter the message: ")
    cipher_text=''
    obj = playfairCipher(message,key,cipher_text)
    key_matrix=obj.encryption_key_generation()
    print(obj.playfairEncrypt())
    cipher_text=input("Enter the encrypted message: ")
    obj = playfairCipher(message,key,cipher_text)
    key_matrix=obj.decryption_key_generation()
    print(obj.playfairDecrypt())
    
