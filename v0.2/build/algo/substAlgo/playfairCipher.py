import string
class playfairCipher:
    def __init__(self, message):
        self.message = message
    key="heyitssecretkey"

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

    global list
    list=[]
    def playfairEncrypt(self):
        key_matrix=self.encryption_key_generation()
        message_pairs=[]
        cipher_text_pairs=[]
        self.message=self.message.replace(" ","")
        self.message=self.message.lower()
        i=0
        cnt=0
        for x in self.message:
                if(not( ord(x)>=97 and ord(x)<=122)):
                    cnt=1
        while i<len(self.message):  
            a=self.message[i]
            b=''
            if((i+1)==len(self.message)):
                b='z'
                list.append(i+1)
            else:
                b=self.message[i+1]

            if(a!=b):
                message_pairs.append(a+b)
                i+=2
            else:
                message_pairs.append(a+'z')
                list.append(i+1)
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
        if(cnt==0):
           return ("".join(cipher_text_pairs)).upper() 
        else:
           return "ERROR: ONLY CHARACTERS ARE ALLOWED"   
        
        
    def decryption_key_generation(self):
        str=string.ascii_lowercase.replace('j','.')
        self.key=self.key.lower()
        key_matrix=['' for i in range(5)]
        i=0
        j=0
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
        key_matrix=self.decryption_key_generation()
        plain_text_pairs=[]
        cipher_text_pairs=[]
        cnt1=0
        self.message=self.message.lower()
        for x in self.message:
                if(not( ord(x)>=97 and ord(x)<=122)):
                    return "ERROR: ONLY CHARACTERS ARE ALLOWED"
        if(len(self.message)%2!=0):
            return "ERROR: CIPHER TEXT SHOULD ONLY BE OF EVEN LENGTH!"
        i=0
        while i<len(self.message):
            a=self.message[i]
            b=self.message[i+1]

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
        x="".join(plain_text_pairs).upper()
        list1=[]
        list1[:0]=x
        for j in list:
            x=list1[j]
            del list1[j]
            
        str=''
        for k in list1:
            str=str+k
        return str
              