import random
import re
import csv
import os

def task1num1():
    print("Введите a")
    a=int(input())
    print("Введите b")
    b=int(input())
    print("Введите c")
    c=int(input())
    if (a==c): #проверка делимости на 0
        print("Нельзя посчиать выражение!")
    else:
        return abs(1-a*(b**c)-a*(b**2-c**2)+(b-c+a)*(12+b)/(c-a))
    
def task1num2(base):
    
    text = ''

    for elem in base:  

        if isinstance(elem, int) and elem % 2 == 0:  

            text += f'{elem} '  # Преобразуем из числа в строку и добавляем к переменной.

    return text
        
def task1num3(list):
    a=1
    n=0
    for i in list:
        if i < 10:
            a*=i
            n=n+1
    if n>0:
        print('Произведение чисел, которые меньше десяти, равно ',a)
    else:
        print('Не найдено элементов, которые меньше десяти')

def task1num4(list):
    [1,34,3,4,54,5,4]
    sum=0
    n=0
    for i in list:
        sum+=i
        n+=1
    srar=sum/n
    return srar       

def task2num1():
    my_number = 1000
    while True: 
        print("Введите число")
        user_number = int(input())
        if user_number == my_number:
            break
    print("Ввод окончен")

def task2num2(list): 
    print("Исходный список",list)
    for str in list:
        if str[len(str)-1] == 'r': 
            print(str)

def task2num3():
 
    a = [str(random.randint(0,9)) for i in range(5)]
    a.insert(random.randint(0,5), '3')
    print(''.join(a))    

def task2num4():
    x = 'порыв 25346 пы ЛЛ лл пырва  олав лоы цу34 4'
    y = []
    for i in x:
        if i == 'л':
            y.append(i)
        elif i=='Л':
            y.append(i)
    print(''.join(y))

def task3num1():
    str = "Я\nучу; язык,программирования\nPython"
    allwords=re.split(";|,|\n", str)
    res=[word for word in allwords if 4<len(word)<11]
    print(*res)    

def task3num2():
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    my_string = my_string.replace('_', '')
    my_string = my_string.split(';')
    
    print(my_string[0]+' '*10+my_string[1]+ ' '*10 + my_string[2] + ' '*15 + 'О студенте')
    print(my_string[5] + ' '*4 + my_string[6] + ' '*5 + my_string[7] + ' '*3 + my_string[9] + ',' + my_string[8])
    print(my_string[10] + ' '*4 + my_string[11] + ' '*4 + my_string[12] + ' '*3 + my_string[14] + ',' + my_string[13])


def task3num4():
    s = "Какой-то текст hxgd hsjdh"
    syms = len(s) 
    words = s.split(' ')
    lenn=len(words)
    print('Кол-во символов:', syms)
    print('Кол-во слов если разделить только пробел:', lenn) 

def task5num1():
    directory = 'C:/Users/777/Desktop/pythonLaba2/4'
    files = os.listdir(directory)
    print(len(files))

def task5num4():
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
    import os
    os.remove("students.csv")


    with open(myDirectory, "w", encoding="cp1251") as file:
                    writer=csv.writer(file, delimiter=';')
                    for a in arr:
                        writer.writerow( 
                            a 
                        )

print('task1num1',  task1num1())
print('task1num2', task1num2([6, 'hdj', 3, 'a', 10, 'asd', 1, 8]))
print('task1num3', task1num3([1, 211, 3, 811, 3911, 1911, 111, 100, 561]))
print('task1num4', task1num4([1,34,3,4,54,5,4]))
print('task2num1')
task2num1()
print('task2num2')
task2num2( ['redr', 'blue', 'ruler', '1redrp'] )
print('task2num3')
task2num3()
print('task2num4')
task2num4()
print('task3num1')
task3num1()
print('task3num2')
task3num2()
print('task3num4')
task3num4()
print('task5num1')
task5num1()
print('task5num4')
task5num4()
