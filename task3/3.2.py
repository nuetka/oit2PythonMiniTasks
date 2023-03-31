my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
my_string = my_string.replace('_', '')
my_string = my_string.split(';')
 
print(my_string[0]+' '*10+my_string[1]+ ' '*10 + my_string[2] + ' '*15 + 'О студенте')
print(my_string[5] + ' '*4 + my_string[6] + ' '*5 + my_string[7] + ' '*3 + my_string[9] + ',' + my_string[8])
print(my_string[10] + ' '*4 + my_string[11] + ' '*4 + my_string[12] + ' '*3 + my_string[14] + ',' + my_string[13])