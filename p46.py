#Goldbach's other conjecture
#Problem 46

def is_prime(n):
    for i in range(2, n//2 + 1):
        if (n % i == 0):
            return False
    return True

def goldbach_conj(n):
    i = 1
    while (True):
        k = n - 2 * i * i
        if (k <= 0):
            return False
        elif is_prime(k):
            return True
        i += 1
        
def compute():
    i = 9
    while(goldbach_conj(i)):
        while(not is_prime(i)):
            i += 1
    return i
    
if __name__ == "__main__":
	print(compute())
