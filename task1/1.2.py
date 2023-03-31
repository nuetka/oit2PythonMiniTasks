base = [6, 'hdj', 3, 'a', 10, 'asd', 1, 8]

text = ''

for elem in base:  

    if isinstance(elem, int) and elem % 2 == 0:  

        text += f'{elem} '  # Преобразуем из числа в строку и добавляем к переменной.

print(text)