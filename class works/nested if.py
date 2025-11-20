data={
    'ajay':{'python':99,'sql':88,'flask':90},
    'santosh':{'python':29,'sql':100,'flask':50},
    'sahithi':{'python':98,'sql':96,'flask':99},
    'nishitha':{'python':85,'sql':86,'flask':87},
    'varun':{'python':50,'sql':70,'flask':64}
    }
user=input("Enter the user:  ")
avg=(data[user]['python']+data[user]['sql']+data[user]['flask'])/3
if 80<=avg<=100:
    print(f'{data[user]} got "A" grade.\nkeep it up')
elif 60<=avg<80:
    print(f'{data[user]} got "B" grade.\nGood')
elif 40<=avg<60:
    print(f'{data[user]} got "C" grade.\nAverage')
elif avg<40:
    print(f'{data[user]} got Failed!\nBring Your Parents')
