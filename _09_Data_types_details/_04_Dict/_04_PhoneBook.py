
# phone book dict{}

#Phones=dict()
Phones={'Naveen':9182206296,'Sai':8500312772}
while True:
    name=input('Enter name (press Enter to stop):')
    if not name:
        break
    
    mobile=input('Enter mobile number:')
    if len(mobile)==10:
        if name in Phones:
            if type(Phones[name]) is list:
                Phones[name].append(mobile)
            else:
                old_mobile=Phones[name]
                mobile1=int(mobile)
                phone_list=[old_mobile,mobile1]
                Phones[name]=phone_list
        else:
            Phones[name]=mobile
    else:
        print('Enter number is invaild:',mobile)
    if mobile in Phones.values():
        print('mobile number is already exist:')
        break    
for k in sorted(Phones.keys()):
    print(k,':',Phones[k])
    
