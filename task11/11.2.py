content={
    '1': ['Название контента1', 'Аннотация1', 'Содержимле1', '1', '2'],
    '2': ['Название контента2', 'Аннотация2', 'Содержимле2', '2', '2'],
    '3': ['Название контента3', 'Аннотация3', 'Содержимле3', '1', '1']
}

author={
    '1':['Ник1', 'Пароль1', 'Почта1'],
    '2':['Ник2', 'Пароль2', 'Почта2']
}

menu={
     '1':['Название1'],
     '2':['Название2']
}

def add():
    print("Введите данные для контента в строку через пробел")
    str=input()
    arr=str.split(" ")
    content[arr[0]]=[arr[1], arr[2], arr[3], arr[4], arr[5]]
    #был ли раеьше такой автор
    aadd=0
    menadd=0
    for a in author.keys():
        if a==arr[4]:
            aadd+=1
            break
    for m in menu.keys():
        if m == arr[5]:
            menadd+=1
            break  
    if aadd==0:
        print("Автор такой раньше не найден введите информаи о нем")
        strok=input()
        arik=strok.split()
        author[arr[4]]=[arik[0], arik[1], arik[2]]
    if menadd==0:
        print("Меню такого раньшн не найдено введите его надвание")
        naz=input()
        menu[arr[5]]=[naz]    


def delete():
    print("Введите индекс контента, который вы хотите удалить")  
    index=input()
    #с учетом того что связь многие ко многим удал оставшиеся без связей пунктц в меню и авторы
    m=0
    a=0
    for cont in content.keys():
        if index!=cont:
            if content[cont][3]==content[index][3]:
                a+=1
            if content[cont][4]==content[index][4]:
                m+=1    
    if a==0:
        del author[str(content[index][3])]
    if m==0:
         del menu[str(content[index][4])]    
    del content[index]  

def update():
    print("Введите индекс контента который хотите обновить")
    index=input()
    print("Введите новые данные")
    str=input()
    arr=str.split(" ")
    #были ли эти индексы раньше нет то добав если у прошлых нет связей то удал их
    content[index]=[arr[0], arr[1], arr[2], arr[3], arr[4]]
    a=0
    m=0
    for cont in content.keys():
        if index!=cont:
            if content[cont][3]==content[index][3]:
                a+=1
            if content[cont][4]==content[index][4]:
                    m+=1    
    countA=0
    countM=0       
    for key in author.keys():
            if key==content[index][3]:
                countA+=1
                break
    for key in menu.keys():
            if key==content[index][4]:
                countM+=1
                break               
    if countA==1:
        if a==0:
                del author[content[index][3]]
    if countM==1:   
        if m==0:
            del menu[content[index][4]]   

    auth=0
    for a in author.keys():
        if a==content[index][3]:
            auth+=1

    men=0
    for m in menu.keys():
        if m==content[index][4]:
            men+=1

    if auth==0:
        print("Автор с таким айди не найден введите информацию о нем!")  
        stringg=input()
        array=stringg.split()
        author[content[index][3]]=[array[0], array[1], array[2]]
    
    if men==0:
        print("Меню с таким индексом не найдено Введите его название")
        namename=input()
        menu[content[index][4]]=[namename]


print("Удалить 1 , добавить 2 , изменить 3 введите")
oh=input()
if oh=='1':
    delete()
elif oh=='2':
    add()
elif oh=='3':
    update()    
print(content)
print(author)
print(menu)