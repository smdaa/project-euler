#Triangular, pentagonal, and hexagonal
#Problem 45


def tn(n):
    return n * (n + 1) // 2

def pn(n):
    return n * (3 * n - 1) // 2

def hn(n):
    return n * (2 * n - 1)


def compute():
    i = 286
    j = 166
    k = 144
    ok = False
    while(not ok):
        triangle = tn(i)
        pentagon = pn(j)
        hexagon = hn(k)
        mi = min(triangle, pentagon, hexagon)
        ma = max(triangle, pentagon, hexagon)
        if (mi == ma):
            ok = True    
        else:
            if (mi == triangle):
                i += 1
            elif (mi == pentagon):
                j += 1
            else:
                k += 1
    return tn(i)
        
    
if __name__ == "__main__":
	print(compute())