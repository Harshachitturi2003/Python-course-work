n=int(input("Enter no of messages: "))
l={}
for i in range(n):
    name,msg=input().split(":")
    if name:
        l[name].append(msg)
    else:
        l[name]=msg

print(l)
c={
    1:'Count total number of messages',
    2:'',
    3:'',
    4:'',
    5:'',
    6:'',
    7:'',
    8:'',
    9:'',
    10:'',
    11:'',
    12:'',
    13:'',
    14:'',
    15:'',
    16:'',
    17:'',
    18:'',
    19:''
}
while True:
    for i in c:
        print(f'{i}. {c[i]}')
    ch= int(input("Enter the choice: "))
    if ch==1:
        print(c[1])
        cnt=0
        for i in l:
            cnt= len(l[i])
        print(cnt)
        print("----------------------------END OF THE PROGRAM----------------------------")

    elif ch==2:
        print(c[2])
        cnt=0
        for i in l:
            cnt=len(i)
        print(cnt)
        print("----------------------------END OF THE PROGRAM----------------------------")

    elif ch==3:
        print(c[3])
    elif ch==4:
        print(c[4])
    elif ch==5:
        print(c[5])
    elif ch==6:
        print(c[6])
    elif ch==7:
        print(c[7])
    elif ch==8:
        print(c[8])
    elif ch==9:
        print(c[9])
    elif ch==10:
        print(c[10])
    elif ch==11:
        print(c[11])
    elif ch==12:
        print(c[12])
    elif ch==13:
        print(c[13])
    elif ch==14:
        print(c[14])
    elif ch==15:
        print(c[15])
    elif ch==16:
        print(c[16])
    elif ch==17:
        print(c[17])
    elif ch==18:
        print(c[18])
    elif ch==19:
        print(c[19])
    elif ch==20:
        print("End of the program")
        break
    else:
        print("INVALID CHOICE")
