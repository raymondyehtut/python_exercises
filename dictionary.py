dict = {'name': 'Aung','age':7}

print ('name:'+ dict ['name'])
print ('age:'+ str( dict ['age']))

print("..........")
person1 = {'name': 'Aung','age':7}
person2= {'name': 'mg','age':8}


room = [person1,person2]
for person in room:
    print ('name:'+ person ['name'])
    print ('age:'+ str(person ['age']))