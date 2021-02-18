#Lattice paths
#Problem 15
def compute(n, m, i=0, j=0):
    return 1 + compute_rec(n, m)
    
    
def compute_rec(n, m, i=0, j=0):
    if (i == n  or j == m ):
        return 0
    elif (i == n - 1 and j < m -1):
        return 1 + compute_rec(n, m, i, j+1)
    elif (i < n - 1 and j == m -1):
        return 1 + compute_rec(n, m, i+1, j)
    else:
        return  1 + compute_rec(n, m, i+1, j) + compute_rec(n, m, i, j+1)

if __name__ == "__main__":
	print(compute(20, 20))
 