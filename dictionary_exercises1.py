
#retrive gender with male
room = [{'Name': 'aung ko','age':7,'gender': 'male'},
        {'Name': 'ko ko','age':8,'gender': 'male'},
        {'Name': 'aye aye','age':7,'gender': 'female'},
        {'Name': 'aung ko','age':7,'gender': 'male'},
        {'Name': 'htet htet','age':8,'gender': 'female'},
        {'Name': 'win aung','age':7,'gender': 'male'}
        ]

for d in room:
    if d.get('gender') == 'male':
        print(d)

for s in room:
      print ('age:'+ str(s ['age']))
      
for e in room:
    if e.get('age')==8:
        print(e)