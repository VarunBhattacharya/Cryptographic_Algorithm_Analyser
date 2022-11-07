# Include libraries
import math


class columnarCipher:
    def __init__(self, message):
        self.message = message
        self.key = "Encryptio"

    def encryptMessage(self):
        cipher = ""

        k_indx = 0 #track key indices

        msg_len = float(len(self.message))
        msg_lst = list(self.message)
        key_lst = sorted(list(self.key))

        col = len(self.key) #calculate column of the matrix

        row = int(math.ceil(msg_len / col)) #calculate maximum row of the matrix

        fill_null = int((row * col) - msg_len) #add the padding character '_' in empty the empty cell of the matix
        msg_lst.extend('_' * fill_null)

        #create Matrix and insert message and padding characters row-wise
        matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

        #read matrix column-wise using key
        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] for row in matrix])
            k_indx += 1

        return cipher.upper()

    def decryptMessage(self):
        msg = ""
        k_indx = 0 #track key indices

        msg_indx = 0 #track msg indices
        msg_len = float(len(self.message))
        msg_lst = list(self.message)

        col = len(self.key) #calculate column of the matrix

        row = int(math.ceil(msg_len / col)) #calculate maximum row of the matrix

        key_lst = sorted(list(self.key))

        dec_cipher = []
        for _ in range(row): dec_cipher += [[None] * col]

        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try: msg = ''.join(sum(dec_cipher, []))
        except TypeError: raise TypeError("Repetition in Key")

        null_count = msg.count('_')

        if null_count > 0: return msg[: -null_count]

        return msg.upper()
