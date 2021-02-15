#Summation of primes
#Problem 10

def is_prime(n):
    for i in range(2, n - 1):
        if (n % i == 0):
            return False
    return True

def compute():
    sum = 0
    for i in range(20000):
        if is_prime(i):
            sum += i
    return sum

if __name__ == "__main__":
	print(compute())
