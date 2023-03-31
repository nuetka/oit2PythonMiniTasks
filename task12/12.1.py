person={
    '1':['HHkh Hh HHh hj', 26, 'm', '1', '2'],
    '2':['JJjjj JJJJ JJJJ', 86, 'm', '1', '2'],
    '3':['AAAA AAAA AAAA', 26, 'f', '2', '1'],
    '4':['AAAA AAAA AAAA', 26, 'f', '2', '2']
}

firm={
    '1': 'Hhhhh',
    '2': 'JJjjj'
}

position={
    '1':'Director',
    '2':'Actor'
}

for f in firm.keys():
    for pos in position.keys():
         for p in person.values():
            if f==p[3] and pos==p[4]:
                print(firm[f]+' '+ position[pos] )
                break
