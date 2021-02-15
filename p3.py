#Largest prime factor
#Problem 3

def is_prime(n):
    for i in range(2, n - 1):
        if (n % i == 0):
            return False
    return True

def compute():
    n = 600851475143
    max = 1
    for i in range(2, n - 1):
        if (is_prime(i) and n % i == 0):
            if (max < i):
                max = i
    return max

if __name__ == "__main__":
	print(compute())
