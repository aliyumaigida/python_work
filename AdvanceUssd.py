

def ussd(code):
    if code == '*123#':

        print("welcome to mtn ussd code:")
        print('''
         1. buy data
         2. check balance
         3.My sevices

           ''')
        user = input('choice:')
        if user == '1':
            print('''choice\n
                  1. 1.5GB for #1000
                  2. 750MB for #700
                  ''')
            user = input("Your choice")
            if user == "1":
               print("Recharge your account balance")
            elif user == "2":
                print("Purchase of 750MB is successful")


        elif user == '2':
            print('remain balance')
        elif user == "3": 
            print('''Our codes have changed. For
                    1. Data plans 312
                    2. Borrow Airtime
                    ''')
            user = input('please your option..')
            if user == "1":
                print('''select plans..
                        1. Data plans
                        2. Social Bundles
                                   ''')
                user = input('please choice your option.')
                if user =='1':
                    print('choose your option\nMTN XtraBye. Price includes VAT')
                    print('1:40Mb\n2:100Mb\n3:200Mb')
                    user=input('Enter your choice:')
                    if user=='1':
                        print('Your have successfully Borrow 40MB, you will be charge from your next recharge')
                    elif user == '2':
                        print('Your have successfully Borrow 100MB, you will be charge from your next recharge') 
                    elif user =='3':
                        print('Your have successfully Borrow 200MB, you will be charge from your next recharge') 
                elif user =='2':
                    print('Only social bundles Data\n1:40MB\n2:150MB\n3:500MB')
                    user =input('Enter your choice') 
                    if user =='1':
                        print('Your have successfully Borrow 40MB, you will be charge from your next recharge') 
                    elif user =='2':
                        print('Your have successfully Borrow 150MB, you will be charge from your next recharge') 
                    elif user =='3':
                        print('Your have successfully Borrow 200MB, you will be charge from your next recharge')                   
                    
            elif user == "2":
                print('MTN Xtratime:Get up to #401. Fees incl. VAT')
                print('1:#400\n2:#200\n3:Borrow Data')  
                user = input('Your choice.')
                if user =="1":
                    print('Your have successfully Borrow up to #400,you will be charge from your next recharge') 
                elif user =="2":
                    print("your have successfully Borrow #200, you will be charge from your next recharge")  

                
                           
        else:
            print("Invalid code")            
            
        
ussd(input('input ussd code:'))