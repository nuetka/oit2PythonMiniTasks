import re
myDirectory = "C:/Users/777/Desktop/pythonLaba2/students.csv"
 
with open(myDirectory, "r", encoding="cp1251") as f:
    supList = f.readlines()
f.close()
 
d={ }
for string in supList:
    oh=re.split(";|\n| ", string)
    if(len(oh)<6): break
    fio=oh[1]+' '+ oh[2]+' ' +oh[3]
    d[oh[0]]=[fio, oh[4], oh[5]]
print(d)  

sorted_tuples = sorted(d.items(), key=lambda item: item[1][2].split("-")[1])

print("Информация о студентах, отсортированных по номеру группы:")
for tuple in sorted_tuples:
         ohh=tuple[1]
         print(tuple[0] + ' ' + tuple[1][0]+' ' +tuple[1][1] + ' '+ tuple[1][2])




