import random
a = []
print("Введите ранг квадратичной матрицы")
size=int(input()) 
for r in range(size):  
    a.append([])  
    for c in range(size):  
        a[r].append(random.randint(0,9))  
 
for r in a:
    print(r)

print(sum(sum([i for i in x])for x in a))
