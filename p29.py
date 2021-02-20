#Distinct powers
#Problem 29

def compute(r1, r2):
    temp = []
    for a in range(r1, r2 + 1):
        for b in range(r1, r2 +1):
            temp1 = a ** b
            temp2 = b ** a
            if not(temp1 in temp):
                temp.append(temp1)
            if not(temp2 in temp):
                temp.append(temp2)
    return len(temp)
                        
if __name__ == "__main__":
	print(compute(2, 100))
 