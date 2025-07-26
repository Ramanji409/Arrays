def diagnals(matrix):
    n=len(matrix)
    primary=sum(matrix[i][i] for i in range(n))
    secondry=sum(matrix[i][n-i-1] for i in range(n))
    return abs(primary-secondry)
matrix=[[13,16,14],[15,110,17],[18,1,234]]
print(diagnals(matrix))