from random import randint
matrix=[[randint(1,9) for _ in range(8)] for i in range(8)]

for a in matrix:
       print(a)
print(' ')
sum=[0]*8
for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        if  matrix[i][k]%2==0:
            sum[k]+= matrix[i][k]
print(sum)