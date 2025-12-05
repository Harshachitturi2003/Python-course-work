def display(s,i):
    if i>len(s):
        return
    print(s[:i])
    display(s,i+1)
    print(s[:i])
 
display('abcde',1)
