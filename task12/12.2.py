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

max=0
name=''
for f in firm.keys():
        count=0
        for p in person.values():
            if p[1]>=20 and p[1]<=30 and p[3]==f:
                    count+=1
        if max<count:
               max=count
               name=firm[f]              
        
print(max)
print(name)       
       