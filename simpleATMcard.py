

def ATMcard_login():
    print('Welcome to Access bank')
    print('''Do you have an account?..\n
          1. Yes
          2. No
          ''')
    user =input('your choice.')
    if user == '1':
     while True:
        print('''please your choice..\n
          1. Withdraw
          2. Deposit
          3. Transfer
          4. Menu
          5. Cancel
          ''')
        user =input('your choice.')
        if user =='1':
            print('''Enter Transaction Type\n
                  1. saving
                  2. current
                  ''')
            user =input('your choice.')
            if user == '1':
                print('''Enter Amount\n
                      1. #2,000
                      2. #5,000
                      3. #10,000
                      4. #20,000''')
                user =input('your choice.')
                if user == '1':
                    print('please take your cash')
                elif user=='2':
                    print('Take your money')
                elif user =='3':
                    print('Take your money')
                elif user =='4':
                   print('Take your money')
    elif user == '2':
        name = input("Enter your name:")
        email = input("Enter your email:")
        pin = input('4-digit pin:')
    newaccount={'name': name,
                'email': email,
                'pin': pin,
                'balance': 3000
                }
    def __init__(self,name,balance=0):
     self.name = name
     name = "Yemi"
     self.balance = balance 

     def deposit(self,amount): 
      self.balance += amount
      return f"deposit #{amount}.New balance:#{self.balance}"  

     def withdraw(self, amount):
       if amount<=self.balance:
         self.balance-=amount
       return f"withdraw #{amount}.New balance:#{self.balance}"
ATMcard_login()


    
         
  
      



    




