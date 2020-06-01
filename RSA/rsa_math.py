import random 

class RSAmath():

    def generate_pq(self, key_size):
        p = self.generate_prime_number(key_size // 2)
        q = self.generate_prime_number(key_size // 2)
        while p == q:
            q = self.generate_prime_number(key_size // 2)
        return p, q
    
    def generate_prime_number(self, bit_length):
        while True:
            temp = random.getrandbits(bit_length)
            if self.is_prime(temp, 10):
                prime_number = temp
                return prime_number
            
    def is_prime(self, p, n):
        if (n <= 1 or n == 4): 
            return False
        if (n <= 3): 
            return True

        d = p - 1 
        while (d % 2 == 0): 
            d //= 2 

        for i in range(n): 
            if (self.millerTest(d, p) == False): 
                return False 
        return True 

    def millerTest(self, d, p): 
        a = random.randint(2, p-2)
        x = pow(a, d, p)
        if (x == 1 or x == p - 1): 
            return True 

        while (d != p - 1): 
            x = pow(x,2,p)
            d *= 2 
            if (x == 1): 
                return False
            if (x == p - 1): 
                return True 
        return False 

    def greatest_common_divisor(self, a, b):
        while b:
            a, b = b, a%b
        return a

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            b_div_a, b_mod_a = divmod(b, a)
            g, x, y = self.egcd(b_mod_a, a)
            return (g, y-b_div_a*x, x)

    def modular_inverse(self, a, m):
        g, x, _ = self.egcd(a, m)
        if g != 1:
            raise Exception('gcd(a, b) != 1')
        return x % m
    