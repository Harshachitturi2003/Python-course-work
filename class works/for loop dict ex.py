lang={1:'python' , 2:'java' , 3:'c' , 4:'c++' , 5:'mysql' , 6:'flask' , 7:'javascript'}
for i in lang:
 print(f'key-{i} value-{lang[i]}')
for i in enumerate(lang):
 print(f'index-{i[0]} key-{i[1]} value-{lang[i[1]]}')
