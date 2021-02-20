#Powerful digit sum
#Problem 56

def sum_digits(n):
    temp = n
    i = 0
    while(temp > 0):
        i += temp % 10
        temp = temp // 10
    return i

def compute(r):
    max = 0
    for a in range(1, r):
        for b in range(1, r):
            temp = sum_digits(a ** b)
            if (temp > max):
                max = temp
    return max 
    
if __name__ == "__main__":
	print(compute(100))
