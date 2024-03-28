import mysql.connector as sql
import random
import datetime as dt
tim = dt.datetime.now().date()
ti = dt.datetime.now()
# mycon = sql.connect(host='localhost', user='root', password='aliyu090')
# print(mycon)
# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE my_atm")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
   

mycon = sql.connect(host='localhost', user='root', passwd='aliyu090', database="my_atm")
mycursor = mycon.cursor()

# mycursor.execute("CREATE TABLE customers_table2 (customer_id INT(4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR(50), Email VARCHAR(50), Pin VARCHAR(4), Account_no VARCHAR(11), Account_balance VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)

class Bank:  
   def __init__(self):
      self.landing_page()

   def landing_page(self):

      print('''
                  welcome to Access bank

      Do you have an account?..
               1. Yes
               2. No
               ''')
      Choice=input("your choice.")
      if Choice == ('1'):
         self.login()
      elif Choice == ('2'):
         self.sign_up()   
  
   def sign_up(self):
      print("Register...")
      Full_name = input("Enter your name:")
      Email = input("Enter your email:")
      Pin = input('Your 4-digit PIN>>>>')
      Account_balance = input("Enter amount:")
      Account_no = random.randint(2000000000, 2999999999)

      query = 'INSERT INTO customers_table2(Full_name,Email,Pin,Account_no,Account_balance) VALUE(%s, %s, %s, %s,%s)'
      val = (Full_name,Email,Pin, Account_no,Account_balance)
      mycursor.execute(query,val)
      mycon.commit()
      print(mycursor.rowcount, 'row added')

      print("account creation is successfully...")

      print('Time:',tim,',',ti.hour,':',ti.minute)
      

   def login(self):
      print("login to your account")
         
      Account_no =input('Account number: ')
      Pin = input('pin: ')
      query = 'SELECT * FROM customers_table2 WHERE Account_no = %s and Pin = %s'
      val = (Account_no, Pin)
      mycursor.execute(query,val)
      details = mycursor.fetchall()
      Account_no = details[0][4]
      print(details)
      if details:
         print('''
         1. Deposit
         2. Withdraw
         3. Balance
         4. Transfer
         5. CloseAccount
         6. Exit
         ''')
         choice = input("Enter your choice:")
         if choice == ('1'):
            self.Deposit()
         elif choice == ('2'):
            self.Withdraw()
         elif choice == ('3'):
            self.Balance()
         elif choice == ('4'):
            self.Transfer()
         elif choice==('5'):
            self.CloseAccount()     
         elif choice == ('6'):
               self.Exit()
   def Deposit(self):
      amount = int(input("Enter the amount>>")) 
      Account_no =input("Enter account_no:")
      a = ("SELECT * FROM customers_table2 WHERE Account_no =%s")
      data = [Account_no]
      mycursor.execute(a, data)
      result=mycursor.fetchall()
      print(result)
      Account_balance = result[0][5]
      new_balance=int(Account_balance) + int(amount)
      query= ("UPDATE customers_table2 SET Account_balance= %s WHERE Account_no = %s")
      dat = (new_balance, Account_no)
      mycursor.execute(query,dat)
      mycon.commit()
      print("Deposit of",amount,"is successfully..")
      print(f"Your new Account_balance is {new_balance}")
      print('Time:',tim,',',ti.hour,':',ti.minute)
   def Withdraw(self):
      amount = int(input("Enter the amount>>"))
      Account_no =input("Enter account_no:")
      a = ("SELECT * FROM customers_table2 WHERE Account_no =%s")
      data = [Account_no]
      mycursor.execute(a, data)
      result=mycursor.fetchall()
      print(result)
      Account_balance = int(result[0][5])
      if int(Account_balance) >= int(amount):
         new_balance=int(Account_balance) - int(amount)
         query= ("UPDATE customers_table2 SET Account_balance= %s WHERE Account_no = %s")
         dat = (new_balance, Account_no)
         mycursor.execute(query,dat)
         mycon.commit()
         print("Withdrawal of",amount, "is successfully..")
         print("Your new account_balance is",new_balance)
         print('Time:',tim,',',ti.hour,':',ti.minute)
      else:
         print("Insufficient balance please recharge and try again..")
      
   def Balance(self):
      account_no =input("Enter account_no:")
      a = ("SELECT * FROM customers_table2 WHERE Account_no =%s")
      data = [account_no]
      mycursor.execute(a, data)
      result=mycursor.fetchall()
      print(result)
      print('Time:',tim,',',ti.hour,':',ti.minute)
      
   def Transfer(self):
      pin =input("Enter your 4 digit_pin to confirm>>>:")
      account_no =input("Enter your account_no:")
      a = ("SELECT * FROM customers_table2 WHERE Pin =%s and Account_no =%s")
      data = [pin,account_no]
      mycursor.execute(a, data)
      result=mycursor.fetchall()
      balance = result[0][5]
      amount = int(input("Enter the amount>>")) 
      if int(balance) >= int(amount):
         new_balance=int(balance)-int(amount)
         query= ("UPDATE customers_table2 SET Account_balance= %s WHERE Account_no = %s")
         dat = (new_balance, account_no)
         mycursor.execute(query,dat)
         mycon.commit()
         account_no =input("Enter receiver account_no:")
         name =input("Verify receivers name:")
         a2 = ("SELECT * FROM customers_table2 WHERE Full_name=%s and Account_no=%s")
         data2 = [name, account_no]
         mycursor.execute(a2, data2)
         result=mycursor.fetchall()
         account_balance = result[0][5]
         new=int(account_balance) + int(amount)
         query2= ("UPDATE customers_table2 SET Account_balance= %s WHERE Account_no = %s")
         dat2 = (new, account_no)
         mycursor.execute(query2,dat2)
         mycon.commit()
         print(f"Dear customer you have successfully transfer {amount} to this account_no:{account_no}, your new account_balance is {new_balance}")
         print('Time:',tim,',',ti.hour,':',ti.minute)  
      else:
         ("Insufficient balance")
         
   def CloseAccount(self):
      account_no = input("Enter the account no:")
      sql1="delete from customers_table2 WHERE Account_no =%s"
      data=[account_no]
      mycursor.execute(sql1,data)
      mycon.commit()
      print("customer with this account no:",account_no,"has successfully deleted his information from our database..")  
      print('Time:',tim,',',ti.hour,':',ti.minute)
   def Exit(self):  
      print("You have successfully ended the session...") 
      print("Thank you for banking with us...") 
      print('Time:',tim,',',ti.hour,':',ti.minute)  
      
bank = Bank()  



             
   