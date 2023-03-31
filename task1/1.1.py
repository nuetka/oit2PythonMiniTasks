print("Введите a")
a=int(input())
print("Введите b")
b=int(input())
print("Введите c")
c=int(input())
if (a==c): #проверка делимости на 0
    print("Нельзя посчиать выражение!")
else:
    s=abs(1-a*(b**c)-a*(b**2-c**2)+(b-c+a)*(12+b)/(c-a))
    print("s = ", s)