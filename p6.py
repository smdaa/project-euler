#Sum square difference
#Problem 6

def compute():
    s1 = 0
    s2 = 0
    for i in range(1, 101):
        s1 += i ** 2
        s2 += i
    s2 = s2** 2

    return s2 - s1

if __name__ == "__main__":
	print(compute())
