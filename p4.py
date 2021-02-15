#Largest palindrome product
#Problem 4

def aux(n):
    temp = n
    i = 0
    while(temp > 0):
        i += 1
        temp = temp // 10
    return i

def is_palindrome(n):
    temp = n
    n_inv = 0
    l = aux(n)
    i = 0
    while(temp > 0):
        r = temp % 10
        temp = temp // 10
        n_inv += r * (10 ** (l - i - 1))
        i += 1
    return n_inv==n

def compute():
    max = 0
    for i in range(400):
        for j in range(400, 700):
            for k in range(700, 1000):
                x = i * j * k
                if (is_palindrome(x)):
                    if (max < x):
                        max = x
    return max

if __name__ == "__main__":
	print(compute())
