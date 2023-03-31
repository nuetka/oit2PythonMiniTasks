my_len = [['БО-331101', ['Пкулова Алена', 'Бабушкина Ксения', 'GHg GHJggh']],['БОВ-421102',['Пhgj Аvcbnvc']]]
for i in my_len:
    for k in i[1]:
        flag=0
        arr=k.split(" ")
        if arr[0][0]=='П':
            if arr[1][0]=='А':
                 if flag==0:
                   print(i[0])
                   print(k)
                   flag=1
                 else:  print(k)
                 
       