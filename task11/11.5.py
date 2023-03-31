import re
import csv
dir1 = "C:/Users/777/Desktop/pythonLaba2/11.1.csv"
dir2="C:/Users/777/Desktop/pythonLaba2/11.2.csv"
dir3="C:/Users/777/Desktop/pythonLaba2/11.3.csv"
 
with open(dir1, "r", encoding="cp1251") as f:
    supList = f.readlines()
f.close()
 

content={ }
for string in supList:
    oh=re.split(";|\n| ", string)
    if(len(oh)<6): break
    content[oh[0]]=[oh[1],oh[2], oh[3], oh[4], oh[5]]
print(content)  



with open(dir2, "r", encoding="cp1251") as f:
    List = f.readlines()
f.close()
 

author={ }
for string in List:
    oh=re.split(";|\n| ", string)
    if(len(oh)<4): break
    author[oh[0]]=[oh[1],oh[2], oh[3]]
print(author)  



with open(dir3, "r", encoding="cp1251") as f:
    supL = f.readlines()
f.close()
 
menu={ }
for string in supL:
    oh=re.split(";|\n| ", string)
    if(len(oh)<2): break
    menu[oh[0]]=[oh[1]]
print(menu)  
              

with open(dir1, "w", encoding="cp1251") as file:
                writer=csv.writer(file, delimiter=';')
                for key in content.keys():
                    writer.writerow( 
                        [key]+content[key]
                    )
with open(dir2, "w", encoding="cp1251") as file:
                writer=csv.writer(file, delimiter=';')
                for key in author.keys():
                    writer.writerow( 
                        [key]+author[key]
                    )
with open(dir3, "w", encoding="cp1251") as file:
                writer=csv.writer(file, delimiter=';')
                for key in menu.keys():
                    writer.writerow( 
                        [key]+menu[key]
                    )                    