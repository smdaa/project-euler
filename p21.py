#Amicable numbers
#Problem 21

def amical(a, b):
    sum_a = 0
    sum_b = 0
    for i in range(1, (a // 2) + 1):
        if not(a % i):
            sum_a += i
    for i in range(1, (b // 2) + 1):
        if not(b % i):
            sum_b += i
    return sum_a == b and sum_b == a 
    
def compute(n):
    sum = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            if amical(i, j):
                sum += (i + j)
    return sum

if __name__ == "__main__":
	print(compute(500))
