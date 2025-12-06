l=[1,2,3,4,5]
names=['santosh','ramya','kavya']
price=[20000,45444,19999]

res=list(map(lambda i:f'{i}%',l))
res1=list(map(lambda i: i.title(),names))
res2=list(map(lambda i: f'{i+i*0.18}',price))

print(res)
print(res1)
print(res2)
