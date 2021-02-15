#Smallest multiple
#Problem 5

def pgcd(a, b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

def compute():
    res = 1
    for i in range(1,21):
        res *= i // pgcd(i, res)
    return res

if __name__ == "__main__":
	print(compute())