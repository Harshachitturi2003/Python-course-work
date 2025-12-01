n=int(input("Enter n: "))
if n<=100:
    print(n*1.5)
elif n>101 and n<=200:
       print(150+(n-100)*2.5)
elif n>201 and n<=500:
       print(400+(n-200)*4)
else:
       print(600+(n-500)*6)
 
