#Lychrel numbers
#Problem 55

def aux(n):
    temp = n
    i = 0
    while(temp > 0):
        i += 1
        temp = temp // 10
    return i

def reverse(n):
    temp = n
    n_inv = 0
    l = aux(n)
    i = 0
    while(temp > 0):
        r = temp % 10
        temp = temp // 10
        n_inv += r * (10 ** (l - i - 1))
        i += 1
    return n_inv

def one_iter_lychrel(n):
    temp = n + reverse(n)
    temp_rev = reverse(temp)
    return temp == temp_rev

def lychrel(n):
    iter = 1
    temp = n
    while(iter <= 50 and (not one_iter_lychrel(temp))):
        temp += reverse(temp)
        iter += 1
    if (iter > 50):
        return False
    return True

def compute():
    res = 0
    for i in range(10000):
        if (lychrel(i)):
            res += 1
    return 10000 - res

if __name__ == "__main__":
	print(compute())
