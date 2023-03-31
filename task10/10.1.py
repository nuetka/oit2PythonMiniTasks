from random import randint
matrix=[[randint(1,9) for _ in range(8)] for i in range(8)]

for a in matrix:
       print(a)
print(' ')
for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        if k%2==0:
            matrix[i][k]=matrix[i][k]**2
for a in matrix:
       print(a)