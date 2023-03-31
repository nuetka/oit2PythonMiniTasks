list = ['redr', 'blue', 'ruler', '1redrp'] 
print("Исходный список",list)
for str in list:
    if str[len(str)-1] == 'r': 
        print(str)