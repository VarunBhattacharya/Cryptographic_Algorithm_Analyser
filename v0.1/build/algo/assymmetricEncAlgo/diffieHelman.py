from math import sqrt
import random

class Diffie_Hellman:
    def __init__(self, p):
        self.p = p
    
    
    def isprime(n):

        if (n <= 1):
            return False
        if (n <= 3):
            return True
    

        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0) :
                return False
            i = i + 6
    
        return True
    
        
    def find_prime_factors(s, n) :
        
        while (n % 2 == 0) :
            s.add(2)
            n = n // 2
    
        for i in range(3, int(sqrt(n)), 2):
            while (n % i == 0) :
                s.add(i)
                n = n // i
            
        if (n > 2) :
            s.add(n)
    
    
    def find_primitive( n) :
        s = set()
    
        if (Diffie_Hellman.isprime(n) == False):
            return -1
    
        phi = n - 1
    
        Diffie_Hellman.find_prime_factors(s, phi)
    
        for r in range(2, phi + 1):
            flag = False
            for it in s:
                if (pow(r, phi // it, n) == 1):
                    flag = True
                    break
                
            if (flag == False):
                return r
    
        return -1


    

    def diffie_hellman(self):
        
        try:
            p= int(self.p)
            if not Diffie_Hellman.isprime(int(p)):
                msg="Number should be prime"
                return msg
            g=Diffie_Hellman.find_primitive(p)
            #here for us value of g is samlles primitive root of p 
            a=random.randint(1, 1000)
            b=random.randint(1,1000)
            A = ((pow(g, a)) % p)           
            B = ((pow(g, b)) % p)
            Ka = ((pow(B, a)) % p)
            Kb = ((pow(A, b)) % p)

            res = f"A = {A}, B = {B}, Ka = {Ka}, Kb = {Kb}"

            return res
        ##print that return values are in sequence of A,B,Ka,Kb
        except:
            err = "Input Should be Prime Number"
            return err

    
    

# if __name__ == "__main__":
#     print("enter key")
#     strInp = input()
#     obj = Diffie_Hellman(strInp)
#     print(obj.diffie_hellman())
    