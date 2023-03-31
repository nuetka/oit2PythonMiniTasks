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
    
def task1num2():
    base=input().split(" ")
    text = ''
    for elem in base:  
        if elem.isdigit() and int(elem) % 2 == 0:  
            text += f'{elem} '  # Преобразуем из числа в строку и добавляем к переменной.
    print( text)
        
def task1num3():
    list=input().split(" ")
    a=1
    n=0
    for i in list:
        if int(i) < 10:
            a*=int(i)
            n=n+1
    if n>0:
        print('Произведение чисел, которые меньше десяти, равно ',a)
    else:
        print('Не найдено элементов, которые меньше десяти')

def task1num4():
    list=input().split(" ")
    sum=0
    n=0
    for i in list:
        sum+=int(i)
        n+=1
    srar=sum/n
    print( srar)       

while(True):
        print('0-выход из программы.1-вызов 1 функции.2-вызов второй функции.3-вызов третьей функции. 4- четвертой')
        a=input()
        if a=='0':
            break 

        elif a=='1': 
            task1num1()
            print('Вы хотите продолжить?')
            b=input()
            if b=='yes' or b=='Y' or b=='1': continue
            elif b=='no' or b=='N' or b=='0': break
        elif a=='2':
            task1num2()
            print('Вы хотите продолжить?')
            b=input()
            if b=='yes' or b=='Y' or b=='1': continue
            elif b=='no' or b=='N' or b=='0': break
        elif a=='3':
            task1num3()
            print('Вы хотите продолжить?')
            b=input()
            if b=='yes' or b=='Y' or b=='1': continue
            elif b=='no' or b=='N' or b=='0': break
        elif a=='4': 
            task1num4()
            print('Вы хотите продолжить?')
            b=input()
            if b=='yes' or b=='Y' or b=='1': continue
            elif b=='no' or b=='N' or b=='0': break
  
    