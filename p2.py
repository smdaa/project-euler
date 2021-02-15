#Even Fibonacci numbers
#Problem 2

def fibonacci(n):
    if (n < 2):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def compute():
    sum = 0
    i = 1
    j = fibonacci(i)
    while(j < 4000000):
        if not(j % 2):
            sum += j
        j = fibonacci(i)
        i += 1
    return sum 

if __name__ == "__main__":
	print(compute())
        