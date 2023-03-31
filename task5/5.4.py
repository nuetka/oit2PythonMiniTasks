import csv
import os
myDirectory = "C:/Users/777/Desktop/pythonLaba2/students.csv"
 
with open(myDirectory, "r", encoding="cp1251") as f:
    supList = f.readlines()
 
arr = [0] * len(supList)
 
for i in range(len(supList)):
    arr[i] = [0] * 4
 
b_index = 0
str1 = ""
 
for i in range(len(supList)):
    str1 = supList[i][: len(supList[i]) - 2] + ";"
    b_index = 0
    for j in range(4):
        arr[i][j] = str1[b_index: str1.index(";")]
        b_index = str1.index(";")
        str1 = str1[: b_index] + str1[b_index + 1:]

def custom_key(people):
     return people[3].split('-')[1]    
arr.sort(key=custom_key)
print("Информация о студентах, отсортированных по номеру группы:")
 
for i in range(len(supList)):
    
        print(arr[i][0], arr[i][1], arr[i][2], arr[i][3])

print("Введите название группы, в которой нужно к возрасту всех студентов прибавить 1!!")
group = input()
print(group)
for i in range(len(supList)):
     print(arr[i][3])
     if arr[i][3]==group:
          numm=int(arr[i][2])
          numm+=1
          arr[i][2]=str(numm)

print("Новый список!")
for i in range(len(supList)):
        print(arr[i][0], arr[i][1], arr[i][2], arr[i][3])
os.remove("students.csv")


with open(myDirectory, "w", encoding="cp1251") as file:
                writer=csv.writer(file, delimiter=';')
                for a in arr:
                    writer.writerow( 
                        a 
                    )
