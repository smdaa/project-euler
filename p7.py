#10001st prime
#Problem 7
from math import sqrt

def is_prime(n):
    for i in range(2, n - 1):
        if (n % i == 0):
            return False
    return True

def compute():
    n = 10001
    i = 2
    j = 1
    while(j <= n):
        if is_prime(i):
            print("i = ",i,"j = ",j)
            j += 1
        i += 1
    return i-1

if __name__ == "__main__":
	print(compute())
