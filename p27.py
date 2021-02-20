#Quadratic primes
#Problem 27

def is_prime(n):
    for i in range(2, n//2 + 1):
        if (n % i == 0):
            return False
    return True

def un(a, b, n):
    return (n ** 2) + a * n + b
    
def compute(r):
    max = 0
    res = 0
    for a in range(-r, r + 1):
        for b in range(-r, r + 1):
            n = 0
            temp = 0
            while(is_prime(un(a, b, n))):
                temp +=1
                n += 1
            if temp > max:
                max = temp
                res = a * b
    return res 
            
if __name__ == "__main__":
	print(compute(1000))
