myDirectory = "C:/Users/777/Desktop/pythonLaba2/students.csv"
 
with open(myDirectory, "r", encoding="cp1251") as f:
    supList = f.readlines()
f.close()
 
for string in supList :
    print( string )
 
arr = [0] * len(supList)
print ( "sup list" + str(arr) )
 
for i in range(len(supList)):
    arr[i] = [0] * 4
print( "new sup list" + str(arr) + "\n" )
print( "dlina spiska = " + str(len(supList)) )
 
b_index = 0
str1 = ""
 
for i in range(len(supList)):
    str1 = supList[i][: len(supList[i]) - 2] + ";"
    print( "stroka = " + str(str1) + "\n" )
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

