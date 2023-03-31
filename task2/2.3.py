import random
 
a = [str(random.randint(0,9)) for i in range(5)]
a.insert(random.randint(0,5), '3')
print(''.join(a))