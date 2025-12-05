'''Positional Arguments'''

def display(Username,email,pwd):
 print(f'username:{Username}\nEmail:{email}\nPwd:{pwd}')

uname=input("Enter the USer name: ")
Email=input("Enter the USer email: ")
password=input("Enter the USer password: ")

display(uname,Email,password)

'''keyword arguments 
def display(Username,email,pwd):
 print(f'username:{Username}\nEmail:{email}\nPwd:{pwd}')

uname=input("Enter the USer name: ")
Email=input("Enter the USer email: ")
password=input("Enter the USer password: ")

display(uname,Email,password)
'''