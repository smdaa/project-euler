#Maximum path sum I
#Problem 18

a0 = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

def compute(a):
    n = len(a)
    a_new = a
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            a_new[i][j] += max(a[i + 1][j], a[i + 1][j + 1])
    return a_new[0][0]

    
if __name__ == "__main__":
	print(compute(a0))  
