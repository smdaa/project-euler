#Special Pythagorean triplet
#Problem 9
from math import sqrt

def compute():
    a = 0
    b = 1
    c = sqrt(a**2 + b**2)
    for a in range(1, 1000 + 1):
        for b in range(a + 1, 1000 + 1):
            c = 1000 - a - b
            if (a ** 2 + b ** 2 == c ** 2):
                return a,b,c,


if __name__ == "__main__":
	print(compute())