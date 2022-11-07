class railfenceCipher:
    def __init__(self, message):
        self.message = message
    key=3
    # function to encrypt a message
    def encryptMessage(self):
        rail = [['\n' for i in range(len(self.message))]
                    for j in range(self.key)]
        
        # to find the direction
        dir_down = False
        row, col = 0, 0
        
        for i in range(len(self.message)):
            if (row == 0) or (row == self.key - 1):
                dir_down = not dir_down
            
            # fill the corresponding alphabet
            rail[row][col] = self.message[i]
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        result = []
        for i in range(self.key):
            for j in range(len(self.message)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return("" . join(result).upper())
        
    def decryptMessage(self):
        rail = [['\n' for i in range(len(self.message))]
                    for j in range(self.key)]
        
        # to find the direction
        dir_down = None
        row, col = 0, 0
        
        # mark the places with '*'
        for i in range(len(self.message)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False
            
            # place the marker
            rail[row][col] = '~'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
        index = 0
        for i in range(self.key):
            for j in range(len(self.message)):
                if ((rail[i][j] == '~') and
                (index < len(self.message))):
                    rail[i][j] = self.message[index]
                    index += 1
            
        result = []
        row, col = 0, 0
        for i in range(len(self.message)):
            
            # check the direction of flow
            if row == 0:
                dir_down = True
            if row == self.key-1:
                dir_down = False
                
            # place the marker
            if (rail[row][col] != '~'):
                result.append(rail[row][col])
                col += 1
                
            # find the next row using
            # direction flag
            if dir_down:
                row += 1
            else:
                row -= 1
        return("".join(result).upper())