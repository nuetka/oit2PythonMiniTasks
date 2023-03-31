x = 'порыв 25346 пы ЛЛ лл пырва  олав лоы цу34 4'
y = []
for i in x:
    if i == 'л':
        y.append(i)
    elif i=='Л':
        y.append(i)
print(''.join(y))