

print("Welcome to SQL College of ICT Ogbomosho\n")
print('varification is composory')

print('\nHow may i help you?\n1. STAFF\n2. STUDENT\n3. VISITOR')
user = input('\nEnter the option: ')
if user == '2':
    print('''
        PAYMENT STATUS
        1. FULL PAID
        2. NO PAY
        3. PAID HALF
        ''')
    user = input('\nYour choice:')
    if user =='1':
        print('Please go to your class')
        
    elif user == '2':
        print('You have to pay before attending class')
    elif user == '3':
        print('Your can go to your class but make sure you complete your payment')    
    else:
        print('invalid')
elif user == '1':
    print('You can go to your office sir')

elif user == '3':
    print("How may i help you sir/ma'am")
else:
    print('invalid')
        