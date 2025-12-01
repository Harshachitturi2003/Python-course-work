hours=int(input("Enter Hours: "))
if hours<=2:
    bill=30
elif hours>2 and hours<24:
    bill=30+(hours-2)*10
elif hours==24:
    bill=200
print(bill)    
