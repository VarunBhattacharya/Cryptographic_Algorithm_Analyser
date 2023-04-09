from math import sqrt
#required for the sqrt() function, if you want to avoid doing **0.5
import random
#required for randrange
from random import randint as rand

#just to use the well known keyword rand() from C++
class rsa:
    bit_length = 4
    p = rand(1, 1000)
    q = rand(1, 1000)
    def __init__(self,message):
        self.message=message
    def gcd(self,a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


    def mod_inverse(self,a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1


    def isprime(self,n):
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
        return True


    #initial two random numbers p,q
    p = rand(1, 1000)
    q = rand(1, 1000)


    def generate_keypair(self,p, q, keysize):
        # keysize is the bit length of n so it must be in range(nMin,nMax+1).
        # << is bitwise operator
        # x << y is same as multiplying x by 2**y
        # i am doing this so that p and q values have similar bit-length.
        # this will generate an n value that's hard to factorize into p and q.

        nMin = 1 << (keysize - 1)
        nMax = (1 << keysize) - 1
        primes = [2]
        # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
        start = 1 << (keysize // 2 - 1)
        stop = 1 << (keysize // 2 + 1)

        if start >= stop:
            return []

        for i in range(3, stop + 1, 2):
            for p in primes:
                if i % p == 0:
                    break
            else:
                primes.append(i)

        while (primes and primes[0] < start):
            del primes[0]

        #choosing p and q from the generated prime numbers.
        while primes:
            p = random.choice(primes)
            primes.remove(p)
            q_values = [q for q in primes if nMin <= p * q <= nMax]
            if q_values:
                q = random.choice(q_values)
                break
        print(p, q)
        n = p * q
        phi = (p - 1) * (q - 1)

        #generate public key 1<e<phi(n)
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)

        while True:
            #as long as gcd(1,phi(n)) is not 1, keep generating e
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)
            #generate private key
            d = self.mod_inverse(e, phi)
            if g == 1 and e != d:
                break

        #public key (e,n)
        #private key (d,n)

        return ((e, n), (d, n))
    # bit_length = 4
    # p = rand(1, 1000)
    # q = rand(1, 1000)
    # public,private=generate_keypair(p,q,2**bit_length)
    
    
    def encrypt(self,public):
        #unpack key value pair
        e, n = public
        msg_ciphertext = [pow(ord(c), e, n) for c in self.message]
        # return msg_ciphertext
        return ''.join(map(lambda x: str(x), msg_ciphertext))


    def decrypt(self,private):
        d, n = private
        msg_plaintext = [chr(pow(int(c), d, n)) for c in self.message.split(",")]
        # No need to use ord() since c is now a number
        # After decryption, we cast it back to character
        # to be joined in a string for the final result
        return (''.join(msg_plaintext))


#-------------------------------------------------------------
# #driver program
# if __name__ == "__main__":
#     bit_length = 4
#     p = rand(1, 1000)
#     q = rand(1, 1000)
#     msg = input()
#     obj=rsa(msg)
#     public, private = obj.generate_keypair(p, q, (2**bit_length))
#     msg_ciphertext,output=(obj.encrypt(public))
#     print(output)
#     print(msg_ciphertext)
#     msg=input()
#     obj2=rsa(msg)
#     print(obj2.decrypt(private))
    