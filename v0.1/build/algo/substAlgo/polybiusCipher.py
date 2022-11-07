class polybiusCipher:
    def __init__(self, message):
        self.message = message

    mainArr = [['a','b','c','d','e'],
                ['f','g','h','i/j','k'], 
                ['l','m','n','o','p'], 
                ['q','r','s','t','u'], 
                ['v','w','x','y','z']]

    def encryptMessage(self):
        self.message = self.message.strip().lower()
        self.message = self.message.replace('/','')
        outputArray = []
        for char in self.message:
            #ignoring all other characters
            if 0<=ord(char)<=47 or 58<=ord(char)<=64 or 91<=ord(char)<=96 or 123<=ord(char)<=127:
                outputArray.append(00)
                continue  

            row = int((ord(char) - ord('a')) / 5) + 1 #get row value
            col = ((ord(char) - ord('a')) % 5) + 1 #get col value

            if char == 'k': #char is k
                row = row - 1
                col = 5 - col + 1

            elif ord(char) >= ord('j'): #char greater than j
                if col == 1 :
                    col = 6
                    row = row - 1
                col = col - 1
                     
            outputArray.append(int(str(row) + str(col)))
        outputArray = [str(i) for i in outputArray]
        res = ''.join(outputArray)
        return res

    def decryptMessage(self):
        flg = 0
        if self.message:
            for i in self.message:
                if 48<=ord(i)<=57:
                    flg += 1
            if flg == len(self.message):
                self.message = self.message.strip()
                self.message = self.message.replace(' ', '')
                inpArray = [int(i) for i in self.message]
                if len(inpArray) % 2 == 1:
                    inpArray.append(0)
                outArray = []
                for i in range(0,len(inpArray),2):
                    row = inpArray[i]
                    col = inpArray[i+1]
                    outArray.append(self.mainArr[row-1][col-1])
                    i += 2
                res = ''.join(outArray)
                return res.upper()
            else:
                return "Invalid Input"


if __name__ == "__main__":
    message = 'varun'
    mes = '5111424533'
    obj = polybiusCipher(message)
    obj1 = polybiusCipher(mes)
    print(obj.encryptMessage())
    print(obj1.decryptMessage())
