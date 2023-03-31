import re
str = "Я\nучу; язык,программирования\nPython"
allwords=re.split(";|,|\n", str)
res=[word for word in allwords if 4<len(word)<11]
print(*res)