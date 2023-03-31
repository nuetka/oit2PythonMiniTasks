import re
import csv
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

print("Введите название группы в которой нужно прибавить к возрасту всех студентов 1")
group=input()
for tuple in sorted_tuples:
      if group==tuple[1][2]:
            num=int(tuple[1][1])+1
            tuple[1][1]=str(num)
            print(tuple[0] + ' ' + tuple[1][0]+' ' +tuple[1][1] + ' '+ tuple[1][2])

#os.remove("students.csv")
print(sorted_tuples)
mass=[0]*len(d)
for i in range(len(d)):
    mass[i] = [0] * 4

i=0
for tuple in sorted_tuples:
                mass[i][0]=tuple[0]
                mass[i][1]=tuple[1][0]
                mass[i][2]=tuple[1][1]
                mass[i][3]=tuple[1][2]
                print(mass[i])
                i=i+1
print(mass)
              
       
with open(myDirectory, "w", encoding="cp1251") as file:
                writer=csv.writer(file, delimiter=';')
                for a in mass:
                    writer.writerow( 
                        a 
                    )
