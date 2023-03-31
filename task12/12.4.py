person={
    '1':['HHkh Hh HHh hj', 26, 'm', '1', '2'],
    '2':['JJjjj JJJJ JJJJ', 86, 'm', '1', '2'],
    '3':['AAAA AAAA AAAA', 26, 'f', '2', '1'],
    '4':['AAAA AAAA AAAA', 26, 'f', '2', '2']
}

firm={
    '1': 'НосковИко',
    '2': 'JJjjj'
}

position={
    '1':'Ди',
    '2':'Директор'
}

for per in person.values():
    if per[4]=='2' and per[3]=='1':
        print(per)